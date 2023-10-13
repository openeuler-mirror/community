#!/usr/bin/python3
"""
This is a sanity checking tool for openEuler community database
"""
import yaml
import sys
import argparse
import os

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

if __name__ == "__main__":
    par = argparse.ArgumentParser()

    par.add_argument("community", type=str, help="Local path of community repository")
    args = par.parse_args()

    openeuler_repo_yaml = load_yaml(args.community, "repository/openeuler.yaml")
    openeuler_repos = openeuler_repo_yaml["repositories"]
    srcopeneuler_repo_yaml = load_yaml(args.community, "repository/src-openeuler.yaml")
    srcopeneuler_repos = srcopeneuler_repo_yaml["repositories"]
    sigs_yaml = load_yaml(args.community, "sig/sigs.yaml")
    sigs = sigs_yaml["sigs"]
 
    os.makedirs(os.path.join(args.community, "repository/openeuler"), exist_ok=True)    
    for openeuler_repo in openeuler_repos:
        dn = os.path.join(args.community, "repository/openeuler", openeuler_repo["name"][0].lower())
        fn = os.path.join(dn, openeuler_repo["name"]+".yaml")
        if not os.path.exists(dn):
            os.mkdir(dn)
        with open(fn, "w") as repo_yaml:
            yaml.dump(openeuler_repo, repo_yaml, sort_keys=False)

    os.makedirs(os.path.join(args.community, "repository/src-openeuler"), exist_ok=True)    
    for srcopeneuler_repo in srcopeneuler_repos:
        dn = os.path.join(args.community, "repository/src-openeuler", srcopeneuler_repo["name"][0].lower())
        fn = os.path.join(dn, srcopeneuler_repo["name"]+".yaml")
        if not os.path.exists(dn):
            os.mkdir(dn)
        with open(fn, "w") as repo_yaml:
            yaml.dump(srcopeneuler_repo, repo_yaml, sort_keys=False)

    for sig in sigs:
        sig_name = sig["name"]
        sig_dn = os.path.join(args.community, "sig", sig_name)
        repos = sig["repositories"]
        for repo in repos:
            org, code = repo.split("/")
            new_path = os.path.join(args.community, "sig", sig_name, org, code[0].lower())
            os.makedirs(new_path, exist_ok=True)
            old_path = os.path.join(args.community, "repository", org, code[0].lower(), code+".yaml")
            if not os.path.exists(old_path):
                print(repo + " not exist")
            else:
                os.rename(old_path, os.path.join(new_path, code+".yaml"))


