---
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
widget:
- text: 'Duration

    • The engagement duration for the professional services will be for a period of
    fourteen (14) months. Renewal will depend on the satisfactory performance of the
    PSP based on the results of performance evaluation. • This SOW may be revised
    during the life of the contract based on ADB’s changing business requirements
    with the necessary adjustments on the pricing based on the required revisions
    through mutual agreement between ADB and the PSP.'
- text: 'Security and Monitoring Tools

    The proposed solution must integrate with the agency''s existing Splunk Enterprise
    instance for log aggregation and monitoring. Static application security testing
    (SAST) must be performed using Checkmarx, and dynamic testing (DAST) must use
    Qualys. Container vulnerability scanning is required using Twistlock. Identity
    and access management (IAM) must be integrated with the agency''s PingFederate
    instance for SAML 2.0 authentication.'
- text: 'Assumptions

    The Service assumes the following in regard to contractor approach: • While it
    is intended that the contractor approaches the site rebuild effort with an eye
    towards design improvements, it is not expected to be a full-fledged redesign
    effort - the most important requirements are focused on ease of managing the content
    on the site (in other words, the Service does not intend to spend an abundance
    of time on a completely new design) • There are two main parts to the CMS: (1)
    A content management interface allowing content creators to work with content
    directly by inputting content via templates and (2) a front-end display that takes
    the content entered into templates and renders it as a cohesive working website.
    Content entry forms should be configured with ease of use/simplicity as a priority'
- text: 'Weekly Deliverables Schedule

    The vendor shall provide a weekly status report every Friday by 12:00 PM EST.
    Bi-weekly sprint demos will be held every other Wednesday at 10:00 AM EST, commencing
    on the second week of the contract.'
- text: 'Background and Project Context

    The current website suffers from outdated technology that is no longer supported,
    leading to security vulnerabilities and a poor user experience. This project will
    rebuild the public-facing site on a modern content management system to empower
    content editors and improve accessibility compliance. The scope encompasses the
    complete content migration, user training, and a one-year warranty period. It
    is assumed that the site''s information architecture and core content will remain
    largely unchanged unless improvements are identified during the discovery phase.'
metrics:
- accuracy
- precision
- recall
- f1_score
- confusion_matrix
pipeline_tag: text-classification
library_name: setfit
inference: true
base_model: sentence-transformers/all-MiniLM-L6-v2
model-index:
- name: SetFit with sentence-transformers/all-MiniLM-L6-v2
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: Unknown
      type: unknown
      split: test
    metrics:
    - type: accuracy
      value: 0.819672131147541
      name: Accuracy
    - type: precision
      value: 0.8209459029131161
      name: Precision
    - type: recall
      value: 0.819672131147541
      name: Recall
    - type: f1_score
      value: 0.8159590864508899
      name: F1_Score
    - type: confusion_matrix
      value:
      - - 10
        - 0
        - 0
        - 0
        - 1
      - - 0
        - 5
        - 0
        - 1
        - 1
      - - 1
        - 1
        - 7
        - 2
        - 0
      - - 2
        - 0
        - 2
        - 19
        - 0
      - - 0
        - 0
        - 0
        - 0
        - 9
      name: Confusion_Matrix
---

# SetFit with sentence-transformers/all-MiniLM-L6-v2

This is a [SetFit](https://github.com/huggingface/setfit) model that can be used for Text Classification. This SetFit model uses [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) as the Sentence Transformer embedding model. A [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance is used for classification.

The model has been trained using an efficient few-shot learning technique that involves:

1. Fine-tuning a [Sentence Transformer](https://www.sbert.net) with contrastive learning.
2. Training a classification head with features from the fine-tuned Sentence Transformer.

## Model Details

### Model Description
- **Model Type:** SetFit
- **Sentence Transformer body:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- **Classification head:** a [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance
- **Maximum Sequence Length:** 256 tokens
- **Number of Classes:** 5 classes
<!-- - **Training Dataset:** [Unknown](https://huggingface.co/datasets/unknown) -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Repository:** [SetFit on GitHub](https://github.com/huggingface/setfit)
- **Paper:** [Efficient Few-Shot Learning Without Prompts](https://arxiv.org/abs/2209.11055)
- **Blogpost:** [SetFit: Efficient Few-Shot Learning Without Prompts](https://huggingface.co/blog/setfit)

### Model Labels
| Label                                                                                                                                                              | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scope - This section describes the scope of the project, including project goals, boundaries, assumptions, and background context.                                 | <ul><li>"Project Objectives and Boundaries\nThe goal of this project is to modernize the legacy customer relationship management (CRM) system to improve data accuracy and user efficiency. The scope includes the analysis, design, development, and implementation of a new cloud-based SaaS solution. This project is bounded to the integration with the existing Oracle financial system and the agency's Active Directory; it does not include any upgrades to those external systems. A key assumption is that the current data quality in the legacy system is sufficient for migration without extensive cleansing."</li><li>'Solution Overview\nThe professional services provider must work with ADB AI Lab and Big Data team to build a production ready AI and big data solutions, required activities below provide further details.'</li><li>'Scope of Services\nThe scope of this support contract includes 24/7 monitoring of server infrastructure, Level 1 and 2 helpdesk support for all internal employees, and proactive system health checks. This is bounded to corporate-owned devices and on-premise data centers; it explicitly excludes support for personal devices (BYOD) and cloud infrastructure managed by other vendors.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Timeline - This section outlines the timeline, including the length of the contract, deadlines, project start and end dates, and other key milestone schedules.    | <ul><li>"Critical Path Deadlines\nThe project has the following non-negotiable deadlines: Environment provisioning must be complete by 2024-10-31. Data migration must be completed by 2025-01-15. Full operational capability (FOC) must be achieved by 2025-06-30. The contractor's proposed schedule must demonstrate how these key dates will be met."</li><li>'Project Timeline\nThe engagement will be for a period of fourteen (14) months. Renewal will depend on the satisfactory performance evaluation.'</li><li>'Proposed Project Phases\nPhase 1 (Discovery & Planning): Weeks 1-4; Phase 2 (Design & Prototyping): Weeks 5-12; Phase 3 (Development): Weeks 13-28; Phase 4 (Testing & Quality Assurance): Weeks 29-36; Phase 5 (Deployment & Transition): Weeks 37-40; Phase 6 (Post-Launch Support): Weeks 41-52.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Deliverables - This section lists the deliverables or tangible outputs the offeror/contractor is required to provide.                                              | <ul><li>'Documentation Deliverables\nThe contractor is required to furnish detailed documentation, including a System Architecture Diagram, Network Security Plan, Database Schema Documentation, and a full set of Operational Runbooks for the IT support team.'</li><li>"Final Project Deliverables\nUpon project completion, the contractor must provide the following: 1) All project code and artifacts transferred to the government's GitHub Enterprise repository. 2) A lessons-learned report conducted with the project team. 3) A production support handoff plan. 4) A 30-day warranty period for all delivered software following acceptance. 5) As-built architecture diagrams reflecting the final deployed state."</li><li>'List of Key Deliverables\nThe contractor shall provide the following tangible outputs: 1) A fully deployed and configured multi-tenant SaaS platform on Azure. 2) Complete source code and architecture documentation deposited in a designated GitHub repository. 3) A user training manual and two live training sessions for end-users. 4) A final project report detailing system performance metrics and deployment architecture.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Technologies - This section specifies the tech stack - the environment, technologies, platforms, software, or tools that will be used or required for the project. | <ul><li>'Technical Approach for Hypothetical #1, Cloud Readiness and Enhancements - 10 points\nHRSA Test Harness is an Enterprise Test Automation Platform that standardizes automated testing processes and promotes collaboration across multiple vendors to support the HRSAs IT mission. The framework supports industry standard testing methodologies such as Data Driven Testing (DDT) and Behavior Driven Development (BDD). It provides an interface to users to define workflows to automate functional testing for an application. These workflows can then be executed against various environments as the software propagates from lower environments to higher ensuring the integrity and quality of the software product. The solution provides the capability for users to create test suites within the application UI with little or no coding. The configured test suites can then be executed either on demand or on a schedule in any given environment. All tests provide detailed reports that allows the user to identify potential defects with the product(s) being tested. The Test Automation Framework natively integrates with enterprise products like Jira for incident management, Jenkins for CI/CD, JMeter for performance testing, and RedGate for test data generation.  Current Challenges Current Test automation Test automation framework is designed to support and implement the automation tests for EHBs. Solution shall consider refactoring / Re-engineering the existing Test automation framework for cloud adoption and readiness. Proposed solution shall also consider  disaster recovery, loosely coupled architecture for APIs, Test Framework execution by bureaus in a containers, incremental modernization, maintaining backward compatibility until the system is fully modernized and migrated, system performance, scalability and cost savings in cloud space using the combination of Infrastructure as Service (IaaS), Platform as Service (PaaS) and Software as Service (SaaS). HRSA is also looking for a riskless migration path to modernize the system in specified duration without impacting business and performance of the current system. Please describe your strategy and approach for Cloud readiness and modernization. Specifically, the Offeror shall address the following requirements: \uf0b7 Review and provide the strategy for cloud adoption and readiness. \uf0b7 Propose the Cloud readiness architecture for all the core components of test harness. The modernization strategy should align with continuous delivery principles. \uf0b7 Enhance Test Harness platform to natively support cloud API testing and provision for third party tools integration \uf0b7 Create service containers for portability, management and test execution. \uf0b7 Ensure Data integrity and protection during transit and at rest. \uf0b7 Cloud adoption strategy should include o Configure auto scaling for performance and maximum throughput o Monitor, measure and Enhance security posture for cloud adoption \uf0b7 Interfaces and systems need to be covered while planning the cloud migration o Detect coordination problems in cloud environment – this is to ensure the applications are well configured with cloud environment'</li><li>'Technical Approach for Hypothetical #5, Robotic Process Automation (RPA) and Data\nGeneration Testing - 10 points HRSA Test Harness is an Enterprise Test Automation Platform that standardizes automated testing processes and promotes collaboration across multiple vendors to support the HRSAs IT mission. Test Automation framework is currently hosted in HRSA network and leveraged for EHB Test Automation activities. Electronic handbooks contains more than 60 modules supporting the different bureau policy changes. Legislative and business policy changes trigger frequent releases, causing challenges in verification and validation activities. Current Challenges In an agile business environment, system changes are required to release every week to support the legislative mandate. During the release process, testing team has to invest several hours in creating test data for functional, regression, and integration testing. In addition, EHBs trainers follow manual process to create training data every two weeks for conducting the user trainings and demos. Those challenges are resulting inefficiency and overheard, operation cost is going high. Here is the summary of the challenges:'</li><li>'Security compliance - ensuring that all enhancements meet the HRSA’s security\nrequirements. The Offeror should describe their strategy and approach to apply unique methodologies, automation frameworks, tools, and techniques to perform usability, accessibility and security compliance testing for ongoing enhancements and upgrades. Specifically, the Offeror shall address the following requirements: \uf0b7 Propose a cost-effective and innovative approach to perform usability testing. \uf0b7 Provide a build-test optimized model to promote agility and automation of Test scripts and test harness platform \uf0b7 Solution must be compatible and address challenges specific to portability, reliability and scalability. \uf0b7 Propose an approach, tools and techniques to perform usability, accessibility, security compliance and cross browser compatibility, performance, and integration and role bases testing. \uf0b7 Provide an automated regression test strategy and outline a test architecture to simplify the regression testing challenges. The proposed strategy should be feasible, realistic, and actionable. \uf0b7 Propose effective solution to maintain the versioning and tracing the changes in functionality to lowest level. \uf0b7 Open to integrate with third-party components or utilities and connect with open source technologies. \uf0b7 Promote effective strategies for Usability, Data generation and Training requirements. \uf0b7 Enhance the DEVSecOps Pipeline Integration process for continuous test suite integration. \uf0b7 Integration to Team Foundation Server to convert user stories to automated test cases.'</li></ul> |
| Company Info - This section provides information about the offeror/contractor, including qualifications, past experience, and mission.                             | <ul><li>'Industry Certifications and Accreditations\nThe offeror shall provide a comprehensive list of all relevant industry certifications and accreditations held by the company, including dates obtained and expiration dates. The proposal must include certifications such as ISO standards, CMMI maturity levels, and any government-sponsored certification programs. The offeror shall provide certificate numbers and issuing organizations for verification purposes.'</li><li>'Management and Staffing Plan (10 points)\nThe Offeror shall describe the overall plan for adequately staffing, organizing and managing the tasks required by this contract. The plan shall indicate how organizational roles and responsibilities will be addressed, decisions made, work monitored, and quality and timeliness of products/services will be ensured. The Offeror shall explain how this management and staffing plan will enable the Offeror to start projects quickly, move efficiently by conducting multiple tasks concurrently, complete complex tasks within narrow timeframes, and assure the quality of products/services provided. If the Offeror proposes to use any Consultants or Subcontractor employees to carry out elements within the SOW under this BPA, the management staffing plan shall specify how the Offeror, Consultants and/or Subcontractors will work together, how the tasks will be coordinated, and how quality assurance will be accomplished. The Offeror shall describe their method of how employees are recruited and maintained for long-term assignments, whether they will be full-time permanent employees, part-time employees, temporary employees, term-of-contract personnel, independent Consultants, and/or Subcontractors are used. Also, describe proposed staffing methodologies when specialized or new skills are required. The Offeror shall describe its available internal and external resources to acquire and maintain an effective and efficient work force that will support HRSA’s mission and produce timely and quality IT solutions. The Offeror shall identify all of the facilities and equipment that are available for the completion of all contract requirements. The Offeror’s should describe corporate office locations in the event staff are required to work offsite at Offeror’s site due to lack of space at HRSA facilities.'</li><li>"Corporate Compliance and Regulatory Experience\nThe offeror must detail their experience with federal compliance requirements including FAR, DFARS, and other applicable regulations. The proposal shall describe the offeror's internal compliance programs, audit processes, and experience with government audits. The offeror shall provide examples of successfully navigating complex regulatory environments."</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Evaluation

### Metrics
| Label   | Accuracy | Precision | Recall | F1_Score | Confusion_Matrix                                                                        |
|:--------|:---------|:----------|:-------|:---------|:----------------------------------------------------------------------------------------|
| **all** | 0.8197   | 0.8209    | 0.8197 | 0.8160   | [[10, 0, 0, 0, 1], [0, 5, 0, 1, 1], [1, 1, 7, 2, 0], [2, 0, 2, 19, 0], [0, 0, 0, 0, 9]] |

## Uses

### Direct Use for Inference

First install the SetFit library:

```bash
pip install setfit
```

Then you can load this model and run inference.

```python
from setfit import SetFitModel

# Download from the 🤗 Hub
model = SetFitModel.from_pretrained("setfit_model_id")
# Run inference
preds = model("Weekly Deliverables Schedule
The vendor shall provide a weekly status report every Friday by 12:00 PM EST. Bi-weekly sprint demos will be held every other Wednesday at 10:00 AM EST, commencing on the second week of the contract.")
```

<!--
### Downstream Use

*List how someone could finetune this model on their own dataset.*
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Set Metrics
| Training set | Min | Median  | Max |
|:-------------|:----|:--------|:----|
| Word count   | 8   | 77.7833 | 453 |

| Label                                                                                                                                                              | Training Sample Count |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| Company Info - This section provides information about the offeror/contractor, including qualifications, past experience, and mission.                             | 12                    |
| Deliverables - This section lists the deliverables or tangible outputs the offeror/contractor is required to provide.                                              | 12                    |
| Scope - This section describes the scope of the project, including project goals, boundaries, assumptions, and background context.                                 | 12                    |
| Technologies - This section specifies the tech stack - the environment, technologies, platforms, software, or tools that will be used or required for the project. | 12                    |
| Timeline - This section outlines the timeline, including the length of the contract, deadlines, project start and end dates, and other key milestone schedules.    | 12                    |

### Training Hyperparameters
- batch_size: (16, 2)
- num_epochs: (1, 16)
- max_steps: -1
- sampling_strategy: oversampling
- body_learning_rate: (2e-05, 1e-05)
- head_learning_rate: 0.01
- loss: CosineSimilarityLoss
- distance_metric: cosine_distance
- margin: 0.25
- end_to_end: False
- use_amp: False
- warmup_proportion: 0.1
- l2_weight: 0.01
- seed: 42
- eval_max_steps: -1
- load_best_model_at_end: False

### Training Results
| Epoch  | Step | Training Loss | Validation Loss |
|:------:|:----:|:-------------:|:---------------:|
| 0.0056 | 1    | 0.2696        | -               |
| 0.2778 | 50   | 0.1419        | -               |
| 0.5556 | 100  | 0.0361        | -               |
| 0.8333 | 150  | 0.0158        | -               |

### Framework Versions
- Python: 3.12.9
- SetFit: 1.1.3
- Sentence Transformers: 5.1.0
- Transformers: 4.49.0
- PyTorch: 2.8.0
- Datasets: 4.0.0
- Tokenizers: 0.21.4

## Citation

### BibTeX
```bibtex
@article{https://doi.org/10.48550/arxiv.2209.11055,
    doi = {10.48550/ARXIV.2209.11055},
    url = {https://arxiv.org/abs/2209.11055},
    author = {Tunstall, Lewis and Reimers, Nils and Jo, Unso Eun Seo and Bates, Luke and Korat, Daniel and Wasserblat, Moshe and Pereg, Oren},
    keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
    title = {Efficient Few-Shot Learning Without Prompts},
    publisher = {arXiv},
    year = {2022},
    copyright = {Creative Commons Attribution 4.0 International}
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->