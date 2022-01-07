#/bin/env python3
# -*- encoding=utf8 -*-
#******************************************************************************
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

    def _change_pkg(self, change_pkgs):
        os.chdir(self.community_path)
        for pkg in change_pkgs:
            res = subprocess.call('git show remotes/origin/master:{0} > {0}.master 2>&1'.format(pkg), shell=True)
            with open(pkg, 'r', encoding='utf-8') as f:
                pkg_yaml = yaml.load(f.read(), Loader=yaml.Loader)
                self.change_msg.append(pkg_yaml)
            if res == 0:
                with open('{}.master'.format(pkg), 'r', encoding='utf-8') as f:
                    pkg_yaml_master = yaml.load(f.read(), Loader=yaml.Loader)
                self.before_change_msg.append(pkg_yaml_master)
            subprocess.call('rm {}.master'.format(pkg), shell=True)
        os.chdir('../')

    def get_change_pkg(self):
        change_pkgs = []
        pr_diff = os.popen('cd {} && git show'.format(self.community_path)).read()
        diff_files = [x.split(' ')[0][2:] for x in pr_diff.split('diff --git ')[1:]]
        for diff_file in diff_files:
            if len(diff_file.split('/')) == 5 and diff_file.split('/')[0] == 'sig' \
                    and diff_file.split('/')[4].endswith('.yaml') and diff_file.split('/')[2] == 'src-openeuler':
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

    def _check_branch(self, mbranch, sbranch, pkg_name='', old_flag=0):
        """
        check
        :parm mbranch: branch which now branch created from
        :parm sbranch: now branch
        """
        if sbranch == "master":
            if mbranch:
                raise CheckError("FAIL: {} master cannot branch from other branch".format(pkg_name))
            else:
                pass
        else:
            self._check_main_branch(mbranch, pkg_name=pkg_name, old_flag=old_flag)
            self._check_sub_branch(mbranch, sbranch, pkg_name=pkg_name, old_flag=old_flag)

    def _check_main_branch(self, mbranch, pkg_name='', old_flag=0):
        """
        check main branch which now branch created from
        :parm mbranch: main branch
        """
        if mbranch not in self.branch_map["branch"].keys():
            if mbranch.startswith("Multi"):
                if mbranch.split("_")[-1] not in self.branch_map["branch"].keys():
                    if old_flag:
                        raise CheckWarn("WARN: {0} Not found main branch {1}".format(pkg_name, mbranch.split("_")[-1]))
                    else:
                        raise CheckError("FAIL: {0} Not found main branch {1}".format(pkg_name, mbranch.split("_")[-1]))
            elif mbranch.startswith("oepkg"):
                tmp = mbranch.split("_")[-1]
                if tmp.startswith("oe"):
                    tmp = tmp.replace("oe", "openEuler")
                    if tmp not in self.branch_map["branch"].keys():
                        if old_flag:
                            raise CheckWarn("WARN: {0} Not found main branch {1}".format(pkg_name, tmp))
                        else:
                            raise CheckError("FAIL: {0} Not found main branch {1}".format(pkg_name, tmp))
                else:
                    if old_flag:
                        raise CheckError("WARN: {0} Not found main branch {1}".format(pkg_name, tmp))
                    else:
                        raise CheckError("FAIL: {0} Not found main branch {1}".format(pkg_name, tmp))
            else:
                if old_flag:
                    raise CheckWarn("WARN: {0} Not found main branch {1}".format(pkg_name, mbranch))
                else:
                    raise CheckError("FAIL: {0} Not found main branch {1}".format(pkg_name, mbranch))

    def _check_sub_branch(self, mbranch, sbranch, pkg_name='', old_flag=0):
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
                if old_flag:
                    raise CheckWarn("WARN: {0} main branch is wrong".format(pkg_name))
                else:
                    raise CheckError("FAIL: {0} main branch is wrong".format(pkg_name))

        if sbranch not in self.branch_map["branch"][mbranch]:
            sb = sbranch.split("_")
            if sbranch.startswith("Multi"):
                if "Multi-Version" != sb[0]:
                    if old_flag:
                        raise CheckWarn("WARN: {0} sub branch {1} is wrong".format(pkg_name, sbranch))
                    else:
                        raise CheckError("FAIL: {0} sub branch {1} is wrong".format(pkg_name, sbranch))
                if sb[-1] not in self.branch_map["branch"][mbranch]:
                    if old_flag:
                        raise CheckWarn("WARN: {0} sub branch {1}\'s {2} not found in list given by main branch "
                                        "{3}".format(pkg_name, sbranch, sb[-1], mbranch))
                    else:
                        raise CheckError("FAIL: {0} sub branch {1}\'s {2} not found in list given by main branch "
                                         "{3}".format(pkg_name, sbranch, sb[-1], mbranch))
            elif sbranch.startswith("oepkg"):
                if sb[-1].startswith("oe"):
                    tmp = sb[-1].replace("oe", "openEuler")
                    if tmp not in self.branch_map["branch"][mbranch]:
                        if old_flag:
                            raise CheckWarn("WARN: {0} sub branch {1}\'s {2} not found in list given by main branch "
                                            "{3}".format(pkg_name, sbranch, sb[-1], mbranch))
                        else:
                            raise CheckError(
                                "FAIL: {0} sub branch {1}\'s {2} not found in list given by main branch "
                                "{3}".format(pkg_name, sbranch, sb[-1], mbranch))
                else:
                    if old_flag:
                        raise CheckWarn("WARN: {0} sub branch is wrong".format(pkg_name))
                    else:
                        raise CheckError("FAIL: {0} sub branch is wrong".format(pkg_name))
            else:
                if old_flag:
                    raise CheckWarn(
                        "WARN: {0} sub branch {1} not found in list given by main branch {2}".format(pkg_name, sbranch,
                                                                                                     mbranch))
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

    def check(self):
        old_flag = 0
        for pkg in self.change_msg:
            pkg_name = pkg["name"]
            branches = pkg["branches"]
            for bch in branches:
                sbranch = bch['name']
                if sbranch == "master":
                    mbranch = None
                else:
                    mbranch = bch['create_from']
                try:
                    for bpkg in self.before_change_msg:
                        if bpkg["name"] == pkg_name:
                            bl = bpkg["branches"]
                            for ob in bl:
                                if ob["name"] == sbranch:
                                    old_flag = 1
                                    break
                            break
                    self._check_branch(mbranch, sbranch, pkg_name=pkg_name, old_flag=old_flag)
                    old_flag = 0
                except CheckError as e:
                    print(e)
                    self.error_flag = self.error_flag + 1
                except CheckWarn as e:
                    print(e)
                    self.warn_flag = self.warn_flag + 1
                except FileError as e:
                    print(e)
                    self.error_flag = self.error_flag + 1
        print("Check PR {0} Result: error {1}, warn {2}".format(self.pr_id, self.error_flag, self.warn_flag))
        if self.error_flag:
            sys.exit(1)


if __name__ == "__main__":
    par = argparse.ArgumentParser()
    par.add_argument("-conf", "--config", help="branch map", required=True)
    par.add_argument("-id", "--pr_id", help="community pr id", required=True)
    par.add_argument("-repo", "--community_repo_path", help="community repo path", required=True)
    args = par.parse_args()
    C = CheckBranch(args.config, args.community_repo_path, args.pr_id)
    C.get_change_pkg()
    C.check()
