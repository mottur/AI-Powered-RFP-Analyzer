---
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
widget:
- text: 'Containerization and Orchestration

    All application components must be containerized using Docker and deployed onto
    a Kubernetes cluster (version 1.24+). Helm charts must be provided for all deployments
    to manage configuration and releases consistently across development, staging,
    and production environments.'
- text: 'Shared common solutions across all functionalities - opening up possibilities
    of automated

    tests across different versions'
- text: 'Period of Performance

    The period of performance of this contract will be for 12 months beginning on
    the date of award. *Subject to further interpretation of the estimated requirements'
- text: 'Corporate Capability Statement

    Describe your company''s organizational structure and core capabilities that make
    it suitable for this project. Detail your quality assurance processes and methodologies.
    Provide evidence of your financial stability, such as a Dunn & Bradstreet number
    or audited financial statements from the last fiscal year. Also, indicate if your
    company is designated as a small business under the applicable NAICS code.'
- text: 'Duration

    • The engagement duration for the professional services will be for a period of
    fourteen (14) months. Renewal will depend on the satisfactory performance of the
    PSP based on the results of performance evaluation. • This SOW may be revised
    during the life of the contract based on ADB’s changing business requirements
    with the necessary adjustments on the pricing based on the required revisions
    through mutual agreement between ADB and the PSP.'
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
      value: 0.8405797101449275
      name: Accuracy
    - type: precision
      value: 0.8720798652148767
      name: Precision
    - type: recall
      value: 0.8405797101449275
      name: Recall
    - type: f1_score
      value: 0.838682698128934
      name: F1_Score
    - type: confusion_matrix
      value:
      - - 10
        - 0
        - 0
        - 0
        - 0
      - - 1
        - 14
        - 0
        - 0
        - 0
      - - 2
        - 2
        - 13
        - 3
        - 0
      - - 0
        - 1
        - 0
        - 11
        - 0
      - - 0
        - 2
        - 0
        - 0
        - 10
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
| Label                                                                                                                                                              | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scope - This section describes the scope of the project, including project goals, boundaries, assumptions, and background context.                                 | <ul><li>'Support for multiple browsers, ensuring the interfaces perform consistently across various\nbrowsers and meet all 508 accessibility requirements and cross browser controls'</li><li>'Initiative Scope and Boundaries\nThe scope of work for this engagement includes a full security audit of all public-facing web applications and the internal network. This involves vulnerability scanning, penetration testing, and social engineering exercises. The project is explicitly bounded to the corporate network within the North American data centers and will not extend to third-party vendor systems or recently acquired international subsidiaries, which are under a separate assessment program.'</li><li>"Project Objectives and Boundaries\nThe goal of this project is to modernize the legacy customer relationship management (CRM) system to improve data accuracy and user efficiency. The scope includes the analysis, design, development, and implementation of a new cloud-based SaaS solution. This project is bounded to the integration with the existing Oracle financial system and the agency's Active Directory; it does not include any upgrades to those external systems. A key assumption is that the current data quality in the legacy system is sufficient for migration without extensive cleansing."</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Timeline - This section outlines the timeline, including the length of the contract, deadlines, project start and end dates, and other key milestone schedules.    | <ul><li>'Agile Sprint Schedule\nThe project will be executed using two-week sprints. The contractor shall provide a sprint schedule for the entire project duration at kick-off, outlining planned features for each sprint. A formal demo and review will be held at the end of each sprint, with a retrospective and planning session for the subsequent sprint to begin within two business days.'</li><li>'Contract Period of Performance\nThe period of performance for this fixed-price contract shall be from October 1, 2024, to September 30, 2025. All work must be completed, and final deliverables accepted, by the end of this period.'</li><li>'Implementation Rollout Plan\nThe rollout will be conducted in a phased approach by geographic region: Pilot Group (Northwest Region): July 10, 2025; Phase 1 (Southwest Region): August 7, 2025; Phase 2 (Northeast Region): September 4, 2025; Full Deployment (All Remaining Regions): October 2, 2025.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Deliverables - This section lists the deliverables or tangible outputs the offeror/contractor is required to provide.                                              | <ul><li>'Contractual Deliverables Schedule\nDeliverables are due according to the following milestones: a signed-off Project Charter by Week 2, High-Fidelity Wireframes by Week 6, a Functional Prototype for User Acceptance Testing by Week 12, and the Final Deployed System by Week 16.'</li><li>'Monthly Deliverables\nThe vendor shall provide a written Monthly Status Report by the 5th business day of each month, detailing progress against the project plan, risks, issues, and key performance indicators (KPIs).'</li><li>'Hardware and Software Deliverables\nThe contractor is responsible for delivering, installing, and configuring five (5) physical application servers, the licensed enterprise software, and a one-year warranty for all provided hardware components.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Technologies - This section specifies the tech stack - the environment, technologies, platforms, software, or tools that will be used or required for the project. | <ul><li>"•  ADB DXP\n• 10 -15 Data products • 5-8 AI Projects • Required Activities • The following activities must be part of the contractor’s deliverables: • Creation and maintenance of ADB's LLM Enterprise architecture • Software development following best practices (unit testing, creation of common libraries, CI/CD, IaC, modern UI/UX) • LLM Data Science Experimentation (Prototyping ideas of LLM applications • Production Grade Application deployment (Infrastructure Monitoring, Backup and Recovery, Cost Optimization, Performance Monitoring) • Security and Compliance (documentation & architecture compliant with ADB's security policies) • Data Platform Lifecycle (Creation of reliable and efficient data pipelines for the LLM's consumption, end to end data lineage) • Develop and Adherence to industry standard responsible ai framework"</li><li>'Cloud Hosting and Services\nThe application must be deployed on Amazon Web Services (AWS). The architecture shall utilize AWS Elastic Kubernetes Service (EKS) for orchestration, Amazon RDS for PostgreSQL for the database, and Amazon S3 for static asset storage. The solution must employ AWS Lambda for serverless functions and use Amazon CloudFront as a content delivery network (CDN). All infrastructure must be defined as code using Terraform.'</li><li>"Development and Collaboration Tools\nThe development lifecycle must utilize Jira for project tracking and task management. Continuous integration and continuous deployment (CI/CD) must be implemented using GitLab CI/CD pipelines. Documentation shall be maintained in Confluence. All communication related to the project must be conducted through the agency's Microsoft Teams channels. The offeror must demonstrate experience with all specified tools."</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Company Info - This section provides information about the offeror/contractor, including qualifications, past experience, and mission.                             | <ul><li>'Proposed prices for the Hypotheticals.\nThe Government reserves the right to reject any quote that includes any assumption(s) that adversely impact(s) the Government’s requirements or fails to comply with any of the requirements outlined herein. Factor 3 - Past Performance The Offeror’s past performance will be evaluated in accordance with the following Past Performance Relevancy Rating Standards and Performance Confidence Assessments Standards. The Government will conduct a past performance evaluation of the Offeror’s past performance as well as that of its subcontractors (if applicable). Past performance consists of past performance relevancy and performance confidence; thus, the Offeror will be assigned two (2) ratings for past performance: First, the Government will evaluate the Offeror’s past performance references to determine how relevant a recent effort is to the current requirement for source selection. Common aspects of relevance include similarity of service/support, complexity, magnitude of effort, dollar value, and contract type. Second, the Government will evaluate the Offeror’ s past performance to determine the quality of work performed and assess the level of expectation that the Offeror can successfully perform the required effort. Past PastPerformancePerformanceRelevancyRelevancy RatingRatingStandardsStandards Rating Definition Very Relevant Present/past performance effort involved essentially the same scope and magnitude of effort and complexities this solicitation requires. Relevant Present/past performance effort involved similar scope and magnitude of effort and complexities this solicitation requires. Somewhat Relevant Present/past performance effort involved some of the scope and magnitude of effort and complexities this solicitation requires. Not Relevant Present/past performance effort involved little or none of the scope and magnitude of effort and complexities this solicitation requires. Performance Confidence Assessment Standards Rating Description Exceptional Confidence Based on the Offeror’s recent/relevant performance record, the Government has very high expectations that the offeror will successfully perform the required effort. Very Good Confidence Based on the Offeror’s recent/relevant performance record, the Government has very good expectations that the offeror will successfully perform the required effort. Satisfactory Confidence Based on the offeror’s recent/relevant performance record, the Government has reasonable expectations that the offeror will successfully perform the required effort.  Marginal Confidence Based on the offeror’s recent/relevant performance record, the Government has minimal expectations that the Offeror will successfully perform the required effort. Unsatisfactory Confidence Based on the offeror’s recent/relevant performance record, the Government has no expectation that the Offeror will successfully perform the required effort. Unknown Confidence No recent/relevant performance record is available or the offeror’s performance (Neutral) record is so sparse that no meaningful confidence assessment rating can be reasonably assigned. The evaluation of the VPAT is independent from the other factors and will be based on the demonstrated capabilities of the prospective Offeror to meet the requirements of all the applicable Section 508 standards as listed in HHSAR clause 352.239-74 Electronic and Information Technology Accessibility. Alternatively, Offerors may propose goods or services that provide equivalent facilitation. Such offers will be considered to have met the standards of the Access Board’s standards for the feature or component providing equivalent facilitation. If none of the Offerors propose goods or services that fully meet all of the applicable Access Board’s standards, those Offerors whose products or services meet some of the applicable standards will be considered eligible for award. ICT vs. EIT Procurement documentation from HHS or other agencies may contain references to “EIT” (Electronic and Information Technology) and “ICT” (Information and Communications Technology). HHS considers these terms to be interchangeable, and “EIT” should always be interpreted to be “ICT” in any HHS procurement. The Section 508 VPAT will be evaluated as described in this chart. ICT Products fully meet intent of all applicable Section 508 Standards. Risk Green of failure to meet all Section 508 Requirements is very low. ICT Products can be made capable of meeting the intent of all applicable products. Risk of failure to meet all Section 508 Requirement is low. Standards or the VPAT is materially incomplete. Risk of failure to meet all Red'</li><li>'Industry Certifications and Accreditations\nThe offeror shall provide a comprehensive list of all relevant industry certifications and accreditations held by the company, including dates obtained and expiration dates. The proposal must include certifications such as ISO standards, CMMI maturity levels, and any government-sponsored certification programs. The offeror shall provide certificate numbers and issuing organizations for verification purposes.'</li><li>'Employee Qualifications and Expertise\nThe offeror shall detail the overall qualifications of their workforce including the percentage of staff with advanced degrees, professional certifications, and security clearances. The proposal must provide statistics on average years of experience in relevant technical domains and federal contracting. The offeror shall describe their approach to maintaining a highly skilled and technically competent workforce.'</li></ul> |

## Evaluation

### Metrics
| Label   | Accuracy | Precision | Recall | F1_Score | Confusion_Matrix                                                                           |
|:--------|:---------|:----------|:-------|:---------|:-------------------------------------------------------------------------------------------|
| **all** | 0.8406   | 0.8721    | 0.8406 | 0.8387   | [[10, 0, 0, 0, 0], [1, 14, 0, 0, 0], [2, 2, 13, 3, 0], [0, 1, 0, 11, 0], [0, 2, 0, 0, 10]] |

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
preds = model("Shared common solutions across all functionalities - opening up possibilities of automated
tests across different versions")
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
| Word count   | 9   | 86.1667 | 647 |

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
| 0.0056 | 1    | 0.2865        | -               |
| 0.2778 | 50   | 0.1588        | -               |
| 0.5556 | 100  | 0.0746        | -               |
| 0.8333 | 150  | 0.0396        | -               |

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