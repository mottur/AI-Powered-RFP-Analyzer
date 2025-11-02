---
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
widget:
- text: 'Information Security Non-Disclosure

    The resultant Contract will be in accordance with the information security and
    non-disclosure terms and conditions as prescribed by FWS IT security policy.'
- text: 'Solution Overview

    The professional services provider must work with ADB AI Lab and Big Data team
    to build a production ready AI and big data solutions, required activities below
    provide further details.'
- text: 'Scope of Work Overview

    The scope encompasses the complete lifecycle of the mobile application development,
    from initial concept and market research to deployment on the Apple App Store
    and Google Play Store. This includes UI/UX design, development for both iOS and
    Android platforms, and backend API integration. The project is bounded to the
    feature set described in Appendix A and assumes that third-party API providers
    (e.g., for payment processing) will maintain service level agreements.'
- text: 'Deliverables

    All written deliverables shall be created in a professional manner and shall include
    meeting summaries, background information, and any appropriate research material
    where requested. All non-branded deliverables shall be submitted in an editable
    (i.e., unprotected) format such as Microsoft Word, Excel, or PowerPoint when applicable.
    All Deliverables will be submitted on or before the due date specified or submitted
    in accordance with a later scheduled date determined by FWS. The following deliverables
    will be prepared by or updated by the Contractor: ● Project plan and schedule
    ● Documentation of any design adjustments that will take place to ‘as-is’ site
    – in form of wire frame/mockup, or written explanations for simple adjustments
    ● End user guidance for site owners as requested ● Drupal Site Pages (Finished
    Product)'
- text: 'Understanding of the Need (10 points total)

    The Offeror shall reflect their knowledge and understanding of the Statement of
    Work (SOW) requirements contained in the RFQ. The Offeror shall explain, in their
    own words, a detailed understanding of the purpose of this RFQ and how well they
    can achieve the scope/objectives of the hypothetical scenario projects and tasks
    as defined in the SOW. The Offeror shall demonstrate their understanding of HRSA
    internal and external operating environment/partners (e.g., HRSA Bureaus and Offices,
    Hospitals, Universities, Health Centers, etc.)'
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
      value: 0.8472222222222222
      name: Accuracy
    - type: precision
      value: 0.852141500474834
      name: Precision
    - type: recall
      value: 0.8472222222222222
      name: Recall
    - type: f1_score
      value: 0.84310830813807
      name: F1_Score
    - type: confusion_matrix
      value:
      - - 12
        - 2
        - 0
        - 0
        - 0
      - - 0
        - 13
        - 1
        - 0
        - 0
      - - 0
        - 3
        - 8
        - 3
        - 0
      - - 1
        - 0
        - 1
        - 22
        - 0
      - - 0
        - 0
        - 0
        - 0
        - 6
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
| Label                                                                                                                                                              | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scope - This section describes the scope of the project, including project goals, boundaries, assumptions, and background context.                                 | <ul><li>'Scope and Key Assumptions\nThis project involves migrating the entire email and collaboration suite from an on-premise exchange server to Microsoft 365. The scope includes tenant setup, mailbox migration, DNS record changes, and user training. A fundamental assumption is that all user workstations meet the minimum software requirements for Office 365 ProPlus. The project is bounded to corporate email and does not include the migration of file shares or departmental SharePoint sites.'</li><li>'Assumptions\nThe Service assumes the following in regard to contractor approach: • While it is intended that the contractor approaches the site rebuild effort with an eye towards design improvements, it is not expected to be a full-fledged redesign effort - the most important requirements are focused on ease of managing the content on the site (in other words, the Service does not intend to spend an abundance of time on a completely new design) • There are two main parts to the CMS: (1) A content management interface allowing content creators to work with content directly by inputting content via templates and (2) a front-end display that takes the content entered into templates and renders it as a cohesive working website. Content entry forms should be configured with ease of use/simplicity as a priority'</li><li>'Scope of Work and Key Assumptions\nThis initiative aims to develop a centralized data analytics platform to unify reporting across the enterprise. The scope of work includes requirements gathering, data pipeline development, warehouse design, and dashboard creation. The project assumes that source system owners will provide timely access to data and subject matter experts. The boundaries of this project are strictly limited to the five source systems listed in Appendix A; integrating additional data sources is considered out of scope and must be handled through a separate change request.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Timeline - This section outlines the timeline, including the length of the contract, deadlines, project start and end dates, and other key milestone schedules.    | <ul><li>'Testing Phase Duration\nThe integrated testing phase is allocated a duration of 8 weeks. System Integration Testing (SIT) will occur from April 1 to April 30. User Acceptance Testing (UAT) will be conducted by the client from May 1 to May 26, with Memorial Day (May 25) excluded. The week of May 27 is reserved for remediation of any UAT findings.'</li><li>'Project Milestone Dates\nKick-off Meeting: January 15, 2025; Finalized Project Charter: January 29, 2025; Hardware Procurement Completed: March 15, 2025; Data Migration Completed: June 30, 2025; User Training Completed: August 15, 2025; Project Closeout: September 30, 2025.'</li><li>'Period of Performance\nThe period of performance of this contract will be for 12 months beginning on the date of award. *Subject to further interpretation of the estimated requirements'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Deliverables - This section lists the deliverables or tangible outputs the offeror/contractor is required to provide, including documentation.                     | <ul><li>'Contractual Deliverables Schedule\nDeliverables are due according to the following milestones: a signed-off Project Charter by Week 2, High-Fidelity Wireframes by Week 6, a Functional Prototype for User Acceptance Testing by Week 12, and the Final Deployed System by Week 16.'</li><li>'Final Project Deliverables\nAcceptance of the project is contingent upon the delivery of the following items: the final application codebase, all environment installation scripts, a certificate of cybersecurity penetration testing from a recognized firm, and signed proof of data destruction from the legacy servers.'</li><li>'Training and Transition Deliverables\nAs part of the knowledge transfer, the offeror must deliver a series of three (3) training workshops for end-users and administrators, along with recorded video tutorials and a searchable FAQ knowledge base portal.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Technologies - This section specifies the tech stack - the environment, technologies, platforms, software, or tools that will be used or required for the project. | <ul><li>'Containerization and Orchestration\nAll application components must be containerized using Docker and deployed onto a Kubernetes cluster (version 1.24+). Helm charts must be provided for all deployments to manage configuration and releases consistently across development, staging, and production environments.'</li><li>'Environment and Tech Stack\nThe solution must be developed using a modern, open-source tech stack. The backend shall be built in Python 3.9+ utilizing the Django web framework. The frontend must be implemented in React.js (v18+) with TypeScript. The database layer shall use PostgreSQL (v14+). All code must be containerized using Docker and orchestrated via Kubernetes. Version control is mandatory using Git in a GitHub repository.'</li><li>'Technical Approach for Hypothetical #1, Cloud Readiness and Enhancements - 10 points\nHRSA Test Harness is an Enterprise Test Automation Platform that standardizes automated testing processes and promotes collaboration across multiple vendors to support the HRSAs IT mission. The framework supports industry standard testing methodologies such as Data Driven Testing (DDT) and Behavior Driven Development (BDD). It provides an interface to users to define workflows to automate functional testing for an application. These workflows can then be executed against various environments as the software propagates from lower environments to higher ensuring the integrity and quality of the software product. The solution provides the capability for users to create test suites within the application UI with little or no coding. The configured test suites can then be executed either on demand or on a schedule in any given environment. All tests provide detailed reports that allows the user to identify potential defects with the product(s) being tested. The Test Automation Framework natively integrates with enterprise products like Jira for incident management, Jenkins for CI/CD, JMeter for performance testing, and RedGate for test data generation.  Current Challenges Current Test automation Test automation framework is designed to support and implement the automation tests for EHBs. Solution shall consider refactoring / Re-engineering the existing Test automation framework for cloud adoption and readiness. Proposed solution shall also consider  disaster recovery, loosely coupled architecture for APIs, Test Framework execution by bureaus in a containers, incremental modernization, maintaining backward compatibility until the system is fully modernized and migrated, system performance, scalability and cost savings in cloud space using the combination of Infrastructure as Service (IaaS), Platform as Service (PaaS) and Software as Service (SaaS). HRSA is also looking for a riskless migration path to modernize the system in specified duration without impacting business and performance of the current system. Please describe your strategy and approach for Cloud readiness and modernization. Specifically, the Offeror shall address the following requirements: \uf0b7 Review and provide the strategy for cloud adoption and readiness. \uf0b7 Propose the Cloud readiness architecture for all the core components of test harness. The modernization strategy should align with continuous delivery principles. \uf0b7 Enhance Test Harness platform to natively support cloud API testing and provision for third party tools integration \uf0b7 Create service containers for portability, management and test execution. \uf0b7 Ensure Data integrity and protection during transit and at rest. \uf0b7 Cloud adoption strategy should include o Configure auto scaling for performance and maximum throughput o Monitor, measure and Enhance security posture for cloud adoption \uf0b7 Interfaces and systems need to be covered while planning the cloud migration o Detect coordination problems in cloud environment – this is to ensure the applications are well configured with cloud environment'</li></ul> |
| Company Info - This section provides information about the offeror/contractor, including qualifications, past experience, and mission.                             | <ul><li>"Corporate Compliance and Regulatory Experience\nThe offeror must detail their experience with federal compliance requirements including FAR, DFARS, and other applicable regulations. The proposal shall describe the offeror's internal compliance programs, audit processes, and experience with government audits. The offeror shall provide examples of successfully navigating complex regulatory environments."</li><li>"Corporate History and Founding Principles\nThe offeror shall provide a detailed corporate history including founding date, original mission statement, and key company development milestones. The proposal must describe the offeror's core values and cultural principles that guide business operations. The offeror shall include information about corporate ownership structure and any parent company or subsidiary relationships."</li><li>"Corporate Risk Management Approach\nThe offeror must describe their corporate risk management philosophy and risk mitigation strategies. The proposal shall detail the offeror's experience managing risks on similar projects and their approach to identifying, assessing, and mitigating potential issues. The offeror shall include information about corporate insurance coverage and risk transfer mechanisms."</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Evaluation

### Metrics
| Label   | Accuracy | Precision | Recall | F1_Score | Confusion_Matrix                                                                         |
|:--------|:---------|:----------|:-------|:---------|:-----------------------------------------------------------------------------------------|
| **all** | 0.8472   | 0.8521    | 0.8472 | 0.8431   | [[12, 2, 0, 0, 0], [0, 13, 1, 0, 0], [0, 3, 8, 3, 0], [1, 0, 1, 22, 0], [0, 0, 0, 0, 6]] |

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
preds = model("Information Security Non-Disclosure
The resultant Contract will be in accordance with the information security and non-disclosure terms and conditions as prescribed by FWS IT security policy.")
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
| Word count   | 9   | 92.95  | 752 |

| Label                                                                                                                                                              | Training Sample Count |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| Company Info - This section provides information about the offeror/contractor, including qualifications, past experience, and mission.                             | 12                    |
| Deliverables - This section lists the deliverables or tangible outputs the offeror/contractor is required to provide, including documentation.                     | 12                    |
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
| 0.0056 | 1    | 0.281         | -               |
| 0.2778 | 50   | 0.1683        | -               |
| 0.5556 | 100  | 0.0688        | -               |
| 0.8333 | 150  | 0.0281        | -               |

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