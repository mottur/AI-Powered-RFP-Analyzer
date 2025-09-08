---
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
widget:
- text: 'Corporate Experience Profile

    We have served over 200 clients in the financial services and healthcare sectors,
    providing us with deep regulatory knowledge of HIPAA and FINRA requirements. This
    extensive experience ensures our solutions are built with compliance and security
    as foundational principles from the outset.'
- text: 'Warranty and Support Period

    Following the system acceptance date, the vendor will provide a 90-day warranty
    period for bug fixes and critical support at no additional cost. Thereafter, an
    optional annual maintenance and support agreement will be available, commencing
    on the first anniversary of the go-live date.'
- text: 'Weekly Deliverables Schedule

    The vendor shall provide a weekly status report every Friday by 12:00 PM EST.
    Bi-weekly sprint demos will be held every other Wednesday at 10:00 AM EST, commencing
    on the second week of the contract.'
- text: 'Implementation Rollout Plan

    The rollout will be conducted in a phased approach by geographic region: Pilot
    Group (Northwest Region): July 10, 2025; Phase 1 (Southwest Region): August 7,
    2025; Phase 2 (Northeast Region): September 4, 2025; Full Deployment (All Remaining
    Regions): October 2, 2025.'
- text: 'Monthly Deliverables

    The vendor shall provide a written Monthly Status Report by the 5th business day
    of each month, detailing progress against the project plan, risks, issues, and
    key performance indicators (KPIs).'
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
        - 3
        - 0
        - 0
        - 0
      - - 0
        - 0
        - 3
        - 0
        - 0
      - - 0
        - 0
        - 0
        - 3
        - 0
      - - 0
        - 0
        - 0
        - 0
        - 3
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
| Label                                                                                                                                                              | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scope - This section describes the scope of the project, including its goals, boundaries, assumptions, and context.                                                | <ul><li>'Implementation Scope\nThe scope for Phase I of the implementation is limited to the core accounting and procurement modules of the new software. This includes configuration to match our business processes, user training for the finance department, and a pilot go-live. The project assumes that all business process re-engineering decisions will be finalized before configuration begins. The scope explicitly excludes any integration with the legacy CRM system in this phase.'</li><li>"Project Objectives and Boundaries\nThe goal of this project is to modernize the legacy customer relationship management (CRM) system to improve data accuracy and user efficiency. The scope includes the analysis, design, development, and implementation of a new cloud-based SaaS solution. This project is bounded to the integration with the existing Oracle financial system and the agency's Active Directory; it does not include any upgrades to those external systems. A key assumption is that the current data quality in the legacy system is sufficient for migration without extensive cleansing."</li><li>'Scope of Services\nThe scope of this support contract includes 24/7 monitoring of server infrastructure, Level 1 and 2 helpdesk support for all internal employees, and proactive system health checks. This is bounded to corporate-owned devices and on-premise data centers; it explicitly excludes support for personal devices (BYOD) and cloud infrastructure managed by other vendors.'</li></ul> |
| Timeline - This section outlines the timeline, including the length of the contract, deadlines, project start and end dates, and other key milestone schedules.    | <ul><li>'Milestone Payment Schedule\nPayment is contingent upon the successful completion and acceptance of the following milestones: 20% upon contract signing and project kick-off, 30% upon completion and acceptance of the development phase, 30% upon successful completion of system integration testing, and the final 20% upon project closure and delivery of all final documentation. Each milestone has a hard deadline as outlined in Attachment C - Schedule of Events.'</li><li>'Development Sprint Timeline\nDevelopment will be organized into two-week sprints. Sprint 1: Jan 10 - Jan 21; Sprint 2: Jan 24 - Feb 4; Sprint 3: Feb 7 - Feb 18; [ ... ] The final sprint, Sprint 18, is scheduled for August 15 - August 26, dedicated to final bug fixes and preparation for deployment.'</li><li>"Critical Path Deadlines\nThe project has the following non-negotiable deadlines: Environment provisioning must be complete by 2024-10-31. Data migration must be completed by 2025-01-15. Full operational capability (FOC) must be achieved by 2025-06-30. The contractor's proposed schedule must demonstrate how these key dates will be met."</li></ul>                                                                                                                                                                                                                                                                                                                                                                     |
| Deliverables - This section lists the deliverables or tangible outputs the offeror/contractor is required to provide.                                              | <ul><li>"Documentation Deliverables\nThe offeror shall provide the following documentation: System Administrator Guide, API Reference Guide, User Acceptance Test (UAT) Plans and Scripts, Security Controls Assessment report, and a Disaster Recovery Runbook. All documentation must adhere to the agency's template and style guide provided in Section J of this RFP."</li><li>'Key Project Deliverables\nThe offeror shall provide the following tangible outputs: a fully configured SaaS application instance, a complete Data Migration Toolset, a comprehensive User Training Manual (both digital and print versions), and a Final Project Report detailing system performance and implementation metrics.'</li><li>'Final Project Deliverables\nAcceptance of the project is contingent upon the delivery of the following items: the final application codebase, all environment installation scripts, a certificate of cybersecurity penetration testing from a recognized firm, and signed proof of data destruction from the legacy servers.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Technologies - This section specifies the tech stack - the environment, technologies, platforms, software, or tools that will be used or required for the project. | <ul><li>'Approved Software Platforms\nAll development and production work must be conducted on the Amazon Web Services (AWS) platform. Specifically, the use of EC2 for compute, S3 for storage, and RDS for PostgreSQL database instances is mandated. The use of competing cloud providers like Microsoft Azure or Google Cloud Platform is not permitted for this project.'</li><li>'Data Platform Specifications\nThe data pipeline must be built using Apache Airflow for orchestration. Data processing shall be performed using Apache Spark (Databricks platform). The data warehouse must be implemented on Snowflake. The offeror must specify their approach to data ingestion from various SaaS platforms using tools like Fivetran or Stitch. All data must be encrypted in transit (TLS 1.2+) and at rest using AES-256 encryption.'</li><li>'Required Technology Stack\nThe solution must be developed using the .NET 6 framework for backend services. The frontend must be built using the React 18 library with TypeScript. The database must be Microsoft SQL Server 2019 or later. All code must be managed in a Git repository and deployed via Azure DevOps pipelines.'</li></ul>                                                                                                                                                                                                                                                                                                                                              |
| Company Info - This section provides background information about the offeror/contractor, including qualifications, past experience, and mission.                  | <ul><li>'Key Personnel Resumes\nThe lead architect proposed for this effort, Dr. Alan Smith, possesses a Ph.D. in Computer Science and holds active certifications as an AWS Solutions Architect Professional and Google Cloud Professional Data Engineer. He has authored three patents in the field of distributed data systems.'</li><li>"Subcontracting Plan and Team Structure\nIf subcontractors will be used, the offeror must provide a detailed description of each subcontractor's role, their corporate experience, and the qualifications of their proposed staff. The prime contractor must demonstrate clear management oversight of all subcontractor efforts. Provide an organizational chart for the entire proposed project team, illustrating reporting lines and communication pathways between the prime and subcontractors."</li><li>'Corporate Overview and History\nFounded in 2005, TechInnovate Solutions Inc. has been a trusted provider of enterprise software development and digital transformation services for over 18 years. Our mission is to empower businesses through cutting-edge technology and deep industry expertise. We are a privately-held company headquartered in Austin, Texas, with additional offices in London and Singapore.'</li></ul>                                                                                                                                                                                                                                                         |

## Evaluation

### Metrics
| Label   | Accuracy | Precision | Recall | F1_Score | Confusion_Matrix                                                                      |
|:--------|:---------|:----------|:-------|:---------|:--------------------------------------------------------------------------------------|
| **all** | 1.0      | 1.0       | 1.0    | 1.0      | [[3, 0, 0, 0, 0], [0, 3, 0, 0, 0], [0, 0, 3, 0, 0], [0, 0, 0, 3, 0], [0, 0, 0, 0, 3]] |

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
preds = model("Monthly Deliverables
The vendor shall provide a written Monthly Status Report by the 5th business day of each month, detailing progress against the project plan, risks, issues, and key performance indicators (KPIs).")
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
| Word count   | 30  | 53.4167 | 88  |

| Label                                                                                                                                                              | Training Sample Count |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| Company Info - This section provides background information about the offeror/contractor, including qualifications, past experience, and mission.                  | 12                    |
| Deliverables - This section lists the deliverables or tangible outputs the offeror/contractor is required to provide.                                              | 12                    |
| Scope - This section describes the scope of the project, including its goals, boundaries, assumptions, and context.                                                | 12                    |
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
| 0.0056 | 1    | 0.2337        | -               |
| 0.2778 | 50   | 0.1184        | -               |
| 0.5556 | 100  | 0.0117        | -               |
| 0.8333 | 150  | 0.0046        | -               |

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