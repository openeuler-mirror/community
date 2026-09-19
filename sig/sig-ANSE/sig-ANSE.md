# sig-ANSE
English | [简体中文](./sig-ANSE_cn.md)


Note: The Charter of this SIG follows the convention described in the openEuler charter [README](/en/governance/README.md), and follows [SIG-governance](/en/technical-committee/governance/SIG-governance.md).

## SIG Mission and Scope

### Goals of sig-ANSE

The ANSE (AI-Native Software Engineering) SIG focuses on AI-involved infrastructure software development, builds cross-tool, cross-project engineering methods covering requirements, design, coding, testing and release, and provides controllable, reliable and evolvable solutions for enterprise-level software delivery.

### Background

The coding capability of AI models is developing rapidly, expanding from code generation to the whole lifecycle of software development. However, multiple studies have shown that a high benchmark score does not necessarily mean high engineering delivery quality. When Agents take on long-chain R&D tasks, problems in scale, efficiency and quality amplify each other: Agents lack global architecture context, deviations in requirements or execution direction accumulate along the long chain, and generated results and decision processes are hard to review. Therefore, it is necessary to redesign task organization, context, constraints and verification mechanisms around human-machine collaboration, which is exactly what AI-native software engineering aims to address.

### Positioning of sig-ANSE

- **Human-machine collaborative R&D**: Humans define intent, constraints and acceptance criteria, while Agents take on task execution. Delivery is guaranteed through architecture context, engineering specifications, traceable artifacts and continuous verification.
- **AI-native software engineering**: With AI-native software engineering methods as the common technical direction, R&D processes are reconstructed around human-machine collaboration.

### Scope of sig-ANSE

- Incubate and co-build AI development tools/frameworks based on AI-native software engineering methods and concepts (with the AET project as the first incubation project).
- Establish software engineering evaluation benchmark sets for infrastructure software and publish them to the openEuler community.
- Revise and publish specifications and reference examples for AI-assisted design/coding/testing in the openEuler community.
- Organize technical exchange activities for enterprises, universities and individual developers in the openEuler community.

### Roadmap

- **August 2026**: Basic capability implementation, including architecture context and domain Agents, Spec clarification with requirements analysis and design, and workflow configuration with installation examples.
- **September 2026**: End-to-end cases and evaluation sets, including coding, self-testing and manual review points, module dependency fences and interruption recovery, link observation and change impact analysis, and Spec evaluation sets based on openEuler community projects.
- **December 2026**: Cross-project expanded reuse, targeting ≥10 evaluation tasks with reports, and ≥2 projects onboarded with specification examples.
- **From 2027**: Engineering experience accumulation and self-evolution, extracting success and failure patterns, converting experience into reusable engineering constraints, and updating Specs and rules with evaluation.

### Differences from and collaboration with existing AI-related SIGs in the openEuler community

| Stack Layer | SIG | Positioning and Goals | Differences from and Collaboration with ANSE |
| --- | --- | --- | --- |
| AI infrastructure layer | sig-AI-Infra, sig-Long | AI-Infra: AI software stack and training/inference infrastructure; Long: AI workload operation and resource management on heterogeneous fusion systems and supernodes | Technical objects clearly differ from ANSE; ANSE can support the requirements, design, coding and testing of their projects to improve development efficiency and quality |
| Agent application layer | sig-Intelligence | Intelligent Q&A, intelligent O&M and other applications and frameworks | Mainly focuses on building agent applications and their ecosystem capabilities |
| Developer engineering and tooling layer | sig-DevStation, sig-MCP-Tools-Ecosystem | DevStation: intelligent development platform and tool ecosystem; MCP Tools Ecosystem: MCP tool sharing marketplace | DevStation and MCP Tools Ecosystem mainly target Agent-form application development, debugging tools and the MCP sharing marketplace, while ANSE mainly targets traditional-form application and infrastructure software development |

ANSE and sig-DevStation have overlapping areas (general orchestration, code review and engineering processes). Both sides will focus on negotiating runtime interfaces, Skill ownership, trace data and evaluation criteria, with maintainers of both SIGs confirming the division of work, owners and acceptance criteria before piloting.

### Repositories and description managed by this SIG

- Project name: AET (Agentic Engineering Team)
  - Deliverable form: source code
  - Repository name: agentic-engineering-team
  - Project positioning: an efficient and reliable AI-assisted R&D engine to improve the efficiency and quality of infrastructure software development
  - Repository address: <https://atomgit.com/openeuler/agentic-engineering-team>

### Cross-domain and external-oriented processes

Cross-domain and externally-oriented processes and actions defined and implemented by this SIG:

- Establishment and publication process of software engineering evaluation benchmark sets for infrastructure software.
- Revision and publication process of specifications and reference examples for AI-assisted design/coding/testing in the openEuler community.
- Organization of technical exchange activities for enterprises, universities and individual developers in the openEuler community.
