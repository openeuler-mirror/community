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


def check_diff_files():
    """
    Check the differences between the current Pull Request and master branch
    :return: a list of different files
    """
    diff_url = 'https://gitee.com/{0}/{1}/pulls/{2}.diff'.format(owner, repo, number)
    response = requests.get(diff_url)
    if response.status_code != 200:
        print('Can not get differences from diff_url, diff_url:', diff_url)
        sys.exit(1)
    diff_files = [x.split(' ')[0][2:] for x in response.text.split('diff --git ')[1:]]
    return diff_files


def check_gitee_id(gitee_id, errors):
    """
    Check validation of gitee_id
    :param gitee_id: gitee_id
    :param errors: errors count
    :return: errors
    """
    url = 'https://gitee.com/api/v5/users/{}?access_token={}'.format(gitee_id, access_token)
    r = requests.get(url)
    if r.status_code == 404:
        print('ERROR! Check gitee_id: invalid gitee_id {}.'.format(gitee_id))
        errors += 1
    return errors


def check_mentors(mentors, errors):
    """
    Check mentors
    :param mentors: mentors of sig-info.yaml
    :param errors: errors count
    :return: errors
    """
    if not mentors:
        pass
    else:
        for mentor in mentors:
            try:
                gitee_id = mentor['gitee_id']
                errors = check_gitee_id(gitee_id, errors)
            except KeyError:
                print('ERROR! Check mentors: gitee_id is required for every mentor.')
                errors += 1
            try:
                email = mentor['email']
                if not email:
                    print('ERROR! Check mentors: email cannot be null for every mentor.')
                    errors += 1
                else:
                    if not re.match(r'^([a-zA-Z0-9_.-]+)+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
                        print('ERROR! Check mentors: invalid email {}.'.format(email))
                        errors += 1
            except KeyError:
                print('ERROR! Check mentors: email must be provided for evevy mentor.')
                errors += 1
    return errors


def check_maintainers(maintainers, errors):
    """
    Check maintainers
    :param maintainers: maintainers of sig-info.yaml
    :param errors: errors count
    :return: errors
    """
    if not maintainers:
        print('ERROR! Check mentors: at least 1 mentor is required.')
        errors += 1
    else:
        for maintainer in maintainers:
            try:
                gitee_id = maintainer['gitee_id']
                errors = check_gitee_id(gitee_id, errors)
            except KeyError:
                print('ERROR! Check maintainers: gitee_id is required for every maintainer.')
                errors += 1
            try:
                email = maintainer['email']
                if not email:
                    print('ERROR! Check maintainers: email cannot be null for every maintainer.')
                    errors += 1
                else:
                    if not re.match(r'^([a-zA-Z0-9_.-]+)+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
                        print('ERROR! Check maintainers: invalid email {}.'.format(email))
                        errors += 1
            except KeyError:
                print('ERROR! Check maintainers: email must be provided for evevy maintainer.')
                errors += 1
    return errors


def check_committers(committers, errors):
    """
    Check committers
    :param committers: committers of sig-info.yaml
    :param errors: errors count
    :return: errors
    """
    if not committers:
        pass
    else:
        for committer in committers:
            try:
                gitee_id = committer['gitee_id']
                errors = check_gitee_id(gitee_id, errors)
            except KeyError:
                print('ERROR! Check committers: gitee_id is required for every committer.')
                errors += 1
            try:
                email = committer['email']
                if not email:
                    print('ERROR! Check committers: email cannot be null for every committer.')
                    errors += 1
                else:
                    if not re.match(r'^([a-zA-Z0-9_.-]+)+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
                        print('ERROR! Check committers: invalid email {}.'.format(email))
                        errors += 1
            except KeyError:
                print('ERROR! Check committers: email must be provided for evevy committer.')
                errors += 1
    return errors


def check_repositories(repositories, sig_name, sigs, errors):
    """
    Check repositories
    :param repositories: repositories of sig
    :param sig_name: name of sig
    :param sigs: content of all sigs
    :param errors: errors count
    :return: errors
    """
    if not repositories:
        print('ERROR! Check repositories: should contain at least 1 repository.')
        errors += 1
    else:
        for sig in sigs:
            if sig['name'] == sig_name:
                repos = sig['repositories']
                for r in repositories:
                    if not (type(r) == dict and 'repo' in r.keys()):
                        print('ERROR! Check repo: every repo should be a dictionary type and at least one key should '
                              'be repo.')
                        sys.exit(1)
                    if r['repo'] not in repos:
                        print('ERROR! Check repo: no repo named {} in sig {} according to sigs.yaml.'.format(r['repo'],
                                                                                                             sig_name))
                        errors += 1
                    else:
                        if 'additional_contributors' in r.keys():
                            additional_contributors = r['additional_contributors']
                            for additional_contributor in additional_contributors:
                                try:
                                    gitee_id = additional_contributor['gitee_id']
                                    errors = check_gitee_id(gitee_id, errors)
                                except KeyError:
                                    print('ERROR! gitee_id is required in additional_contributors.')
                                    errors += 1
                                try:
                                    email = additional_contributor['email']
                                    if not email:
                                        print('ERROR! Check repositories: email cannot be null for every '
                                              'additional_contributor.')
                                        errors += 1
                                    else:
                                        if not re.match(r'^([a-zA-Z0-9_.-]+)+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',
                                                        email):
                                            print('ERROR! Check repositories: invalid email {}.'.format(email))
                                            errors += 1
                                except KeyError:
                                    print('ERROR! Check repositories: email must be provided for evevy '
                                          'additional_contributor.')
                                    errors += 1
                for r in repos:
                    try:
                        if r not in [x['repo'] for x in repositories]:
                            print('ERROR! Check repo: repo {} belongs to sig {} according to sigs.yaml should be '
                                  'listed but missed.'.format(r, sig_name))
                            errors += 1
                    except TypeError:
                        print('ERROR! Check repo: every repo should be a dictionary type and at least one key should '
                              'be repo.')
                        sys.exit(1)
    return errors


def check_description(sig_info, errors):
    """
    Check description
    :param sig_info: content of sig-info.yaml
    :param errors: errors count
    :return: errors
    """
    if 'description' not in sig_info.keys():
        print('ERROR! description is a required field')
        errors += 1
    else:
        print('Check description: PASS')
    return errors


def check_mailing_list(sig_info, errors):
    """
    Check mailing_list
    :param sig_info: content of sig-info.yaml
    :param errors: errors count
    :return: errors
    """
    if 'mailing_list' not in sig_info.keys():
        print('ERROR! mailing_list is a required field')
        errors += 1
    else:
        print('Check mailing_list: PASS')
    return errors


def check_meeting_url(sig_info, errors):
    """
    Check meeting_url
    :param sig_info: content of sig-info.yaml
    :param errors: errors count
    :return: errors
    """
    if 'meeting_url' not in sig_info.keys():
        print('ERROR! meeting_url is a required field')
        errors += 1
    else:
        print('Check meeting_url: PASS')
    return errors


def check_sig_name(sig_name, sigs, errors):
    """
    Check sig name
    :param sig_name: name of sig in sig-info.yaml
    :param sigs: content of all sigs
    :param errors: errors count
    :return: errors
    """
    if sig_name not in [x['name'] for x in sigs]:
        print('ERROR! sig named {} does not exist in sigs.yaml.'.format(sig_name))
        errors += 1
    return errors


def check_sig_info_yaml(file_name, sigs):
    """
    Check sig-info.yaml, contains multiple independent check items
    :param file_name: name of modified file in current Pull Request
    :param sigs: content of all sigs
    :return:
    """
    errors = 0
    content = load_yaml(os.path.join('community', file_name))
    trust_list = ['name', 'description', 'mailing_list', 'meeting_url', 'mature_level', 'mentors', 'maintainers',
                  'committers', 'security_contacts', 'repositories']
    for i in content.keys():
        if i not in trust_list:
            print('ERROR! Check fields: invalid field {}.'.format(i))
            errors += 1
    try:
        name = content['name']
        mentors = content['mentors'] if 'mentors' in content.keys() else None
        maintainers = content['maintainers']
        committers = content['committers'] if 'committers' in content.keys() else None
        repositories = content['repositories']
    except KeyError as e:
        print('ERROR!', e)
        sys.exit(1)
    errors = check_sig_name(name, sigs, errors)
    errors = check_maintainers(maintainers, errors)
    errors = check_repositories(repositories, name, sigs, errors)
    if mentors:
        errors = check_mentors(mentors, errors)
    if committers:
        errors = check_committers(committers, errors)
    if errors != 0:
        print('Found {} errors, please check!'.format(errors))
        sys.exit(1)
    else:
        print('PASS :)')


def main():
    """
    Main function
    """
    count = 0
    errors = 0
    diff_files = check_diff_files()
    if 'sig/sigs.yaml' in diff_files:
        os.system('cd community && git show remotes/origin/master:sig/sigs.yaml > sig/sigs.master.yaml')
        try:
            sigs_master = load_yaml('community/sig/sigs.master.yaml')['sigs']
            sigs = load_yaml('community/sig/sigs.yaml')['sigs']
        except KeyError as e:
            print(e)
            sys.exit(1)
        remove_repos = []
        add_repos = []
        add_count = 0
        remove_count = 0
        for sig in sigs:
            for r in sig['repositories']:
                for sig_master in sigs_master:
                    if sig_master['name'] == sig['name']:
                        add_count = 1
                        if r not in sig_master['repositories']:
                            add_repos.append(','.join((sig['name'], r)))
                if add_count == 0:
                    add_repos.append(','.join((sig['name'], r)))
        for sig_master in sigs_master:
            for r in sig_master['repositories']:
                for sig in sigs:
                    if sig['name'] == sig_master['name']:
                        remove_count = 1
                        if r not in sig['repositories']:
                            remove_repos.append(','.join((sig_master['name'], r)))
                if remove_count == 0:
                    remove_repos.append(','.join((sig_master['name'], r)))

        for diff_file in diff_files:
            if re.match(r'^sig/.+/sig-info.yaml$', diff_file):
                count += 1
                sig_info = load_yaml(os.path.join('community', diff_file))
                for r in remove_repos:
                    for sig in sigs_master:
                        if r in sig['repositories']:
                            sig_name = sig['name']
                            if sig_name == sig_info['name']:
                                if r in sig_info['repositories']:
                                    print('ERROR! remove repo {0} from sigs.yaml should also remove repo {0} from '
                                          '{1}.'.format(r, diff_file))
                            else:
                                if os.path.exists(os.path.join('community', sig_name, 'sig-info.yaml')):
                                    print('ERROR! remove repo {0} from sigs.yaml should also remove repo {0} from'
                                          ' {1}.'.format(r, diff_file))
                                    errors += 1
                for r in add_repos:
                    for sig in sigs:
                        if r in sig['repositories']:
                            sig_name = sig['name']
                            if sig_name == sig_info['name']:
                                if r not in [x['repo'] for x in sig_info['repositories']]:
                                    print('ERROR! add repo {0} to sigs.yaml should also add repo {0} to '
                                          '{1}.'.format(r, diff_file))
                                    errors += 1
                            else:
                                if os.path.exists(os.path.join('community', sig_name, 'sig-info.yaml')):
                                    print('ERROR! add repo {0} to sigs.yaml should also add repo {0} to '
                                          '{1}.'.format(r, diff_file))
                                    errors += 1
                check_sig_info_yaml(diff_file, sigs)
        if count == 0:
            for r in remove_repos:
                for sig in sigs:
                    if r in sig['repositories']:
                        sig_info_yaml = 'sig/{}/sig-info.yaml'.format(sig['name'])
                        if os.path.exists('community/sig/{}/sig-info.yaml'.format(sig['name'])):
                            print('ERROR! remove repo {0} from sigs.yaml should also remove repo {0} from {1}, '
                                  'but no sig-info.yaml changed.'.format(r, sig_info_yaml))
                            errors += 1
            for r in add_repos:
                for sig in sigs:
                    if r in sig['repositories']:
                        sig_info_yaml = 'sig/{}/sig-info.yaml'.format(sig['name'])
                        if os.path.exists('community/sig/{}/sig-info.yaml'.format(sig['name'])):
                            print('ERROR! add repo {0} to sigs.yaml should also add repo {0} to {1}, but no '
                                  'sig-info.yaml changed.'.format(r, sig_info_yaml))
                            errors += 1
        if errors != 0:
            sys.exit(1)
    else:
        sigs = load_yaml('community/sig/sigs.yaml')['sigs']
        for diff_file in diff_files:
            if re.match(r'^sig/.+/sig-info.yaml$', diff_file):
                count += 1
                check_sig_info_yaml(diff_file, sigs)
        if count == 0:
            print('Found no sig-info.yaml in Pull Request.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A tool for checking the consistency between multiple SIG information'
                                                 ' and sigs.yaml, and validation of fields for every SIG information.')
    parser.add_argument('-o', '--owner', help='owner of Pull Request', required=True)
    parser.add_argument('-r', '--repo', help='repo of Pull Request', required=True)
    parser.add_argument('-n', '--number', help='number of Pull Request', required=True)
    parser.add_argument('-t', '--token', help='access_token', required=True)
    args = parser.parse_args()
    owner = args.owner
    repo = args.repo
    number = args.number
    access_token = args.token
    main()

