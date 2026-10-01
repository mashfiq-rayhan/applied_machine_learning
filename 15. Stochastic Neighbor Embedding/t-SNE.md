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

# t-SNE

## Table of Contents

[01. What is t-SNE](#01-what-is-t-sne)

[02. Neighborhood of a Point, Embedding](#02-neighborhood-of-a-point-embedding)

[03. Geometric Intuition of t-SNE](#03-geometric-intuition-of-t-sne)

[04. Crowding Problem](#04-crowding-problem)

[05. How to Apply t-SNE and Interpret Its Output](#05-how-to-apply-t-sne-and-interpret-its-output)

[06. t-SNE on MNIST](#06-t-sne-on-mnist)

[07. Code Example of t-SNE](#07-code-example-of-t-sne)

[08. Revision Questions](#08-revision-questions)

## 01. What is t-SNE

![t-SNE](./assets/01.%20t-SNE.jpg)

### t-SNE (t-Distributed Stochastic Neighbor Embedding)

**t-SNE** stands for **t-Distributed Stochastic Neighbor Embedding**.

It is currently considered one of the **best** dimensionality reduction techniques for **visualization**.

### Background

- PCA is the basic / classical method (finds linear directions of maximum variance)
- Older techniques: MDS, Sammon Mapping, Graph-based methods (≈ 20 years older)
- t-SNE was introduced in **2008** (by Laurens van der Maaten & Geoffrey Hinton)
- It became extremely popular around 2017

### Purpose

t-SNE is mainly used for:

$$
d\text{-dimensional data} \quad \xrightarrow{\text{t-SNE}} \quad 2\text{D or 3D}
$$

so that we can **visualize** high-dimensional data.

### t-SNE vs PCA

| Aspect              | PCA                              | t-SNE                          |
|---------------------|----------------------------------|--------------------------------|
| Type                | Linear                           | Non-linear                     |
| What it preserves   | Global structure / shape of data | Local structure / neighborhoods |
| Main use            | Dimensionality reduction + Viz   | Primarily Visualization        |
| Strength            | Fast, interpretable              | Excellent at revealing clusters |

**Geometric difference:**

- PCA tries to preserve the overall shape (global structure) of the data cloud.
- t-SNE focuses on preserving **local neighborhoods** — points that are close in high dimension should remain close in the 2D embedding.

This is why t-SNE often produces much clearer and more separated clusters than PCA when visualizing complex datasets like MNIST.

## 02. Neighborhood of a Point, Embedding

![t-SNE](./assets/02.%20t-SNE.jpg)

### What is a Neighborhood?

In high-dimensional space (e.g. MNIST: 784 dimensions), the **neighborhood** of a point $x_i$ is the set of points that are geometrically close to it.

$$
N(x_i) = \{ x_j \mid x_i \text{ and } x_j \text{ are geometrically close} \}
$$

**Distance:**

$$
\|x_i - x_j\|^2 = \text{distance}^2
$$

**Example:**

$$
N(x_1) = \{x_2, x_3, x_4\}
$$

This neighborhood does **not** contain far-away points such as $x_{10}$ or $x_{20}$.

### What is an Embedding?

An **embedding** is the low-dimensional representation of the original high-dimensional points.

- Original points: $x_i \in \mathbb{R}^d$ (high dimension)
- Embedded points: $x_i' \in \mathbb{R}^2$ or $\mathbb{R}^3$ (low dimension)

### Key Idea of t-SNE

t-SNE tries to preserve **local neighborhoods**.

- Points that are close in the original high-dimensional space should remain close in the low-dimensional embedding.
- Points that are far apart can be placed more freely (global structure is less important).

In short:

> t-SNE finds a low-dimensional embedding that preserves the **local neighborhoods** of the original high-dimensional data.

This focus on local structure is the main reason why t-SNE produces clearer clusters than PCA when visualizing complex datasets.

## 03. Geometric Intuition of t-SNE

![t-SNE](./assets/03.%20t-SNE.jpg)

### Neighborhood Preserving Embedding

t-SNE creates a low-dimensional embedding (usually 2D) that tries to preserve distances **inside local neighborhoods**.

**High-dimensional space** ($x_i \in \mathbb{R}^d$):

- $N(x_1) = \{x_2, x_3\}$ → these points are close to $x_1$
- $N(x_4) = \{x_5\}$ → $x_5$ is close to $x_4$
- Distance between different neighborhoods (e.g. $x_1$ and $x_4$) is large

**Low-dimensional embedding** ($x_i' \in \mathbb{R}^2$):

t-SNE tries to satisfy:

- $d(x_1, x_2) \approx d(x_1', x_2')$
- $d(x_1, x_3) \approx d(x_1', x_3')$
- $d(x_4, x_5) \approx d(x_4', x_5')$

But it does **not** try to preserve large distances:

- $d(x_1, x_4) \not\approx d(x_1', x_4')$  (these can be distorted)

### Summary

| Type of Distance              | Does t-SNE try to preserve it? |
|-------------------------------|--------------------------------|
| Distances inside a neighborhood | Yes                           |
| Distances between different neighborhoods | No (can be changed)     |

This is why t-SNE is excellent at revealing **local clusters**, even if the global arrangement of clusters is not perfectly preserved.

## 04. Crowding Problem

![t-SNE](./assets/04.%20t-SNE.jpg)

### What is the Crowding Problem?

t-SNE (and earlier SNE) tries to preserve distances **inside local neighborhoods**.

However, sometimes it is **impossible** to preserve all neighborhood distances when reducing dimensionality.

**Example (2D → 1D):**

- In 2D, a point $x_1$ has two neighbors $x_2$ and $x_4$ at equal distance $d$.
- $x_3$ is also at distance $d$ from $x_1$ (forming a square).

When we try to embed this into 1D while preserving the neighborhood distances:

- It becomes impossible to keep all the equal distances.
- Some points that should be close get pushed far away (or vice versa).

This mismatch is called the **Crowding Problem**.

### Why does it happen?

In high dimensions there is a lot of “space”.  
When we force the points into a much lower dimension (especially 2D or 1D), there is not enough room to keep all the local distances intact.

### How is it resolved?

- The original **SNE** suffers from the crowding problem.
- **t-SNE** solves it by using the **Student’s t-distribution** (heavy-tailed) in the low-dimensional space instead of a Gaussian.

This allows moderately distant points to be placed farther apart in the embedding, which greatly reduces the crowding effect.

## 05. How to Apply t-SNE and Interpret Its Output

https://distill.pub/2016/misread-tsne/

watch lecture video


## 06. t-SNE on MNIST

https://colah.github.io/posts/2014-10-Visualizing-MNIST/

watch lecture video

## 07. Code Example of t-SNE

[Open the t-SNE Notebook](./t-SNE.ipynb)

## 08. Revision Questions

[1. What is Dimensionality Reduction?](#1-what-is-dimensionality-reduction)  
[2. Explain Principal Component Analysis (PCA)](#2-explain-principal-component-analysis-pca)  
[3. Importance of PCA](#3-importance-of-pca)  
[4. Limitations of PCA](#4-limitations-of-pca)  
[5. What is t-SNE?](#5-what-is-t-sne)  
[6. What is the Crowding Problem?](#6-what-is-the-crowding-problem)  
[7. How to apply t-SNE and interpret its output?](#7-how-to-apply-t-sne-and-interpret-its-output)  

### 1. What is Dimensionality Reduction?

Dimensionality Reduction is the process of reducing the number of features (dimensions) in a dataset from a high dimension $d$ to a lower dimension $d'$ where $d' < d$, while trying to preserve as much important information as possible.

$$
x_i \in \mathbb{R}^d \quad \longrightarrow \quad x_i' \in \mathbb{R}^{d'}
$$

**Main goals:**
- Visualization (especially 2D / 3D)
- Speed up machine learning models
- Remove noise and redundant features
- Overcome the curse of dimensionality

### 2. Explain Principal Component Analysis (PCA)

PCA is the simplest and most fundamental linear dimensionality reduction technique.

**Core idea:**  
Find new orthogonal directions (principal components) such that the variance of the projected data is maximized.

**Steps:**
1. Column-standardize the data matrix $X$
2. Compute the covariance matrix $S = X^T X$
3. Find eigenvalues and eigenvectors of $S$
4. Sort eigenvalues: $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_d$
5. The top eigenvectors $v_1, v_2, \dots, v_{d'}$ become the new axes
6. Project the data onto these directions:

$$
x_i' = \big[ x_i^T v_1,\ x_i^T v_2,\ \dots,\ x_i^T v_{d'} \big]
$$

The first principal component $v_1$ is the direction of maximum variance.

### 3. Importance of PCA

- Reduces dimensionality while preserving maximum variance (information)
- Helps in visualization of high-dimensional data
- Speeds up training of machine learning models
- Removes multicollinearity
- Useful as a preprocessing step before clustering or classification
- Easy to interpret (linear method)

### 4. Limitations of PCA

- It is a **linear** method → cannot capture non-linear structures
- When eigenvalues are similar ($\lambda_1 \approx \lambda_2$), information loss is high
- Focuses only on variance → may not be optimal for classification
- Sensitive to scaling (hence we must standardize)
- Global structure is preserved, but local clusters may get mixed

For complex non-linear data, techniques like t-SNE or UMAP are often better for visualization.

### 5. What is t-SNE?

**t-SNE** stands for **t-Distributed Stochastic Neighbor Embedding**.

It is a non-linear dimensionality reduction technique mainly used for **visualization** of high-dimensional data in 2D or 3D.

**Key idea:**  
Preserve **local neighborhoods**. Points that are close in high dimension should remain close in the low-dimensional embedding.

- Introduced in 2008 by Laurens van der Maaten and Geoffrey Hinton
- Became extremely popular around 2017
- Much better than PCA at revealing clusters in complex datasets (e.g. MNIST)

### 6. What is the Crowding Problem?

The Crowding Problem occurs when we try to preserve all local neighborhood distances while reducing dimensionality.

In high dimensions there is a lot of space. When we force points into 2D or 1D, there is not enough room to keep all the local distances intact. Some points that should be close get pushed away (or vice versa).

- Original **SNE** suffers from the crowding problem
- **t-SNE** solves it by using the **Student’s t-distribution** (heavy-tailed) in the low-dimensional space instead of a Gaussian

### 7. How to apply t-SNE and interpret its output?

**How to apply:**
- Usually reduce high-dimensional data (e.g. 784D) directly to 2D or 3D
- Important hyperparameters: `perplexity`, `learning_rate`, `n_iter`
- Always run multiple times (t-SNE is stochastic)

**How to interpret:**
- Points that form tight clusters in the t-SNE plot were close in the original high-dimensional space
- Distance between different clusters is **not** meaningful (global structure is not preserved)
- t-SNE is excellent for visualizing clusters but should **not** be used as a general dimensionality reduction step before machine learning models (use PCA for that)

**Rule of thumb:**
- Use **PCA** when you need a reduced feature set for ML models
- Use **t-SNE** when you want to visualize and understand the structure of the data