This document provides guidance on how to participate in the openEuler community.

# Welcome

Welcome to openEuler!

- [Welcome](#welcome)
- [Before You Start](#before-you-start)
  - [Signing the CLA](#signing-the-cla)
  - [Community Code of Conduct](#community-code-of-conduct)
- [Engaging in Community Contributions](#engaging-in-community-contributions)
  - [Finding the Work of Your Interest](#finding-the-work-of-your-interest)
    - [Introduction to the SIG](#introduction-to-the-sig)
    - [Find the SIG or Project of Your Interest](#find-the-sig-or-project-of-your-interest)
  - [Starting Your Contribution](#starting-your-contribution)
    - [Assign an Issue to Yourself](#assign-an-issue-to-yourself)
    - [Raise Problems or Suggestions](#raise-problems-or-suggestions)
    - [Set Up the Development Environment](#set-up-the-development-environment)
      - [Prepare the Development Environment](#prepare-the-development-environment)
      - [Download and Build Software Packages](#download-and-build-software-packages)
    - [Participate in Coding](#participate-in-coding)
      - [Understand the SIG and Development Precautions in the Project](#understand-the-sig-and-development-precautions-in-the-project)
      - [Download Code and Create a Branch](#download-code-and-create-a-branch)
      - [Build Modification and Local Verification](#build-modification-and-local-verification)
      - [Submit a PR](#submit-a-pr)
      - [Add a Software Package](#add-a-software-package)
    - [Code Review](#code-review)
  - [Testing](#testing)
  - [Engaging in Community Component Packaging](#engaging-in-community-component-packaging)
  - [Participating in Non-Code Contributions](#participating-in-non-code-contributions)
- [Installing openEuler](#installing-openeuler)
- [Disclosure of Community Security Issues](#disclosure-of-community-security-issues)
- [Participating in Community Activities](#participating-in-community-activities)
  - [Communication Methods in the Community](#communication-methods-in-the-community)
  - [Community News and Events](#community-news-and-events)
  - [Community Meetups](#community-meetups)
- [Feedback](#feedback)



# Before You Start

Welcome to openEuler!



## Signing the CLA

You must sign a [Contributor License Agreement](https://clasign.osinfra.cn/sign/Z2l0ZWUlMkZvcGVuZXVsZXI=) (CLA) before you can contribute to the community.



## Community Code of Conduct

openEuler is an open source community, which relies on the friendly development and collaboration environment jointly maintained by the members. Read and comply with the [Code of Conduct](/code-of-conduct.md) of the openEuler community before contributing to the community.



# Engaging in Community Contributions

**Welcome to join us anytime!**

The community documents can be improved (such as the one you are reading), code needs to be reviewed, functions or variables can be reconstructed or commented, and test cases can be continuously supplemented and optimized. We will help you understand the organization of openEuler SIGs and walk you through your first contribution. If you're interested, take action now!



## Finding the Work of Your Interest

### Introduction to the SIG

SIG is short for Special Interest Group. The openEuler community is organized into different SIGs to better manage and improve the work process.

- SIGs are open. Anyone is welcome to join and contribute to SIGs.
- A SIG is established for one or more specific technical topics. SIG members promote the output of deliverables and strive to make the deliverables a part of the openEuler distributions.
- Core members of the SIG lead the SIG governance. For details, see [Community Membership](./../../community-membership.md). You can accumulate experience and improve your influence while making contributions.
- Each SIG has one or more projects on Gitee. These projects have one or more repositories. The SIG deliverables are stored in these repositories.
- You can submit issues in the repository corresponding to the SIG, participate in discussion of specific issues, resolve issues, and participate in review.
- You can also communicate with other members in the SIG through the mailing list, Internet Relay Chat (IRC) channel, and video conference.



### Find the SIG or Project of Your Interest

Finding the SIG you are interested in can help you ask questions in the right place and get a quicker response from the community.

- **Method 1**: If you do not know which SIGs or projects exist, you can view the [list of SIGs](https://www.openeuler.org/en/sig/sig-list/) established in the openEuler community. You can use the list to quickly locate the SIG corresponding to the field that you are interested in. The following information about the SIG is also provided:
  
  - Projects under the SIG and the repository address of the projects
  - Communication methods in the SIG, including the mailing list and IRC channel
  - Contact information of the maintainers
  
- **Method 2**: If you know the project name, you can perform fuzzy search in the repository list of openEuler to quickly locate the home page address of the corresponding project. Generally, you can find the SIG information, communication methods, members, and contact information of the project in the **README.md** file on the project home page.

  

  If you cannot locate the SIG you are interested in using either of the preceding methods, you can send an email to community@openeuler.org for help. You are advised to use **[Development Process Question]** as the title of the email and write down the characteristics of the SIG or project that you are looking for in the content. We are glad to help.



## Starting Your Contribution

### Assign an Issue to Yourself

- **Find the issue list**: On the toolbar of the home page (repository of the project on Gitee) of the project that you are interested in, click <img src="figures/Issues-icon.jpg" style="zoom:50%;" /> to find the issue list of the SIG (for example, the issue list address of the community SIG is <https://gitee.com/openeuler/community/issues>).

- **Find an issue that you want to handle**: If you want to handle one of the issues, you can assign it to yourself. You only need to enter **/assign** or **/assign @yourself** in the comment area. The bot will assign the issue to you and your name will be displayed in the assignee list.
- **Participate in discussion within an issue**: An issue may have been discussed by participants. If you are interested in the issue, you can leave your comment in the comment area.



### Raise Problems or Suggestions

- **Raise a problem**: If you find a problem or defect and want to report it to the community, you can submit the problem by creating an issue. You only need to submit the issue to the issue list in the repository of the project. For details, see [Issue Submission and Handling Guide](issue-submit.md). When submitting a problem, comply with the issue submission rules.
- **Suggestions**: If you want to share your opinions or suggestions in the SIG, you can also submit an issue. Everyone can fully communicate and discuss about this issue. To attract more attention, you can also attach the issue link to the email and send it to everyone through the mailing list.



### Set Up the Development Environment

#### Prepare the Development Environment

If you want to contribute code, you need to prepare the openEuler development environment. For details, see [Development Environment Preparations](prepare-environment.md).



#### Download and Build Software Packages

If you want to download, modify, build, and verify the software packages provided by openEuler, see [Software Package Building](package-install.md).



### Participate in Coding

#### Understand the SIG and Development Precautions in the Project

The coding language, development environment, and coding conventions used in each SIG project may be different. If you want to understand and participate in coding, you can find the contributor guide provided by the project for developers. The guide is generally provided in the **CONTRIBUTING.md** file on the SIG home page or in **README.md** of the project repository. For details about how to find the project repository, see the [previous section](#finding-the-work-of-your-interest).

In addition to these files, the SIG may also provide other guidance information. This information is located in the specific community directory of the SIG or its projects. If you do not find related information or have questions about related information, you can submit issues in the SIG or send the issues or questions to the mailing list of the SIG to which the project belongs. If you do not receive a response for a long time, you can ask community@openeuler.org for help.



#### Download Code and Create a Branch

To contribute code, you also need to know how to download code from Gitee and merge the code through a pull request (PR). The code of the openEuler community is hosted on Gitee. For details, see [Gitee Workflow](Gitee-workflow.md). The method of using Gitee is similar to that of GitHub. If you have used GitHub before, you can have a quick look at or even skip this chapter.



#### Build Modification and Local Verification

After the modification is complete on the local branch, perform build and verification locally by referring to [Software Package Building](package-install.md).



#### Submit a PR

When you submit a PR, you are starting to contribute code to the community. For details, see [Pull Request Submission Guide](pull-requests.md).

#### Add a Software Package
openEuler can automatically create a repository with the same name on openEuler:Factory of OBS when a software package is added to Gitee. In this way, when the code is submitted to the created Gitee repository, the code compilation is automatically checked. For details, see [Adding a New Software Package](create-package.md).

### Code Review

openEuler is an open community and everyone involved is expected to be an active reviewer. For details about the roles and responsibilities of different types of contributors, see [Community Membership](community-membership.md).

**As a contributor**, to make your submissions easier to accept, you need to:

+ Comply with the coding conventions of the SIG, if any.
+ Write good commit messages.
+ If the amount of code submitted at a time is large, decompose a large commit into a series of small commits to make it easier for reviewers to understand your ideas.
+ Label the PR with the appropriate SIG and reviewer labels. The community bot will send you a message to help you better complete the entire PR process.



**As a reviewer**, it is strongly recommended that you comply with the [Code of Conduct](/code-of-conduct.md) and respect others to promote collaboration and improve yourself. When reviewing others' PRs, you can refer to a series of key review points provided in [The Gentle Art Of Patch Review](https://sage.thesharps.us/2014/09/01/the-gentle-art-of-patch-review/), which indicates that the code reviewer is expected to encourage new contributors to actively participate in the program instead of putting off reviewing contributions from new-comers and giving nit-picking comments. Therefore, pay attention to the following points during the review:

+ Whether the idea behind the contribution is reasonable.
+ Whether the structure of the contribution is correct.
+ Whether the contribution is complete.

Note: If your PR does not attract enough attention, you can ask for help through the mailing list of the SIG or send email to dev@openeuler.org.



## Testing

Testing is the responsibility of all contributors. The [QA SIG](https://gitee.com/openeuler/QA) is the official organization responsible for testing activities related to the versions of the community edition . If you want to carry out testing on your own infrastructure, see [Community Test System](https://gitee.com/openeuler/QA/blob/master/community-test-system.md).

A successful release of the community edition requires multiple types of testing activities. The code to be tested and environments required for running the tests vary with the test activity types. For details, see [Community Developer Test Contribution Guide](https://gitee.com/openeuler/QA/blob/master/community-developer-test-contribution-guide.md).



## Engaging in Community Component Packaging

You can also participate in community component packaging. For details, see the [openEuler Packaging Guide](packaging.md).



## Participating in Non-Code Contributions

If you are not interested in writing code, you can find the work of your interest in [Non-Code Contributions](non-code-contributions.md).





# Installing openEuler

See [openEuler Download](https://www.openeuler.org/en/download/).



# Disclosure of Community Security Issues

+ [Security Handling Process](https://gitee.com/openeuler/security-committee/blob/master/security-process-en.md): This document briefly describes the process for handling security issues.
+ [Security Disclosure Information](https://gitee.com/openeuler/security-committee/blob/master/security-disclosure-en.md): If you want to report security vulnerabilities, please refer to this page.



# Participating in Community Activities

## Communication Methods in the Community

Communication methods in the openEuler community include the mailing lists, IRC channels, and video conference. For details, see [openEuler Communication](../../en/communication/README.md).



## Community News and Events

Information about community meetings and technical exchanges attended or held by openEuler can be found on the [openEuler News](https://www.openeuler.org/en/interaction/news-list/) page.




## Community Meetups

The community holds developer conferences every year. Get in touch with us through contact information on [https://openeuler.org](https://openeuler.org) or send email to <dev@openeuler.org>. Come and join us!



# Feedback

If you have any questions about the contributor guide or the development process, please feel free to [tell us](community@openeuler.org) through the mailing lists and write down your questions and doubts in the email with the subject line in the format of **[Development Process Question]**. The openEuler community operations team will coordinate and assign related personnel to answer your questions.
