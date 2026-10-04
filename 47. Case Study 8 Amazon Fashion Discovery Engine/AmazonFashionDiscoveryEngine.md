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

# Amazon Fashion Discovery Engine


# Product Similarity Recommendation System

## Table of Contents

[01. Problem Statement: Recommend Similar Apparel Products in E-Commerce Using Product Descriptions and Images](#01-problem-statement-recommend-similar-apparel-products-in-e-commerce-using-product-descriptions-and-images)

[02. Plan of Action](#02-plan-of-action)

[03. Amazon Product Advertising API](#03-amazon-product-advertising-api)

[04. Data Folders and Paths](#04-data-folders-and-paths)

[05. Overview of the Data and Terminology](#05-overview-of-the-data-and-terminology)

[06. Data Cleaning and Understanding: Missing Data in Various Features](#06-data-cleaning-and-understanding-missing-data-in-various-features)

[07. Understand Duplicate Rows](#07-understand-duplicate-rows)

[08. Remove Duplicates: Part 1](#08-remove-duplicates-part-1)

[09. Remove Duplicates: Part 2](#09-remove-duplicates-part-2)

[10. Text Pre-Processing: Tokenization and Stop-Word Removal](#10-text-pre-processing-tokenization-and-stop-word-removal)

[11. Stemming](#11-stemming)

[12. Text-Based Product Similarity: Converting Text to an n-D Vector Using Bag of Words](#12-text-based-product-similarity-converting-text-to-an-nd-vector-using-bag-of-words)

[13. Code for Bag of Words-Based Product Similarity](#13-code-for-bag-of-words-based-product-similarity)

[14. TF-IDF: Featurizing Text Based on Word Importance](#14-tf-idf-featurizing-text-based-on-word-importance)

[15. Code for TF-IDF-Based Product Similarity](#15-code-for-tf-idf-based-product-similarity)

[16. Code for IDF-Based Product Similarity](#16-code-for-idf-based-product-similarity)

[17. Text Semantics-Based Product Similarity: Word2Vec](#17-text-semantics-based-product-similarity-word2vec)

[18. Code for Average Word2Vec Product Similarity](#18-code-for-average-word2vec-product-similarity)

[19. TF-IDF Weighted Word2Vec](#19-tf-idf-weighted-word2vec)

[20. Code for IDF Weighted Word2Vec Product Similarity](#20-code-for-idf-weighted-word2vec-product-similarity)

[21. Weighted Similarity Using Brand and Color](#21-weighted-similarity-using-brand-and-color)

[22. Code for Weighted Similarity](#22-code-for-weighted-similarity)

[23. Building a Real-World Solution](#23-building-a-real-world-solution)

[24. Deep Learning-Based Visual Product Similarity: ConvNets](#24-deep-learning-based-visual-product-similarity-convnets)

[25. Using Keras + TensorFlow to Extract Features](#25-using-keras--tensorflow-to-extract-features)

[26. Visual Similarity-Based Product Similarity](#26-visual-similarity-based-product-similarity)

[27. Measuring Goodness of Our Solution: A/B Testing](#27-measuring-goodness-of-our-solution-ab-testing)

[28. Exercise: Build a Weighted Nearest Neighbor Model Using Visual, Text, Brand and Color](#28-exercise-build-a-weighted-nearest-neighbor-model-using-visual-text-brand-and-color)

# Amazon Fashion Discovery Engine

# Product Similarity Recommendation System

## 01. Problem Statement: Recommend Similar Apparel Products in E-Commerce Using Product Descriptions and Images

![LR](./assets/01.01.jpg)

![LR](./assets/01.02.jpg)

## 02. Plan of Action

![LR](./assets/02.01.jpg)

![LR](./assets/02.02.jpg)

## 03. Amazon Product Advertising API

![LR](./assets/03.01.jpg)

![LR](./assets/03.02.jpg)

## 04. Data Folders and Paths

![LR](./assets/04.01.jpg)

![LR](./assets/04.02.jpg)

## 05. Overview of the Data and Terminology

![LR](./assets/05.01.jpg)

![LR](./assets/05.02.jpg)

## 06. Data Cleaning and Understanding: Missing Data in Various Features

![LR](./assets/06.01.jpg)

![LR](./assets/06.02.jpg)

## 07. Understand Duplicate Rows

![LR](./assets/07.01.jpg)

![LR](./assets/07.02.jpg)

## 08. Remove Duplicates: Part 1

![LR](./assets/08.01.jpg)

![LR](./assets/08.02.jpg)

## 09. Remove Duplicates: Part 2

![LR](./assets/09.01.jpg)

![LR](./assets/09.02.jpg)

## 10. Text Pre-Processing: Tokenization and Stop-Word Removal

![LR](./assets/10.01.jpg)

![LR](./assets/10.02.jpg)

## 11. Stemming

![LR](./assets/11.01.jpg)

![LR](./assets/11.02.jpg)

## 12. Text-Based Product Similarity: Converting Text to an n-D Vector Using Bag of Words

![LR](./assets/12.01.jpg)

![LR](./assets/12.02.jpg)

## 13. Code for Bag of Words-Based Product Similarity

![LR](./assets/13.01.jpg)

![LR](./assets/13.02.jpg)

## 14. TF-IDF: Featurizing Text Based on Word Importance

![LR](./assets/14.01.jpg)

![LR](./assets/14.02.jpg)

## 15. Code for TF-IDF-Based Product Similarity

![LR](./assets/15.01.jpg)

![LR](./assets/15.02.jpg)

## 16. Code for IDF-Based Product Similarity

![LR](./assets/16.01.jpg)

![LR](./assets/16.02.jpg)

## 17. Text Semantics-Based Product Similarity: Word2Vec

![LR](./assets/17.01.jpg)

![LR](./assets/17.02.jpg)

## 18. Code for Average Word2Vec Product Similarity

![LR](./assets/18.01.jpg)

![LR](./assets/18.02.jpg)

## 19. TF-IDF Weighted Word2Vec

![LR](./assets/19.01.jpg)

![LR](./assets/19.02.jpg)

## 20. Code for IDF Weighted Word2Vec Product Similarity

![LR](./assets/20.01.jpg)

![LR](./assets/20.02.jpg)

## 21. Weighted Similarity Using Brand and Color

![LR](./assets/21.01.jpg)

![LR](./assets/21.02.jpg)

## 22. Code for Weighted Similarity

![LR](./assets/22.01.jpg)

![LR](./assets/22.02.jpg)

## 23. Building a Real-World Solution

![LR](./assets/23.01.jpg)

![LR](./assets/23.02.jpg)

## 24. Deep Learning-Based Visual Product Similarity: ConvNets

![LR](./assets/24.01.jpg)

![LR](./assets/24.02.jpg)

## 25. Using Keras + TensorFlow to Extract Features

![LR](./assets/25.01.jpg)

![LR](./assets/25.02.jpg)

## 26. Visual Similarity-Based Product Similarity

![LR](./assets/26.01.jpg)

![LR](./assets/26.02.jpg)

## 27. Measuring Goodness of Our Solution: A/B Testing

![LR](./assets/27.01.jpg)

![LR](./assets/27.02.jpg)

## 28. Exercise: Build a Weighted Nearest Neighbor Model Using Visual, Text, Brand and Color

![LR](./assets/28.01.jpg)

![LR](./assets/28.02.jpg)
