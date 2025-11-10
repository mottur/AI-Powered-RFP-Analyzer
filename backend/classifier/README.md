---
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
widget:
- text: 'The data creation for testing is laborious and complex requiring good understanding
    of the prior

    processes. The Offeror should describe their strategy and approach to apply unique
    methodologies, automation frameworks, tools, and techniques to automatically generate
    the data for testing and training. In addition, offeror shall also propose a method
    to integrate the process using robust data validation engine using RPA. Specifically,
    the Offeror shall address the following requirements:   Propose an automation
    regression test strategy for the specific EHB modules with data complexity including
    data centric use cases.  The automation test strategy should align with continuous
    delivery principles by integrating the services with EHBs test harness platform
     The strategy should ensure data-centric use cases and ensure that the business
    rules are validated.  The solution should ensure the data integrity and quality
    checks are performed using an automated approach  Propose an automation regression
    test approach and roll out for the data generation process that is feasible and
    realistic.'
- text: 'Scope

    • As set out in this SOW, the PSP is expected to meet each requirement in the
    delivery of efficient operational support on AI and Big Data Platforms and initiatives.'
- text: 'Place of Performance

    All work shall be performed remotely via Government Approved Remote Access solutions
    unless otherwise agreed upon.'
- text: 'Project Overview and Goals

    This initiative aims to design and deploy a comprehensive enterprise resource
    planning (ERP) system to unify financial, HR, and supply chain operations. The
    scope encompasses end-to-end process mapping, software configuration, data migration
    from legacy systems, and user acceptance testing. The project is bounded by the
    existing IT infrastructure and will not include hardware upgrades or the development
    of custom manufacturing modules.'
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
      value: 0.8918918918918919
      name: Accuracy
    - type: precision
      value: 0.8985600726777196
      name: Precision
    - type: recall
      value: 0.8918918918918919
      name: Recall
    - type: f1_score
      value: 0.8934576592277831
      name: F1_Score
    - type: confusion_matrix
      value:
      - - 16
        - 0
        - 0
        - 0
        - 1
      - - 0
        - 9
        - 1
        - 0
        - 0
      - - 0
        - 0
        - 22
        - 4
        - 0
      - - 0
        - 0
        - 2
        - 13
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
| Label                                                                                                                                                              | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scope - This section describes the scope of the project, including project goals, boundaries, assumptions, and background context.                                 | <ul><li>'Technical Approach for Hypothetical #4, 508 compliance Verification - 10 points\nHRSA Test Automation framework is currently hosted in HRSA network and leveraged for EHB Test Automation activities. Electronic handbooks contains more than 60 modules supporting the different bureau policy changes. Legislative and business policy changes trigger frequent releases, causing challenges in verification and validation activities. Current Challenges In an agile business environment, enhancements are ongoing and require frequent user engagement, usability testing, and a feedback loop. Performing manual 508 verification for all new developments and frequent system changes is a recurring and required activity to comply with EPLC process. It is important that the web pages be developed using accessibility best practices, which is often performed hastily, and sometimes is overlooked altogether. The Offeror should describe their strategy and approach to apply unique methodologies, tools, and  techniques to perform 508 compliance verification for ongoing enhancements and upgrades. Offeror shall also propose a solution to automatically execute these test scripts from DEVSecOps pipeline. Specifically, the Offeror shall address the following requirements: conformance testing tool to automatically test and scan electronic content of EHB’s. \uf0b7 Proposed tool must foster adoption in multi-vendor agile environment \uf0b7 Proposed tool should customize scanning and test ruleset parameters. \uf0b7 Control and synchronize error and remediation messages presented to users for customized rules. \uf0b7 Flag false positives and ensure the errors are not repeated in subsequent test results. \uf0b7 Categorize issues by type, frequency, and severity. \uf0b7 Integrate test tools and conformance monitoring into test automation environments (Dev/Ops). \uf0b7 Produce accessible system and report outputs for EPLC reviews'</li><li>'Service Delivery Approach\n• The delivery of the service is expected to be divided into three (3) phases. Provided below are the defined set of activities, deliverables, for each phase.'</li><li>'Quotes and revisions of quotes shall be uploaded electronically via the GSA e-Buy RFQ system under\nthe appropriate solicitation number. Offerors shall notify the Contracting Officer of any revisions to quotations before the closing date in GSA eBuy. b. Offerors shall submit quotes in response to this solicitation in English and in U.S. dollars. c. Quotes may be withdrawn at any time before award. Withdrawals are effective upon receipt of written notice by the Contracting Officer.'</li></ul> |
| Timeline - This section outlines the timeline, including the length of the contract, deadlines, project start and end dates, and other key milestone schedules.    | <ul><li>'Critical Deadline for Submission\nA critical milestone is the delivery of the beta software build for internal testing. This deliverable must be received by the client no later than 5:00 PM EST on May 15, 2025. Failure to meet this deadline may result in the assessment of liquidated damages.'</li><li>'Weekly Deliverables Schedule\nThe vendor shall provide a weekly status report every Friday by 12:00 PM EST. Bi-weekly sprint demos will be held every other Wednesday at 10:00 AM EST, commencing on the second week of the contract.'</li><li>'Phase 1 Implementation Timeline\nPhase 1 of the project must commence no later than 15 business days after contract signing and shall be completed within a 90-day period. The deadline for the Phase 1 preliminary design review is 45 days after kick-off. The final deliverable for this phase, a working prototype, is due no later than 5:00 PM EST on the 90th day.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Deliverables - This section lists the deliverables or tangible outputs the offeror/contractor is required to provide, including documentation.                     | <ul><li>'Final Project Deliverables\nAcceptance of the project is contingent upon the delivery of the following items: the final application codebase, all environment installation scripts, a certificate of cybersecurity penetration testing from a recognized firm, and signed proof of data destruction from the legacy servers.'</li><li>"•  ADB DXP\n• 10 -15 Data products • 5-8 AI Projects • Required Activities • The following activities must be part of the contractor’s deliverables: • Creation and maintenance of ADB's LLM Enterprise architecture • Software development following best practices (unit testing, creation of common libraries, CI/CD, IaC, modern UI/UX) • LLM Data Science Experimentation (Prototyping ideas of LLM applications • Production Grade Application deployment (Infrastructure Monitoring, Backup and Recovery, Cost Optimization, Performance Monitoring) • Security and Compliance (documentation & architecture compliant with ADB's security policies) • Data Platform Lifecycle (Creation of reliable and efficient data pipelines for the LLM's consumption, end to end data lineage) • Develop and Adherence to industry standard responsible ai framework"</li><li>'List of Key Deliverables\nThe contractor shall provide the following tangible outputs: 1) A fully deployed and configured multi-tenant SaaS platform on Azure. 2) Complete source code and architecture documentation deposited in a designated GitHub repository. 3) A user training manual and two live training sessions for end-users. 4) A final project report detailing system performance metrics and deployment architecture.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Technologies - This section specifies the tech stack - the environment, technologies, platforms, software, or tools that will be used or required for the project. | <ul><li>'Technical Approach (10 points)\nThe Offeror shall provide a detailed realistic description of the proposed technical approach/methodology to be used and how it will address the project requirements, scope, challenges, purpose, and vision for the Electronic Handbooks (EHBs) program. The Offeror shall demonstrate that its processes are compliant with Capability Maturity Model Integration (CMMI) Level 3 or ISO 9000 on Quality Management and provide written proof of CMMI Level 3 Certification or ISO 9000 family/series Certification at the time of quote submission. The Offeror shall demonstrate that all work activities associated with the proposed approach can be accomplished in a comprehensive manner. The Offeror shall demonstrate innovation in the proposed technical approach. Innovation is defined as continual evolution (i.e., modification, enhancement, and/or replacement) of the enterprise EHBs processing system to infuse new technologies and approaches as they become available throughout the life of the contract. The proposed approach should be results-oriented and improve e testing efficiency and the predictability of resourcing and scheduling needs. Furthermore, the approach should include a balanced input and output that is user friendly, simplistic and trackable. The Offeror shall demonstrate their ability to identify and deal with program risk, both in proactive and reactive (emergency) situations. Anticipated risks should be made clear and mitigation strategies presented proactively.'</li><li>'Database and Middleware Specifications\nThe primary data store shall be Oracle Database 19c. The application layer must use the Java Spring Boot framework (version 2.7+). Message queuing shall be implemented with Apache Kafka to ensure durable, asynchronous communication between microservices.'</li><li>'Frontend Development Requirements\nThe user interface shall be a single-page application (SPA) built with the Angular 15 framework. The application must use the NgRx library for state management and be styled according to the Google Material Design specification using Angular Material components.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Company Info - This section provides information about the offeror/contractor, including qualifications, past experience, and mission.                             | <ul><li>'Knowledge and Skills\nThe Contractor shall identify the resources necessary to successfully perform the work contained herein. Contractor shall possess and maintain the requisite knowledge and expertise to successfully accomplish the objectives of this Statement of Work. The Contractor will be responsible for ensuring that, at a minimum, the proposed resource(s) possesses the following: ● Proven development performance with the use of Drupal Content Management System and ● Minimum of 5 years of programing/database admin experience. ● General knowledge of DOI HR policies / processes. ● The ability to write, and verbally present complex subjects in a clear and concise manner.'</li><li>'Personnel (10 points)\nThe Offeror must include the name(s) of Key Personnel (Attachment Q1 - EHBs V&V Labor Categories) with demonstrated current experience (defined as, within the last 3 years) managing similar BPA type vehicles. These individuals must possess and demonstrate experience involving Verification & Validation of Enterprise IT Systems. These individuals will be responsible for all activity under this BPA and the resulting completion of each BPA Call. These individuals should have experience in similar engagements and should be current employees of the Offeror. The skill level and qualifications of the BPA management Key Personnel shall be maintained throughout the completion of the BPA.'</li><li>'Industry Certifications and Accreditations\nThe offeror shall provide a comprehensive list of all relevant industry certifications and accreditations held by the company, including dates obtained and expiration dates. The proposal must include certifications such as ISO standards, CMMI maturity levels, and any government-sponsored certification programs. The offeror shall provide certificate numbers and issuing organizations for verification purposes.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Evaluation

### Metrics
| Label   | Accuracy | Precision | Recall | F1_Score | Confusion_Matrix                                                                         |
|:--------|:---------|:----------|:-------|:---------|:-----------------------------------------------------------------------------------------|
| **all** | 0.8919   | 0.8986    | 0.8919 | 0.8935   | [[16, 0, 0, 0, 1], [0, 9, 1, 0, 0], [0, 0, 22, 4, 0], [0, 0, 2, 13, 0], [0, 0, 0, 0, 6]] |

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
preds = model("Place of Performance
All work shall be performed remotely via Government Approved Remote Access solutions unless otherwise agreed upon.")
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
| Training set | Min | Median   | Max |
|:-------------|:----|:---------|:----|
| Word count   | 9   | 101.7833 | 752 |

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
| 0.0056 | 1    | 0.2803        | -               |
| 0.2778 | 50   | 0.1748        | -               |
| 0.5556 | 100  | 0.0869        | -               |
| 0.8333 | 150  | 0.0416        | -               |

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