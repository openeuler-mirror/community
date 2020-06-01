#!/usr/bin/python3
import yaml
import sys
import argparse
import os.path

def check_1(sigs, exps):
    """
    Repository in src-openeuler and openeuler should be managed by the single SIG.
    """
    print("Repository in src-openeuler and openeuler should be managed by the single SIG.")

    repositories = {}
    errors_found = 0

    for sig in sigs:
        if sig["name"] == "Private":
            continue
        for repo in sig["repositories"]:
            repo_name = repo.replace("src-openeuler/", "").replace("openeuler/", "") 
            supervisor = repositories.get(repo_name, set())
            supervisor.add(sig["name"])
            repositories[repo_name] = supervisor

    for k in repositories:
        v = repositories[k]
        if len(v) != 1:
            if k in exps:
                continue
            print("WARNING! " + k + ": Co-managed by these SIGs " + str(v) + "\n")
            errors_found = errors_found + 1

    if errors_found == 0:
        print("PASS WITHOUT ISSUES FOUND.")
    return errors_found


def check_2(sigs, exps):
    """
    Repository in src-openeuler or openeuler should never be duplicated.
    """
    print("Repository in src-openeuler or openeuler should never be duplicated.")

    repositories = {}
    errors_found = 0

    for sig in sigs:
        if sig["name"] == "Private":
            continue
        for repo in sig["repositories"]:
            supervisor = repositories.get(repo, set())
            if sig["name"] in supervisor:
                print("WARNING! " + repo + " has been managed by " + sig["name"] + " multiple times.\n")
                errors_found = errors_found + 1
            else:
                supervisor.add(sig["name"])
            repositories[repo] = supervisor

    for k in repositories:
        v = repositories[k]
        if len(v) != 1:
            if k in exps:
                continue
            print(repo + ": " + v + "\n")
            errors_found = errors_found + 1

    if errors_found == 0:
        print("PASS WITHOUT ISSUES FOUND.")
    return errors_found


def check_3(sigs):
    """
    Repository managed by both SIG and Private.
    """
    print("Repository managed by both SIG and Private.")

    supervisors = {}

    for sig in sigs:
        for repo in sig["repositories"]:
            supervisor = supervisors.get(repo, set())
            supervisor.add(sig["name"])
            supervisors[repo] = supervisor

    print("There're " + str(len(supervisors)) + " repositories in total.")

    co_managed = 0
    private_only = 0

    for k in supervisors:
        v = supervisors[k]
        if "Private" in v:
            if len(v) != 1:
                co_managed = co_managed + 1
            else:
                private_only = private_only + 1
    print("There're " + str(co_managed) + " repositories co-managed by Private")
    print("There're " + str(private_only) + " repositories managed by Private only")
    return supervisors


def check_4(sigs, exps, prefix, oe_repos, supervisors, cross_checked_repo):
    """
    YAML in repository/ should be consisitent with sigs.yaml
    """
    print("repository/{prefix}.yaml should be consisitent with sigs.yaml".format(prefix=prefix))

    errors_found = 0

    for repo in oe_repos:
        name = prefix + "/" + repo["name"]
        if name in cross_checked_repo:
            print("WARNING! Repository {name} in {prefix}.yaml has duplication.".format(name=name, prefix=prefix))
            errors_found = errors_found + 1
        if not supervisors.get(name, False):
            if name not in exps:
                print("WARNING! Repository {name} in {prefix}.yaml cannot be found in sigs.yaml".format(name=name, prefix=prefix))
                errors_found = errors_found + 1
        if repo["type"] == "public" and "Private" in supervisors.get(name, set()):
            print("WARNING! Repository {name} marked as public in {prefix}.yaml, but listed in Private SIG.".format(name=name, prefix=prefix))
            errors_found = errors_found + 1

        if repo["type"] == "private" and "Private" not in supervisors.get(name, set()):
            print("WARNING! Repository {name} marked as private in {prefix}.yaml, but not listed in Private SIG.".format(name=name, prefix=prefix))
            errors_found = errors_found + 1	

        cross_checked_repo.add(name)

    if errors_found == 0:
        print("PASS WITHOUT ISSUES FOUND.")
    return errors_found, cross_checked_repo


def check_6(cross_checked_repo, supervisors):
    """
    All repositories in sigs.yaml must list in either openeuler.yaml or src-openeuler.yaml
    """
    print("All repositories in sigs.yaml must list in either openeuler.yaml or src-openeuler.yaml")
    errors_found = 0

    if len(cross_checked_repo) != len(supervisors):
        for repo in supervisors:
            if not repo in cross_checked_repo:
                print("WARNING! {name} listed in sigs.yaml, but neither openeuler.yaml nor src-openeuler.yaml".format(name=reop))
                errors_found = errors_found + 1

    if errors_found == 0:
        print("PASS WITHOUT ISSUES FOUND.")

    return errors_found


def load_yaml(d, f):
    """
    Helper for load YAML database
    """
    p = os.path.expanduser(os.path.join(d, f))
    try:
        y = yaml.load(open(p), Loader=yaml.Loader)
    except FileNotFoundError:
        print("Cannot Load {path}".format(path=p))
        print("Could be wrong path")
        sys.exit(1)
    return y


if __name__ == "__main__":
    """
      Sanity check among different YAML database inside openEuler community
    """
    par = argparse.ArgumentParser()

    par.add_argument("community", type=str, help="Local path of community repository")
    args = par.parse_args()

    sigs_yaml = load_yaml(args.community, "sig/sigs.yaml")
    sigs = sigs_yaml["sigs"]
    known_exceptions_yaml = load_yaml(args.community, "zh/technical-committee/governance/exceptions.yaml")
    exps = known_exceptions_yaml["exceptions"]
    openeuler_repo_yaml = load_yaml(args.community, "repository/openeuler.yaml")
    openeuler_repos = openeuler_repo_yaml["repositories"]
    srcopeneuler_repo_yaml = load_yaml(args.community, "repository/src-openeuler.yaml")
    srcopeneuler_repos = srcopeneuler_repo_yaml["repositories"]
 
    supervisors = {}
    cross_checked_repo = set()

    print("Sanity Check among different YAML database inside openEuler community.")
    issues_found = 0
    print("\nCheck 1:")
    issues_found = issues_found + check_1(sigs, exps)

    print("\nCheck 2:")
    issues_found = issues_found + check_2(sigs, exps)

    print("\nCheck 3:")
    supervisors =  check_3(sigs)

    print("\nCheck 4:")
    issues, cross_checked_repo = check_4(sigs, exps, "openeuler", openeuler_repos, supervisors, cross_checked_repo)
    issues_found = issues_found + issues

    print("\nCheck 5:")
    issues, cross_checked_repo = check_4(sigs, exps, "src-openeuler", srcopeneuler_repos, supervisors, cross_checked_repo)
    issues_found = issues_found + issues

    print("\nCheck 6:")
    issues_found = issues_found + check_6(cross_checked_repo, supervisors)

    sys.exit(issues_found)
