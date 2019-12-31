# SIG  Management Guidance

All SIGs in the openEuler community have a charter that clarifies the scope and governance.

+ Scope defines what the SIG is responsible for
+ Governance rules must account for responsibilities in the SIG, as well as the roles and how the work is carried out


## How to Create a New SIG

**1. Copy the SIG group template and name it**

Fork gitee.com/openeuler/community to you gitee.


```
git clone https://gitee.com/YOURGITEE/community

cd ./community/sig

cp -r sig-template sig-YOURSIGNAME

cd sig-YOURSIGNAME

```


**2. Fill the information for the new SIG**

Please refer to [Recommendations and Requirements](./ SIG-governance-requirements.md) to complete the application for the new SIG.


```
mv sig-template_cn.md sig-YOURSIGNAME_cn.md

mv sig-template.md sig-YOURSIGNAME.md

vi sig-YOURSIGNAME_cn.md

vi sig-YOURSIGNAME.md

```

**3. Assign members for your SIG**

Edit the file OWNERS to finish the add memebers.

```
vi OWNERS

```

**4. Configure repositories which the SIG maintain**

In openEuler Community there are 2 repositories:
- **Code Source** to store the source code of software. 

- **Package Source** to store the software packages used to build the operatig system. 


```
vi ../../repository/src-openeuler.yaml

# or / and

vi ../../repository/openeuler.yaml

```

**5. Add the description for your new SIG in sigs.ymal**


```
vi ../sigs.yaml

- name: sig-YOURSIGNAME
  repositories:
  - openeuler/aaa
  - src-openeuler/bbb
```

**6. Create a new Pull Request**

Create a Pull Request on Gitee. 

**7. Send an application email to Techincal Committee**

给技术委员会发邮件（邮箱<tc@openeuler.org>），并在正文中包含主题“[*新SIG提案]*”和PR的链接

Send an application email to Technical Committee (<tc@openeuler.org>) with the title starting with [New SIG].


