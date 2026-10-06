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

# Solving Optimization Problems

# Optimization & Gradient Descent

## Table of Contents

[01. Differentiation](#01-differentiation)

[02. Online Differentiation Tools](#02-online-differentiation-tools)

[03. Maxima and Minima](#03-maxima-and-minima)

[04. Vector Calculus Grad](#04-vector-calculus-grad)

[05. Gradient Descent Geometric Intuition](#05-gradient-descent-geometric-intuition)

[06. Learning Rate](#06-learning-rate)

[07. Gradient Descent for Linear Regression](#07-gradient-descent-for-linear-regression)

[08. SGD Algorithm](#08-sgd-algorithm)

[09. Constrained Optimization & PCA](#09-constrained-optimization-pca)

[10. Logistic Regression Formulation Revisited](#10-logistic-regression-formulation-revisited)

[11. Why L1 Regularization Creates Sparsity](#11-why-l1-regularization-creates-sparsity)

[12. Assignment 6: Implement SGD for Linear Regression](#12-assignment-6-implement-sgd-for-linear-regression)

[13. Revision Questions](#13-revision-questions)

# Optimization & Gradient Descent

## 01. Differentiation

![LR](./assets/01.01.jpg)

![LR](./assets/01.02.jpg)

**Solving Optimization Problems: Differentiation**

Many core ML algorithms are optimization problems:

- PCA
- Logistic Regression
- Linear Regression

In Machine Learning we mainly use:

- Differentiation (single-variable and vector)
- Finding maxima and minima

(11th & 12th standard + undergraduate calculus covers ~99% of what we need)

Integration and differential equations are used much less frequently.

### Single-Variable Differentiation

Given $y = f(x)$

$$
\frac{dy}{dx} = \frac{df}{dx} = y' = f'
$$

This is the differentiation of $y$ with respect to $x$.

**Intuitive meaning:**

$$
\frac{dy}{dx} = \text{rate of change of } y \text{ as } x \text{ changes}
$$

(How much does $y$ change when $x$ changes)

### Geometric Interpretation

$$
\frac{dy}{dx} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}
$$

- The tangent is the line we obtain as $\Delta x \to 0$
- $\tan\theta = \dfrac{dy}{dx}$

As $x_2 \to x_1$, we have $\Delta x \to 0$, and

$$
\frac{\Delta y}{\Delta x} \to \frac{dy}{dx}
$$

**Important statements:**

- $\dfrac{dy}{dx}$ = slope of the tangent to $f(x)$
- $\left.\dfrac{dy}{dx}\right|_{x_1}$ = slope of the tangent to $f(x)$ at $x = x_1$

### Historical Note

Differentiation was developed in the late 1600s by:

- **Newton** → _Principia Mathematica_
- **Leibniz**

Originally used for displacement, velocity, acceleration, gravity, orbital motion (rate of change).

### Geometric Meaning of Slope ($\tan\theta$)

- $0 \leq \theta < 90^\circ$ → positive slope
- $\theta = 0$ (tangent parallel to x-axis) → $\tan\theta = 0$
- $\theta = 90^\circ$ → $\tan 90^\circ$ is undefined
- $90^\circ < \theta < 180^\circ$ → negative slope

### Basic Differentiation Rules

$$
\begin{align*}
\frac{d}{dx}(x^n) &= n x^{n-1} \\
\frac{d}{dx}(x^2) &= 2x \\
\frac{d}{dx}(3x) &= 3 \\
\frac{d}{dx}(c) &= 0 \\
\frac{d}{dx}(c x^n) &= c\, n x^{n-1} \\
\frac{d}{dx}\log(x) &= \frac{1}{x} \\
\frac{d}{dx}e^x &= e^x \\
\frac{d}{dx}\big(f(x) + g(x)\big) &= \frac{d}{dx}f(x) + \frac{d}{dx}g(x)
\end{align*}
$$

### Chain Rule

$$
\frac{d}{dx}f\big(g(x)\big) = \frac{df}{dg} \cdot \frac{dg}{dx}
$$

**Example:**

Let $f(g(x)) = (a - bx)^2$

- Let $g(x) = a - bx = z$
- $f(z) = z^2$

Then

$$
\frac{d}{dx}f(g(x)) = \frac{df}{dg} \cdot \frac{dg}{dx} = 2(a - bx) \cdot (-b) = -2b(a - bx)
$$

## 02. Online Differentiation Tools

> **`Watch Lecture Video`**

## 03. Maxima and Minima

![LR](./assets/03.01.jpg)

![LR](./assets/03.02.jpg)

> **Maxima & Minima**

At both maxima and minima the **slope = 0**.

### Finding Maxima / Minima

Set the derivative to zero:

$$
\frac{df}{dx} = 0 \quad \Rightarrow \quad \text{slope} = 0
$$

**Example:**

$$
f(x) = x^2 - 3x + 2
$$

$$
\frac{df}{dx} = 2x - 3 = 0 \quad \Rightarrow \quad x = \frac{3}{2} = 1.5
$$

At $x = 1.5$, slope = 0.

Check values:

- $f(1.5) = -0.25$
- $f(1) = 0$

Since $f(1.5) < f(1)$, the point $x = 1.5$ is a **minimum**.

### Important Observations

- A function **may or may not** have maxima and minima.
- Example $y = x^2$:
  - No maxima
  - Minima at $x = 0$

- Some functions have **neither** minima nor maxima (strictly increasing/decreasing curves).

### Global vs Local

A function can have:

- Multiple **local minima**
- Multiple **local maxima**
- One **global minimum**
- One **global maximum**

### Connection to Machine Learning

Many loss functions (e.g. logistic loss) look like:

$$
f(x) = \log\big(1 + \exp(ax)\big)
$$

Setting the derivative to zero:

$$
\frac{df}{dx} = \frac{a\exp(ax)}{1 + \exp(ax)} = 0
$$

Solving this analytically is **not trivial** (very hard).

Therefore in practice we use:

$$
\frac{df}{dx} = 0 \quad \xrightarrow{\text{solved by}} \quad \textbf{Gradient Descent}
$$

## 04. Vector Calculus Grad

![LR](./assets/04.01.jpg)

![LR](./assets/04.02.jpg)

> **Vector Differentiation: Gradient**

So far we treated $x$ as a **scalar**.

In high-dimensional space $x$ is a **vector**:

$$
\mathbf{x} = \langle x_1, x_2, \dots, x_d \rangle
$$

Example linear function:

$$
f(\mathbf{x}) = y = \mathbf{a}^\top \mathbf{x} = \sum_{i=1}^{d} a_i x_i
$$

where $\mathbf{a} = \langle a_1, a_2, \dots, a_d \rangle$ are constants.

### Definition of Gradient

When $\mathbf{x}$ is a vector, the derivative becomes the **gradient**:

$$
\frac{df}{d\mathbf{x}} = \nabla_{\mathbf{x}} f
$$

The gradient is itself a vector in $\mathbb{R}^d$:

$$
\nabla_{\mathbf{x}} f =
\begin{bmatrix}
\dfrac{\partial f}{\partial x_1} \\
\dfrac{\partial f}{\partial x_2} \\
\vdots \\
\dfrac{\partial f}{\partial x_d}
\end{bmatrix}
\in \mathbb{R}^d
$$

Each component is a **partial derivative**.

### Important Result

For the linear function $f(\mathbf{x}) = \mathbf{a}^\top \mathbf{x}$:

$$
\nabla_{\mathbf{x}} (\mathbf{a}^\top \mathbf{x}) = \mathbf{a}
$$

(Compare with the scalar case: $\dfrac{d}{dx}(ax) = a$)

### Application to Logistic Regression Loss

The regularized logistic loss is:

$$
\mathcal{L}(\mathbf{w}) = \sum_{i=1}^{n} \log\Big(1 + \exp(-y_i \mathbf{w}^\top \mathbf{x}_i)\Big) + \lambda \mathbf{w}^\top \mathbf{w}
$$

Here $\langle \mathbf{x}_i, y_i \rangle$ are constants (training data).

Taking the gradient with respect to $\mathbf{w}$ and setting it to zero:

$$
\nabla_{\mathbf{w}} \mathcal{L} =
\frac{(-y_i \mathbf{x}_i)\exp(-y_i \mathbf{w}^\top \mathbf{x}_i)}{1 + \exp(-y_i \mathbf{w}^\top \mathbf{x}_i)}
+ 2\lambda \mathbf{w}
= \mathbf{0}
$$

Solving $\nabla_{\mathbf{w}} \mathcal{L} = \mathbf{0}$ analytically is hard → we use **Gradient Descent**.

## 05. Gradient Descent Geometric Intuition

![LR](./assets/05.01.jpg)

![LR](./assets/05.02.jpg)

> **Gradient Descent Algorithm**

We want to solve:

$$
\mathbf{x}^* = \arg\min_{\mathbf{x}} f(\mathbf{x})
$$

At maxima and minima we have:

$$
\frac{df}{dx} = 0 \qquad \text{or} \qquad \nabla_{\mathbf{x}} f = \mathbf{0}
$$

Gradient Descent is an **iterative algorithm**:

- Start with an initial guess $x_0$
- Produce $x_1$ (iteration 1)
- Produce $x_2$ (iteration 2)
- …
- After $K$ iterations we get $x_K \approx x^*$

### Geometric Intuition

At a minimum the slope changes sign (from negative to positive).

- One side of the minimum → slope is negative
- Other side of the minimum → slope is positive

Also note the useful identities:

$$
\min f(x) \;=\; \max \big(-f(x)\big)
$$

$$
\max f(x) \;=\; \min \big(-f(x)\big)
$$

As we move closer to $x^*$, the **slope reduces**.

### Gradient Descent Update Rule

1. Pick an initial point $x_0$ (usually at random)

2. Update:

$$
x_1 = x_0 - \gamma \left.\frac{df}{dx}\right|_{x_0}
$$

where $\gamma$ is the **step-size** (learning rate).

**Case when slope is positive** (point is to the right of the minimum):

$$
x_1 = x_0 - \gamma \cdot (+ve) \quad \Rightarrow \quad x_1 < x_0
$$

→ we move left, closer to $x^*$.

**Case when slope is negative** (point is to the left of the minimum):

$$
x_1 = x_0 - \gamma \cdot (-ve) \quad \Rightarrow \quad x_1 > x_0
$$

→ we move right, closer to $x^*$.

3. General iterative update:

$$
x_{i+1} = x_i - \gamma \left.\frac{df}{dx}\right|_{x_i}
$$

(or in vector form using the gradient $\nabla_{\mathbf{x}} f$)

### Termination

Keep iterating:

$$
x_0,\; x_1,\; x_2,\; \dots,\; x_k,\; x_{k+1}
$$

If the change $(x_{k+1} - x_k)$ becomes very small, stop and declare:

$$
x^* = x_k
$$

## 06. Learning Rate

![LR](./assets/06.01.jpg)

![LR](./assets/06.02.jpg)

> **Learning Rate (or) Step-size ($\gamma$)**

In the Gradient Descent update equation:

$$
x_i = x_{i-1} - \gamma \left.\frac{df}{dx}\right|_{x_{i-1}}
$$

$\gamma$ is a **constant** called the learning rate (or step-size).

In Deep Learning we choose $\gamma$ more carefully / effectively.

### Problem of Oscillation (when $\gamma$ is too large)

Take the simple function $f(x) = x^2$.

$$
\frac{df}{dx} = 2x
$$

Let $\gamma = 1$ and start at $x_i = 0.5$:

$$
\begin{align*}
x_{i+1} &= 0.5 - 1 \cdot (2 \times 0.5) = 0.5 - 1 = -0.5 \\
x_{i+2} &= -0.5 - 1 \cdot (2 \times (-0.5)) = -0.5 - 1 \cdot (-1) = 0.5
\end{align*}
$$

The algorithm keeps oscillating between $x = 0.5$ and $x = -0.5$ and **never converges** to $x^* = 0$.  
We simply jumped over the minimum.

### Remedy for Oscillation

**Change $\gamma$ with each iteration.**

One common technique: **reduce $\gamma$ with each iteration**.

$$
\gamma = h(i)
$$

where $i$ is the iteration number.

As the iteration number increases ($i \uparrow$), the learning rate decreases ($\gamma \downarrow$).

## 07. Gradient Descent for Linear Regression

![LR](./assets/07.01.jpg)

![LR](./assets/07.02.jpg)

> **Gradient Descent for Linear Regression**

We want to solve (no regularization, and ignoring the intercept $w_0$ for simplicity):

$$
\mathbf{w}^* = \arg\min_{\mathbf{w}} \sum_{i=1}^{n} \big(y_i - \mathbf{w}^\top \mathbf{x}_i\big)^2
$$

### Loss and Gradient

$$
\mathcal{L}(\mathbf{w}) = \sum_{i=1}^{n} \big(y_i - \mathbf{w}^\top \mathbf{x}_i\big)^2
$$

$$
\nabla_{\mathbf{w}} \mathcal{L} = \sum_{i=1}^{n} \Big\{ 2\big(y_i - \mathbf{w}^\top \mathbf{x}_i\big)(-\mathbf{x}_i) \Big\}
$$

### Gradient Descent Steps

1. Pick a random vector $\mathbf{w}_0 = \langle \dots \rangle$

2. Update:

$$
\mathbf{w}_1 = \mathbf{w}_0 - \gamma \sum_{i=1}^{n} (-2\mathbf{x}_i)\big(y_i - \mathbf{w}_0^\top \mathbf{x}_i\big)
$$

3. Next iteration:

$$
\mathbf{w}_2 = \mathbf{w}_1 - \gamma \sum_{i=1}^{n} (-2\mathbf{x}_i)\big(y_i - \mathbf{w}_1^\top \mathbf{x}_i\big)
$$

Continue:

$$
\mathbf{w}_0,\; \mathbf{w}_1,\; \mathbf{w}_2,\; \dots,\; \mathbf{w}_k,\; \mathbf{w}_{k+1}
$$

When $\mathbf{w}_{k+1} - \mathbf{w}_k$ becomes a vector of very small values, stop and set:

$$
\mathbf{w}^* = \mathbf{w}_k
$$

### General Update Rule

$$
\mathbf{w}_j = \mathbf{w}_{j-1} - \gamma \sum_{i=1}^{n} (-2\mathbf{x}_i)\big(y_i - \mathbf{w}_{j-1}^\top \mathbf{x}_i\big)
$$

### Problem with Batch Gradient Descent

When $n$ is large (e.g. $n = 1$ million), computing the full sum $\sum_{i=1}^{n}$ at every iteration is **very expensive**.

This is the main motivation for moving to **Stochastic Gradient Descent (SGD)**.

## 08. SGD Algorithm

![LR](./assets/08.01.jpg)

![LR](./assets/08.02.jpg)

> **Stochastic Gradient Descent (SGD)**

SGD is the **most important optimization algorithm** in Machine Learning.

### Problem with Batch Gradient Descent

For Linear Regression the full (batch) update is:

$$
\mathbf{w}_{j+1} = \mathbf{w}_j - \gamma \sum_{i=1}^{n} (-2\mathbf{x}_i)\big(y_i - \mathbf{w}_j^\top \mathbf{x}_i\big)
$$

When $n$ is large (e.g. $n = 1$ million), computing the full sum at every iteration takes a lot of time.

### Stochastic Gradient Descent

Instead of using all $n$ points, we use only a small random subset of $K$ points:

$$
\mathbf{w}_{j+1} = \mathbf{w}_j - \gamma \sum_{i=1}^{K} (-2\mathbf{x}_i)\big(y_i - \mathbf{w}_j^\top \mathbf{x}_i\big)
$$

where $1 \leq K \leq n$ and we pick a **random set of $K$ points** at each iteration.

- $\mathbf{w}^*_{\text{GD}} = \mathbf{w}^*_{\text{SGD}}$ (both converge to the same solution)

### How many iterations are needed?

- Batch GD ($n = 1$ million): roughly **100 iterations** to converge to $\mathbf{x}^*$
- SGD with $K = 1000$: needs more than 100 iterations (≈ 500)
- SGD with $K = 10$: needs even more iterations (≈ 1000)

$K$ = number of random points that you use at each iteration for updating.

### Batch-size in SGD

- $K$ is called the **batch-size**
- Often $K = 1$ → pure Stochastic Gradient Descent
- When $1 < K < n$ (e.g. $K = 10$ or $K = 100$) → **Mini-batch SGD**

**SGD is the most important optimization algorithm in Machine Learning.**  
(In Deep Learning we also use improved versions such as Adam, Adagrad, etc.)

## 09. Constrained Optimization & PCA

![LR](./assets/09.01.jpg)

![LR](./assets/09.02.jpg)

## 10. Logistic Regression Formulation Revisited

![LR](./assets/10.01.jpg)

![LR](./assets/10.02.jpg)

## 11. Why L1 Regularization Creates Sparsity

![LR](./assets/11.01.jpg)

![LR](./assets/11.02.jpg)

## 12. Assignment 6: Implement SGD for Linear Regression

![LR](./assets/12.01.jpg)

![LR](./assets/12.02.jpg)

## 13. Revision Questions

**Questions**

[1. Explain about Logistic regression?](#1-explain-about-logistic-regression)  
[2. What is Sigmoid function & Squashing?](#2-what-is-sigmoid-function--squashing)  
[3. Explain about Optimization problem in logistic regression.](#3-explain-about-optimization-problem-in-logistic-regression)  
[4. Explain Importance of Weight vector in logistic regression.](#4-explain-importance-of-weight-vector-in-logistic-regression)  
[5. L2 Regularization: Overfitting and Underfitting.](#5-l2-regularization-overfitting-and-underfitting)  
[6. L1 regularization and sparsity.](#6-l1-regularization-and-sparsity)  
[7. What is Probabilistic Interpretation: Gaussian Naive Bayes?](#7-what-is-probabilistic-interpretation-gaussian-naive-bayes)  
[8. Explain about Hyperparameter search: Grid Search and Random Search?](#8-explain-about-hyperparameter-search-grid-search-and-random-search)  
[9. What is Column Standardization?](#9-what-is-column-standardization)  
[10. Explain about Collinearity of features?](#10-explain-about-collinearity-of-features)  
[11. Find Train & Run time space and time complexity of Logistic regression?](#11-find-train--run-time-space-and-time-complexity-of-logistic-regression)  

### 1. Explain about Logistic regression?

Logistic Regression is a linear classification algorithm that finds a hyperplane to separate classes.

**Geometric view**:
- Decision surface: $ \pi: w^T x + b = 0 $
- A point $ x_i $ is correctly classified when $ y_i (w^T x_i) > 0 $ (using labels $ y_i \in \{-1, +1\} $)
- Goal: Find the best $ w $ and $ b $ that maximize the number of correctly classified points.

**Key properties**:
- Simple and elegant
- Outputs probabilities (via sigmoid)
- Works well when classes are almost linearly separable
- Can be extended with regularization

It is both a geometric method (hyperplane) and a probabilistic method (sigmoid + log-loss).

### 2. What is Sigmoid function & Squashing?

The **Sigmoid function** (also called logistic function) is:

$ \sigma(z) = \frac{1}{1 + e^{-z}} $

**Properties**:
- Range is always between 0 and 1
- S-shaped curve
- $ \sigma(0) = 0.5 $
- As $ z \to +\infty $, $ \sigma(z) \to 1 $
- As $ z \to -\infty $, $ \sigma(z) \to 0 $

**Squashing**:
- The linear score $ w^T x + b $ can take any real value ($ -\infty $ to $ +\infty $)
- Sigmoid “squashes” this unbounded value into the range $ (0, 1) $
- This allows us to interpret the output as a **probability**:
  $ P(y=1|x) = \sigma(w^T x + b) $

### 3. Explain about Optimization problem in logistic regression.

We want to find the best weight vector $ w $ that correctly classifies as many points as possible.

Using labels $ y_i \in \{-1, +1\} $, a point is correctly classified when:

$ y_i (w^T x_i) > 0 $

**Optimization formulation**:

$ w^* = \arg\max_w \sum_{i=1}^{n} y_i (w^T x_i) $

In practice we minimize the **logistic loss** (negative log-likelihood):

$ L(w) = \sum_{i=1}^{n} \log \big(1 + e^{-y_i (w^T x_i)}\big) $

(with optional regularization term)

This is a convex optimization problem and can be solved using Gradient Descent, SGD, or second-order methods (Newton, LBFGS).

### 4. Explain Importance of Weight vector in logistic regression.

The weight vector $ w $ has dual importance:

1. **Geometric meaning**:
   - $ w $ is the **normal vector** to the decision hyperplane
   - Direction of $ w $ points towards the positive class
   - Magnitude of $ w $ affects the steepness of the sigmoid

2. **Feature importance**:
   - $ |w_j| $ tells how important feature $ j $ is
   - Sign of $ w_j $ tells the direction of influence (positive or negative)
   - After column standardization, the magnitudes become directly comparable

3. **Decision rule**:
   - $ w^T x + b > 0 \rightarrow $ predict positive class
   - $ w^T x + b < 0 \rightarrow $ predict negative class

### 5. L2 Regularization: Overfitting and Underfitting.

**L2 Regularization** (Ridge) adds the term $ \lambda \|w\|_2^2 = \lambda \sum w_j^2 $ to the loss:

$ L(w) = \sum \log(1 + e^{-y_i w^T x_i}) + \lambda \|w\|_2^2 $

**Effect**:
- Penalizes large weights
- Keeps weights small and distributed across features
- Controls the bias-variance trade-off

**Overfitting vs Underfitting**:
- **High $ \lambda $** → strong regularization → high bias, low variance → underfitting
- **Low $ \lambda $** → weak regularization → low bias, high variance → overfitting
- Optimal $ \lambda $ is chosen via cross-validation

L2 never makes weights exactly zero; it only shrinks them.

### 6. L1 regularization and sparsity.

**L1 Regularization** (Lasso) adds the term $ \lambda \|w\|_1 = \lambda \sum |w_j| $:

$ L(w) = \sum \log(1 + e^{-y_i w^T x_i}) + \lambda \|w\|_1 $

**Key property – Sparsity**:
- L1 can drive some weights **exactly to zero**
- This performs automatic feature selection
- The resulting model is sparse (uses only a subset of features)

**Comparison with L2**:
- L1 → sparse solutions (feature selection)
- L2 → small but non-zero weights (weight shrinkage)

L1 is preferred when we believe only a few features are truly important.

### 7. What is Probabilistic Interpretation: Gaussian Naive Bayes?

Under certain assumptions, Logistic Regression and Gaussian Naive Bayes are closely related.

**Assumptions of Gaussian Naive Bayes**:
- Features are independent given the class
- Features follow a Gaussian distribution in each class

When class-conditional densities are Gaussian with the **same covariance matrix**, the posterior probability $ P(y=1|x) $ takes exactly the logistic (sigmoid) form:

$ P(y=1|x) = \sigma(w^T x + b) $

Thus, Logistic Regression can be viewed as the discriminative counterpart of Gaussian Naive Bayes (with shared covariance).

- Generative model → Gaussian NB
- Discriminative model → Logistic Regression

### 8. Explain about Hyperparameter search: Grid Search and Random Search?

Hyperparameters in Logistic Regression mainly include:
- Regularization strength $ \lambda $ (or $ C = 1/\lambda $)
- Type of regularization (L1 / L2)
- Solver, etc.

**Grid Search**:
- Tries every possible combination from a predefined set of values
- Exhaustive but computationally expensive
- Guarantees finding the best combination within the grid

**Random Search**:
- Randomly samples hyperparameter combinations
- More efficient when only a few hyperparameters matter
- Often finds good solutions faster than Grid Search
- Better for high-dimensional hyperparameter spaces

Both are usually combined with cross-validation.

### 9. What is Column Standardization?

**Column Standardization** (Z-score normalization) transforms each feature:

$ x_j' = \frac{x_j - \mu_j}{\sigma_j} $

After this:
- Every feature has mean = 0 and standard deviation = 1

**Why it is important for Logistic Regression**:
- Features are brought to the same scale
- Weight magnitudes become comparable (feature importance)
- Helps optimization algorithms converge faster
- Regularization works properly (otherwise features with large scale dominate)

Always fit the mean and std only on the training data.

### 10. Explain about Collinearity of features?

**Collinearity** (or multicollinearity) occurs when two or more features are highly linearly correlated.

**Problems it causes in Logistic Regression**:
- Weights become unstable and hard to interpret
- Small changes in data can cause large changes in $ w $
- Feature importance becomes unreliable
- Optimization can become numerically unstable

**How to detect**:
- Correlation matrix
- Variance Inflation Factor (VIF)

**How to handle**:
- Remove one of the correlated features
- Use L1 / L2 regularization
- Apply PCA or other dimensionality reduction
- Collect more data if possible

### 11. Find Train & Run time space and time complexity of Logistic regression?

**Training Time Complexity**:
- Using Gradient Descent / SGD: roughly $ O(n \cdot d \cdot k) $
  - $ n $ = number of training points
  - $ d $ = number of features
  - $ k $ = number of iterations

**Run-time (Prediction) Time Complexity**:
- $ O(d) $ per test point (just compute $ w^T x + b $ and apply sigmoid)

**Space Complexity**:
- $ O(d) $ to store the weight vector $ w $ and bias $ b $
- During training, additional space may be needed for gradients and data

Logistic Regression is very efficient at prediction time compared to many other algorithms (e.g., k-NN, kernel methods).