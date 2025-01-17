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
        self.unmaintained_branches = None

    @staticmethod
    def _read_yaml(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                file_msg = yaml.load(f, Loader=yaml.FullLoader)
        return file_msg

    @staticmethod
    def get_current_branch():
        return subprocess.getoutput("git branch | grep \\*").split(' ')[-1]

    def refresh_unmaintained_branches(self):
        fn = "ci-scripts/unmaintained_branches.yaml"
        if self.unmaintained_branches == None:
            bches_list = yaml.load(open(fn, encoding="utf-8"), Loader=yaml.Loader)
            self.unmaintained_branches = set(bches_list)

    def get_master_repos_tree(self):
        print('\nGet master repos tree')
        master_repos_tree = []
        current_branch = self.get_current_branch()
        subprocess.call('git checkout master >/dev/null', shell=True)
        for i in os.listdir('sig'):
            if i in ['README.md', 'sig-template', 'create_sig_info_template.py']:
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
            from_org = from_pkg.split('/')[2]
            to_org = to_pkg.split('/')[2]
            if from_pkg in master_repos_tree:
                from_pkg_yaml = subprocess.getoutput('git show remotes/origin/master:{}'.format(from_pkg))
                from_pkg_dict = yaml.load(from_pkg_yaml, Loader=yaml.Loader)
                from_pkg_dict['org'] = from_org
                self.before_change_msg.append(from_pkg_dict)
            if os.path.exists(to_pkg):
                with open(to_pkg, 'r') as f:
                    to_pkg_dict = yaml.load(f.read(), Loader=yaml.Loader)
                    to_pkg_dict['org'] = to_org
                    to_pkg_dict['from_pkg'] = from_pkg
                    to_pkg_dict['to_pkg'] = to_pkg
                    self.change_msg.append(to_pkg_dict)

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
                    diff_file_from.split('/')[2] in ['openeuler', 'src-openeuler'] and \
                    diff_file_from.split('/')[4].endswith('.yaml') and \
                    len(diff_file_to.split('/')) == 5 and \
                    diff_file_to.split('/')[0] == 'sig' and \
                    diff_file_to.split('/')[2] in ['openeuler', 'src-openeuler'] and \
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

    def _check_branch(self, p_branch, c_branch, pkg):
        """
        check
        :parm p_branch: parent branch
        :parm c_branch: child branch to be forked from parent branch
        """
        pkg_name = pkg['name']
        if c_branch == "master" and p_branch:
            raise CheckError("FAIL: {} tries to create \"master\" branch from other branch".format(pkg_name))
        if c_branch != "master" and not p_branch:
            raise CheckError("FAIL: {0} tries to create \"{1}\" branch without parent branch".format(pkg_name, c_branch))

        if c_branch.startswith("oepkg") or not p_branch:
            # Ignore branching rule for oepkg
            # Ignore if p_branch is None
            return
        else:
            self._check_parent_branch(p_branch, pkg)
            if pkg['org'] == 'openeuler':
                return
            self._check_child_branch(p_branch, c_branch, pkg_name=pkg_name)

    def _check_parent_branch(self, p_branch, pkg):
        """
        check parent branch which now branch created from
        :parm p_branch: parent branch
        """
        pkg_name = pkg['name']
        if p_branch not in [branch['name'] for branch in pkg['branches']]:
            raise CheckError("FAIL: {1} tries to create from parent branch \"{0}\", "
                    "but \"{0}\" does not exist in repo configuration".format(p_branch, pkg_name))
        if pkg['org'] == 'openeuler':
            return
        if p_branch not in self.branch_map["branch"].keys():
            if p_branch.startswith("Multi-Version"):
                if p_branch.split("_")[-1] not in self.branch_map["branch"].keys():
                    raise CheckError("FAIL: {0} tries to create Multi-Version branch based on \"{1}\", "
                            "which is not permitted by configuration.".format(pkg_name, p_branch.split("_")[-1]))
            else:
                raise CheckError("FAIL: {0} tries to create new branch from parent branch \"{1}\", "
                        "which is not permitted by configuration.".format(pkg_name, p_branch))

    def _check_child_branch(self, p_branch, c_branch, pkg_name=''):
        """
        check child branch
        :parm p_branch: parent branch
        :parm c_branch: child branch
        """
        if p_branch not in self.branch_map["branch"].keys():
            if p_branch.startswith("Multi"):
                p_branch = p_branch.split("_")[-1]
            elif p_branch.startswith("oepkg"):
                if "_oe" in p_branch:
                    p_branch = p_branch.split("_")[-1].replace("oe", "openEuler")
            else:
                raise CheckError("FAIL: {0} tries to fork from an invalid branch \"{1}\"".format(pkg_name, p_branch))

        if c_branch not in self.branch_map["branch"][p_branch]:
            sb = c_branch.split("_")
            if c_branch.startswith("Multi"):
                if "Multi-Version" != sb[0]:
                    raise CheckError("FAIL: {0} tries to create Multi-Version branch, "
                            "but \"{1}\" is not valid name.".format(pkg_name, c_branch))
                if sb[-1] not in self.branch_map["branch"][p_branch]:
                    raise CheckError("FAIL: {0} tries to create child branch \"{1}\" from parent branch \"{2}\", "
                            "which is not permitted by configuration.".format(pkg_name, c_branch, p_branch))
            else:
                raise CheckError("FAIL: {0} tries to create child branch \"{1}\" from parent branch \"{2}\", "
                            "which is not permitted by configuration.".format(pkg_name, c_branch, p_branch))

    @staticmethod
    def _check_createfrom_valid(reponame, c_branches, p_branches):
        """
        check if the create_from branch is created or creating.
        """
        for br in p_branches:
            if br is None:
                continue
            if br not in c_branches:
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

    def unmaintained_check(self, bch, pkg):
        """
        check if unmaintained branches already readonly
        """
        if bch['name'] in self.unmaintained_branches:
            if bch['type'] != "readonly":
                print("Unmaintained bracnh {b} of {p} should be readonly".format(b=bch['name'], p=pkg))
                return False
            else:
                return True
        else:
            return True

    def history_check(self, history_branches, pkg):
        """
        check history branches
        :param history_branches: branches be same between self.change_msg and self.before_change_msg of the same package
        :param pkg: a dict of the package
        :return:
        """
        for bch in history_branches:
            c_branch = str(bch['name'])
            if c_branch == "master":
                p_branch = None
            else:
                p_branch = str(bch['create_from'])
            try:
                self._check_branch(p_branch, c_branch, pkg)
            except CheckError as e:
                print(str(e).replace('FAIL', 'WARNING'))
                self.warn_flag = self.warn_flag + 1
            except FileError as e:
                print(e)
                self.error_flag = self.error_flag + 1

            if not self.unmaintained_check(bch, pkg):
                self.warn_flag = self.warn_flag + 1

    def differences_check(self, changed_branches, pkg):
        """
        check changed branches
        :param changed_branches: branches diff between self.change_msg and self.before_change_msg of the same package
        :param pkg: a dict of the package
        :return:
        """
        for bch in changed_branches:
            c_branch = str(bch['name'])

            p_branch = bch.get('create_from', None)
            if p_branch:
                p_branch = str(p_branch)

            try:
                self._check_branch(p_branch, c_branch, pkg)
            except CheckError as e:
                print(e)
                #TEMP DISABLE
                self.warn_flag = self.warn_flag + 1
                #self.error_flag = self.error_flag + 1
            except FileError as e:
                print(e)
                self.error_flag = self.error_flag + 1

            if not self.unmaintained_check(bch, pkg):
                self.error_flag = self.error_flag + 1

    def recycle_branch_check(self, pkg):
        """
        recycle branch not allowed modify
        """
        to_pkg = pkg.get("to_pkg")
        branches = pkg.get("branches")
        if "sig-recycle/src-openeuler" in to_pkg and branches:
            self.error_flag += 1
            print(f"src-openeuler repo in sig recycle not allowed to modify: {to_pkg}")

    def check(self):
        self.refresh_unmaintained_branches()

        for pkg in self.change_msg:
            history_branches, changed_branches = self.get_branches(pkg)
            if history_branches:
                self.history_check(history_branches, pkg)
            if changed_branches:
                self.differences_check(changed_branches, pkg)

            self.recycle_branch_check(pkg)

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

