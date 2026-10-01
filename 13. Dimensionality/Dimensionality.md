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

# Dimensionality Reduction

## Table of Contents

[01. What is Dimensionality Reduction](#01-what-is-dimensionality-reduction)  
[02. Row Vector and Column Vector](#02-row-vector-and-column-vector)  
[03. How to Represent a Data Set](#03-how-to-represent-a-data-set)  
[04. How to Represent a Dataset as a Matrix](#04-how-to-represent-a-dataset-as-a-matrix)  
[05. Data Preprocessing: Feature/Column Normalisation](#05-data-preprocessing-featurecolumn-normalisation)  
[06. Mean of a Data Matrix](#06-mean-of-a-data-matrix)  
[07. Data Preprocessing: Column Standardization](#07-data-preprocessing-column-standardization)  
[08. Co-variance of a Data Matrix](#08-co-variance-of-a-data-matrix)  
[09. MNIST Dataset (784 Dimensional)](#09-mnist-dataset-784-dimensional)  
[10 - Code to Load MNIST Data Set](#10-code-to-load-mnist-data-set)

## 01. What is Dimensionality Reduction

**Problem:**

- 2D and 3D data → We can easily visualize using **scatter plots**
- 4D, 5D, 6D data → Can use **pair plots**
- But what about **10D, 100D, or 1000D** data?

**Solution:**  
Dimensionality Reduction techniques help us reduce high-dimensional data ($n$D) to 2D or 3D so that we can visualize and understand it.

**Popular techniques:**

- **PCA** (Principal Component Analysis)
- **t-SNE** (t-Distributed Stochastic Neighbor Embedding)

## 02. Row Vector and Column Vector

In machine learning, a data point is usually represented as a **vector**.

**Example (Iris flower features):**

- Features: Sepal Length (SL), Sepal Width (SW), Petal Length (PL), Petal Width (PW)

By default, we treat a data point as a **column vector**:

$$
x_i = \begin{bmatrix}
x_{i1} \\
x_{i2} \\
x_{i3} \\
x_{i4}
\end{bmatrix}
= \begin{bmatrix}
\text{SL} \\
\text{SW} \\
\text{PL} \\
\text{PW}
\end{bmatrix}
\in \mathbb{R}^4
$$

**Row vector** (transpose):

$$
x_i^T = [2.1,\ 3.3,\ 9.8,\ 1.2]
$$

**Important Convention:**

> In most mathematical formulations in Machine Learning, we assume $x_i$ is a **column vector**.

## 03. How to Represent a Data Set

A dataset $D$ with $n$ data points is written as:

$$
D = \left\{ (x_i, y_i) \right\}_{i=1}^{n}
$$

Where:

- $n$ = number of data points
- $x_i \in \mathbb{R}^d$ → feature vector (column vector)
- $y_i$ → class label

**Example (Iris Dataset):**

- $x_i \in \mathbb{R}^4$ (4 features: SL, SW, PL, PW)
- $y_i \in \{\text{Setosa},\ \text{Versicolor},\ \text{Virginica}\}$

$$
x_i = \begin{bmatrix}
\text{SL} \\
\text{SW} \\
\text{PL} \\
\text{PW}
\end{bmatrix}
$$

## 04. How to Represent a Dataset as a Matrix

$$
X = 
\begin{bmatrix}
\begin{array}{c|cccccc}
 & f_1 & f_2 & f_3 & \cdots & f_j & \cdots & f_d \\
\hline
x_1 & & & &  & a_{1} &  & \\
x_2 & & & &  & a_{2} &  & \\
\vdots & \vdots & \vdots & \vdots &  & \vdots &  &  \\
x_i &  &  & x_i^T &  & a_{i} &  &  \\
\vdots & \vdots & \vdots & \vdots &  & \vdots &  &  \\
x_n &  &  &  &  & a_{n} &  &  \\
\end{array}
\end{bmatrix}_{n \times d}
\quad
Y = 
\begin{bmatrix}
y_1 \\
y_2 \\
\vdots \\
y_i \\
\vdots \\
y_n
\end{bmatrix}_{n \times 1}
$$

- Dataset: $D = \{(x_i, y_i)\}_{i=1}^n$
- $x_i \in \mathbb{R}^d$
- $y_i \in \{\text{se}, \text{ve}, \text{vi}\}$
- Each row of $X$ = one data point
- Each column of $X$ = one feature
- $x_i$ is a column vector $\rightarrow$ $x_i^T$ is a row vector

$$
X^T =
\begin{bmatrix}
 &  & 1 & 2 & 3 & \dots & i & \dots & n \\
\hline
f_1 &  &  &  &  &  &  &  &  \\
f_2 &  &  &  &  &  &  &  &  \\
\vdots &  &  &  &  &  &  x_i  &  \\
f_j &  &  &  f_j  &  &  &  &  \\
\vdots &  &  &  &  &  &  &  &  \\
f_d &  &  &  &  &  &  &  &
\end{bmatrix}_{d \times n}
$$

- Each **column** = one data point
- Each **row** = one feature / variable
- Example: $f_1$ = PL, $f_2$ = PW, $f_3$ = SL, $f_4$ = SW

**Like a Table**

|          |          | SL    | SW    | PL    | PW    |
| -------- | -------- | ----- | ----- | ----- | ----- |
|          |          | $f_1$ | $f_2$ | $f_3$ | $f_4$ |
| $fl_1$   | $x_1$    |       |       |       |       |
| $fl_2$   | $x_2$    |       |       |       |       |
| $fl_3$   | $x_3$    |       |       |       |       |
| $\ldots$ | $\ldots$ |       |       |       |       |
| $\ldots$ | $\ldots$ |       |       |       |       |
| $\ldots$ | $\ldots$ |       |       |       |       |

## 05. Data Preprocessing: Feature/Column Normalisation

### Data Preprocessing: Column Normalization

Data Preprocessing → Feature Normalization (Column Normalization)

We do column normalization before applying any model (including Dimensionality Reduction).

Original data matrix

$$
X = 
\begin{bmatrix}
\begin{array}{c|cccccc}
 & f_1 & f_2 & f_3 & \cdots & f_j & \cdots & f_d \\
\hline
x_1 & & & &  & a_{1} &  & \\
x_2 & & & &  & a_{2} &  & \\
\vdots & \vdots & \vdots & \vdots &  & \vdots &  &  \\
x_i &  &  & x_i^T &  & a_{i} &  &  \\
\vdots & \vdots & \vdots & \vdots &  & \vdots &  &  \\
x_n &  &  &  &  & a_{n} &  &  \\
\end{array}
\end{bmatrix}_{n \times d}
\quad
Y = 
\begin{bmatrix}
y_1 \\
y_2 \\
\vdots \\
y_i \\
\vdots \\
y_n
\end{bmatrix}_{n \times 1}
$$

- $X \in \mathbb{R}^{n \times d}$
- Each $x_i$ is a column vector of size $d \times 1$
- $Y$ is the label vector of size $n \times 1$
- $x_i \in \mathbb{R}^d$, $y_i$ is the corresponding class label

This is the form of the data **before** applying column normalization.

After column normalization we get a new matrix where every column is scaled.

### **Question:** What is column normalization?

### Column Normalization

$$
X = 
\begin{bmatrix}
\begin{array}{c|cccccc}
 & f_1 & f_2 & f_3 & \cdots & f_j & \cdots & f_d \\
\hline
x_1 & & & &  & a_{1} &  & \\
x_2 & & & &  & a_{2} &  & \\
\vdots & \vdots & \vdots & \vdots &  & \vdots &  &  \\
x_i &  &  & x_i^T &  & a_{i} &  &  \\
\vdots & \vdots & \vdots & \vdots &  & \vdots &  &  \\
x_n &  &  &  &  & a_{n} &  &  \\
\end{array}
\end{bmatrix}_{n \times d}
\quad
Y = 
\begin{bmatrix}
y_1 \\
y_2 \\
\vdots \\
y_i \\
\vdots \\
y_n
\end{bmatrix}_{n \times 1}
$$

- Each column of $X^{T}$ is a data point $x_i = \begin{bmatrix} a_{1i} \\ a_{2i} \\ \vdots \\ a_{di} \end{bmatrix}$
- $a_{ji}$ = value of feature $f_j$ for the $i$-th data point
- Rows correspond to features $f_1, f_2, \dots, f_d$
- $Y$ is the label vector

For a column $f_j$ with $n$ values:

$$
[a_1, a_2, \dots, a_i, \dots, a_n]
$$

$$
\max(a_i) = a_{\max}, \quad i = 1 \dots n
$$

$$
\min(a_i) = a_{\min}, \quad i = 1 \dots n
$$

Normalized value:

$$
a_i' = \dfrac{a_i - a_{\min}}{a_{\max} - a_{\min}}
$$

After normalization:

$$
a_i' \in [0, 1]
$$

So the whole column becomes:

$$
[a_1', a_2', \dots, a_n'] \quad \text{;} \quad a_i' \in [0,1]
$$

> step ➡
$$
[a_1, a_2, \dots, a_i, \dots, a_n] \quad \text{;} \quad  a_i \in \mathbb{R}
$$


$$
\dfrac{a_i - a_{\min}}{a_{\max} - a_{\min}}
$$

$$
[a_1', a_2', \dots a_i' \dots, a_n'] \quad \text{;} \quad a_i' \in [0,1]
$$

### Why Column Normalization?

![tbl](./assets/05.%20G3.jpg)

Different features can have very different scales (example: height in cm, weight in kg, age in years).

If we do not normalize:
- Features with larger numbers dominate
- Distance calculations become biased

After column normalization:
- Every feature lies in the same range $[0,1]$
- All features become comparable
- Getting rid of scale
- Everything in same scale

### Geometric Intuition
> 2D:

![G](./assets/05.%20G1.jpg)

> 3D:

![G](./assets/05.%20G2.jpg)

**Before normalization:**
- Data is stretched differently along different axes

**After column normalization:**
- 2D data lies inside a unit square
- 3D data lies inside a unit cube
- High-dimensional data lies inside a unit hypercube

This is why we almost always perform column normalization before applying PCA, t-SNE, or any distance-based method.

## 06. Mean of a Data Matrix

$$
X = 
\begin{bmatrix}
\begin{array}{c|cccccc}
 & f_1 & f_2 & f_3 & \cdots & f_j & \cdots & f_d \\
\hline
x_1 & & & &  & a_{1} &  & \\
x_2 & & & &  & a_{2} &  & \\
\vdots & \vdots & \vdots & \vdots &  & \vdots &  &  \\
x_i &  &  & x_i^T &  & a_{i} &  &  \\
\vdots & \vdots & \vdots & \vdots &  & \vdots &  &  \\
x_n &  &  &  &  & a_{n} &  &  \\
\end{array}
\end{bmatrix}_{n \times d}
\quad
Y = 
\begin{bmatrix}
y_1 \\
y_2 \\
\vdots \\
y_i \\
\vdots \\
y_n
\end{bmatrix}_{n \times 1}
$$

- Dataset: $D = \{(x_i, y_i)\}_{i=1}^n$
- $x_i \in \mathbb{R}^d$
- $y_i \in \{\text{se}, \text{ve}, \text{vi}\}$
- Each row of $X$ = one data point
- Each column of $X$ = one feature
- $x_i$ is a column vector $\rightarrow$ $x_i^T$ is a row vector

I have provided a transcription of the handwritten lecture note for you below:

Let $x_i \in \mathbb{R}^d$

$$x_1 = [2.2, 9.2] \to \mathbb{R}^2$$

$$x_2 = [1.2, 3.2] \to \mathbb{R}^2$$

$$x_1 + x_2 = [3.4, 7.4]$$


$$\bar{x} \in \mathbb{R}^d$$

$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i \quad \quad \bar{x} \in \mathbb{R}^d$$

$$= \frac{1}{n}(x_1 + x_2 + \dots + x_n) \quad x_i \in \mathbb{R}^d$$

mean vector.

**Geometric:**

> $x_2 = W$ $x_1 = L$

![mean](./assets/06.%20G1.jpg)


$$x_i \in \mathbb{R}^d, \quad [L, W] \to [f_1, f_2]$$

$$\bar{x} = [L_{\bar{x}}, W_{\bar{x}}] = [\bar{f}_1, \bar{f}_2]$$

$$\bar{x} = [L_{\bar{x}}, W_{\bar{x}}] = [f_{\bar{1}}, f_{\bar{2}}]$$

$$
L_{\bar{x}} = mean(L_i)_{i=1}^n
$$

$$
W_{\bar{x}} = mean(W_i)_{i=1}^n
$$

$$\bar{x} = [L_{\bar{x}}, W_{\bar{x}}] = [\bar{f}_1, \bar{f}_2]$$

> `mean` $\to$ `central value`  ;  `mean vector` $\to$ `central vector`.

## 07. Data Preprocessing: Column Standardization

Column normalization: transforms each feature to the range $[0,1]$ (gets rid of the scale of each feature).

**`Column Standardization`** is used **more often** than **`Column Normalization`**.

**Original data matrix:**

$$
X = 
\begin{bmatrix}
\begin{array}{c|cccccc}
 & f_1 & f_2 & f_3 & \cdots & f_j & \cdots & f_d \\
\hline
x_1 &  &  &  &  & a_1 &  &  \\
x_2 &  &  &  &  & a_2 &  &  \\
\vdots & \vdots & \vdots & \vdots &  & \vdots &  &  \\
x_i &  &  & x_i^T &  & a_i &  &  \\
\vdots & \vdots & \vdots & \vdots &  & \vdots &  &  \\
x_n &  &  &  &  & a_n &  &  \\
\end{array}
\end{bmatrix}_{n \times d}
\quad
Y = 
\begin{bmatrix}
y_1 \\
y_2 \\
\vdots \\
y_i \\
\vdots \\
y_n
\end{bmatrix}_{n \times 1}
$$

- Dataset: $D = \{(x_i, y_i)\}_{i=1}^n$
- $x_i \in \mathbb{R}^d$
- Each row of $X$ = one data point
- Each column of $X$ = one feature
- $x_i$ is a column vector $\rightarrow$ $x_i^T$ is a row vector

For a column $f_j$ with values:

$$
[a_1, a_2, \dots, a_i, \dots, a_n]
$$

After **column standardization**:

$$
[a_1', a_2', \dots, a_i', \dots, a_n']
$$

where

$$
\text{mean}\{a_i'\}_{i=1}^n = 0, \quad \text{std-dev}\{a_i'\}_{i=1}^n = 1
$$

**Formula:**

$$
\bar{a} = \text{Mean}\{a_i\}_{i=1}^n
$$

$$
s = \text{Std-Dev}\{a_i\}_{i=1}^n
$$

$$
a_i' = \dfrac{a_i - \bar{a}}{s}
$$

This is similar to the standard normal variate:

$$
Z = \dfrac{x - \mu}{\sigma}
$$

If $x \sim \mathcal{N}(\mu, \sigma)$, then $Z \sim \mathcal{N}(0,1)$.

### Geometric Intuition

![G1](./assets/07.%20G1.jpg)

**Before column standardization:**
- Data cloud is centered at some mean vector
- Different features have different spreads (variances)

**After column standardization:**
1. Moves the mean vector to the **origin** $[0, 0, \dots, 0]$
2. Squashes / expands each axis so that the standard deviation of every feature becomes **1**

Result: data is centered at the origin with unit variance along every feature.

Column standardization = **mean centering** (to origin) + **scaling** (std-dev = 1)

## 08. Co-variance of a Data Matrix

**Data Matrix:**

$$
X = 
\begin{bmatrix}
\begin{array}{c|cccc}
 & f_1 & f_2 & \cdots & f_d \\
\hline
 &  &  &  &  \\
 &  & x_i^T &  &  \\
 &  &  &  &  \\
\end{array}
\end{bmatrix}_{n \times d}
$$

**Definition: Covariance Matrix of $X$**

$$
S = 
\begin{bmatrix}
s_{ij}
\end{bmatrix}_{d \times d}
$$

Where

$$
s_{ij} = \text{Cov}(f_i, f_j)
$$

$$
\text{Cov}(X,Y) = \dfrac{1}{n} \sum_{i=1}^{n} (x_i - \mu_x)(y_i - \mu_y)
$$

**Properties:**

1. $\text{Cov}(f_i, f_i) = \text{Var}(f_i)$
2. $\text{Cov}(f_i, f_j) = \text{Cov}(f_j, f_i)$

Therefore $S$ is a **symmetric matrix**:

$$
s_{ij} = s_{ji}
$$

- Diagonal elements of $S$ = variances of the features
- Off-diagonal elements = covariances between different features
- $S$ is a square symmetric matrix of size $d \times d$

**After Column Standardization:**

If $X$ has been column-standardized, then:

- Mean of each feature $f_j$ = 0
- Std-dev of each feature $f_j$ = 1

In this case the covariance simplifies to:

$$
\text{Cov}(f_1, f_2) = \dfrac{1}{n} \sum_{i=1}^{n} x_{i1} \cdot x_{i2} = \dfrac{f_1^T f_2}{n}
$$

In matrix form (when $X$ is column-standardized):

$$
S = \dfrac{1}{n} X^T X
$$

**Matrix multiplication view:**

$$
X^T X = 
\begin{bmatrix}
 &  &  \\
 &  &  \\
\end{bmatrix}_{d \times n}
\times
\begin{bmatrix}
 &  &  \\
 &  &  \\
\end{bmatrix}_{n \times d}
= 
\begin{bmatrix}
 &  &  \\
 &  &  \\
\end{bmatrix}_{d \times d}
$$

This is why, after column standardization, the covariance matrix can be computed very efficiently using the simple formula $S = \frac{1}{n} X^T X$.

## 09. MNIST Dataset (784 Dimensional)

https://colah.github.io/posts/2014-10-Visualizing-MNIST/

**MNIST Dataset**

- 60,000 training data points
- 10,000 test data points
- Classification problem
- Labels: $y_i \in \{0,1,2,3,4,5,6,7,8,9\}$

Each data point $x_i$ is a **28 × 28** grayscale image of a handwritten digit.

$$
x_i = 
\begin{bmatrix}
\text{28 × 28 pixels}
\end{bmatrix}
$$

But for machine learning algorithms we need **vectors**, not matrices.

**Flattening:**

We convert the 28 × 28 image into a long vector of size 784:

$$
x_i \in \mathbb{R}^{784}
$$

- Black pixel → 1
- White pixel → 0
- Gray pixel → value between 0 and 1

So each image becomes a **784-dimensional** numerical vector.

**Dataset representation:**

$$
D = \left\{ (x_i, y_i) \right\}_{i=1}^{60000}
$$

$$
X \in \mathbb{R}^{60000 \times 784}, \quad
Y \in \mathbb{R}^{60000 \times 1}
$$

- $n = 60{,}000$
- $d = 784$

**Why Dimensionality Reduction?**

784-dimensional data is extremely hard to visualize or understand directly.

We use techniques such as:

- **t-SNE**
- **PCA**

to reduce the data from **784D → 2D** (or 3D) so that we can plot and visually inspect the clusters of different digits.

## 10. Code to Load MNIST Data Set
[Open the Dimensionality notebook](./Dimensionality.ipynb)
