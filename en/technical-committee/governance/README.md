# SIG Management Procedure

> Note: Repository URLs and Git commands in this document use AtomGit as an example.

All SIGs in the openEuler community have a charter that clarifies the scope and governance.

+ Scope defines what the SIG is responsible for
+ Governance rules must account for responsibilities in the SIG, as well as the roles and how the work is carried out


## How to Create a New SIG

**1. Copy the SIG group template and name it**

Fork the openeuler/community repository to your code hosting platform account.


```
git clone https://atomgit.com/YOUR_ACCOUNT/community

cd ./community/sig

cp -r sig-template sig-YOURSIGNAME

cd sig-YOURSIGNAME

```


**2. Fill the information for the new SIG**

Please refer to [Recommendations and Requirements](./SIG-governance-requirements.md) to complete the application for the new SIG.


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

**4. Configure repositories which the SIG maintains**

Create a repository YAML file under the corresponding SIG directory:

- Community-maintained projects: `sig/<SIG>/openeuler/<first-letter>/<repository>.yaml`
- Introduced software packages: `sig/<SIG>/src-openeuler/<first-letter>/<repository>.yaml`

For the YAML format, see [sig/README.md](/sig/README.md). For the procedure, see [Adding a New Software Package](/en/contributors/create-package.md).

**5. Add the new SIG information to sig-info.yaml**

Open `sig/<SIG>/sig-info.yaml` and fill in the SIG name, maintainers, repositories, and other information according to [sig/README.md](/sig/README.md).

**6. Create a new Pull Request**

Create a Pull Request on the code hosting platform.

**7. Send an application email to Techincal Committee**


Send an application email to Technical Committee (<tc@openeuler.org>) with the title starting with [New SIG].


