#!/usr/bin/python3
# -*- encoding=utf8 -*-
# ******************************************************************************
# Copyright (c) Huawei Technologies Co., Ltd. 2020-2020. All rights reserved.
# licensed under the Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
#     http://license.coscl.org.cn/MulanPSL2
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR
# PURPOSE.
# See the Mulan PSL v2 for more details.
# Author: miao_kaibo
# Create: 2021-06-18
# ******************************************************************************
import argparse
import os
import subprocess
import sys
import yaml


class CheckError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class FileError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class CheckWarn(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class CheckBranch(object):
    def __init__(self, branch_map_yaml, community_path, pr_id):
        """
        :parm branch_map_yaml: yaml file of branch map
        :parm community_path: community repo path
        :parm pr_id: id of community pr
        """
        self.error_flag = 0
        self.warn_flag = 0
        self.branch_map = None
        self.branch_map_yaml = branch_map_yaml
        self.pr_id = pr_id
        self.community_path = community_path
        self._get_branch_map()
        self.change_msg = []
        self.before_change_msg = []

    @staticmethod
    def _read_yaml(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                file_msg = yaml.load(f, Loader=yaml.FullLoader)
        return file_msg

    @staticmethod
    def get_current_branch():
        return subprocess.getoutput("git branch | grep \\*").split(' ')[-1]

    def get_master_repos_tree(self):
        print('\nGet master repos tree')
        master_repos_tree = []
        current_branch = self.get_current_branch()
        subprocess.call('git checkout master >/dev/null', shell=True)
        for i in os.listdir('sig'):
            if i in ['README.md', 'sig-template']:
                continue
            if 'openeuler' in os.listdir(os.path.join('sig', i)):
                for filesdir, _, repos in os.walk(os.path.join('sig', i, 'openeuler')):
                    for repo in repos:
                        master_repos_tree.append(os.path.join(filesdir, repo))
            if 'src-openeuler' in os.listdir(os.path.join('sig', i)):
                for filesdir, _, src_repos in os.walk(os.path.join('sig', i, 'src-openeuler')):
                    for src_repo in src_repos:
                        master_repos_tree.append(os.path.join(filesdir, src_repo))
        subprocess.call('git checkout {}  >/dev/null'.format(current_branch), shell=True)
        return master_repos_tree

    def _change_pkg(self, change_pkgs):
        master_repos_tree = self.get_master_repos_tree()
        for pkg in change_pkgs:
            from_pkg = pkg['from']
            to_pkg = pkg['to']
            if from_pkg in master_repos_tree:
                from_pkg_yaml = subprocess.getoutput('git show remotes/origin/master:{}'.format(from_pkg))
                self.before_change_msg.append(yaml.load(from_pkg_yaml, Loader=yaml.Loader))
            if os.path.exists(to_pkg):
                with open(to_pkg, 'r') as f:
                    self.change_msg.append(yaml.load(f.read(), Loader=yaml.Loader))

    def get_change_pkg(self):
        print('Get diffs of Pull Request')
        current_branch = self.get_current_branch()
        subprocess.call('git checkout master-{}  >/dev/null'.format(args.pr_id), shell=True)
        change_pkgs = []
        pr_diff = subprocess.getoutput('git show')
        subprocess.call('git checkout {}  >/dev/null'.format(current_branch), shell=True)
        diff_files = [{'from': x.split(' ')[0][2:], 'to': x.split(' ')[1][2:].split('\n')[0]} for x in
                      pr_diff.split('diff --git ')[1:]]
        for diff_file in diff_files:
            diff_file_from = diff_file['from']
            diff_file_to = diff_file['to']
            if len(diff_file_from.split('/')) == 5 and \
                    diff_file_from.split('/')[0] == 'sig' and \
                    diff_file_from.split('/')[2] == 'src-openeuler' and \
                    diff_file_from.split('/')[4].endswith('.yaml') and \
                    len(diff_file_to.split('/')) == 5 and \
                    diff_file_to.split('/')[0] == 'sig' and \
                    diff_file_to.split('/')[2] == 'src-openeuler' and \
                    diff_file_to.split('/')[4].endswith('.yaml'):
                change_pkgs.append(diff_file)
        self._change_pkg(change_pkgs)

    def _get_branch_map(self):
        """
        get branch map from yaml file
        """
        if os.path.exists(self.branch_map_yaml):
            with open(self.branch_map_yaml, 'r', encoding='utf-8') as f:
                self.branch_map = yaml.load(f, Loader=yaml.FullLoader)
        else:
            raise FileError("ERROR: No file {0}".format(self.branch_map_yaml))

    def _check_branch(self, mbranch, sbranch, pkg):
        """
        check
        :parm mbranch: branch which now branch created from
        :parm sbranch: now branch
        """
        pkg_name = pkg['name']
        if sbranch == "master":
            if mbranch:
                raise CheckError("FAIL: {} master cannot branch from other branch".format(pkg_name))
            else:
                pass
        else:
            self._check_main_branch(mbranch, pkg)
            self._check_sub_branch(mbranch, sbranch, pkg_name=pkg_name)

    def _check_main_branch(self, mbranch, pkg):
        """
        check main branch which now branch created from
        :parm mbranch: main branch
        """
        pkg_name = pkg['name']
        if mbranch not in self.branch_map["branch"].keys():
            if mbranch in [branch['name'] for branch in pkg['branches']]:
                return
            if mbranch.startswith("Multi"):
                if mbranch.split("_")[-1] not in self.branch_map["branch"].keys():
                    raise CheckError("FAIL: {0} Not found main branch {1}".format(pkg_name, mbranch.split("_")[-1]))
            elif mbranch.startswith("oepkg"):
                tmp = mbranch.split("_")[-1]
                if tmp.startswith("oe"):
                    tmp = tmp.replace("oe", "openEuler")
                    if tmp not in self.branch_map["branch"].keys():
                        raise CheckError("FAIL: {0} Not found main branch {1}".format(pkg_name, tmp))
                else:
                    raise CheckError("FAIL: {0} Not found main branch {1}".format(pkg_name, tmp))
            else:
                raise CheckError("FAIL: {0} Not found main branch {1}".format(pkg_name, mbranch))

    def _check_sub_branch(self, mbranch, sbranch, pkg_name=''):
        """
        check sub branch
        :parm mbranch: main branch
        :parm sbranch: sub branch
        """
        if mbranch not in self.branch_map["branch"].keys():
            if mbranch.startswith("Multi"):
                mbranch = mbranch.split("_")[-1]
            elif mbranch.startswith("oepkg"):
                if "_oe" in mbranch:
                    mbranch = mbranch.split("_")[-1].replace("oe", "openEuler")
            else:
                raise CheckError("FAIL: {0} main branch is wrong".format(pkg_name))

        if sbranch not in self.branch_map["branch"][mbranch]:
            sb = sbranch.split("_")
            if sbranch.startswith("Multi"):
                if "Multi-Version" != sb[0]:
                    raise CheckError("FAIL: {0} sub branch {1} is wrong".format(pkg_name, sbranch))
                if sb[-1] not in self.branch_map["branch"][mbranch]:
                    raise CheckError("FAIL: {0} sub branch {1}\'s {2} not found in list given by main branch "
                                     "{3}".format(pkg_name, sbranch, sb[-1], mbranch))
            elif sbranch.startswith("oepkg"):
                if sb[-1].startswith("oe"):
                    tmp = sb[-1].replace("oe", "openEuler")
                    if tmp not in self.branch_map["branch"][mbranch]:
                        raise CheckError(
                            "FAIL: {0} sub branch {1}\'s {2} not found in list given by main branch "
                            "{3}".format(pkg_name, sbranch, sb[-1], mbranch))
                else:
                    raise CheckError("FAIL: {0} sub branch is wrong".format(pkg_name))
            else:
                raise CheckError(
                    "FAIL: {0} sub branch {1} not found in list given by main branch {2}".format(pkg_name, sbranch,
                                                                                                 mbranch))

    @staticmethod
    def _check_createfrom_valid(reponame, sbranches, mbranches):
        """
        check if the create_from branch is created or creating.
        """
        for br in mbranches:
            if br is None:
                continue
            if br not in sbranches:
                raise CheckError(
                    "FAIL: Branch( {0} ) of repo( {1} ) is not created or creating but in "
                    "create_from.".format(br, reponame))
            else:
                continue
        return

    def get_branches(self, pkg):
        """
        get history branches and change_branches of a package
        :param pkg: a dict of the package
        :return: a tuple of history branches and change_branches
        """
        pkg_name = pkg['name']
        branches = pkg['branches']
        history_branches = []
        changed_branches = []
        if pkg_name not in [bf_pkg['name'] for bf_pkg in self.before_change_msg]:
            return [], branches
        for bf_pkg in self.before_change_msg:
            bf_pkg_name = bf_pkg['name']
            if bf_pkg_name != pkg_name:
                continue
            bf_branches = bf_pkg['branches']
            for bch in branches:
                if bch in bf_branches:
                    history_branches.append(bch)
                else:
                    changed_branches.append(bch)
        return history_branches, changed_branches

    def history_check(self, history_branches, pkg):
        """
        check history branches
        :param history_branches: branches be same between self.change_msg and self.before_change_msg of the same package
        :param pkg: a dict of the package
        :return:
        """
        for bch in history_branches:
            sbranch = bch['name']
            if sbranch == "master":
                mbranch = None
            else:
                mbranch = bch['create_from']
            try:
                self._check_branch(mbranch, sbranch, pkg)
            except CheckError as e:
                print(str(e).replace('FAIL', 'WARNING'))
                self.warn_flag = self.warn_flag + 1
            except FileError as e:
                print(e)
                self.error_flag = self.error_flag + 1

    def differences_check(self, changed_branches, pkg):
        """
        check changed branches
        :param changed_branches: branches diff between self.change_msg and self.before_change_msg of the same package
        :param pkg: a dict of the package
        :return:
        """
        for bch in changed_branches:
            sbranch = bch['name']
            if sbranch == "master":
                mbranch = None
            else:
                mbranch = bch['create_from']
            try:
                self._check_branch(mbranch, sbranch, pkg)
            except CheckError as e:
                print(e)
                self.error_flag = self.error_flag + 1
            except FileError as e:
                print(e)
                self.error_flag = self.error_flag + 1

    def check(self):
        for pkg in self.change_msg:
            history_branches, changed_branches = self.get_branches(pkg)
            if history_branches:
                self.history_check(history_branches, pkg)
            if changed_branches:
                self.differences_check(changed_branches, pkg)
        print("\nCheck PR {0} Result: error {1}, warn {2}".format(self.pr_id, self.error_flag, self.warn_flag))
        if self.error_flag:
            sys.exit(1)


if __name__ == "__main__":
    par = argparse.ArgumentParser()
    par.add_argument("-conf", "--config", help="branch map", required=True)
    par.add_argument("-id", "--pr_id", help="community pr id", required=True)
    par.add_argument("-repo", "--community_repo_path", help="community repo path", required=True)
    args = par.parse_args()
    current_dir = os.getcwd()
    C = CheckBranch(args.config, args.community_repo_path, args.pr_id)
    os.chdir(args.community_repo_path)
    C.get_change_pkg()
    C.check()
    os.chdir(current_dir)

