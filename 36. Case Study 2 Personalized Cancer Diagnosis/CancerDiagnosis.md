<style>
  @import url("https://fonts.googleapis.com/css2?family=Play:wght@400;700&display=swap");
  @import url("https://cdnjs.cloudflare.com/ajax/libs/latin-modern/1.1.0/css/latinmodern-math.min.css");

  :root {
    --la-ink: #3f6386;
    --la-teal: #3f6386;
    --la-teal-soft: #e8f6f7;
    --la-coral: #9333ea;
    --la-coral-soft: #fff1ed;
    --la-cdf: #17283a;
    --la-line: #5b5c5c;
    --la-surface: #f7faf9;
    --la-text: #c9c9c9;
    --la-panel: #00070e;
    --la-chip: #17283a;
    --la-amber: #9a6b16;
    --la-amber-soft: #fff8e6;
  }

  *,
  *::before,
  *::after {
    font-family: "Play", sans-serif !important;
  }

  pre,
  pre code {
    font-family: Consolas, "Courier New", monospace !important;
  }

  body,
  .markdown-body,
  p,
  li {
    color: var(--la-text) !important;
  }

  h1 {
    color: var(--la-ink);
    border-bottom: 4px solid var(--la-teal);
    padding-bottom: 0.35em;
  }

  h2 {
    color: var(--la-teal);
    border-left: 6px solid var(--la-teal);
    padding-left: 0.55em;
    margin-top: 2em;
  }

  h3,
  h4 {
    color: var(--la-coral);
  }

  a {
    color: var(--la-coral);
    text-decoration: none;
  }

  a:hover {
    text-decoration: underline;
  }

  blockquote {
    background: var(--la-panel);
    border-left: 5px solid var(--la-cdf) !important;
    border-radius: 6px;
    color: var(--la-text);
    padding: 0.75em 1em;
  }

  code {
    background: var(--la-chip);
    border-radius: 4px;
    color: var(--la-text);
    padding: 0.1em 0.3em;
  }

  pre {
    background: var(--la-panel);
    border: 1px solid var(--la-line);
    border-radius: 8px;
    overflow-x: auto;
    padding: 1em;
  }

  table {
    border: 1px solid var(--la-line);
    border-collapse: collapse;
    border-radius: 8px;
    overflow: hidden;
    width: 100%;
  }

  th {
    background: var(--la-panel);
    color: var(--la-text);
    padding: 0.7em 0.8em;
    text-align: left;
  }

  td {
    color: var(--la-text);
    padding: 0.7em 0.8em;
  }

  tr:nth-child(even) {
    background: var(--la-chip);
  }

  hr {
    border: 0;
    border-top: 2px solid var(--la-line);
    margin: 2.2em 0;
  }

  .summary-grid,
  .ml-grid,
  .intuition-grid {
    display: flex;
    gap: 1em;
    margin: 1.25em 0;
  }

  .summary-card,
  .ml-card,
  .intuition-card {
    background: var(--la-panel);
    border-radius: 7px;
    color: var(--la-text);
    flex: 1 1 0;
    min-width: 0;
    padding: 1em;
  }

  .summary-card {
    border-top: 5px solid var(--la-teal);
  }

  .summary-card.pdf,
  .ml-card.diagnostics,
  .intuition-card.pdf {
    border-top-color: var(--la-coral);
  }

  .summary-card.cdf,
  .intuition-card.cdf {
    border-top-color: var(--la-cdf);
  }

  .summary-card h3,
  .ml-card h3,
  .intuition-card h3 {
    margin-top: 0;
  }

  .summary-tag,
  .panel-kicker {
    color: var(--la-teal);
    font-size: 0.82em;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }

  .relationship-banner,
  .ml-workflow {
    align-items: center;
    background: var(--la-panel);
    border: 1px solid var(--la-teal);
    border-radius: 7px;
    color: var(--la-text);
    display: flex;
    flex-wrap: wrap;
    gap: 0.6em;
    justify-content: center;
    margin: 1.25em 0;
    padding: 0.85em 1em;
    text-align: center;
  }

  .relationship-banner strong,
  .ml-workflow strong,
  .relationship-item strong,
  .insight-item strong {
    color: var(--la-coral);
  }

  .relationship-banner .arrow {
    color: var(--la-teal);
    font-size: 1.2em;
  }

  .relationship-item,
  .insight-item {
    background: var(--la-panel);
    border-left: 5px solid var(--la-teal);
    border-radius: 5px;
    color: var(--la-text);
    margin: 0.65em 0;
    padding: 0.55em 0.85em;
  }

  .insight-item {
    border-left-color: var(--la-coral);
  }

  .insight-list,
  .feature-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55em;
    list-style: none;
    margin: 0.5em 0 1em;
    padding: 0;
  }

  .insight-list li,
  .feature-chips li {
    background: var(--la-chip);
    border: 1px solid var(--la-teal);
    border-radius: 999px;
    color: var(--la-text);
    padding: 0.35em 0.75em;
  }

  .feature-chips li {
    border-radius: 4px;
    border-left: 3px solid var(--la-coral);
    border-right: none;
    border-top: none;
    border-bottom: none;
    flex: 1 1 calc(50% - 0.45em);
  }

  .concept-flow {
    align-items: center;
    display: flex;
    flex-direction: column;
    margin: 1.25em 0;
  }

  .concept-flow .flow-step {
    background: var(--la-panel);
    border: 1px solid var(--la-teal);
    border-radius: 7px;
    color: var(--la-text);
    max-width: 22em;
    padding: 0.7em 1.2em;
    text-align: center;
    width: 100%;
  }

  .concept-flow .flow-step strong {
    color: var(--la-coral);
  }

  .concept-flow .flow-arrow {
    color: var(--la-teal);
    font-size: 1.35em;
    line-height: 1.25;
  }

  .percentile-callout {
    background: var(--la-panel);
    border-left: 5px solid var(--la-cdf);
    border-radius: 7px;
    color: var(--la-text);
    margin: 1.25em 0;
    padding: 1em;
  }

  .percentile-callout strong {
    color: var(--la-cdf);
  }

  .katex-display,
  .math,
  .math-block {
    background: #00070e;
    border-left: 6px solid #2f005c;
    border-radius: 6px;
    padding: 0.6em 0.8em;
    overflow-x: auto;
    color: #c9c9c9 !important;
    font-family: "Latin Modern Math", "Cambria Math", "STIX Two Math", serif !important;
  }

  .katex,
  .katex * {
    color: #9b9a9a !important;
    font-family: "Latin Modern Math", "Cambria Math", "STIX Two Math", serif !important;
  }

  @media (max-width: 700px) {
    .summary-grid,
    .ml-grid,
    .intuition-grid {
      flex-direction: column;
    }
  }
</style>


> # Personalized Cancer Diagnosis

## Table of Contents

[01. Business/Real-World Problem: Overview](#01-businessreal-world-problem-overview)

[02. Business Objectives and Constraints](#02-business-objectives-and-constraints)

[03. ML Problem Formulation: Data](#03-ml-problem-formulation-data)

[04. ML Problem Formulation: Mapping Real World to ML Problem](#04-ml-problem-formulation-mapping-real-world-to-ml-problem)

[05. ML Problem Formulation: Train, CV and Test Data Construction](#05-ml-problem-formulation-train-cv-and-test-data-construction)

[06. Exploratory Data Analysis: Reading Data & Preprocessing](#06-exploratory-data-analysis-reading-data--preprocessing)

[07. Exploratory Data Analysis: Distribution of Class-Labels](#07-exploratory-data-analysis-distribution-of-class-labels)

[08. Exploratory Data Analysis: Random Model](#08-exploratory-data-analysis-random-model)

[09. Univariate Analysis: Gene Feature](#09-univariate-analysis-gene-feature)

[10. Univariate Analysis: Variation Feature](#10-univariate-analysis-variation-feature)

[11. Univariate Analysis: Text Feature](#11-univariate-analysis-text-feature)

[12. Machine Learning Models: Data Preparation](#12-machine-learning-models-data-preparation)

[13. Baseline Model: Naive Bayes](#13-baseline-model-naive-bayes)

[14. K-Nearest Neighbors Classification](#14-k-nearest-neighbors-classification)

[15. Logistic Regression with Class Balancing](#15-logistic-regression-with-class-balancing)

[16. Logistic Regression without Class Balancing](#16-logistic-regression-without-class-balancing)

[17. Linear SVM](#17-linear-svm)

[18. Random Forest with One-Hot Encoded Features](#18-random-forest-with-one-hot-encoded-features)

[19. Random Forest with Response-Coded Features](#19-random-forest-with-response-coded-features)

[20. Stacking Classifier](#20-stacking-classifier)

[21. Majority Voting Classifier](#21-majority-voting-classifier)

[22. Assignments](#22-assignments)





> # 36. Personalized Cancer Diagnosis

## 01. Business/Real-World Problem: Overview

![LR](./assets/01.01.jpg)  

![LR](./assets/01.02.jpg)  





## 02. Business Objectives and Constraints

![LR](./assets/02.01.jpg)  

![LR](./assets/02.02.jpg)  





## 03. ML Problem Formulation: Data

![LR](./assets/03.01.jpg)  

![LR](./assets/03.02.jpg)  





## 04. ML Problem Formulation: Mapping Real World to ML Problem

![LR](./assets/04.01.jpg)  

![LR](./assets/04.02.jpg)  





## 05. ML Problem Formulation: Train, CV and Test Data Construction

![LR](./assets/05.01.jpg)  

![LR](./assets/05.02.jpg)  





## 06. Exploratory Data Analysis: Reading Data & Preprocessing

![LR](./assets/06.01.jpg)  

![LR](./assets/06.02.jpg)  





## 07. Exploratory Data Analysis: Distribution of Class-Labels

![LR](./assets/07.01.jpg)  

![LR](./assets/07.02.jpg)  





## 08. Exploratory Data Analysis: Random Model

![LR](./assets/08.01.jpg)  

![LR](./assets/08.02.jpg)  





## 09. Univariate Analysis: Gene Feature

![LR](./assets/09.01.jpg)  

![LR](./assets/09.02.jpg)  





## 10. Univariate Analysis: Variation Feature

![LR](./assets/10.01.jpg)  

![LR](./assets/10.02.jpg)  





## 11. Univariate Analysis: Text Feature

![LR](./assets/11.01.jpg)  

![LR](./assets/11.02.jpg)  





## 12. Machine Learning Models: Data Preparation

![LR](./assets/12.01.jpg)  

![LR](./assets/12.02.jpg)  





## 13. Baseline Model: Naive Bayes

![LR](./assets/13.01.jpg)  

![LR](./assets/13.02.jpg)  





## 14. K-Nearest Neighbors Classification

![LR](./assets/14.01.jpg)  

![LR](./assets/14.02.jpg)  





## 15. Logistic Regression with Class Balancing

![LR](./assets/15.01.jpg)  

![LR](./assets/15.02.jpg)  





## 16. Logistic Regression without Class Balancing

![LR](./assets/16.01.jpg)  

![LR](./assets/16.02.jpg)  





## 17. Linear SVM

![LR](./assets/17.01.jpg)  

![LR](./assets/17.02.jpg)  





## 18. Random Forest with One-Hot Encoded Features

![LR](./assets/18.01.jpg)  

![LR](./assets/18.02.jpg)  





## 19. Random Forest with Response-Coded Features

![LR](./assets/19.01.jpg)  

![LR](./assets/19.02.jpg)  





## 20. Stacking Classifier

![LR](./assets/20.01.jpg)  

![LR](./assets/20.02.jpg)  





## 21. Majority Voting Classifier

![LR](./assets/21.01.jpg)  

![LR](./assets/21.02.jpg)  





## 22. Assignments

![LR](./assets/22.01.jpg)  

![LR](./assets/22.02.jpg)