#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/25 14:31
# @Author : zhangwuji2022
# @File : sig_info_check_v2.py
# @Software: PyCharm
# Description:
"""
A tool for checking the consistency between multiple SIG information and sigs.yaml, and validation of fields for every
SIG information.
"""
import argparse
import os
import requests
import re
import sys
import yaml

SIG_INFO_FIELDS = ['name', 'description', 'mailing_list', 'meeting_url', 'mature_level', 'mentors', 'maintainers',
                   'repositories', 'created_on']
SIG_INFO_REQUIRED_FIELDS = ['name', 'maintainers']


def load_yaml(file_path):
    """
    Load yaml file
    :param file_path: path of the yaml file ready to load
    :return: content of the file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = yaml.load(f.read(), Loader=yaml.Loader)
            return content
    except yaml.MarkedYAMLError as e:
        print('YAML FORMAT ERROR!')
        print(e)
        sys.exit(1)


def check_diff_files(owner, repo, number):
    """
    Check the differences between the current Pull Request and master branch
    :param owner: owner of Pull Request
    :param repo: repo of Pull Request
    :param number: number of Pull Request
    :return: a list of different files
    """
    diff_url = 'https://gitee.com/{0}/{1}/pulls/{2}.diff'.format(owner, repo, number)
    response = requests.get(diff_url)
    if response.status_code != 200:
        print('Can not get differences from diff_url, diff_url:', diff_url)
        sys.exit(1)
    diff_files = [{'from': x.split(' ')[0][2:], 'to': x.split(' ')[1][2:].split('\n')[0]} for x in
                  response.text.split('diff --git ')[1:]]
    return diff_files


def check_gitee_id(gitee_id, access_token, errors):
    """
    Check validation of gitee_id
    :param gitee_id: login id of gitee
    :param access_token: access_token of gitee
    :param errors: issues number
    :return: errors
    """
    url = 'https://gitee.com/api/v5/users/{}?access_token={}'.format(gitee_id, access_token)
    r = requests.get(url)
    if r.status_code == 404:
        print('ERROR! Check gitee_id: invalid gitee_id {}.'.format(gitee_id))
        errors += 1
    return errors


def check_fields(sig_info, errors):
    """
    Check fields of sig-info.yaml
    :param sig_info: content of sig-info.yaml
    :param errors: issues number
    :return: errors
    """
    fields = list(sig_info.keys())
    for field in fields:
        if field not in SIG_INFO_FIELDS:
            print('ERROR! Find unexpected field [{}] in sig-info'.format(field))
            errors += 1
    for sig_info_field in SIG_INFO_REQUIRED_FIELDS:
        if sig_info_field not in fields:
            print('ERROR! Current sig-info has no field {} yet'.format(sig_info_field))
            errors += 1
    return errors


def check_sig_name(sig, sig_info, errors):
    """
    Check sig name of sig-info.yaml
    :param sig: name of the sig
    :param sig_info: content of sig-info.yaml
    :param errors: issues number
    :return: errors
    """
    name = sig_info.get('name')
    if name != sig:
        print('ERROR! The name must be equal to sig name, but sig-info name={}, sig={}'.format(name, sig))
        errors += 1
    return errors


def check_email(email_address):
    """
    Check validation of email address
    :param email_address: the target email address
    :param errors: issues number
    :return: errors
    """
    if not re.match(r'^[a-zA-Z0-9_\-.]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email_address):
        print('WARNING! It seems that {} is not a email address'.format(email_address))


def check_member(member, access_token, errors):
    """
    Check validation of a member
    :param member: a dict of member info
    :param access_token: access_token of gitee
    :param errors: issues number
    :return: errors
    """
    gitee_id = member.get('gitee_id')
    email = member.get('email')
    errors += check_gitee_id(gitee_id, access_token, errors)
    check_email(email)
    return errors


def check_maintainers(maintainers, access_token, errors):
    """
    Check validation of maintainers
    :param maintainers: a list of maintainers
    :param access_token: access_token of gitee
    :param errors: issues number
    :return: errors
    """
    if not maintainers:
        print('ERROR! The SIG must has at least 1 maintainer')
        errors += 1
        return errors
    if not isinstance(maintainers, list):
        print('ERROR! The maintainers must be a list')
        errors += 1
        return errors
    for maintainer in maintainers:
        check_member(maintainer, access_token, errors)
    return errors


def get_sig_info_repos(sig_info_repos):
    """
    Get all repositories list in sig-info.yaml
    :param sig_info_repos: field repositories of sig-info.yaml
    :return: a list of repositories all list in sig-info.yaml
    """
    all_sig_info_repos = []
    all_sig_info_committers = []
    all_sig_info_contributors = []
    for each_group_repos in sig_info_repos:
        if isinstance(each_group_repos.get("repo"), list):
            for each_repo in each_group_repos.get("repo"):
                all_sig_info_repos.append(each_repo)

        if each_group_repos.get("committers") and isinstance(each_group_repos.get("committers"), list):
            for each_committers in each_group_repos.get("committers"):
                all_sig_info_committers.append(each_committers)

        if each_group_repos.get("contributors") and isinstance(each_group_repos.get("contributors"), list):
            for each_contributors in each_group_repos.get("contributors"):
                all_sig_info_contributors.append(each_contributors)

    return all_sig_info_repos, all_sig_info_committers, all_sig_info_contributors


def get_sig_repos(sig_dir_path):
    """
    Get all repositories under directories of the sig
    :param sig_dir_path: sig directory path
    :return: a list of repositories all belong to the sig
    """
    sig_dir_repos = []
    for root, _, files in os.walk(sig_dir_path):
        for f_name in files:
            sub_dir_yaml_file = os.path.join(root, f_name)
            org_name = sub_dir_yaml_file.split("/")[-3]
            repo_name = sub_dir_yaml_file.split("/")[-1].split(".yaml")[0]
            repo_full_name = "{}/{}".format(org_name, repo_name)
            sig_dir_repos.append(repo_full_name)

    return sig_dir_repos


def check_repos_consistency(sig_info_repos, sig_repos, errors):
    """
    Check consistency between sig_info_repos and sig_repos
    :param sig_info_repos: all repositories list in sig-info.yaml
    :param sig_repos: all repositories under directories of the sig
    :param errors: issues number
    :return: errors
    """
    for sig_info_repo in sig_info_repos:
        if sig_info_repo not in sig_repos:
            print('ERROR! Find extra repo {} list in sig-info.yaml'.format(sig_info_repo))
            errors += 1
    for sig_repo in sig_repos:
        if sig_repo not in sig_info_repos:
            print('ERROR! Find repo {} not exist in sig-info.yaml'.format(sig_repo))
            errors += 1
    return errors


def check_info_repositories(sig_repositories, errors):
    """
    Check validation of sig_info_repos
    :param sig_repositories: repositories of sig-info.yaml
    :param errors: issues number
    :return: errors
    """
    if not sig_repositories:
        return errors

    if not isinstance(sig_repositories, list):
        print('ERROR! Check sig_repositories: sig_repositories should be a list type')
        errors += 1

    for each_group_repos in sig_repositories:
        if not (isinstance(each_group_repos, dict) and 'repo' in each_group_repos.keys()):
            print('ERROR! Check repo: every repo should be a dictionary type and at least one key should '
                  'be repo.')
            errors += 1

        if not isinstance(each_group_repos.get("repo"), list):
            print('ERROR! Check each repo: repo should be a list type')
            errors += 1

        if each_group_repos.get("committers") and not isinstance(each_group_repos.get("committers"), list):
            print('ERROR! Check committers: committers should be a list type')
            errors += 1

        if each_group_repos.get("contributors") and not isinstance(each_group_repos.get("contributors"), list):
            print('ERROR! Check contributors: contributors should be a list type')
            errors += 1

    return errors


def get_all_sig_dir_data(sig_dir_path):
    sig_dir_repos = []
    openeuler = os.path.join(sig_dir_path, "openeuler")
    src_openeuler = os.path.join(sig_dir_path, "src-openeuler")

    if os.path.exists(openeuler):
        sig_dir_openeuler_repos = get_sig_repos(openeuler)
        sig_dir_repos.extend(sig_dir_openeuler_repos)

    if os.path.exists(src_openeuler):
        sig_dir_src_openeuler_repos = get_sig_repos(src_openeuler)
        sig_dir_repos.extend(sig_dir_src_openeuler_repos)
    return sig_dir_repos


def check_sig_info(sig, access_token, errors):
    print('\nStarting to check sig info of sig {}'.format(sig))
    # 1. Get sig-info.yaml
    sig_info_path = os.path.join("community", 'sig', sig, 'sig-info.yaml')
    sig_dir_path = os.path.join("community", 'sig', sig)

    if not os.path.exists(sig_info_path):
        print('WARNING! sig {} has no sig-info.yaml file'.format(sig))
        return errors

    sig_info = load_yaml(sig_info_path)
    print('\nCheck 1: Check fields of sig-info')
    check1 = check_fields(sig_info, errors)
    if check1 != 0:
        return check1

    print('\nCheck 2: Check sig name')
    check2 = check_sig_name(sig, sig_info, errors)
    if check2 != 0:
        return check2

    print('\nCheck 3: Check maintainers')
    maintainers = sig_info['maintainers']
    check3 = check_maintainers(maintainers, access_token, errors)

    sig_repositories = sig_info['repositories']

    print('\nCheck 4: Check repositories')
    check4 = check_info_repositories(sig_repositories, errors)
    if check4 != 0:
        return check3 + check4

    all_sig_info_repos, all_sig_info_committers, all_sig_info_contributors = get_sig_info_repos(sig_repositories)
    sig_dir_repos = get_all_sig_dir_data(sig_dir_path)

    print('\nCheck 5: Check repositories consistency')
    check5 = check_repos_consistency(all_sig_info_repos, sig_dir_repos, errors)

    return check3 + check5


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='A tool for checking the consistency between multiple SIG information'
                    ' and sigs.yaml, and validation of fields for every SIG information.')
    parser.add_argument('-o', '--owner', help='owner of Pull Request', required=True)
    parser.add_argument('-r', '--repo', help='repo of Pull Request', required=True)
    parser.add_argument('-n', '--number', help='number of Pull Request', required=True)
    parser.add_argument('-t', '--token', help='access_token', required=True)
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    owner = args.owner
    repo = args.repo
    number = args.number
    access_token = args.token
    # get diff files of the Pull Request
    diff_files = check_diff_files(owner, repo, number)
    # get all sigs have changed
    change_sigs = []
    for diff_file in diff_files:
        from_file = diff_file['from']
        to_file = diff_file['to']
        if len(from_file) > 2 and from_file.split('/')[0] == 'sig':
            change_sigs.append(from_file.split('/')[1])
        if len(to_file) > 2 and to_file.split('/')[0] == 'sig':
            change_sigs.append(to_file.split('/')[1])
    change_sigs = sorted(list(set(change_sigs)))
    # check sig info for every sig
    errors = 0
    for change_sig in change_sigs:
        errors += check_sig_info(change_sig, access_token, errors)
        if os.path.exists(os.path.join("community", 'sig', change_sig, 'OWNERS')):
            print('WARNING! sig {} has OWNERS file yet, found {} warnings'.format(change_sig, errors))
            errors = 0

    if errors != 0:
        print('Check sig info: Find {} errors.'.format(errors))
        sys.exit(1)
    print('Check sig info: PASS :)')


if __name__ == '__main__':
    main()

