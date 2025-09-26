---
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
widget:
- text: 'Scope of Work Overview

    The scope encompasses the complete lifecycle of the mobile application development,
    from initial concept and market research to deployment on the Apple App Store
    and Google Play Store. This includes UI/UX design, development for both iOS and
    Android platforms, and backend API integration. The project is bounded to the
    feature set described in Appendix A and assumes that third-party API providers
    (e.g., for payment processing) will maintain service level agreements.'
- text: 'Approved Software Platforms

    All development and production work must be conducted on the Amazon Web Services
    (AWS) platform. Specifically, the use of EC2 for compute, S3 for storage, and
    RDS for PostgreSQL database instances is mandated. The use of competing cloud
    providers like Microsoft Azure or Google Cloud Platform is not permitted for this
    project.'
- text: 'Goals and Project Context

    The goal is to automate the customer onboarding workflow to reduce manual processing
    time by 70%. The project scope includes the analysis of the current state process,
    identification of automation opportunities, development of RPA bots, and implementation
    with the operations team. This initiative is bounded to the onboarding process
    for standard commercial accounts and does not include complex institutional account
    onboarding procedures.'
- text: 'Critical Path Deadlines

    The project has the following non-negotiable deadlines: Environment provisioning
    must be complete by 2024-10-31. Data migration must be completed by 2025-01-15.
    Full operational capability (FOC) must be achieved by 2025-06-30. The contractor''s
    proposed schedule must demonstrate how these key dates will be met.'
- text: 'Development and Collaboration Tools

    The development lifecycle must utilize Jira for project tracking and task management.
    Continuous integration and continuous deployment (CI/CD) must be implemented using
    GitLab CI/CD pipelines. Documentation shall be maintained in Confluence. All communication
    related to the project must be conducted through the agency''s Microsoft Teams
    channels. The offeror must demonstrate experience with all specified tools.'
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
      - - 5
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
        - 9
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
| Label                                                                                                                                                              | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scope - This section describes the scope of the project, including project goals, boundaries, assumptions, and background context.                                 | <ul><li>"Background and Project Context\nThe current website suffers from outdated technology that is no longer supported, leading to security vulnerabilities and a poor user experience. This project will rebuild the public-facing site on a modern content management system to empower content editors and improve accessibility compliance. The scope encompasses the complete content migration, user training, and a one-year warranty period. It is assumed that the site's information architecture and core content will remain largely unchanged unless improvements are identified during the discovery phase."</li><li>'Objectives and Key Assumptions\nThe primary objective is to increase customer engagement by 25% through a redesigned digital experience platform. The project scope includes user research, information architecture, UI/UX design, and front-end development for the main website and mobile app. A key assumption is that the current content management system (CMS) can support the new design with minimal backend customization. The scope excludes any changes to the underlying product database schema.'</li><li>'Assumptions\nThe Service assumes the following in regard to contractor approach: • While it is intended that the contractor approaches the site rebuild effort with an eye towards design improvements, it is not expected to be a full-fledged redesign effort - the most important requirements are focused on ease of managing the content on the site (in other words, the Service does not intend to spend an abundance of time on a completely new design) • There are two main parts to the CMS: (1) A content management interface allowing content creators to work with content directly by inputting content via templates and (2) a front-end display that takes the content entered into templates and renders it as a cohesive working website. Content entry forms should be configured with ease of use/simplicity as a priority'</li></ul> |
| Timeline - This section outlines the timeline, including the length of the contract, deadlines, project start and end dates, and other key milestone schedules.    | <ul><li>'Implementation Rollout Plan\nThe rollout will be conducted in a phased approach by geographic region: Pilot Group (Northwest Region): July 10, 2025; Phase 1 (Southwest Region): August 7, 2025; Phase 2 (Northeast Region): September 4, 2025; Full Deployment (All Remaining Regions): October 2, 2025.'</li><li>'Testing Phase Duration\nThe integrated testing phase is allocated a duration of 8 weeks. System Integration Testing (SIT) will occur from April 1 to April 30. User Acceptance Testing (UAT) will be conducted by the client from May 1 to May 26, with Memorial Day (May 25) excluded. The week of May 27 is reserved for remediation of any UAT findings.'</li><li>'Development Sprint Timeline\nDevelopment will be organized into two-week sprints. Sprint 1: Jan 10 - Jan 21; Sprint 2: Jan 24 - Feb 4; Sprint 3: Feb 7 - Feb 18; [ ... ] The final sprint, Sprint 18, is scheduled for August 15 - August 26, dedicated to final bug fixes and preparation for deployment.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Deliverables - This section lists the deliverables or tangible outputs the offeror/contractor is required to provide.                                              | <ul><li>'Contractual Deliverables Schedule\nDeliverables are due according to the following milestones: a signed-off Project Charter by Week 2, High-Fidelity Wireframes by Week 6, a Functional Prototype for User Acceptance Testing by Week 12, and the Final Deployed System by Week 16.'</li><li>'Deliverables\nAll written deliverables shall be created in a professional manner and shall include meeting summaries, background information, and any appropriate research material where requested. All non-branded deliverables shall be submitted in an editable (i.e., unprotected) format such as Microsoft Word, Excel, or PowerPoint when applicable. All Deliverables will be submitted on or before the due date specified or submitted in accordance with a later scheduled date determined by FWS. The following deliverables will be prepared by or updated by the Contractor: ● Project plan and schedule ● Documentation of any design adjustments that will take place to ‘as-is’ site – in form of wire frame/mockup, or written explanations for simple adjustments ● End user guidance for site owners as requested ● Drupal Site Pages (Finished Product)'</li><li>'Hardware and Software Deliverables\nThe contractor is responsible for delivering, installing, and configuring five (5) physical application servers, the licensed enterprise software, and a one-year warranty for all provided hardware components.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Technologies - This section specifies the tech stack - the environment, technologies, platforms, software, or tools that will be used or required for the project. | <ul><li>'Cloud Hosting and Services\nThe application must be deployed on Amazon Web Services (AWS). The architecture shall utilize AWS Elastic Kubernetes Service (EKS) for orchestration, Amazon RDS for PostgreSQL for the database, and Amazon S3 for static asset storage. The solution must employ AWS Lambda for serverless functions and use Amazon CloudFront as a content delivery network (CDN). All infrastructure must be defined as code using Terraform.'</li><li>'Content Management System\nThe public website must be built upon the WordPress VIP platform. All custom themes and plugins must be developed according to WordPress VIP coding standards and must be submitted for security review via the designated GitHub repository.'</li><li>'Database and Middleware Specifications\nThe primary data store shall be Oracle Database 19c. The application layer must use the Java Spring Boot framework (version 2.7+). Message queuing shall be implemented with Apache Kafka to ensure durable, asynchronous communication between microservices.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Company Info - This section provides information about the offeror/contractor, including qualifications, past experience, and mission.                             | <ul><li>"Subcontracting Plan and Team Structure\nIf subcontractors will be used, the offeror must provide a detailed description of each subcontractor's role, their corporate experience, and the qualifications of their proposed staff. The prime contractor must demonstrate clear management oversight of all subcontractor efforts. Provide an organizational chart for the entire proposed project team, illustrating reporting lines and communication pathways between the prime and subcontractors."</li><li>'Contacts\nContracting Officer (CO): Lorenzo Aragon; E-Mail: Lorenzo_aragon@fws.gov; Ph# 505-248-6627'</li><li>'Knowledge and Skills\nThe Contractor shall identify the resources necessary to successfully perform the work contained herein. Contractor shall possess and maintain the requisite knowledge and expertise to successfully accomplish the objectives of this Statement of Work. The Contractor will be responsible for ensuring that, at a minimum, the proposed resource(s) possesses the following: ● Proven development performance with the use of Drupal Content Management System and ● Minimum of 5 years of programing/database admin experience. ● General knowledge of DOI HR policies / processes. ● The ability to write, and verbally present complex subjects in a clear and concise manner.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## Evaluation

### Metrics
| Label   | Accuracy | Precision | Recall | F1_Score | Confusion_Matrix                                                                      |
|:--------|:---------|:----------|:-------|:---------|:--------------------------------------------------------------------------------------|
| **all** | 1.0      | 1.0       | 1.0    | 1.0      | [[5, 0, 0, 0, 0], [0, 4, 0, 0, 0], [0, 0, 9, 0, 0], [0, 0, 0, 3, 0], [0, 0, 0, 0, 4]] |

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
preds = model("Critical Path Deadlines
The project has the following non-negotiable deadlines: Environment provisioning must be complete by 2024-10-31. Data migration must be completed by 2025-01-15. Full operational capability (FOC) must be achieved by 2025-06-30. The contractor's proposed schedule must demonstrate how these key dates will be met.")
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
| Word count   | 9   | 58.55  | 218 |

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
| 0.0056 | 1    | 0.2427        | -               |
| 0.2778 | 50   | 0.1234        | -               |
| 0.5556 | 100  | 0.0165        | -               |
| 0.8333 | 150  | 0.0063        | -               |

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