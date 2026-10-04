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


# Linear Regression

## Table of Contents

[01. Geometric Intuition of Linear Regression](#01-geometric-intuition-of-linear-regression)

[02. Mathematical Formulation](#02-mathematical-formulation)

[03. Need for Regularization in Linear Regression](#03-need-for-regularization-in-linear-regression)

[04. Real-World Cases](#04-real-world-cases)

[05. Code Sample for Linear Regression](#05-code-sample-for-linear-regression)

# Linear Regression

## 01. Geometric Intuition of Linear Regression

![LR](./assets/01.01.jpg)
![LR](./assets/01.02.jpg)

> **Linear Regression**

- Linear Regression → **actual regression**
- Logistic Regression → classification

Both belong to the family of **Generalized Linear Models (GLM)**.

Dataset:

$$
\mathcal{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^n
$$

- $\mathbf{x}_i \in \mathbb{R}^d$
- For **regression**: $y_i \in \mathbb{R}$
- For **classification**: $y_i \in \{-1, +1\}$

### Geometry of Linear Regression

**Example:** Predict height ($y \in \mathbb{R}$) given weight, gender, ethnicity, hair color, etc.

Linear Regression finds a **line / plane** that best fits the given data.

In 1-D (only weight as feature):

$$
\text{height} = w_1 \cdot \text{weight} + w_0
$$

which is the familiar equation of a straight line:

$$
y = mx + c
$$

In 2-D (weight and hair color):

$$
\mathbf{x}_i = \langle x_{i1}, x_{i2} \rangle
$$

$$
\text{height} = w_1 f_1 + w_2 f_2 + w_0
$$

$$
y_i = w_1 x_{i1} + w_2 x_{i2} + w_0
$$

In vector form:

$$
y_i = \mathbf{w}^\top \mathbf{x}_i + w_0
$$

### Goal

Find a line / plane that **best fits** the data points.

“Best fit” means **minimize the error**.

For a point $(x_1, y_1)$:

- Predicted value: $\hat{y}_1 = f(x_1) = w_1 x_1 + w_0$
- Error: $y_1 - \hat{y}_1$

We want to **minimize the sum of errors** across all training points.

## 02. Mathematical Formulation

![LR](./assets/02.01.jpg)
![LR](./assets/02.02.jpg)

> **Mathematical Formulation of Linear Regression**

Errors can be positive or negative:

- $\text{error}_1 = y_1 - \hat{y}_1 = +ve$
- $\text{error}_2 = y_2 - \hat{y}_2 = -ve$
- $\text{error}_3 = 0$ (point lies on the line)

Best-fit line = minimize the **sum of errors**.

### Ordinary Least Squares (OLS) / Linear Least Squares (LLS)

Linear Regression is also called **OLS** or **LLS**.

The hyperplane is:

$$
\pi:\ \mathbf{w}^\top \mathbf{x} + w_0 = 0
$$

**Optimization problem:**

$$
(\mathbf{w}^*, w_0^*) = \arg\min_{\mathbf{w}, w_0} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

where

$$
\hat{y}_i = f(\mathbf{x}_i) = \mathbf{w}^\top \mathbf{x}_i + w_0
$$

This is the **squared loss** (Sq-loss).

Expanded form:

$$
(\mathbf{w}^*, w_0^*) = \arg\min_{\mathbf{w}, w_0} \sum_{i=1}^{n} \Big\{ y_i - (\mathbf{w}^\top \mathbf{x}_i + w_0) \Big\}^2
$$

### Regularization

Just like Logistic Regression, we can add regularization:

$$
(\mathbf{w}^*, w_0^*) = \arg\min_{\mathbf{w}, w_0} \sum_{i=1}^{n} \Big\{ y_i - (\mathbf{w}^\top \mathbf{x}_i + w_0) \Big\}^2 + \lambda \|\mathbf{w}\|_2^2
$$

- L2-regularization is the most common.
- We can also use L1-regularization or Elastic-Net (same as in Logistic Regression).

### Probabilistic Interpretation (GLM)

Linear Regression assumes:

$$
P(y_i \mid \mathbf{x}_i) = \mathcal{N}(\mu, \sigma^2)
$$

The squared loss term $(y_i - f(\mathbf{x}_i))^2$ comes naturally from the Gaussian assumption.

### Three Interpretations of Linear Regression

Same as Logistic Regression:

1. **Geometric** interpretation
2. **Probabilistic** interpretation (GLM)
3. **Loss-minimization** interpretation

### Loss-Minimization View

- Squared loss $\rightarrow$ parabola ($y = x^2$)
- 0-1 loss is for classification; squared loss is for regression.

For regression the residual is:

$$
y_i - f(\mathbf{x}_i)
$$

For classification we used:

$$
z_i = y_i \cdot f(\mathbf{x}_i)
$$

**Summary of Loss-Min Framework for Regression**

$$
\text{Squared Loss} \;\longrightarrow\; \text{Linear Regression (OLS)}
$$

## 03. Need for Regularization in Linear Regression

![LR](./assets/03.01.jpg)
![LR](./assets/03.02.jpg)

> **Why use Regularization in Linear Regression?**

The regularized objective is:

$$
\mathbf{w}^* = \arg\min_{\mathbf{w}} \sum_{i=1}^{n} \big(y_i - \mathbf{w}^\top \mathbf{x}_i\big)^2 + \lambda \|\mathbf{w}\|_2^2
$$

- First term → Squared error (wants to fit the data)
- Second term → L2-regularization (forces the $w_i$’s to be **small**)

Without regularization, weights can become very large ($\mathbf{w} \to \infty$).

### Simulation Example

Suppose the true underlying relationship uses only 2 features:

$$
y_i = 2x_{i1} + 3x_{i2} + 0\cdot x_{i3}
$$

Ideal solution:

$$
\mathbf{w} = [2,\ 3,\ 0]
$$

We generate a simulated dataset $\mathcal{D}$ with 10 000 points and 3 features.

**Real-world analogy**

- $y$ = height
- $f_1$ = weight
- $f_2$ = age
- $f_3$ = gender (0 or 1)

In real data there is always small noise $\varepsilon_i$:

$$
y_i = 2x_{i1} + 3x_{i2} + 0\cdot x_{i3} + \varepsilon_i
$$

### What happens when we train

**Without regularization (Linear Regression + no-reg):**

$$
\mathbf{w} \approx [2.1,\ 3.06,\ 0.12]
$$

The model tries to fit the noise and gives a non-zero weight to the irrelevant feature → **overfitting**.

**With regularization (Linear Regression + reg):**

$$
\mathbf{w} \approx [2.01,\ 3.003,\ 0.003]
$$

The weights stay very close to the true underlying values $[2,\ 3,\ 0]$.

### Summary

- Squared loss → tries to **reduce error**
- L2-regularization → tries to **reduce the $w_i$’s**

Regularization prevents the model from fitting noise and keeps the weights small, which improves generalization to unseen test data.

## 04. Real-World Cases

![LR](./assets/04.01.jpg)
![LR](./assets/04.02.jpg)

> **Cases for Linear Regression**

### Imbalanced Data
- Same as Logistic Regression → use **Upsampling** or **Downsampling**

### Feature Importance & Interpretability
- Same condition as Logistic Regression: features should **not** be multicollinear
- Feature importance comes from $|w_j|$
- Regularization:
  - L1-regularization → sparsity
  - As $\lambda$ increases → sparsity increases

### Multi-class
- Linear Regression has **no direct multi-class** capability (unlike Logistic Regression)

### Feature Engineering / Feature Transforms
- Extremely important (same as in Logistic Regression)
- After good feature transforms we can apply Linear Regression

### Outliers

**Logistic Regression**  
- Sigmoid function limits the impact of outliers

**Linear Regression**  
- Uses **Squared Loss**:
  $$
  \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
  $$
- Outliers can impact the model **heavily** (large residuals get squared)

### Handling Outliers in Linear Regression → RANSAC

1. Train on $D_{\text{train}}$ → obtain $\mathbf{w}^*, w_0^*$
2. Find points that are very far away from the hyperplane $\pi$  
   (i.e., points with large $|y_i - \hat{y}_i|$)
3. Remove these points as outliers
4. Form cleaned dataset:
   $$
   D'_{\text{train}} = D_{\text{train}} - \text{Outliers}
   $$
5. Retrain the model on $D'_{\text{train}}$
6. Iterate if needed

This procedure is known as **RANSAC** (Random Sample Consensus).

## 05. Code Sample for Linear Regression

> ### [`LinearRegression.ipynb`](./LinearRegression.ipynb)
