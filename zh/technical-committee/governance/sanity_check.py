#!/usr/bin/python3
"""
This is a sanity checking tool for openEuler community database
"""
import yaml
import sys
import argparse
import os.path
import subprocess

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
            repo_name = repo.replace("src-openeuler/", "").replace("openeuler/", "").lower()
            supervisor = repositories.get(repo_name, set())
            supervisor.add(sig["name"])
            repositories[repo_name] = supervisor

    for k in repositories:
        v = repositories[k]
        if len(v) != 1:
            if k in exps:
                continue
            print("WARNING! " + k + ": Co-managed by these SIGs " + str(v))
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
            repo = repo.lower()
            supervisor = repositories.get(repo, set())
            if sig["name"] in supervisor:
                print("WARNING! " + repo + " has been managed by " + sig["name"] + " multiple times.")
                errors_found = errors_found + 1
            else:
                supervisor.add(sig["name"])
            repositories[repo] = supervisor

    for k in repositories:
        v = repositories[k]
        if len(v) != 1:
            if k in exps:
                continue
            print(k + ": " + str(v) + "")
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
            repo = repo.lower()
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


def check_4(exps, prefix, oe_repos, supervisors, cross_checked_repo):
    """
    YAML in repository/ should be consisitent with sigs.yaml
    """
    print("repository/{prefix}.yaml should be consisitent with sigs.yaml".format(prefix=prefix))

    errors_found = 0

    for repo in oe_repos:
        name = prefix + "/" + repo["name"].lower()
        if "type" not in repo.keys():
            print("WARNING! Repository {name} has no type tag".format(name=name))
            errors_found = errors_found + 1
            continue
            
        if name in cross_checked_repo:
            print("WARNING! Repository {name} in {prefix}.yaml has duplication.".format(name=name, prefix=prefix))
            errors_found = errors_found + 1
        if not supervisors.get(name, False):
            if name not in exps:
                print("WARNING! Repository {name} in {prefix}.yaml cannot be found in sigs.yaml"
                        .format(name=name, prefix=prefix))
                errors_found = errors_found + 1
        if repo["type"] == "public" and "Private" in supervisors.get(name, set()):
            print("WARNING! Repository {name} marked as public in {prefix}.yaml, but listed in Private SIG."
                    .format(name=name, prefix=prefix))
            errors_found = errors_found + 1

        if repo["type"] == "private" and "Private" not in supervisors.get(name, set()):
            print("WARNING! Repository {name} marked as private in {prefix}.yaml, but not listed in Private SIG."
                    .format(name=name, prefix=prefix))

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

    # if len(cross_checked_repo) != len(supervisors):

    for repo in supervisors:
        if not repo in cross_checked_repo:
            print("WARNING! {name} listed in sigs.yaml, but neither openeuler.yaml nor src-openeuler.yaml"
                    .format(name=repo))
            errors_found = errors_found + 1

    if errors_found == 0:
        print("PASS WITHOUT ISSUES FOUND.")

    return errors_found


def check_7(oe_repos, srcoe_repos):
    """
    All repositories' name must follow the gitee requirements
    """
    print("All repositories' name must follow the gitee requirements")

    errors_found = 0
    error_msg = """Repo name allos only letters, numbers, or an underscore (_), dash (-), and period (.). 
It must start with a letter, and its length is 2 to 200 characters"""

    for repos in oe_repos, srcoe_repos:
        for r in repos:
            repo_name = r["name"].lower()
            if len(repo_name) < 2 or len(repo_name) > 200:
                print("WARNING! {name} too long or too short".format(name=repo_name))
                errors_found += 1
            else:
                new_repo_name = repo_name.replace("_", "").replace("-", "").replace(".", "")
                if not new_repo_name.isalnum():
                    print("WARNING! {name} contains invalid character".format(name=repo_name))
                    errors_found += 1
                elif not repo_name[0].isalpha():
                    print("WARNING! {name} must start with a letter".format(name=repo_name))
                    errors_found += 1


    if errors_found != 0:
        print(error_msg)
    else:
        print("PASS WITHOUT ISSUES FOUND.")

    return errors_found


def check_8(oe_repos, srcoe_repos, p_oe_repos, p_srcoe_repos):
    """
    Newly added/exposed repositories must follow the OE requirements
    """
    print("Newly added/exposed repositories must follow the OE requirements")
    errors_found = 0
    error_msg = """Some newly added/exposed repositories doesn't follow the OE requirments"""

    oe_dict = {f["name"]: f for f in oe_repos}
    srcoe_dict = {f["name"]: f for f in srcoe_repos}

    remove_oe = set()
    remove_srcoe = set()

    for f in p_oe_repos:
        if f["name"] in oe_dict:
            if f["type"] == "private" and oe_dict[f["name"]]["type"] == "public":
                continue
            else:
                oe_dict.pop(f["name"])
        else:
            remove_oe.add(f["name"])

    for f in p_srcoe_repos:
        if f["name"] in srcoe_dict:
            if f["type"] == "private" and srcoe_dict[f["name"]]["type"] == "public":
                continue
            else:
                srcoe_dict.pop(f["name"])
        else:
            remove_srcoe.add(f["name"])

            
    for oe in oe_dict:
        o = oe_dict[oe]
        if len(o.get("description", "")) < 10:
            print("WARNING! openeuler/" + o["name"] + "\'s description is too short.")
            errors_found += 1
        if o.get("rename_from", "") in remove_oe:
            remove_oe.remove(o.get("rename_from"))

    for src in srcoe_dict:
        s = srcoe_dict[src]
        if s.get("upstream", "") == "":
            print("WARNING! src-openeuler/" + s["name"] + " missed upstream information.")
            errors_found += 1
        if len(s.get("description", "")) < 10:
            print("WARNING! src-openeuler/" + s["name"] + "\'s description is too short.")
            errors_found += 1
        if s.get("rename_from", "") in remove_srcoe:
            remove_srcoe.remove(s.get("rename_from"))

    for r in remove_oe:
        print("WARNING! deleting openeuler/%s."%r)
    for r in remove_srcoe:
        print("WARNING! deleting src-openeuler/%s."%r)

    if errors_found != 0:
        print(error_msg)
    else:
        print("PASS WITHOUT ISSUES FOUND.")

    return errors_found


def prepare_master_branch_yaml(d):
    """
    Helper for preparing previous openeuler.yaml and src-openeuler.yaml
    """
    o = os.getcwd()
    os.chdir(d)
    subprocess.check_output("git show master^:repository/src-openeuler.yaml > repository/src-openeuler.master.yaml",
            shell=True)
    subprocess.check_output("git show master^:repository/openeuler.yaml > repository/openeuler.master.yaml",
            shell=True)
    os.chdir(o)


def cleanup_master_branch_yaml(d):
    """
    Helper for cleaning up previous openeuler.yaml and src-openeuler.yaml
    """
    o = os.getcwd()
    os.chdir(d)
    os.remove("repository/src-openeuler.master.yaml")
    os.remove("repository/openeuler.master.yaml")
    os.chdir(o)


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

    sigs_yaml = load_yaml(args.community, "sig/sigs.yaml")
    sig_list = sigs_yaml["sigs"]
    known_exceptions_yaml = load_yaml(args.community, "zh/technical-committee/governance/exceptions.yaml")
    exception_list = known_exceptions_yaml["exceptions"]
    openeuler_repo_yaml = load_yaml(args.community, "repository/openeuler.yaml")
    openeuler_repos = openeuler_repo_yaml["repositories"]
    srcopeneuler_repo_yaml = load_yaml(args.community, "repository/src-openeuler.yaml")
    srcopeneuler_repos = srcopeneuler_repo_yaml["repositories"]
 
    repo_supervisors = {}
    repo_cross_checked = set()

    print("Sanity Check among different YAML database inside openEuler community.")
    issues_found = 0
    print("\nCheck 1:")
    issues_found = issues_found + check_1(sig_list, exception_list)

    print("\nCheck 2:")
    issues_found = issues_found + check_2(sig_list, exception_list)

    print("\nCheck 3:")
    repo_supervisors = check_3(sig_list)

    print("\nCheck 4:")
    issues, repo_cross_checked = check_4(exception_list, "openeuler", 
            openeuler_repos, repo_supervisors, repo_cross_checked)
    issues_found = issues_found + issues

    print("\nCheck 5:")
    issues, repo_cross_checked = check_4(exception_list, "src-openeuler", 
            srcopeneuler_repos, repo_supervisors, repo_cross_checked)
    issues_found = issues_found + issues

    print("\nCheck 6:")
    issues_found = issues_found + check_6(repo_cross_checked, repo_supervisors)

    print("\nCheck 7:")
    issues_found = issues_found + check_7(openeuler_repos, srcopeneuler_repos)

    prepare_master_branch_yaml(args.community)
    prev_openeuler_repos = load_yaml(args.community, "repository/openeuler.master.yaml")["repositories"]
    prev_srcopeneuler_repos = load_yaml(args.community, "repository/src-openeuler.master.yaml")["repositories"]

    print("\nCheck 8:")
    issues_found = issues_found + check_8(openeuler_repos, srcopeneuler_repos, 
            prev_openeuler_repos, prev_srcopeneuler_repos)

    cleanup_master_branch_yaml(args.community)

    sys.exit(issues_found)
