---
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
widget:
- text: 'Critical Path Deadlines

    The project has the following non-negotiable deadlines: Environment provisioning
    must be complete by 2024-10-31. Data migration must be completed by 2025-01-15.
    Full operational capability (FOC) must be achieved by 2025-06-30. The contractor''s
    proposed schedule must demonstrate how these key dates will be met.'
- text: 'Code based user interface (UI) validations and business rules - making it
    challenging for

    rapid release response times'
- text: 'Quotes and revisions of quotes shall be uploaded electronically via the GSA
    e-Buy RFQ system under

    the appropriate solicitation number. Offerors shall notify the Contracting Officer
    of any revisions to quotations before the closing date in GSA eBuy. b. Offerors
    shall submit quotes in response to this solicitation in English and in U.S. dollars.
    c. Quotes may be withdrawn at any time before award. Withdrawals are effective
    upon receipt of written notice by the Contracting Officer.'
- text: 'Corporate Compliance and Regulatory Experience

    The offeror must detail their experience with federal compliance requirements
    including FAR, DFARS, and other applicable regulations. The proposal shall describe
    the offeror''s internal compliance programs, audit processes, and experience with
    government audits. The offeror shall provide examples of successfully navigating
    complex regulatory environments.'
- text: 'Environment Details

    • The contractor will provide manage service on the below items required for development'
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
      value: 0.8441558441558441
      name: Accuracy
    - type: precision
      value: 0.8528786315164022
      name: Precision
    - type: recall
      value: 0.8441558441558441
      name: Recall
    - type: f1_score
      value: 0.8440467233529433
      name: F1_Score
    - type: confusion_matrix
      value:
      - - 24
        - 1
        - 3
        - 0
        - 0
      - - 0
        - 5
        - 0
        - 0
        - 0
      - - 1
        - 0
        - 14
        - 3
        - 0
      - - 0
        - 0
        - 1
        - 14
        - 0
      - - 2
        - 0
        - 1
        - 0
        - 8
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
| Label                                                                                                                                                              | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scope - This section describes the scope of the project, including project goals, boundaries, assumptions, and background context.                                 | <ul><li>'Shared common solutions across all functionalities - opening up possibilities of automated\ntests across different versions'</li><li>'Scope of Work and Key Assumptions\nThis initiative aims to develop a centralized data analytics platform to unify reporting across the enterprise. The scope of work includes requirements gathering, data pipeline development, warehouse design, and dashboard creation. The project assumes that source system owners will provide timely access to data and subject matter experts. The boundaries of this project are strictly limited to the five source systems listed in Appendix A; integrating additional data sources is considered out of scope and must be handled through a separate change request.'</li><li>'Initiative Scope and Boundaries\nThe scope of work for this engagement includes a full security audit of all public-facing web applications and the internal network. This involves vulnerability scanning, penetration testing, and social engineering exercises. The project is explicitly bounded to the corporate network within the North American data centers and will not extend to third-party vendor systems or recently acquired international subsidiaries, which are under a separate assessment program.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Timeline - This section outlines the timeline, including the length of the contract, deadlines, project start and end dates, and other key milestone schedules.    | <ul><li>'Contract signing      contract and other required                      10%\ncontractual documents Kick-off meeting Kick-off meeting completed 1-2 weeks 0 Submission of Submission of a satisfactory 10% (estimate) Detailed-level AI solution design document, accepted Lab Framework by ADB and Architecture (AI and Big Data) Implementation of -Submission of satisfactory the Lab Framework documented tools, framework, best'</li><li>'Quality Review       review on AI models and addresses                 10%\nany action points Final Project Sign- Submission of satisfactory Final4 10% off Project Report, accepted by ADB'</li><li>'Weekly Deliverables Schedule\nThe vendor shall provide a weekly status report every Friday by 12:00 PM EST. Bi-weekly sprint demos will be held every other Wednesday at 10:00 AM EST, commencing on the second week of the contract.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Deliverables - This section lists the deliverables or tangible outputs the offeror/contractor is required to provide.                                              | <ul><li>'Key Project Deliverables\nThe offeror shall provide the following tangible outputs: a fully configured SaaS application instance, a complete Data Migration Toolset, a comprehensive User Training Manual (both digital and print versions), and a Final Project Report detailing system performance and implementation metrics.'</li><li>"Final Project Deliverables\nUpon project completion, the contractor must provide the following: 1) All project code and artifacts transferred to the government's GitHub Enterprise repository. 2) A lessons-learned report conducted with the project team. 3) A production support handoff plan. 4) A 30-day warranty period for all delivered software following acceptance. 5) As-built architecture diagrams reflecting the final deployed state."</li><li>'Design Phase Deliverables\nThe deliverables for the design phase shall include: User Personas, Customer Journey Maps, a Sitemap, an Interactive Prototype, and a UI Style Guide with a complete component library for developers.'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Technologies - This section specifies the tech stack - the environment, technologies, platforms, software, or tools that will be used or required for the project. | <ul><li>'Technical Approach for Hypothetical #1, Cloud Readiness and Enhancements - 10 points\nHRSA Test Harness is an Enterprise Test Automation Platform that standardizes automated testing processes and promotes collaboration across multiple vendors to support the HRSAs IT mission. The framework supports industry standard testing methodologies such as Data Driven Testing (DDT) and Behavior Driven Development (BDD). It provides an interface to users to define workflows to automate functional testing for an application. These workflows can then be executed against various environments as the software propagates from lower environments to higher ensuring the integrity and quality of the software product. The solution provides the capability for users to create test suites within the application UI with little or no coding. The configured test suites can then be executed either on demand or on a schedule in any given environment. All tests provide detailed reports that allows the user to identify potential defects with the product(s) being tested. The Test Automation Framework natively integrates with enterprise products like Jira for incident management, Jenkins for CI/CD, JMeter for performance testing, and RedGate for test data generation. Refer all the relevant documents such as architecture, tools and technologies and technical design documents while responding to this hypothetical project. Current Challenges Current Test automation Test automation framework is designed to support and implement the automation tests for EHBs. Solution shall consider refactoring / Re-engineering the existing Test automation framework for cloud adoption and readiness. Proposed solution shall also consider  disaster recovery, loosely coupled architecture for APIs, Test Framework execution by bureaus in a containers, incremental modernization, maintaining backward compatibility until the system is fully modernized and migrated, system performance, scalability and cost savings in cloud space using the combination of Infrastructure as Service (IaaS), Platform as Service (PaaS) and Software as Service (SaaS). HRSA is also looking for a riskless migration path to modernize the system in specified duration without impacting business and performance of the current system. Please describe your strategy and approach for Cloud readiness and modernization. Specifically, the Offeror shall address the following requirements: \uf0b7 Review and provide the strategy for cloud adoption and readiness. \uf0b7 Propose the Cloud readiness architecture for all the core components of test harness. The modernization strategy should align with continuous delivery principles. \uf0b7 Enhance Test Harness platform to natively support cloud API testing and provision for third party tools integration \uf0b7 Create service containers for portability, management and test execution. \uf0b7 Ensure Data integrity and protection during transit and at rest. \uf0b7 Cloud adoption strategy should include o Configure auto scaling for performance and maximum throughput o Monitor, measure and Enhance security posture for cloud adoption \uf0b7 Interfaces and systems need to be covered while planning the cloud migration o Detect coordination problems in cloud environment – this is to ensure the applications are well configured with cloud environment'</li><li>'Technical Approach for Hypothetical #2, EHBs Test Automation\nFramework and platform Enhancements – (10 points) visual testing using Artificial Intelligence and Machine Learning (AI/ML)– (10 points)'</li><li>'Integration Technologies\nIntegration with the legacy ERP system will be accomplished using MuleSoft Anypoint Platform as the enterprise service bus (ESB). APIs must be designed in accordance with RESTful principles and must utilize OAuth 2.0 for authorization.'</li></ul> |
| Company Info - This section provides information about the offeror/contractor, including qualifications, past experience, and mission.                             | <ul><li>'Offerors must comply with the detailed instructions for the format and content of the quote; quotes that do not\ncomply with the detailed instructions for the format and content of the quote will be considered non- responsive and will render the offeror ineligible for award. \uf0b7 Quote Format: Offerors shall submit quotes in accordance with the following guidelines. All filenames shall include the offeror’s company name and title/subject of content. \uf0b7 All documents requested herein shall be compatible with Microsoft Office formats or Adobe PDF. \uf0b7 Offerors shall identify all Non-FSS items or services in their quotations. 3. Page format The Technical Quote shall be single spaced and shall be printable on 8.5 x 11 inch paper containing text no smaller than 12 point for text and 9 point for graphics (including call out boxes and tables). Each page shall be inch foldouts only to display graphics, flow charts, organizational charts, or drawings. The technical proposal shall not exceed 40 single-spaced pages, excluding cover pages, table of contents, and other required appendices. The foldouts when used to meet a technical evaluation criteria or a SOW element in the technical quote, it must be included in the page count (each 11 x 17 can be counted as 1-page). Offerors are advised to strictly observe limitations on the length and format specified since review of the technical proposal will be limited to 40 pages. In addition, up to 10 pages for each Hypotheticals will be accepted. The clarity, relevance, and conciseness of the quote is important, not the length.'</li><li>"The offeror shall identify the GSA schedule and contract utilized, the schedule price, any unit prices used\nany discounts proposed and any other relevant pricing information. The offeror's price quote shall consist of the following:"</li><li>'To facilitate the evaluations, four (4) separate volumes titled technical quote, price quote, past performance,\nand VPAT shall be submitted separately and clearly labeled. Each of these parts shall be separate and complete in itself so that the evaluation of one may be accomplished independently of the evaluation of the other. Volume I–Technical Quote must not contain references to price; however, resource information such as data concerning labor hours and categories, materials, subcontracts, etc., must be contained in the Technical Quote so that your understanding of the statement of objectives may be evaluated. It must disclose your approach in sufficient detail to provide a clear and concise presentation that includes the requirements of the proposal instructions. Volume I must include a statement indicating whether any exceptions are taken to the terms and conditions of the request for quotation (RFQ) as part of the transmittal letter. Any exceptions must include identification of the specific paragraphs and rationale for each exception. Exceptions shall also be noted in the quote at the location of the exception. Volume Title I Technical Quote II Price Quote III Past Performance IV VPAT'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Evaluation

### Metrics
| Label   | Accuracy | Precision | Recall | F1_Score | Confusion_Matrix                                                                         |
|:--------|:---------|:----------|:-------|:---------|:-----------------------------------------------------------------------------------------|
| **all** | 0.8442   | 0.8529    | 0.8442 | 0.8440   | [[24, 1, 3, 0, 0], [0, 5, 0, 0, 0], [1, 0, 14, 3, 0], [0, 0, 1, 14, 0], [2, 0, 1, 0, 8]] |

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
preds = model("Environment Details
• The contractor will provide manage service on the below items required for development")
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
| Word count   | 15  | 97.6333 | 752 |

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
| 0.0056 | 1    | 0.3231        | -               |
| 0.2778 | 50   | 0.1543        | -               |
| 0.5556 | 100  | 0.0522        | -               |
| 0.8333 | 150  | 0.021         | -               |

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