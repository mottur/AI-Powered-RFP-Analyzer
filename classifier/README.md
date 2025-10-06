---
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
widget:
- text: 'Initiative Scope and Boundaries

    The scope of work for this engagement includes a full security audit of all public-facing
    web applications and the internal network. This involves vulnerability scanning,
    penetration testing, and social engineering exercises. The project is explicitly
    bounded to the corporate network within the North American data centers and will
    not extend to third-party vendor systems or recently acquired international subsidiaries,
    which are under a separate assessment program.'
- text: 'Scope of Work and Key Assumptions

    This initiative aims to develop a centralized data analytics platform to unify
    reporting across the enterprise. The scope of work includes requirements gathering,
    data pipeline development, warehouse design, and dashboard creation. The project
    assumes that source system owners will provide timely access to data and subject
    matter experts. The boundaries of this project are strictly limited to the five
    source systems listed in Appendix A; integrating additional data sources is considered
    out of scope and must be handled through a separate change request.'
- text: 'Containerization and Orchestration

    All application components must be containerized using Docker and deployed onto
    a Kubernetes cluster (version 1.24+). Helm charts must be provided for all deployments
    to manage configuration and releases consistently across development, staging,
    and production environments.'
- text: 'Scope of Work Overview

    The scope encompasses the complete lifecycle of the mobile application development,
    from initial concept and market research to deployment on the Apple App Store
    and Google Play Store. This includes UI/UX design, development for both iOS and
    Android platforms, and backend API integration. The project is bounded to the
    feature set described in Appendix A and assumes that third-party API providers
    (e.g., for payment processing) will maintain service level agreements.'
- text: 'Documentation Deliverables

    The offeror shall provide the following documentation: System Administrator Guide,
    API Reference Guide, User Acceptance Test (UAT) Plans and Scripts, Security Controls
    Assessment report, and a Disaster Recovery Runbook. All documentation must adhere
    to the agency''s template and style guide provided in Section J of this RFP.'
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
      value: 1.0
      name: Accuracy
    - type: precision
      value: 1.0
      name: Precision
    - type: recall
      value: 1.0
      name: Recall
    - type: f1_score
      value: 1.0
      name: F1_Score
    - type: confusion_matrix
      value:
      - - 3
        - 0
        - 0
        - 0
        - 0
      - - 0
        - 4
        - 0
        - 0
        - 0
      - - 0
        - 0
        - 5
        - 0
        - 0
      - - 0
        - 0
        - 0
        - 4
        - 0
      - - 0
        - 0
        - 0
        - 0
        - 4
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
| Label                                                                                                                                                              | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scope - This section describes the scope of the project, including project goals, boundaries, assumptions, and background context.                                 | <ul><li>"Background and Project Context\nThe current website suffers from outdated technology that is no longer supported, leading to security vulnerabilities and a poor user experience. This project will rebuild the public-facing site on a modern content management system to empower content editors and improve accessibility compliance. The scope encompasses the complete content migration, user training, and a one-year warranty period. It is assumed that the site's information architecture and core content will remain largely unchanged unless improvements are identified during the discovery phase."</li><li>"Goals and Out-of-Scope Items\nThe primary goal is to enhance cybersecurity posture by implementing a multi-factor authentication (MFA) solution for all internal applications. The scope includes the procurement of a vendor product, configuration, integration with existing systems, and user rollout. Specifically out of scope are any hardware upgrades to end-user workstations and the development of custom MFA software. This project operates under the assumption that the chosen vendor solution will be compatible with the agency's existing identity provider."</li><li>"Project Objectives and Boundaries\nThe goal of this project is to modernize the legacy customer relationship management (CRM) system to improve data accuracy and user efficiency. The scope includes the analysis, design, development, and implementation of a new cloud-based SaaS solution. This project is bounded to the integration with the existing Oracle financial system and the agency's Active Directory; it does not include any upgrades to those external systems. A key assumption is that the current data quality in the legacy system is sufficient for migration without extensive cleansing."</li></ul> |
| Timeline - This section outlines the timeline, including the length of the contract, deadlines, project start and end dates, and other key milestone schedules.    | <ul><li>'Project Schedule and Key Milestones\nThe total period of performance for this contract shall be 12 months from the date of award. Key milestones include: Completion of Requirements Gathering by Month 1, Final Design Approval by Month 3, System Implementation by Month 8, User Acceptance Testing (UAT) by Month 10, and Final Project Sign-off by Month 12. The contractor must provide a detailed Gantt chart outlining all activities and dependencies.'</li><li>'Project Milestone Dates\nKick-off Meeting: January 15, 2025; Finalized Project Charter: January 29, 2025; Hardware Procurement Completed: March 15, 2025; Data Migration Completed: June 30, 2025; User Training Completed: August 15, 2025; Project Closeout: September 30, 2025.'</li><li>"Critical Path Deadlines\nThe project has the following non-negotiable deadlines: Environment provisioning must be complete by 2024-10-31. Data migration must be completed by 2025-01-15. Full operational capability (FOC) must be achieved by 2025-06-30. The contractor's proposed schedule must demonstrate how these key dates will be met."</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Deliverables - This section lists the deliverables or tangible outputs the offeror/contractor is required to provide.                                              | <ul><li>'Design Phase Deliverables\nThe deliverables for the design phase shall include: User Personas, Customer Journey Maps, a Sitemap, an Interactive Prototype, and a UI Style Guide with a complete component library for developers.'</li><li>'Analysis Deliverables\nThe primary deliverable for the discovery phase is a Detailed Requirements Specification document, which must include functional requirements, non-functional requirements, and a traceability matrix linking requirements to proposed solutions.'</li><li>'Documentation Deliverables\nThe contractor is required to furnish detailed documentation, including a System Architecture Diagram, Network Security Plan, Database Schema Documentation, and a full set of Operational Runbooks for the IT support team.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Technologies - This section specifies the tech stack - the environment, technologies, platforms, software, or tools that will be used or required for the project. | <ul><li>'Data Analytics and Reporting Tools\nThe business intelligence module must utilize Tableau Server 2022.2 for generating dashboards and reports. Data must be ingested into the analytics platform using Apache NiFi pipelines and processed using PySpark scripts running on a Databricks platform.'</li><li>"Security and Compliance Technologies\nAll application authentication must integrate with the client's existing PingFederate instance for SAML 2.0-based single sign-on (SSO). Static code analysis must be performed using SonarQube, and dynamic scanning must be conducted with the OWASP ZAP tool prior to each release."</li><li>'Required Technology Stack\nThe solution must be developed using the .NET 6 framework for backend services. The frontend must be built using the React 18 library with TypeScript. The database must be Microsoft SQL Server 2019 or later. All code must be managed in a Git repository and deployed via Azure DevOps pipelines.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Company Info - This section provides information about the offeror/contractor, including qualifications, past experience, and mission.                             | <ul><li>'Key Personnel Resumes\nThe offeror must identify the proposed Project Manager, Lead Architect, and Lead Data Scientist assigned to this effort. For each key personnel, provide a resume that outlines their specific experience with cloud migration projects, relevant certifications (e.g., PMP, AWS Solutions Architect), and their role and duration on projects of similar size and complexity. Resumes shall not exceed two pages each.'</li><li>'Employee Qualifications and Expertise\nThe offeror shall detail the overall qualifications of their workforce including the percentage of staff with advanced degrees, professional certifications, and security clearances. The proposal must provide statistics on average years of experience in relevant technical domains and federal contracting. The offeror shall describe their approach to maintaining a highly skilled and technically competent workforce.'</li><li>"Client Testimonials and Success Stories\nThe offeror must provide at least five client testimonials from previous government or commercial clients that demonstrate the company's performance excellence. The proposal shall include specific examples of successful project delivery, problem-solving capabilities, and client satisfaction. Each testimonial must include the client organization, project scope, and measurable outcomes achieved."</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Evaluation

### Metrics
| Label   | Accuracy | Precision | Recall | F1_Score | Confusion_Matrix                                                                      |
|:--------|:---------|:----------|:-------|:---------|:--------------------------------------------------------------------------------------|
| **all** | 1.0      | 1.0       | 1.0    | 1.0      | [[3, 0, 0, 0, 0], [0, 4, 0, 0, 0], [0, 0, 5, 0, 0], [0, 0, 0, 4, 0], [0, 0, 0, 0, 4]] |

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
preds = model("Containerization and Orchestration
All application components must be containerized using Docker and deployed onto a Kubernetes cluster (version 1.24+). Helm charts must be provided for all deployments to manage configuration and releases consistently across development, staging, and production environments.")
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
| Training set | Min | Median | Max |
|:-------------|:----|:-------|:----|
| Word count   | 15  | 54.1   | 117 |

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
| 0.0056 | 1    | 0.2413        | -               |
| 0.2778 | 50   | 0.1147        | -               |
| 0.5556 | 100  | 0.0152        | -               |
| 0.8333 | 150  | 0.0065        | -               |

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