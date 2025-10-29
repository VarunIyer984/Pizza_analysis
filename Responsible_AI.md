# [cite_start]Responsible AI Checklist: Pizza Price Analysis [cite: 140]

## [cite_start]Fairness [cite: 141]

* [cite_start]**Check model bias:** Does the model unfairly predict higher or lower prices based on the pizza `company` or `category` (e.g., veg vs. non-veg)? [cite: 142]
* [cite_start]**Analyze performance:** Analyze model performance (e.g., error rates) across different pizza categories to ensure one is not predicted significantly less accurately than others. [cite: 143]

## [cite_start]Privacy [cite: 144]

* **PII Check:** The dataset is confirmed to contain no Personally Identifiable Information (PII) like customer names, addresses, or phone numbers.
* [cite_start]**Data Source:** The data is based on public menu information and does not contain private user data. [cite: 145]

## [cite_start]Consent & Transparency [cite: 147]

* **Model Purpose:** This model is intended for analysis and demonstration. It predicts pizza prices based on listed features.
* **Explainability:** The dashboard includes a section for SHAP/LIME explanations to make the model's predictions interpretable.
* **Accountability:** The code, notebooks, and this report are available in this public GitHub repository for review.