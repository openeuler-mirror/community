#!/usr/bin/python3
"""
This is a tool to close unmaintained branches of openEuler community
"""
import yaml
import sys
import argparse
import os
import re


def load_yaml(d, f):
    """
    Helper for load YAML database
    """
    p = os.path.expanduser(os.path.join(d, f))
    try:
        y = yaml.load(open(p, encoding="utf-8"), Loader=yaml.Loader)
    except FileNotFoundError:
        print("Cannot Load {path}".format(path=p))
        print("Could be wrong path")
        sys.exit(1)
    except yaml.scanner.ScannerError as e:
        print("%s: Invalid YAML file"%(p))
        print("Detailed Error Information:")
        print(e)
        sys.exit(1)
    return y

def disable_src_openeuler_yamls(community, unmaintained_list):
    """
    Disable branches in all src-openeuler repositories definition
    """
    print("Disabling unmaintained branches for all repos definition in src-openeuler")

    src_oe_repos = []
    sig_path = os.path.expanduser(os.path.join(community, "sig"))

    yaml_pattern = re.compile("(.*)/sig/(.*)/(src-openeuler)/([a-z])/(.*).yaml")

    for root, dirs, files in os.walk(sig_path):
        for f in files:
            fn = os.path.join(root, f)
            match_obj = yaml_pattern.match(fn)
            if match_obj:
                need_close = False
                src_repo = load_yaml(root, f)
                # print(f)
                for branch in src_repo["branches"]:
                    if branch["name"] in unmaintained_list and branch["type"] != "readonly":
                        branch["type"] = "readonly"
                        need_close = True
                if need_close:
                    src_oe_repos.append({'fn':fn, 'yaml':src_repo})
    return src_oe_repos


if __name__ == "__main__":
    par = argparse.ArgumentParser()

    par.add_argument("community", type=str, help="Local path of community repository")
    par.add_argument("-d", "--disable_branch", type=str, help="Additional branch name to disable", default="")
    par.add_argument("-c", "--check-only", help="Do checking only, don't change any YAML file", action="store_true")

    args = par.parse_args()

    branches_file = "ci-scripts/unmaintained_branches.yaml"
    unmaintained_list = load_yaml(args.community, branches_file)
    print("Current disabled branches:")
    print(unmaintained_list)

    if args.disable_branch != "":
        if args.disable_branch in unmaintained_list:
            print("Already disabled branch " + args.disable_branch)
            sys.exit(1)
        else:
            unmaintained_list.append(args.disable_branch)
    
    unmaintained_set = set(unmaintained_list)
    repos = disable_src_openeuler_yamls(args.community, unmaintained_set)

    for repo in repos:
        if not os.path.exists(repo['fn']):
            print("Error while file not found: " + repo['fn'])
            sys.exit(1)
        if args.check_only:
            print("{fn} has unmaintained branches, but not readonly".format(fn=repo['fn']))
        else:
            with open(repo['fn'], "w") as repo_yaml:
                yaml.dump(repo['yaml'], repo_yaml, sort_keys=False)

    if args.disable_branch != "":
        print("Writing back additional disabled branch")
        fn = os.path.join(args.community, branches_file)
        with open(fn, "w") as bn:
            yaml.dump(unmaintained_list, bn, sort_keys=False)

    print("Finished!")
