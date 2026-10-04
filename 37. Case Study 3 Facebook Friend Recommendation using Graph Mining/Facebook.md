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


# Facebook Friend Recommendation using Graph Mining

## Table of Contents

[01. Problem Definition](#01-problem-definition)

[02. Overview of Graphs: Node/Vertex, Edge/Link, Directed Edge, Path](#02-overview-of-graphs-nodevertex-edgelink-directed-edge-path)

[03. Data Format & Limitations](#03-data-format--limitations)

[04. Mapping to a Supervised Classification Problem](#04-mapping-to-a-supervised-classification-problem)

[05. Business Constraints & Metrics](#05-business-constraints--metrics)

[06. EDA: Basic Stats](#06-eda-basic-stats)

[07. EDA: Follower and Following Stats](#07-eda-follower-and-following-stats)

[08. EDA: Binary Classification Task](#08-eda-binary-classification-task)

[09. EDA: Train and Test Split](#09-eda-train-and-test-split)

[10. Feature Engineering on Graphs: Jaccard & Cosine Similarities](#10-feature-engineering-on-graphs-jaccard--cosine-similarities)

[11. PageRank](#11-pagerank)

[12. Shortest Path](#12-shortest-path)

[13. Connected Components](#13-connected-components)

[14. Adar Index](#14-adar-index)

[15. Katz Centrality](#15-katz-centrality)

[16. HITS Score](#16-hits-score)

[17. SVD](#17-svd)

[18. Weight Features](#18-weight-features)

[19. Modeling](#19-modeling)





# 37. Facebook Friend Recommendation using Graph Mining

## 01. Problem Definition

![LR](./assets/01.01.jpg)  

![LR](./assets/01.02.jpg)  





## 02. Overview of Graphs: Node/Vertex, Edge/Link, Directed Edge, Path

![LR](./assets/02.01.jpg)  

![LR](./assets/02.02.jpg)  





## 03. Data Format & Limitations

![LR](./assets/03.01.jpg)  

![LR](./assets/03.02.jpg)  





## 04. Mapping to a Supervised Classification Problem

![LR](./assets/04.01.jpg)  

![LR](./assets/04.02.jpg)  





## 05. Business Constraints & Metrics

![LR](./assets/05.01.jpg)  

![LR](./assets/05.02.jpg)  





## 06. EDA: Basic Stats

![LR](./assets/06.01.jpg)  

![LR](./assets/06.02.jpg)  





## 07. EDA: Follower and Following Stats

![LR](./assets/07.01.jpg)  

![LR](./assets/07.02.jpg)  





## 08. EDA: Binary Classification Task

![LR](./assets/08.01.jpg)  

![LR](./assets/08.02.jpg)  





## 09. EDA: Train and Test Split

![LR](./assets/09.01.jpg)  

![LR](./assets/09.02.jpg)  





## 10. Feature Engineering on Graphs: Jaccard & Cosine Similarities

![LR](./assets/10.01.jpg)  

![LR](./assets/10.02.jpg)  





## 11. PageRank

![LR](./assets/11.01.jpg)  

![LR](./assets/11.02.jpg)  





## 12. Shortest Path

![LR](./assets/12.01.jpg)  

![LR](./assets/12.02.jpg)  





## 13. Connected Components

![LR](./assets/13.01.jpg)  

![LR](./assets/13.02.jpg)  





## 14. Adar Index

![LR](./assets/14.01.jpg)  

![LR](./assets/14.02.jpg)  





## 15. Katz Centrality

![LR](./assets/15.01.jpg)  

![LR](./assets/15.02.jpg)  





## 16. HITS Score

![LR](./assets/16.01.jpg)  

![LR](./assets/16.02.jpg)  





## 17. SVD

![LR](./assets/17.01.jpg)  

![LR](./assets/17.02.jpg)  





## 18. Weight Features

![LR](./assets/18.01.jpg)  

![LR](./assets/18.02.jpg)  





## 19. Modeling

![LR](./assets/19.01.jpg)  

![LR](./assets/19.02.jpg)