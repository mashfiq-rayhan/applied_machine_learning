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

# Principle Component Analysis

## Table of Contents

[01. Why Learn PCA](#01-why-learn-pca)

[02. Geometric Intuition of PCA](#02-geometric-intuition-of-pca)

[03. Mathematical Objective Function of PCA](#03-mathematical-objective-function-of-pca)

[04. Alternative Formulation of PCA: Distance Minimization](#04-alternative-formulation-of-pca-distance-minimization)

[05. Eigen Values and Eigen Vectors (PCA) Dimensionality Reduction](#05-eigen-values-and-eigen-vectors-pca-dimensionality-reduction)

[06. PCA for Dimensionality Reduction and Visualization](#06-pca-for-dimensionality-reduction-and-visualization)

[07. Visualize MNIST Dataset](#07-visualize-mnist-dataset)

[08. Limitations of PCA](#08-limitations-of-pca)

[09. PCA Code Example](#09-pca-code-example)

[10 - PCA for Dimensionality Reduction (Not-Visualization)](#10-pca-for-dimensionality-reduction-not-visualization)

## 01. Why Learn PCA

PCA is the **simplest** and most **fundamental** dimensionality reduction technique.


We want to reduce data from $d$-dimensions to $d'$-dimensions where $d' < d$:

$$
x_i \in \mathbb{R}^d \quad \longrightarrow \quad x_i' \in \mathbb{R}^{d'}
$$

**Examples:**
1. MNIST: $784$-dim $\rightarrow$ $2$-dim (for visualization)
2. General case: $d$-dim $\rightarrow$ $d'$-dim (e.g. $d' = 10$)


## 02. Geometric Intuition of PCA

https://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues

![PCA](./assets/02.%20PCA.jpg)

**Goal of PCA:**  
Find a new direction (axis) such that when we project the data onto that direction, the **variance (spread)** of the projected points is **maximized**.

**Simple case: 2D → 1D**

- Original data lives in 2 dimensions ($f_1$ and $f_2$)
- We want to find a single new direction $f_1'$ such that the spread of the projected points on $f_1'$ is maximum.

**Steps (2D → 1D):**
1. Rotate the axes to find the direction $f_1'$ that has maximum variance.
2. Drop the direction $f_2'$ that has very small variance.
3. Project all points $x_i$ onto $f_1'$.

Result: 2-dimensional data is reduced to 1-dimensional data while preserving as much information (variance) as possible.

### After Column Standardization

Assume the data matrix $X$ is already column-standardized:

$$
\text{mean}\{f_1\} = \text{mean}\{f_2\} = 0
$$

$$
\text{Var}\{f_1\} = \text{Var}\{f_2\} = 1
$$

The data cloud is centered at the origin.

PCA finds the direction of **maximum spread** (maximum variance) through this cloud.

### Key Idea of PCA

> We want to find a direction $f'$ such that the variance of the projected points $x_i$ onto $f'$ is **maximal**.

This direction of maximum variance is called the **First Principal Component**.

## 03. Mathematical Objective Function of PCA
![PCA](./assets/03.%20PCA.jpg)

> ### PCA – Finding the First Principal Component

### Projection onto a Direction

Let $u_1$ be a **unit vector** (direction) in the feature space:

$$
\|u_1\| = 1
$$

The projection of a data point $x_i$ onto the direction $u_1$ is:

$$
x_i' = \text{proj}_{u_1} x_i = u_1^T x_i
$$

(Since $\|u_1\| = 1$, the formula simplifies to the dot product.)

If we have the dataset

$$
D = \{x_i\}_{i=1}^n
$$

then the projected dataset becomes

$$
D' = \{x_i'\}_{i=1}^n = \{u_1^T x_i\}_{i=1}^n
$$

### Mean of the Projected Points

$$
\bar{x}' = u_1^T \bar{x}
$$

where $\bar{x}$ is the mean of the original data points.

### Objective: Maximize Variance of Projected Points

We want to find the unit vector $u_1$ such that the variance of the projected points is **maximal**:

$$
\text{Var}\{x_i'\}_{i=1}^n = \dfrac{1}{n} \sum_{i=1}^{n} (u_1^T x_i - u_1^T \bar{x})^2
$$

**Assuming the data is already column-standardized:**

$$
\bar{x} = [0, 0, \dots, 0]^T
$$

The variance simplifies to:

$$
\text{Var}\{x_i'\}_{i=1}^n = \dfrac{1}{n} \sum_{i=1}^{n} (u_1^T x_i)^2
$$

### Optimization Problem

We solve the following optimization problem:

$$
\max_{u_1} \quad \dfrac{1}{n} \sum_{i=1}^{n} (u_1^T x_i)^2
$$

subject to the constraint

$$
u_1^T u_1 = 1 \quad (\|u_1\| = 1)
$$

This is the mathematical formulation of finding the **first principal component** — the direction of maximum variance.

## 04. Alternative Formulation of PCA: Distance Minimization

https://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues/

![PCA](./assets/04.%20PCA.jpg)

PCA can also be formulated as a **distance minimization** problem.

### Idea

Instead of maximizing the projected variance, we can minimize the sum of squared distances from the original points to their projections on the line $u_1$.

Let $d_i$ be the distance from point $x_i$ to the direction $u_1$.

We solve:

$$
\min_{u_1} \sum_{i=1}^{n} d_i^2
$$

### Distance Formula

Since $u_1$ is a unit vector ($u_1^T u_1 = 1$):

$$
d_i^2 = \|x_i\|^2 - (u_1^T x_i)^2
$$

$$
d_i^2 = x_i^T x_i - (u_1^T x_i)^2
$$

### Optimization Problem (Distance Minimization)

$$
\min_{u_1} \sum_{i=1}^{n} \left( x_i^T x_i - (u_1^T x_i)^2 \right)
$$

subject to

$$
u_1^T u_1 = 1
$$

### Equivalence of the Two Formulations

Notice that:

$$
\sum_{i=1}^{n} \left( x_i^T x_i - (u_1^T x_i)^2 \right) = \text{constant} - \sum_{i=1}^{n} (u_1^T x_i)^2
$$

Therefore:

- **Minimizing** the sum of squared distances  
is exactly equivalent to  

- **Maximizing** the projected variance

$$
\max_{u_1} \dfrac{1}{n} \sum_{i=1}^{n} (u_1^T x_i)^2
\quad \text{subject to} \quad u_1^T u_1 = 1
$$

Both formulations give the same solution — the first principal component.

## 05. Eigen Values and Eigen Vectors (PCA) Dimensionality Reduction
![PCA](./assets/05.%20PCA-01.jpg)

### Solution to the PCA Optimization Problem

### Covariance Matrix

Assume $X$ is already **column-standardized**. Then the covariance matrix is:

$$
S = X^T X \quad (d \times d)
$$

$S$ is a square symmetric matrix.

### Eigenvalues and Eigenvectors

Let the eigenvalues and eigenvectors of $S$ be:

$$
\text{Eigenvalues: } \lambda_1 \ge \lambda_2 \ge \lambda_3 \ge \dots \ge \lambda_d
$$

$$
\text{Eigenvectors: } v_1, v_2, v_3, \dots, v_d
$$

By definition:

$$
S v_i = \lambda_i v_i
$$

The eigenvectors are **orthogonal**:

$$
v_i \perp v_j \quad \Rightarrow \quad v_i^T v_j = 0 \quad (i \neq j)
$$

### First Principal Component

The solution to the optimization problem is:

$$
u_1 = v_1
$$

where $v_1$ is the eigenvector corresponding to the **largest eigenvalue** $\lambda_1$.

$v_1$ is the direction of **maximum variance**.

### Higher Principal Components

- $v_1$ → direction of maximum variance
- $v_2$ → direction of second maximum variance (orthogonal to $v_1$)
- $v_3$ → direction of third maximum variance
- ...
- $v_d$ → direction of least variance

### Steps to Compute PCA

1. Column-standardize the data matrix $X$
2. Compute the covariance matrix $S = X^T X$
3. Find the eigenvalues and eigenvectors of $S$
4. Sort them: $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_d$
5. The first principal component is $u_1 = v_1$

### Explained Variance

The total variance in the data is:

$$
\sum_{i=1}^{d} \lambda_i
$$

The percentage of variance explained by the first principal component is:

$$
\dfrac{\lambda_1}{\sum_{i=1}^{d} \lambda_i}
$$

**Examples (2D case):**

- If $\lambda_1 = 3$, $\lambda_2 = 0$ → 100% variance explained by $v_1$
- If $\lambda_1 = 3$, $\lambda_2 = 1$ → 75% variance explained by $v_1$
- If $\lambda_1 = 3$, $\lambda_2 = 3$ → 50% variance explained by $v_1$

![PCA](./assets/05.%20PCA-02.jpg)
This tells us how much information we retain when we reduce the dimensionality.

## 06. PCA for Dimensionality Reduction and Visualization
![PCA](./assets/06.%20PCA-01.jpg)
![PCA](./assets/06.%20PCA-02.jpg)

### Projecting onto the First Principal Component (2D → 1D)

Given a column-standardized data matrix $X \in \mathbb{R}^{n \times d}$:

1. Compute the covariance matrix $S = X^T X$
2. Find the eigenvector $v_1$ corresponding to the largest eigenvalue $\lambda_1$
3. Project every data point onto $v_1$:

$$
x_i' = x_i^T v_1
$$

The new data matrix becomes:

$$
X' = 
\begin{bmatrix}
x_1' \\
x_2' \\
\vdots \\
x_n'
\end{bmatrix}
\in \mathbb{R}^{n \times 1}
$$

### General Case: Reducing to $d'$ Dimensions

Suppose we want to reduce from $d$ dimensions to $d'$ dimensions ($d' < d$).

1. Compute $S = X^T X$
2. Find the top $d'$ eigenvectors corresponding to the largest eigenvalues:

$$
\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_{d'} \ge \dots \ge \lambda_d
$$

$$
v_1, v_2, \dots, v_{d'}
$$

3. Form the projection matrix using these top eigenvectors.
4. Project each data point:

$$
x_i' = \big[ x_i^T v_1,\ x_i^T v_2,\ \dots,\ x_i^T v_{d'} \big]
$$

The reduced data matrix is:

$$
X' \in \mathbb{R}^{n \times d'}
$$

### Example: MNIST (784D → 2D)

- Original: $X \in \mathbb{R}^{n \times 784}$
- Take the top 2 eigenvectors $v_1$ and $v_2$
- New representation:

$$
x_i' = \big[ x_i^T v_1,\ x_i^T v_2 \big]
$$

- Result: $X' \in \mathbb{R}^{n \times 2}$ (can be visualized)

### How to Choose $d'$?

We look at the **explained variance**.

We want to preserve a large percentage of the total variance (e.g. 99%):

$$
\dfrac{\lambda_1 + \lambda_2 + \dots + \lambda_{d'}}{\sum_{i=1}^{d} \lambda_i} \approx 0.99
$$

**Example:**
- Original dimension $d = 100$
- If the first 51 eigenvalues capture 99% of the variance
- Then we can safely reduce to $d' = 51$

This way we significantly reduce dimensionality while retaining almost all the information.

## 07. Visualize MNIST Dataset
https://colah.github.io/posts/2014-10-Visualizing-MNIST/

![PCA](./assets/07.%20PCA.jpg)

### MNIST → 2D using PCA

- Original data: 784-dimensional images
- Apply PCA and keep the top 2 principal components $v_1$ and $v_2$
- Every image $x_i$ is projected to a 2D point:

$$
x_i' = \big( x_i^T v_1,\ x_i^T v_2 \big)
$$

We can now plot all the points in 2D and color them according to their digit label $y_i \in \{0,1,2,\dots,9\}$.

### Observations from the Plot

- Different digits form visible clusters in the 2D space.
- Some digits are well separated, while others overlap.
- The two axes correspond to the directions of maximum variance in the original 784-dimensional space.

### Simple Decision Rules (Examples from the plot)

- If $v_1 < 2$ and $v_2 < 10$ → the digit is likely **1**
- If $v_1 > 10$ and $v_2 < 10$ → the digit is likely **0**

These are rough regions that can be observed from the 2D scatter plot after PCA.

### Key Takeaway

Even though we reduced the data from **784 dimensions to only 2 dimensions**, a significant amount of structure is preserved.  
Digits that were different in the high-dimensional space still tend to form separate groups in the PCA 2D plot.

This is why PCA is extremely useful for:
- Visualization of high-dimensional data
- Getting a quick understanding of the structure of the dataset
- As a preprocessing step before applying other machine learning algorithms

## 08. Limitations of PCA
![PCA](./assets/08.%20PCA.jpg)

PCA is a powerful and widely used technique, but it has important limitations.

### 1. When eigenvalues are similar ($\lambda_1 \approx \lambda_2$)

If the data is roughly circular (spread is almost equal in all directions), then:

- $\lambda_1 \approx \lambda_2$
- There is no clear direction of maximum variance
- Reducing from 2D to 1D causes **very high information loss**

In such cases, projecting onto $v_1$ discards almost as much variance as it keeps.

### 2. PCA is a linear method

PCA only finds **linear** directions of maximum variance.

It cannot capture non-linear structures in the data.

**Example:**
- Data lying on a curved manifold (like a sine wave or a Swiss roll)
- The direction of maximum variance ($v_1$) may not follow the actual shape of the data
- Important non-linear patterns are lost

### 3. Clusters may get mixed

When multiple clusters exist, PCA may project them in a way that causes overlapping, especially if the direction of maximum variance does not separate the classes well.

### Summary of Limitations

- Works best when there is a clear direction of high variance
- Assumes linear relationships
- Can lose important non-linear structure
- Not always optimal for classification tasks (since it ignores class labels)

For data with complex non-linear structure, other techniques such as **t-SNE**, **UMAP**, or **Kernel PCA** are often preferred.

## 09. PCA Code Example

[Open the PCA Notebook](./PCA.ipynb)


## 10. PCA for Dimensionality Reduction (Not-Visualization)
![PCA](./assets/10.%20PCA.jpg)

PCA is not only used for visualization (2D/3D).  
It is also widely used to reduce high-dimensional data before feeding it into machine learning models.

### Example

- Original MNIST data: 784 dimensions
- For visualization we reduce to 2 dimensions
- For machine learning models we often reduce to a higher number (e.g. 10, 50, 100, 200, …) while still keeping $d' \ll 784$

$$
784 \;\xrightarrow{\text{PCA}}\; d' \quad (d' < 784)
$$

### How the Projection Works

Given a data matrix $X \in \mathbb{R}^{n \times 784}$:

1. Compute the covariance matrix $C = X^T X$
2. Find its eigenvalues and eigenvectors
3. Select the top $d'$ eigenvectors $v_1, v_2, \dots, v_{d'}$ (corresponding to the largest eigenvalues)
4. Form the projection matrix $V \in \mathbb{R}^{784 \times d'}$
5. Project the data:

$$
X' = X V \quad \in \mathbb{R}^{n \times d'}
$$

### Choosing the Right $d'$

We look at the **percentage of variance explained**:

$$
\text{Percentage of variance explained by first } d' \text{ components}
= \dfrac{\lambda_1 + \lambda_2 + \dots + \lambda_{d'}}{\sum_{i=1}^{784} \lambda_i}
$$

**Common targets:**
- 90% of variance
- 95% of variance
- 99% of variance

### Typical Results on MNIST

From the cumulative explained variance plot:

- 784 → 10 dimensions ≈ 75% variance retained
- 784 → 200 dimensions ≈ 90% variance retained
- 784 → 350 dimensions ≈ 95% variance retained

### Code Pattern 

[Open the PCA Notebook](./PCA.ipynb)

### Key Takeaway

When using PCA for dimensionality reduction before machine learning:

- We do **not** reduce all the way to 2D
- We choose the smallest $d'$ that still preserves a high percentage of the total variance (usually 90–99%)
- This gives us a much smaller feature space while keeping most of the information


