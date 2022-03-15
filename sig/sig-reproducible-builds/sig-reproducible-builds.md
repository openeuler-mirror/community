# Reproducible-Builds SIG
English | [简体中文](./sig-reproducible-builds_cn.md)

## Reproducible-Builds SIG

### Mission
- Build the reproducible builds capability of RPM system in the openEuler community; any released RPM package can be bit reproduced with the same source code, build environment, dependencies, project configuration, etc.
- Upstream project patches and other works to reproducible builds community;
- Work in stages based on core packages and peripheral packages; aligning with the Debian community's reproducible build capabilities 

### Scope
- Update openEuler package release policy to include factors affecting reproducibility 
- Collaborate with https://reproducible-builds.org/ to share existing tools and experiences and contribute locally developed tools
- Build reproducible builds tooling for openEuler  
  1. automatically collects build environment, source code list, dependencies, project configuration, etc. into buildInfo format
  2. tool to restore time, build environment, project, dependencies, etc based on buildInfo file
  3. binary comparison tool, binary difference comparison visualization, automatic location
  4. automated CI testing, timely problem detection, issue reporting, automatic email push, automatic issue submission
  5. statistical analysis of the overall situation, graphical presentation
  6. classification of common problems, to give automated repair guidance
  7. support for developers and partners to restore the build environment, source code, project configuration and other information in one click to check for reproducibility
- Build a mechanism of fixing reproducibility bugs and upstreaming fixes
- Build a mechanism to collaborate with other openEuler SIG
- Operation and management of all relevante documentation, meetings, mailing lists and IRC channel

###  Repositories and description managed by this SIG

- Project name: Reproducible-Builds 
- Spec repository: openeuler/reproducible-builds

### Deliverbles:
- Packaging policy
- Documentation
- Tooling
