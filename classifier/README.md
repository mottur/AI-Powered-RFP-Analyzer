---
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
widget:
- text: 'Content Management System

    The public website must be built upon the WordPress VIP platform. All custom themes
    and plugins must be developed according to WordPress VIP coding standards and
    must be submitted for security review via the designated GitHub repository.'
- text: 'Module has tight data and navigation integration with other EHB modules,
    2) The module is used

    across HRSA by all bureaus with few specific deviations and automation for certain
    specific programs, 3) The process supports complex data driven business rules,'
- text: 'Phase 1 Implementation Timeline

    Phase 1 of the project must commence no later than 15 business days after contract
    signing and shall be completed within a 90-day period. The deadline for the Phase
    1 preliminary design review is 45 days after kick-off. The final deliverable for
    this phase, a working prototype, is due no later than 5:00 PM EST on the 90th
    day.'
- text: 'Employee Qualifications and Expertise

    The offeror shall detail the overall qualifications of their workforce including
    the percentage of staff with advanced degrees, professional certifications, and
    security clearances. The proposal must provide statistics on average years of
    experience in relevant technical domains and federal contracting. The offeror
    shall describe their approach to maintaining a highly skilled and technically
    competent workforce.'
- text: 'Foundation building   practice guides and engineering      4-6 weeks        10%

    (architecture, tools standards, and responsible AI and infrastructure) Framework,
    security alignment -Establish business outcomes & success criteria, accepted by
    ADB -Production ready AI and Big Data Lab (segregation of development and production
    environment), accepted by ADB 5% after the design and -Design and build each AI
    build is Design and Build 1 accepted by or more Data Estimated 2 ADB. Product
    + Design months per AI 5% upon and Build 1 AI product completion of -Application
    development, Product application Application of responsible AI development, Framework
    plus 1 Data Product accepted by ADB. 5% after the design and -Design and build
    each AI build is Design and Build 1 accepted by or more Data Estimated 2 ADB.
    Product + Design months per AI 5% upon and Build 1 AI product completion of -Application
    development, Product application Application of responsible AI development, Framework
    plus 1 Data Product accepted by ADB. 5% after the'
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
      value: 0.8695652173913043
      name: Accuracy
    - type: precision
      value: 0.8815951501373497
      name: Precision
    - type: recall
      value: 0.8695652173913043
      name: Recall
    - type: f1_score
      value: 0.8693451215190345
      name: F1_Score
    - type: confusion_matrix
      value:
      - - 10
        - 1
        - 0
        - 0
        - 0
      - - 0
        - 13
        - 0
        - 0
        - 0
      - - 1
        - 1
        - 16
        - 1
        - 0
      - - 0
        - 1
        - 1
        - 12
        - 0
      - - 0
        - 1
        - 1
        - 1
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
| Label                                                                                                                                                              | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scope - This section describes the scope of the project, including project goals, boundaries, assumptions, and background context.                                 | <ul><li>'Project Overview and Goals\nThis initiative aims to design and deploy a comprehensive enterprise resource planning (ERP) system to unify financial, HR, and supply chain operations. The scope encompasses end-to-end process mapping, software configuration, data migration from legacy systems, and user acceptance testing. The project is bounded by the existing IT infrastructure and will not include hardware upgrades or the development of custom manufacturing modules.'</li><li>'Scope of Work and Key Assumptions\nThis initiative aims to develop a centralized data analytics platform to unify reporting across the enterprise. The scope of work includes requirements gathering, data pipeline development, warehouse design, and dashboard creation. The project assumes that source system owners will provide timely access to data and subject matter experts. The boundaries of this project are strictly limited to the five source systems listed in Appendix A; integrating additional data sources is considered out of scope and must be handled through a separate change request.'</li><li>"Background and Project Context\nThe current website suffers from outdated technology that is no longer supported, leading to security vulnerabilities and a poor user experience. This project will rebuild the public-facing site on a modern content management system to empower content editors and improve accessibility compliance. The scope encompasses the complete content migration, user training, and a one-year warranty period. It is assumed that the site's information architecture and core content will remain largely unchanged unless improvements are identified during the discovery phase."</li></ul> |
| Timeline - This section outlines the timeline, including the length of the contract, deadlines, project start and end dates, and other key milestone schedules.    | <ul><li>'Milestone Payment Schedule\nPayment is contingent upon the successful completion and acceptance of the following milestones: 20% upon contract signing and project kick-off, 30% upon completion and acceptance of the development phase, 30% upon successful completion of system integration testing, and the final 20% upon project closure and delivery of all final documentation. Each milestone has a hard deadline as outlined in Attachment C - Schedule of Events.'</li><li>'Development Sprint Timeline\nDevelopment will be organized into two-week sprints. Sprint 1: Jan 10 - Jan 21; Sprint 2: Jan 24 - Feb 4; Sprint 3: Feb 7 - Feb 18; [ ... ] The final sprint, Sprint 18, is scheduled for August 15 - August 26, dedicated to final bug fixes and preparation for deployment.'</li><li>'Project Milestone Dates\nKick-off Meeting: January 15, 2025; Finalized Project Charter: January 29, 2025; Hardware Procurement Completed: March 15, 2025; Data Migration Completed: June 30, 2025; User Training Completed: August 15, 2025; Project Closeout: September 30, 2025.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Deliverables - This section lists the deliverables or tangible outputs the offeror/contractor is required to provide.                                              | <ul><li>'Training and Transition Deliverables\nAs part of the knowledge transfer, the offeror must deliver a series of three (3) training workshops for end-users and administrators, along with recorded video tutorials and a searchable FAQ knowledge base portal.'</li><li>"Required Deliverables List\nBy the conclusion of the contract, the vendor must deliver a production-ready mobile application published on the iOS App Store and Google Play Store, a fully documented API for third-party integration, and source code deposited into the client's designated GitHub repository."</li><li>'Monthly Deliverables\nThe vendor shall provide a written Monthly Status Report by the 5th business day of each month, detailing progress against the project plan, risks, issues, and key performance indicators (KPIs).'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Technologies - This section specifies the tech stack - the environment, technologies, platforms, software, or tools that will be used or required for the project. | <ul><li>"•  ADB DXP\n• 10 -15 Data products • 5-8 AI Projects • Required Activities • The following activities must be part of the contractor’s deliverables: • Creation and maintenance of ADB's LLM Enterprise architecture • Software development following best practices (unit testing, creation of common libraries, CI/CD, IaC, modern UI/UX) • LLM Data Science Experimentation (Prototyping ideas of LLM applications • Production Grade Application deployment (Infrastructure Monitoring, Backup and Recovery, Cost Optimization, Performance Monitoring) • Security and Compliance (documentation & architecture compliant with ADB's security policies) • Data Platform Lifecycle (Creation of reliable and efficient data pipelines for the LLM's consumption, end to end data lineage) • Develop and Adherence to industry standard responsible ai framework"</li><li>'Frontend Development Requirements\nThe user interface shall be a single-page application (SPA) built with the Angular 15 framework. The application must use the NgRx library for state management and be styled according to the Google Material Design specification using Angular Material components.'</li><li>'Integration Technologies\nIntegration with the legacy ERP system will be accomplished using MuleSoft Anypoint Platform as the enterprise service bus (ESB). APIs must be designed in accordance with RESTful principles and must utilize OAuth 2.0 for authorization.'</li></ul>                                                                                                                                                                                                                                                                         |
| Company Info - This section provides information about the offeror/contractor, including qualifications, past experience, and mission.                             | <ul><li>"Executive Leadership Profiles\nThe offeror must submit professional profiles of the executive leadership team, including the CEO, CTO, and other key executives. Each profile shall include educational background, years of industry experience, previous leadership roles, and specific expertise relevant to this procurement. The offeror shall describe the leadership team's vision and their commitment to government contracting excellence."</li><li>'Business Continuity and Disaster Recovery\nThe offeror shall provide an overview of their corporate business continuity and disaster recovery capabilities. The proposal must describe infrastructure redundancy, data backup strategies, and recovery time objectives. The offeror shall include information about any recent business continuity tests or certifications the company has undergone.'</li><li>"Client Testimonials and Success Stories\nThe offeror must provide at least five client testimonials from previous government or commercial clients that demonstrate the company's performance excellence. The proposal shall include specific examples of successful project delivery, problem-solving capabilities, and client satisfaction. Each testimonial must include the client organization, project scope, and measurable outcomes achieved."</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                           |

## Evaluation

### Metrics
| Label   | Accuracy | Precision | Recall | F1_Score | Confusion_Matrix                                                                          |
|:--------|:---------|:----------|:-------|:---------|:------------------------------------------------------------------------------------------|
| **all** | 0.8696   | 0.8816    | 0.8696 | 0.8693   | [[10, 1, 0, 0, 0], [0, 13, 0, 0, 0], [1, 1, 16, 1, 0], [0, 1, 1, 12, 0], [0, 1, 1, 1, 9]] |

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
preds = model("Module has tight data and navigation integration with other EHB modules, 2) The module is used
across HRSA by all bureaus with few specific deviations and automation for certain specific programs, 3) The process supports complex data driven business rules,")
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
| Word count   | 9   | 93.4667 | 752 |

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
| 0.0056 | 1    | 0.3313        | -               |
| 0.2778 | 50   | 0.1791        | -               |
| 0.5556 | 100  | 0.0663        | -               |
| 0.8333 | 150  | 0.0257        | -               |

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