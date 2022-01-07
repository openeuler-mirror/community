#!/usr/bin/python3
"""
Validation for users and projects
"""
import argparse
import os
import requests
import sys
import yaml


def load_yaml(yaml_file):
    """
    Load yaml content
    :param yaml_file: path of yaml file
    :return: content of the yaml file when it can be opened normally or exit abnormally
    """
    try:
        with open(yaml_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError as e1:
        print(e1)
        sys.exit(1)
    except yaml.MarkedYAMLError as e2:
        print(e2)
        sys.exit(1)


def get_diff_files():
    """
    Get changed filenames
    :return: a list of changed filenames
    """
    pr_diff = os.popen('git show').read()
    diff_files = [x.split(' ')[0][2:] for x in pr_diff.split('diff --git ')[1:]]
    return diff_files


def get_all_repos(sig_exception_list):
    """
    Get all repositories belong openeuler or src-openeuler through file directories
    :return: A list of all repositories
    """
    repositories = []
    for i in os.listdir('sig'):
        if i in sig_exception_list:
            continue
        if 'openeuler' in os.listdir(os.path.join('sig', i)):
            for _, _, repos in os.walk(os.path.join('sig', i, 'openeuler')):
                for repo in repos:
                    repositories.append(os.path.join('openeuler', os.path.splitext(os.path.basename(repo))[0]))
        if 'src-openeuler' in os.listdir(os.path.join('sig', i)):
            for _, _, src_repos in os.walk(os.path.join('sig', i, 'src-openeuler')):
                for src_repo in src_repos:
                    repositories.append(os.path.join('src-openeuler', os.path.splitext(os.path.basename(src_repo))[0]))
    return repositories


def get_ignore_projects():
    """
    Get ignore repositories
    :return: A list of ignore repositories
    """
    ignore_projects = []
    diff_files = get_diff_files()
    for diff_file in diff_files:
        if len(diff_file.split('/')) == 5:
            if diff_file.split('/')[2] == 'openeuler' or diff_file.split('/')[2] == 'src-openeuler':
                repo_file = diff_file.split('/')[4]
                repo = os.path.splitext(repo_file)[0]
                ignore_projects.append(os.path.join(diff_file.split('/')[2], repo))
    return ignore_projects


def get_total_page(access_token):
    """
    Get total_page needs to query
    :return: total_page
    """
    url = 'https://gitee.com/api/v5/enterprises/open_euler/repos'
    params = {
        'type': 'all',
        'page': 1,
        'per_page': 100,
        'access_token': access_token
    }
    r = requests.get(url, params)
    if r.status_code != 200:
        print(r.status_code, r.json())
        sys.exit(1)
    else:
        return r.headers['total_page']


def check_user_exists(user, access_token):
    """
    Check whether a user exists through the user query interface
    :param user: gitee_id
    :param access_token: access_token of gitee
    :return: True when the user exists or False
    """
    print('Starting to validate user {}'.format(user))
    url = 'https://gitee.com/api/v5/users/{}?access_token={}'.format(user, access_token)
    r = requests.get(url)
    if r.status_code == 200:
        return True
    else:
        return False


def validate_users(access_token, sig_exception_list):
    """
    Validate users of all sigs
    """
    invalid_users = []
    sigs = os.listdir('sig')
    for sig in sigs:
        if sig in sig_exception_list:
            continue
        owners_file = os.path.join('sig', sig, 'OWNERS')
        if os.path.exists(owners_file):
            maintainers = load_yaml(owners_file).get('maintainers')
            for maintainer in maintainers:
                if not check_user_exists(maintainer, access_token):
                    invalid_users.append(maintainer)
    invalid_users = list(set(invalid_users))
    for invalid_user in invalid_users:
        if not invalid_user:
            invalid_users.remove(invalid_user)
    if invalid_users:
        print('Failed to validate users:')
        for invalid_user in invalid_users:
            print('    {}'.format(invalid_user))
        sys.exit(1)
    else:
        print('Owners successfully verified.')


def validate_projects(access_token, sig_exception_list):
    """
    Validate all repositories
    :return:
    """
    print('Starting to validating all of the repos')
    repos = get_all_repos(sig_exception_list)
    total_page = get_total_page(access_token)
    projects = []
    for i in range(int(total_page)):
        print('Starting to fetch project lists {}/{} from enterpise open_euler'.format(i + 1, total_page))
        url = 'https://gitee.com/api/v5/enterprises/open_euler/repos'
        params = {
            'type': 'all',
            'page': i + 1,
            'per_page': 100,
            'access_token': access_token
        }
        r = requests.get(url, params=params)
        if len(r.json()) == 0:
            return
        else:
            for repo in r.json():
                projects.append(repo['full_name'])
    ignore_projects = get_ignore_projects()
    non_enterprise_projects = []
    for repo in repos:
        if repo not in ignore_projects and repo not in projects:
            non_enterprise_projects.append(repo)
    if non_enterprise_projects:
        print('[Error] Failed to recognize gitee {} projects:'.format(len(non_enterprise_projects)))
        for non_enterprise_project in non_enterprise_projects:
            print('    {}'.format(non_enterprise_project.split('.yaml')[0]))
        sys.exit(1)
    else:
        print('Projects successfully verified.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', help='validation action', required=True)
    parser.add_argument('-d', '--directory', help='path of repo', required=True)
    parser.add_argument('-t', '--token', help='access_token', required=True)
    args = parser.parse_args()
    action = args.action
    directory = args.directory
    access_token = args.token
    sig_exception_list = ['README.md', 'sig-recycle', 'sig-template']
    os.chdir(directory)
    if action == 'users':
        validate_users(access_token, sig_exception_list)
    elif action == 'projects':
        validate_projects(access_token, sig_exception_list)
    else:
        print('Wrong action.')


if __name__ == '__main__':
    main()
