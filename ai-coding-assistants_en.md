# openEuler Community Generative AI Use and Open Source Contribution Policy

## 1. Openness Strategy

Guided by the spirit of openness, collaboration, and innovation, the openEuler community recognizes generative AI and intelligent agents as essential drivers for advancing community technologies. While we allow the use of generative AI tools in making contributions, provided such use is reasonable, transparent, and reviewable, we strictly adhere to the following principles:

* **Core Principle 1: Open & AI-Development-Oriented**

  The openEuler community actively embraces new technologies. Open to AI-centric development, we are committed to building an intelligent open-source ecosystem that is equally friendly to both human developers and AI agents. The openEuler community welcomes both developers and automated agents to contribute deeply to the community, whether through code writing, document translation, test case generation, or O&M automation.

* **Core Principle 2: Developer Ultimate Responsibility**

  AI is strictly a supporting tool for human contributors. **Human contributors hold ultimate responsibility and legal accountability for the quality of their submissions**. Whether an output is human-developed, or generated or triggered with AI assistance, contributors must assume final responsibility for the accuracy, security, compliance, and quality of their submissions. Review, merging, or publishing the submissions by community maintainers does not constitute an endorsement or warranty by the community that the AI output in the submissions is free of infringement, secure, or fit for a particular purpose.

* **Core Principle 3: Transparency and Traceability**

  Upon submission, contributors should disclose the use of AI tools, sources of third-party materials, license information, and human review status associated with the submission. The openEuler community enforces a strict metadata tracking system to fully log **critical metadata for AI-generated content, including the agent platform, model, and prompt summaries**. This guarantees a clear audit trail for AI-assisted code contributions.

## 2. Scope of Application

This policy applies to all forms of contributions submitted to the openEuler community (including but not limited to all code and documentation repositories under the openEuler organization):

* **Source code and scripts**: including various core code, test cases, and build scripts.
* **Technical documents and community content**: including API references, deployment guides, release logs, and Wiki pages.
* **Configurations and metadata**: including Containerfiles/Dockerfiles, and CI/CD configuration files.

## 3. Legal & Compliance

Any submissions incorporating AI-generated content to the openEuler community shall be governed by the following legal and compliance frameworks:

### 3.1 Contributor License Agreement (CLA)

The openEuler community implements a **Contributor License Agreement (CLA)**.

* Contributors must sign the CLA before submitting any contributions.
* According to the CLA, by submitting a contribution that contains AI-generated content to the community, the contributor is deemed to have lawful rights to dispose of that submission (e.g., having obtained sufficient authorization). The AI-generated nature of the content shall not serve as a ground to exempt the contributors from their obligations and legal liabilities pledged in the CLA.

### 3.2 Traceability: Full Logging of Key Metadata

For contributions that contain code or documents **fundamentally generated or automatically processed by AI**, contributors shall fully record and attach the following **key metadata** in both the pull request (PR) and commit message.

Commit message:
* **Co-Authored-By:** Specify the name and version of the generative AI model used (e.g., `GPT-4o`, `DeepSeek-V3`, etc.).

PR:

* **Agent Platform:** Specify the name and version of the agent platform used (e.g., `Claude Code 2.1.156`, `Qwen Code 0.16.1`, etc.).
* **Model:** Specify the name and version of the generative AI model used (e.g., `GPT-4o`, `DeepSeek-V3`, etc.).
* **Prompt Summary:** Briefly describe the core prompts or intent that guided the AI generation (e.g., `"Optimize memory allocation for Spec file"`). AI-generated content submitted with ambiguous prompts or unclear intent is prohibited.

**Example (PR):**

```text
### AI involvement in this PR:
[]  No
[x]  Yes
__1. Agent platform: Claude Code 2.1.156
__2. Model: DeepSeek-V3
__3. Prompt summary: Based on the existing code logic, complete the code, optimize logic, add missing branches, and improve annotations to help with function development and problem fixing.

### Notes for reviewers:
1. The code was developed with AI assistance. The developer has manually reviewed the logic line-by-line and verified its functionality to ensure it behaves exactly as expected.
```

**Example (commit message):**

```text
Co-Authored-By: DeepSeek-V3
```

*Note: The openEuler CI gate checks whether the AI model name in the Co-authored-by commit trailer matches the model declared in the PR. Any discrepancy between the two will cause the CI check to fail and block the PR.*

## 4. Standard Prompt for Agents

To ensure that various AI programming assistants and automated agents (such as automated PR reviewers and auto-fixing agents) strictly comply with the preceding policies when serving the openEuler community, the following **system prompt** is formulated:

```text
# Role and objective:
You are an AI agent dedicated to serving the openEuler community. Your goal is to assist human developers in contributing efficiently while strictly adhering to the compliance baseline, ensuring all outputs meet the openEuler community's compliance and quality standards.

# Core Code of Conduct

## 1. Clarify responsibilities and development orientation.
- You serve as an efficiency amplifier for developers, but you must understand that human developers will bear the ultimate legal and quality liability for your outputs. Therefore, your generated code must be clean, readable, and easy for human developers to review.
- Do not generate any complex code blocks with ambiguity, debugging difficulties, or black-box logic.

## 2. Legal and license compliance (red line)
- Do not directly replicate or paraphrase any code snippets from repositories under restrictive licenses (such as GPL-2.0, GPL-3.0, etc.) or proprietary repositories of commercially licensed software without adhering to the applicable licenses.
- If your generated code directly references specific open-source components or public algorithmic implementations, such code must retain its original copyright notices (including but not limited to preserving the copyright notices of the original components or algorithms) and license notices, which shall not be deleted or modified.

## 3. Explicit exposure of key metadata
- When assisting humans in code generation or when independently submitting PRs to openEuler repositories as an automated agent, compliance with the designated PR and commit message templates is mandatory.

- Required metadata in a PR:
  - Agent platform: [Agent platform name and version]
  - Model: [AI model name and version]
  - Prompt summary: [core prompts or intent]

- Required metadata in the commit message:
  - Co-authored-by: [AI model name and version]

## 4. openEuler technology stack adaptation
- Code style: Before submitting any code to the openEuler community, analyze the coding style of the target repository. Your modifications must strictly conform to that repository's code style guide.
- Security first: Do not introduce security vulnerabilities such as memory leaks and buffer overflows. Always prefer secure functions verified by the openEuler community.
```

## 5. Prohibited or Risky Behaviors

- Unreviewed AI outputs;
- Code that contributors cannot explain, maintain, or verify the source of;
- Content where AI clearly reproduces third-party code, documentation, images, or copyrighted expressions without providing legitimate sources, licenses, and necessary attributions;
- Content that is incompatible with the project's license;
- Content that violates AI terms of service, employer policies, confidentiality obligations, export controls, data compliance regulations, or third-party rights;
- Prompts, outputs, or contributions that contain trade secrets, personal information, sensitive data, private code, internal documents, or undisclosed vulnerability information;
- Contributions submitted in batch by AI agents or lacking substantial participation by human contributors.

## 6. Contributor Responsibilities

When submitting AI-assisted contributions to the community, contributors shall acknowledge and agree that they:

- Have manually reviewed the AI-assisted contributions to be submitted;
- Understand the technical implications, design impact, and maintenance costs of the AI-assisted contributions to be submitted;
- Have completed all necessary testing, builds, license checks, and security reviews on the AI-assisted contributions to be submitted;
- Have verified that the AI output does not introduce content incompatible with the project license;
- Have confirmed that the AI-assisted contributions do not include any known unauthorized third-party materials, or that any third-party materials, licenses, copyright notices, and attributions have been fully disclosed as required by this project;
- Have complied with all applicable policies of the contributors' employers, clients, academic institutions, or affiliated organizations regarding AI tools and open-source contributions;
- Take the same responsibility for AI-assisted contributions as for non-AI-assisted contributions.

## 7. Review and Merging Rules

Community maintainers may request modifications, additional explanations, resubmissions of AI-assisted contributions by the contributors, or reject AI-assisted contributions for any of the following reasons:

- The contributor fails to disclose information regarding the AI-assisted contribution as required;
- The contributor is unable to explain the logic or source of the submitted code;
- The contribution is substantially similar to unauthorized third-party code, documentation, or images;
- The licensing, copyright, or attribution information is unclear;
- The AI-assisted contribution is of poor quality, untested, unmaintainable, or introduces security risks;
- Automated, mass submissions of low-quality AI-assisted contributions disrupt the maintainability and operations of the community;
- The community maintainers consider the AI-assisted contribution inappropriate for merging based on the openEuler project's risk control.
