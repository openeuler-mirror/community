Code for committing openEuler kernel patch
==========================================

Revision Record

| Date      | Revision Version | Section Number | Change Description | Author            |
| --------- | ---------------- | -------------- | ------------------ | ----------------- |
| 2023.3.8  | 1.0              |                | First draft        | Xiuqi Xie, Wei Li |
| 2023.8.14 | 1.1              |                |                    | Wei Li            |

1 Why use unified patch format
------------------------------

### 1.1 long term maintainability

openEuler will merge massive patches. If all patches are merged by casual
changelog format without a unified format, the git log will be messy, and
then it's hard to figure out the original patch.

### 1.2 kernel upgrade

We definitely will upgrade our openEuler kernel in someday, using strict
patch management will alleviate the pain to migrate patches during big upgrade.

### 1.3 easy for script parsing

Keyword highlighting is necessary for script parsing.

### 1.4 easy for porting to other branches/distribusion

Sufficient patch information could make porting patches or features to other
branches or other distribusion more easier.

2 Patch format definition
-------------------------

The format definition:

```
    $inclusion-tags         [M]
    from $version           [O]
    commit $id              [O]
    category: $category     [M]
    bugzilla: $bug-url      [M]
    CVE: $cve-id            [O]
    Reference: $refer-url   [O]

    --------------------------------

    original commitlog
    ...
    [additional changelog]                        [O]
    Signed-off-by:$yourname <$yourname@xxx.com>   [M]
```

[M] stands for "mandatory"
[O] stands for "optional"

### 2.1 $inclusion-tags

Patch inclusion classification make more esier to count the patches of related
areas or subsystems. This is not a complete classification, but a suggested
classification. If you don't know which one to choose, just pick the one you
think is right.

| inclusion tags      | discription                                      |
| :------------------ | :----------------------------------------------- |
| mainline inclusion  | backporting patches from linux upstream mainline |
| stable inclusion    | backporting patches from linux stable branch     |
| community inclusion | open source patches but not applied by mainline  |
| kunpeng inclusion   | patches for Kunpeng platform but not in mainline |
| ascend inclusion    | patches for Ascend platform but not in mainline  |
| dist inclusion      | patches from other distribusion                  |
| driver inclusion    | other out of tree driver patches                 |

### 2.2 $version

Please provide the uptream version of backported patches :

1. mainline-3.5, mainline-v5.4 ... if mainline inclusion;
2. stable-4.19.123, stable-v5.10.15... if stable inclusion;
3. the right version of discription if dist inclusion.

### 2.3 $id

The full commit id if mainline or stable inclusion, not needed for other inclusion.

### 2.4 $category

Could be: cleanup, bugfix, performance, feature, doc, other...

### 2.5 $bug-url

If the patch is related to bugzilla/issue, then we need add the corresponding
tag like below:

```
    bugzilla: https://gitee.com/openeuler/kernel/issues/I46HJ6
```

### 2.6 $cve-id

If the patch is related to a CVE, then we need annotate the cve id like "CVE-2020-1234",
otherwise please remove this tag.

### 2.7 $refer-url

Provide the full url for the patch or patchset reference, if community inclusion.

### 2.8 original commitlog

If the patch is backported, just leave the original commitlog as it is, or you should

describe your changes, see [Describe your changes — The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/process/submitting-patches.html#describe-your-changes).

### 2.9 additional changelog

Additional changelog should include at least one of the flollwing:

1. Why we should apply this patch
2. What real problem in product does this patch resolved
3. How could we reproduce this bug or how to test
4. Other useful information for help to understand this patch or problem

The detail information is very useful for porting patch to another kenrel branch or
kernel major upgrade.
You can also provide more details in bugzilla/issue if you want.

### 2.10 sign-off

As the same of upstream kernel community, you also need to sign your patch, see

[Sign your work - the Developer’s Certificate of Origin](https://www.kernel.org/doc/html/latest/process/submitting-patches.html#sign-your-work-the-developer-s-certificate-of-origin).

The sign-off is a simple line at the end of the explanation for the patch, like:

```
    Signed-off-by: Random J Developer <random@developer.example.org>
```

using your real name (sorry, no pseudonyms or anonymous contributions).

### 2.11 Examples

```
    mainline inclusion
    from mainline-4.10
    commit 0becc0ae5b42828785b589f686725ff5bc3b9b25
    category: bugfix
    bugzilla: https://bugzilla.openeuler.org/show_bug.cgi?id=3004

    -------------------------------------------------

    original changelog

    `<original S-O-B>`
    [The patch fixes a BUG_ON: injecting single bit ECC error
    to memory before system boot use hardware inject tools, which cause a
    large amount of CMCI during system booting.]
    Signed-off-by: Zhang San <zhangsan@huawei.com>
    Tested-by: Li Si <lisi@huawei.com>
```

3 Coding style
--------------

Coding style for openEuler kernel is as the same as native linux kernel, you can read

[Linux kernel coding style — The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/process/coding-style.html) for more details.
