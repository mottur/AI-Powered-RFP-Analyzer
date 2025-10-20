---
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
widget:
- text: 'Security compliance - ensuring that all enhancements meet the HRSA’s security

    requirements. The Offeror should describe their strategy and approach to apply
    unique methodologies, automation frameworks, tools, and techniques to perform
    usability, accessibility and security compliance testing for ongoing enhancements
    and upgrades. Specifically, the Offeror shall address the following requirements:
     Propose a cost-effective and innovative approach to perform usability testing.
     Provide a build-test optimized model to promote agility and automation of Test
    scripts and test harness platform  Solution must be compatible and address challenges
    specific to portability, reliability and scalability.  Propose an approach, tools
    and techniques to perform usability, accessibility, security compliance and cross
    browser compatibility, performance, and integration and role bases testing. 
    Provide an automated regression test strategy and outline a test architecture
    to simplify the regression testing challenges. The proposed strategy should be
    feasible, realistic, and actionable.  Propose effective solution to maintain
    the versioning and tracing the changes in functionality to lowest level.  Open
    to integrate with third-party components or utilities and connect with open source
    technologies.  Promote effective strategies for Usability, Data generation and
    Training requirements.  Enhance the DEVSecOps Pipeline Integration process for
    continuous test suite integration.  Integration to Team Foundation Server to
    convert user stories to automated test cases.'
- text: 'Module has tight data and navigation integration with other EHB modules,
    2) The module is used

    across HRSA by all bureaus with few specific deviations and automation for certain
    specific programs, 3) The process supports complex data driven business rules,'
- text: 'Background and Project Context

    The current website suffers from outdated technology that is no longer supported,
    leading to security vulnerabilities and a poor user experience. This project will
    rebuild the public-facing site on a modern content management system to empower
    content editors and improve accessibility compliance. The scope encompasses the
    complete content migration, user training, and a one-year warranty period. It
    is assumed that the site''s information architecture and core content will remain
    largely unchanged unless improvements are identified during the discovery phase.'
- text: 'Organizational Experience (10 points)

    The Offeror shall describe and demonstrate the organization’s experience in successfully
    managing federal government contracts involving verification and validation of
    large Enterprise IT applications, best practices and similar projects. The Offeror
    shall provide a list and description of at least three (3) Enterprise IT verification
    and validation projects within the past three (3) years, or that they are currently
    performing, that demonstrates the Offeror’s experience with similar scope, size,
    and/or complexity as this requirement. The Offeror shall demonstrate how their
    corporate experience specifically correlates to this project using a side-by-side
    “crosswalk” comparison. Experience information must include a contract number,
    contract type, dollar value, date of award, performance period, and a brief narrative
    describing the nature and complexity of the work. Include name, current phone
    numbers, mailing address, and email address of the person who will verify this
    experience, the number of projects, complexity, workload, and dollar amount/contract
    value.'
- text: 'Project Overview and Goals

    This initiative aims to design and deploy a comprehensive enterprise resource
    planning (ERP) system to unify financial, HR, and supply chain operations. The
    scope encompasses end-to-end process mapping, software configuration, data migration
    from legacy systems, and user acceptance testing. The project is bounded by the
    existing IT infrastructure and will not include hardware upgrades or the development
    of custom manufacturing modules.'
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
      value: 0.8833333333333333
      name: Accuracy
    - type: precision
      value: 0.896957671957672
      name: Precision
    - type: recall
      value: 0.8833333333333333
      name: Recall
    - type: f1_score
      value: 0.8850088507983245
      name: F1_Score
    - type: confusion_matrix
      value:
      - - 11
        - 0
        - 0
        - 0
        - 1
      - - 0
        - 9
        - 0
        - 0
        - 1
      - - 1
        - 0
        - 10
        - 1
        - 0
      - - 2
        - 1
        - 0
        - 17
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
| Label                                                                                                                                                              | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scope - This section describes the scope of the project, including project goals, boundaries, assumptions, and background context.                                 | <ul><li>'Initiative Scope and Boundaries\nThe scope of work for this engagement includes a full security audit of all public-facing web applications and the internal network. This involves vulnerability scanning, penetration testing, and social engineering exercises. The project is explicitly bounded to the corporate network within the North American data centers and will not extend to third-party vendor systems or recently acquired international subsidiaries, which are under a separate assessment program.'</li><li>'Scope and Key Assumptions\nThis project involves migrating the entire email and collaboration suite from an on-premise exchange server to Microsoft 365. The scope includes tenant setup, mailbox migration, DNS record changes, and user training. A fundamental assumption is that all user workstations meet the minimum software requirements for Office 365 ProPlus. The project is bounded to corporate email and does not include the migration of file shares or departmental SharePoint sites.'</li><li>'Objectives and Key Assumptions\nThe primary objective is to increase customer engagement by 25% through a redesigned digital experience platform. The project scope includes user research, information architecture, UI/UX design, and front-end development for the main website and mobile app. A key assumption is that the current content management system (CMS) can support the new design with minimal backend customization. The scope excludes any changes to the underlying product database schema.'</li></ul>                                                                                                                                                                             |
| Timeline - This section outlines the timeline, including the length of the contract, deadlines, project start and end dates, and other key milestone schedules.    | <ul><li>'Proposed Project Phases\nPhase 1 (Discovery & Planning): Weeks 1-4; Phase 2 (Design & Prototyping): Weeks 5-12; Phase 3 (Development): Weeks 13-28; Phase 4 (Testing & Quality Assurance): Weeks 29-36; Phase 5 (Deployment & Transition): Weeks 37-40; Phase 6 (Post-Launch Support): Weeks 41-52.'</li><li>'Phase 1 Implementation Timeline\nPhase 1 of the project must commence no later than 15 business days after contract signing and shall be completed within a 90-day period. The deadline for the Phase 1 preliminary design review is 45 days after kick-off. The final deliverable for this phase, a working prototype, is due no later than 5:00 PM EST on the 90th day.'</li><li>'Duration\n• The engagement duration for the professional services will be for a period of fourteen (14) months. Renewal will depend on the satisfactory performance of the PSP based on the results of performance evaluation. • This SOW may be revised during the life of the contract based on ADB’s changing business requirements with the necessary adjustments on the pricing based on the required revisions through mutual agreement between ADB and the PSP.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Deliverables - This section lists the deliverables or tangible outputs the offeror/contractor is required to provide.                                              | <ul><li>'Deliverables\nAll written deliverables shall be created in a professional manner and shall include meeting summaries, background information, and any appropriate research material where requested. All non-branded deliverables shall be submitted in an editable (i.e., unprotected) format such as Microsoft Word, Excel, or PowerPoint when applicable. All Deliverables will be submitted on or before the due date specified or submitted in accordance with a later scheduled date determined by FWS. The following deliverables will be prepared by or updated by the Contractor: ● Project plan and schedule ● Documentation of any design adjustments that will take place to ‘as-is’ site – in form of wire frame/mockup, or written explanations for simple adjustments ● End user guidance for site owners as requested ● Drupal Site Pages (Finished Product)'</li><li>'Phase 1 Deliverables\nFor the Discovery and Design phase, the required deliverables are: a comprehensive Current State Assessment report, a Future State Architecture diagram, a Data Migration Strategy document, a detailed Project Roadmap, and a signed-off Functional Requirements Specification. All documents must be submitted in both PDF and editable Microsoft Word formats.'</li><li>"Final Project Deliverables\nUpon project completion, the contractor must provide the following: 1) All project code and artifacts transferred to the government's GitHub Enterprise repository. 2) A lessons-learned report conducted with the project team. 3) A production support handoff plan. 4) A 30-day warranty period for all delivered software following acceptance. 5) As-built architecture diagrams reflecting the final deployed state."</li></ul> |
| Technologies - This section specifies the tech stack - the environment, technologies, platforms, software, or tools that will be used or required for the project. | <ul><li>'Technical Approach for Hypothetical #1, Cloud Readiness and\nEnhancements - 10 points'</li><li>'Environment Details\n• The contractor will provide manage service on the below items required for development'</li><li>'Code based user interface (UI) validations and business rules - making it challenging for\nrapid release response times'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Company Info - This section provides information about the offeror/contractor, including qualifications, past experience, and mission.                             | <ul><li>'Contacts\nContracting Officer (CO): Lorenzo Aragon; E-Mail: Lorenzo_aragon@fws.gov; Ph# 505-248-6627'</li><li>'Labor Categories: State the labor categories proposed, indicating discounted rates, if applicable, that are\nto be used over the life of the BPA. Include both on-site and off-site rates.'</li><li>'Corporate Awards and Recognition\nThe offeror must list any industry awards, performance recognition, or quality awards received in the past five years. The proposal shall include awards for project excellence, workplace quality, innovation, or other relevant achievements. The offeror shall provide context for each award including the awarding organization and criteria for selection.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Evaluation

### Metrics
| Label   | Accuracy | Precision | Recall | F1_Score | Confusion_Matrix                                                                         |
|:--------|:---------|:----------|:-------|:---------|:-----------------------------------------------------------------------------------------|
| **all** | 0.8833   | 0.8970    | 0.8833 | 0.8850   | [[11, 0, 0, 0, 1], [0, 9, 0, 0, 1], [1, 0, 10, 1, 0], [2, 1, 0, 17, 0], [0, 0, 0, 0, 6]] |

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
| Training set | Min | Median | Max |
|:-------------|:----|:-------|:----|
| Word count   | 9   | 56.95  | 262 |

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
| 0.0056 | 1    | 0.3203        | -               |
| 0.2778 | 50   | 0.1613        | -               |
| 0.5556 | 100  | 0.0601        | -               |
| 0.8333 | 150  | 0.0225        | -               |

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