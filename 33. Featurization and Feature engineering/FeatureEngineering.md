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

# Featurization and Feature Engineering

> # Feature Engineering

## Table of Contents

[01. Introduction](#01-introduction)

[02. Moving Window for Time Series Data](#02-moving-window-for-time-series-data)

[03. Fourier Decomposition](#03-fourier-decomposition)

[04. Deep Learning Features: LSTM](#04-deep-learning-features-lstm)

[05. Image Histogram](#05-image-histogram)

[06. Keypoints: SIFT](#06-keypoints-sift)

[07. Deep Learning Features: CNN](#07-deep-learning-features-cnn)

[08. Relational Data](#08-relational-data)

[09. Graph Data](#09-graph-data)

[10. Indicator Variables](#10-indicator-variables)

[11. Feature Binning](#11-feature-binning)

[12. Interaction Variables](#12-interaction-variables)

[13. Mathematical Transforms](#13-mathematical-transforms)

[14. Model-Specific Featurizations](#14-model-specific-featurizations)

[15. Feature Orthogonality](#15-feature-orthogonality)

[16. Domain-Specific Featurizations](#16-domain-specific-featurizations)

[17. Feature Slicing](#17-feature-slicing)

[18. Kaggle Winners' Solutions](#18-kaggle-winners-solutions)





# Feature Engineering

## 01. Introduction

![LR](./assets/01.01.jpg)  

![LR](./assets/01.02.jpg)  





## 02. Moving Window for Time Series Data

![LR](./assets/02.01.jpg)  

![LR](./assets/02.02.jpg)  





## 03. Fourier Decomposition

![LR](./assets/03.01.jpg)  

![LR](./assets/03.02.jpg)  





## 04. Deep Learning Features: LSTM

![LR](./assets/04.01.jpg)  

![LR](./assets/04.02.jpg)  





## 05. Image Histogram

![LR](./assets/05.01.jpg)  

![LR](./assets/05.02.jpg)  





## 06. Keypoints: SIFT

![LR](./assets/06.01.jpg)  

![LR](./assets/06.02.jpg)  





## 07. Deep Learning Features: CNN

![LR](./assets/07.01.jpg)  

![LR](./assets/07.02.jpg)  





## 08. Relational Data

![LR](./assets/08.01.jpg)  

![LR](./assets/08.02.jpg)  





## 09. Graph Data

![LR](./assets/09.01.jpg)  

![LR](./assets/09.02.jpg)  





## 10. Indicator Variables

![LR](./assets/10.01.jpg)  

![LR](./assets/10.02.jpg)  





## 11. Feature Binning

![LR](./assets/11.01.jpg)  

![LR](./assets/11.02.jpg)  





## 12. Interaction Variables

![LR](./assets/12.01.jpg)  

![LR](./assets/12.02.jpg)  





## 13. Mathematical Transforms

![LR](./assets/13.01.jpg)  

![LR](./assets/13.02.jpg)  





## 14. Model-Specific Featurizations

![LR](./assets/14.01.jpg)  

![LR](./assets/14.02.jpg)  





## 15. Feature Orthogonality

![LR](./assets/15.01.jpg)  

![LR](./assets/15.02.jpg)  





## 16. Domain-Specific Featurizations

![LR](./assets/16.01.jpg)  

![LR](./assets/16.02.jpg)  





## 17. Feature Slicing

![LR](./assets/17.01.jpg)  

![LR](./assets/17.02.jpg)  





## 18. Kaggle Winners' Solutions

![LR](./assets/18.01.jpg)  

![LR](./assets/18.02.jpg)