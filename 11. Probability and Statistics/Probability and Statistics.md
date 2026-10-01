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

# Probability and Statistics

## Table of Contents
[01. Introduction to Probability and Statistics](#01-introduction-to-probability-and-statistics)  
[02. Population and Sample](#02-population-and-sample)  
[03. Gaussian (Normal) Distribution and its PDF](#03-gaussian-normal-distribution-and-its-pdf)  
[04. CDF of $ X \sim \mathcal{N}(\mu, \sigma^2) $ and the 68-95-99.7 Rule](#04-cdf-of--x--mathcalnmu-sigma2--and-the-68-95-997-rule)  
[05. Symmetric Distribution, Skewness, Kurtosis](#05-symmetric-distribution-skewness-kurtosis)  
[06. Standard Normal Variate ($Z$) and Standardization](#06-standard-normal-variate-z-and-standardization)  
[07. Kernel Density Estimation (KDE)](#07-kernel-density-estimation-kde)   
[08. Sampling Distribution & Central Limit Theorem (CLT)](#08-sampling-distribution--central-limit-theorem-clt)  
[09. Q-Q Plot (Quantile-Quantile Plot)](#09-q-q-plot-quantile-quantile-plot)  
[10. How / Where to Use Distributions?](#10-how--where-to-use-distributions)  
[11. Chebyshev's inequality](#11-chebyshev's-inequality)  
[12. Discrete and Continuous Uniform Distributions](#12-discrete-and-continuous-uniform-distributions)  
[13. How to Randomly Sample Data Points](#13-how-to-randomly-sample-data-points)  
[14. Bernoulli and Binomial Distribution](#14-bernoulli-and-binomial-distribution)  
[15. Log-Normal Distribution](#15-log-normal-distribution)  
[16. Power-Law Distribution](#16-power-law-distribution)  
[17. Box-Cox Transform](#17-box-cox-transform)  
[18. Applications of Non-Gaussian Distributions](#18-applications-of-non-gaussian-distributions)  
[19. Covariance](#19-covariance)  
[20. Pearson Correlation Coefficient](#20-pearson-correlation-coefficient)  
[21. Spearman Rank Correlation Coefficient](#21-spearman-rank-correlation-coefficient)  
[22. Correlation vs Causation](#22-correlation-vs-causation)  
[23. How to Use Correlations](#23-how-to-use-correlations)  
[24. Confidence Interval Introduction](#24-confidence-interval-introduction)  
[25. Computing Confidence Interval Given the Underlying Distribution](#25-computing-confidence-interval-given-the-underlying-distribution)  
[26. Confidence Interval for the Mean of a Normal Random Variable](#26-confidence-interval-for-the-mean-of-a-normal-random-variable)  
[27. Confidence Interval Using Bootstrapping](#27-confidence-interval-using-bootstrapping)  
[28. Hypothesis Testing Methodology](#28-hypothesis-testing-methodology)  
[29. Hypothesis Testing Intuition with a Coin Toss](#29-hypothesis-testing-intuition-with-a-coin-toss)  
[30. Resampling and Permutation Test](#30-resampling-and-permutation-test)  
[31. Hypothesis Testing QA](#31-hypothesis-testing-qa)    
[32. K-S Test for Similarity of Two Distributions](#32-k-s-test-for-similarity-of-two-distributions)  
[33. K-S Test for P-value](#33-k-s-test-p-value)  
[34. Code Snippet: K-S Test](#34-code-snippet-k-s-test)  
[35. Hypothesis Testing: Another Example](#35-hypothesis-testing-another-example)  
[36. Resampling and Permutation Test: Another Example](#36-resampling-and-permutation-test-another-example)  
[37. How to Use Hypothesis Testing](#37-how-to-use-hypothesis-testing)  
[38. Proportional Sampling](#38-proportional-sampling)  
[39. Revision Questions](#39-revision-questions)  

--- 
## 01. Introduction to Probability and Statistics

Probability and Statistics is a **fundamental area** of mathematics that helps us understand uncertainty, variability, and patterns in data.

Key concepts we will encounter:

- Histogram
- Probability Density Function (PDF)
- Cumulative Distribution Function (CDF)
- Mean
- Variance
- Standard Deviation

### Random Variables

A **random variable** is a variable whose value is determined by the outcome of a random experiment.

Examples:

- \( x = 2 \)
- \( x = 3 \)


### Discrete Random Variable – Fair Dice

A fair six-sided die has outcomes:

$$
X = \{1, 2, 3, 4, 5, 6\}
$$

All outcomes are **equally likely**.

$$
P(X = 1) = \dfrac{1}{6}, \quad P(X = 2) = \dfrac{1}{6}
$$

**Probability that the outcome is even:**

$$
\begin{align*}
P(X \text{ is even}) &= P(X=2) + P(X=4) + P(X=6) \\
&= \dfrac{1}{6} + \dfrac{1}{6} + \dfrac{1}{6} \\
&= \dfrac{3}{6} = \dfrac{1}{2}
\end{align*}
$$

**Probability that the outcome is odd:**

$$
P(X \text{ is odd}) = \dfrac{1}{2}
$$

In general:

$$
P(X = x_i) = P(x_i)
$$

### Discrete Random Variable – Coin Toss

When tossing a fair coin:

$$
Y = \{H, T\}
$$

### Continuous Random Variable – Height

Height of a randomly selected student typically lies between **120 cm – 190 cm**.

Examples of possible values:

- $ Y = 162.95 $
- $ Y = 132.62 $

These are examples of a **continuous random variable**.

### Outliers

Consider the heights of students:

$$
Y = \{122.2,\ 116.9,\ 132.5,\ \dots,\ 12.6,\ 156.23,\ \dots\}
$$

Here, **12.6** is an **outlier** (clearly unrealistic height).

| Affected by Outliers | Not Affected by Outliers        |
| -------------------- | ------------------------------- |
| Mean                 | Median                          |
| Variance             | MAD (Median Absolute Deviation) |
| Standard Deviation   |                                 |

> **Key Insight**: Outliers can heavily distort the mean, variance, and standard deviation, but have little or no effect on the median and MAD.

## 02. Population and Sample

### Population

The **population** is the complete set of all individuals or items of interest.  
Example: Set of **all people in the world**.

### Sample

A **sample** is a subset of the population.  
Example: A random sample of size **1000**.

We use the sample to **estimate** population parameters (e.g., average height of humans).

### Population Mean vs Sample Mean

**Population mean** ($\mu$ ):

$$
\mu = \dfrac{1}{N} \sum_{i=1}^{N} h_i
$$

**Sample mean** ($\bar{x}$ ):

$$
\bar{x} = \dfrac{1}{1000} \sum_{i=1}^{1000} h_i
$$

### Relationship Between Sample Size and Accuracy

As the **sample size increases**:

$$
\bar{x} \approx \mu
$$

$$
\text{Sample Mean} \;\longrightarrow\; \text{Population Mean}
$$

### Summary

<div class="summary-grid">
  <div class="summary-card">
    <div class="summary-tag">Discrete R.V.</div>
    <h3>Finite / Countable Outcomes</h3>
    <p>Dice, Coin Toss</p>
    
$ X = {1, 2, 3, 4, 5, 6} $
    
  </div>

  <div class="summary-card pdf">
    <div class="summary-tag">Continuous R.V.</div>
    <h3>Infinite Possible Values</h3>
    <p>Height, Weight, Temperature<br>
    Can take any value in an interval</p>
  </div>

  <div class="summary-card cdf">
    <div class="summary-tag">Estimation</div>
    <h3>Sample → Population</h3>
    <p>Dice, Coin Toss</p>

$ X = \{1,2,3,4,5,6\} $

  </div>
</div>

## 03. Gaussian (Normal) Distribution and its PDF

The **Gaussian distribution** (also called the **Normal distribution**) is one of the most important distributions in probability and statistics.

### Shape of the PDF

The Probability Density Function (PDF) of a Gaussian random variable has a characteristic **bell-shaped curve**.

$$
f(x) = \dfrac{1}{\sigma\sqrt{2\pi}}\, \exp\left(-\dfrac{(x-\mu)^2}{2\sigma^2}\right)
$$

$$
f(x) = \dfrac{1}{\sigma \sqrt{2\pi}} \, e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

$$
X \sim \mathcal{N}(\mu, \sigma^2)
$$

- $ X $ is a **continuous** random variable.
- If the PDF of $ X $ looks like a symmetric bell curve, then $ X $ is said to be **Gaussian / Normally distributed**.

![Normal Distribution PDF](./assets/01.%20Normal_Distribution_PDF.jpg)

**Observations from the PDF plot:**

1. **Effect of Variance ($\sigma^2$)**  
   - Blue curve ($\sigma^2 = 0.2$): Very tall and narrow → data is highly concentrated around the mean.  
   - Red curve ($\sigma^2 = 1.0$): Medium height and width (standard shape).  
   - Yellow curve ($\sigma^2 = 5.0$): Short and wide → data is much more spread out.

2. **Effect of Mean ($\mu$)**  
   - Green curve ($\mu = -2$, $\sigma^2 = 0.5$): The entire bell curve is shifted to the left.  
   - Changing $\mu$ only moves the curve left or right — it does **not** change the shape.

3. **Key Visual Properties**  
   - All curves are **symmetric** about their mean.  
   - Higher peak ↔ smaller variance.  
   - Lower peak ↔ larger variance.  
   - The total area under every curve is always **1**.

4. **Practical Meaning**  
   - Small $\sigma^2$ → values are tightly clustered around $\mu$.  
   - Large $\sigma^2$ → values are more dispersed.  
   - $\mu$ tells us the **center**, $\sigma^2$ tells us the **spread**.

### Why is the Normal Distribution Important?

- Extremely common in nature (height, weight, measurement errors, etc.)
- Simple mathematical model that contains a lot of useful information
- **Unimodal** (has only one peak)
- Completely characterized by just **two parameters**:
  - $ \mu $ → mean (location of the center)
  - $ \sigma^2 $ → variance (controls the spread)

### Notation

$$
X \sim \mathcal{N}(\mu, \sigma^2)
$$

| Distribution       | Notation                             | Meaning                 |
| ------------------ | ------------------------------------ | ----------------------- |
| Standard Normal    | $ X \sim \mathcal{N}(0,1) $          | $ \mu=0 $, $ \sigma=1 $ |
| Mean 0, Variance 4 | $ X \sim \mathcal{N}(0,4) $          | $ \mu=0 $, $ \sigma=2 $ |
| General case       | $ X \sim \mathcal{N}(\mu,\sigma^2) $ | Any mean and variance   |

### Understanding the PDF Formula

For the **standard normal** $ X \sim \mathcal{N}(0,1) $:

$$
P(x) = \dfrac{1}{\sqrt{2\pi}}\, e^{-x^2/2}
$$

The shape is mainly controlled by the exponential term $ e^{-x^2/2} $.

| $ x $   | Approximate value of $ e^{-x^2} $ | Observation     |
| ------- | --------------------------------- | --------------- |
| $ x=0 $ | $ 1 $                             | Maximum (peak)  |
| $ x=1 $ | $ \approx 0.367 $                 | Noticeable drop |
| $ x=2 $ | $ \approx 0.018 $                 | Very small      |
| $ x=3 $ | $ \approx 0.000123 $              | Extremely small |

**Key Observations:**

1. The curve is **symmetric** about the mean $ \mu $.
2. As $ x $ moves farther from $ \mu $, the PDF value decreases rapidly.
3. Most of the probability mass is concentrated near the mean.

## 04. CDF of $ X \sim \mathcal{N}(\mu, \sigma^2) $ and the 68-95-99.7 Rule

The **Cumulative Distribution Function (CDF)** is:

$$
F(x) = P(X \leq x) = \int_{-\infty}^{x} f(t)\, dt
$$

![Normal Distribution CDF](./assets/02.%20Normal_Distribution_CDF.jpg)

**Observations from the CDF plot:**

1. **General Shape**  
   - All CDF curves are **S-shaped** (sigmoid).  
   - They start near 0 on the far left and approach 1 on the far right.  
   - The total probability always goes from 0 → 1.

2. **Effect of Variance ($ \sigma^2 $)**  
   - Blue curve ($ \sigma^2 = 0.2$): Very **steep** rise → probability accumulates quickly around the mean.  
   - Red curve ($ \sigma^2 = 1.0$): Moderately steep.  
   - Yellow curve ($ \sigma^2 = 5.0$): Much more **gradual** rise → probability spreads over a wider range.

3. **Effect of Mean ($ \mu $)**  
   - Green curve ($ \mu = -2 $, $ \sigma^2 = 0.5 $): The entire S-curve is shifted to the left.  
   - Changing $ \mu $ moves the steep part of the curve left or right without changing how steep it is.

4. **Key Relationships**  
   - Smaller variance → steeper CDF.  
   - Larger variance → flatter CDF.  
   - The point where the CDF reaches 0.5 is exactly at the mean $ \mu $ (because the normal distribution is symmetric).

5. **Practical Meaning**  
   - A steep CDF means most of the probability mass is concentrated near the mean.  
   - A flat CDF means the values are more spread out.  
   - The CDF directly gives $ P(X \leq x) $.

### The Empirical Rule (68-95-99.7 Rule)

For **any** normal distribution $ X \sim \mathcal{N}(\mu, \sigma^2) $:

| Interval            | Approximate Probability | Percentage |
| ------------------- | ----------------------- | ---------- |
| $ \mu \pm 1\sigma $ | $ \approx 0.6827 $      | **68.27%** |
| $ \mu \pm 2\sigma $ | $ \approx 0.9545 $      | **95.45%** |
| $ \mu \pm 3\sigma $ | $ \approx 0.9973 $      | **99.73%** |


![Standard Deviation Percentages](./assets/03.%20Standard_deviation.jpg)

**Observations from the Standard Deviation (Bell Curve) plot:**

1. **Symmetry**  
   - The curve is perfectly **symmetric** around the mean $\mu$.  
   - The left side and right side have identical percentages.

2. **68-95-99.7 Rule (Detailed Breakdown)**  

   | Distance from Mean | Percentage on **one side** | Percentage on **both sides** |
   |--------------------|----------------------------|------------------------------|
   | $0$ to $1\sigma$   | 34.1%                      | **68.2%**                    |
   | $1\sigma$ to $2\sigma$ | 13.6%                   | **95.4%** (cumulative)       |
   | $2\sigma$ to $3\sigma$ | 2.1%                    | **99.6%** (cumulative)       |
   | Beyond $3\sigma$   | 0.1%                       | Almost everything (99.8%)    |

3. **Key Percentages**  
   - **68%** of the data lies within $\mu \pm 1\sigma$  
   - **95%** of the data lies within $\mu \pm 2\sigma$  
   - **99.7%** of the data lies within $\mu \pm 3\sigma$

4. **Practical Insights**  
   - Only about **0.3%** of values fall outside $\mu \pm 3\sigma$ (very rare).  
   - Most of the data (nearly 95%) is concentrated within just 2 standard deviations of the mean.  
   - The tall central region ($34.1\% + 34.1\%$) shows that the majority of values are close to the mean.

5. **Visual Takeaway**  
   - The darker central area represents the highest concentration of probability.  
   - The curve gets thinner and lower as we move farther from $\mu$, matching the rapid drop in the PDF.


![68-95-99.7 Rule](./assets/04.%2068-95-99.7.jpg)

**Observations from the 68-95-99.7 Rule plot:**

1. **Overall Structure**  
   - This is the standard normal distribution centered at $0$ (mean $\mu = 0$).  
   - The horizontal axis is marked in units of standard deviation: $-3\sigma$, $-2\sigma$, $-1\sigma$, $0$, $+1\sigma$, $+2\sigma$, $+3\sigma$.

2. **Detailed Area Breakdown**

   | Region                        | Percentage | Notes                              |
   |-------------------------------|------------|------------------------------------|
   | $0$ to $+1\sigma$             | 34.1%      | Right half of the central peak     |
   | $-1\sigma$ to $0$             | 34.1%      | Left half of the central peak      |
   | $+1\sigma$ to $+2\sigma$      | 13.6%      | Right shoulder                     |
   | $-2\sigma$ to $-1\sigma$      | 13.6%      | Left shoulder                      |
   | $+2\sigma$ to $+3\sigma$      | 2.1%       | Far right tail                     |
   | $-3\sigma$ to $-2\sigma$      | 2.1%       | Far left tail                      |
   | Beyond $\pm 3\sigma$         | 0.1% each  | Extremely rare values              |

3. **Cumulative Rule**  
   - Within $\pm 1\sigma$: $34.1\% + 34.1\% = \mathbf{68.2\%}$  
   - Within $\pm 2\sigma$: $68.2\% + 13.6\% + 13.6\% = \mathbf{95.4\%}$  
   - Within $\pm 3\sigma$: $95.4\% + 2.1\% + 2.1\% = \mathbf{99.6\%}$ (≈ 99.7%)

4. **Key Insights**  
   - Almost all data (99.7%) lies within 3 standard deviations of the mean.  
   - Only **0.3%** of observations fall outside $\pm 3\sigma$ (very unusual events).  
   - The curve is perfectly symmetric — left and right sides are mirror images.

5. **Practical Meaning**  
   - If a value is more than $3\sigma$ away from the mean, it is considered an extreme outlier in a normal distribution.  
   - This rule gives a quick way to understand spread without calculating exact probabilities.


### Detailed Breakdown (Standard Normal)

| Interval                   | Percentage | Cumulative from center |
| -------------------------- | ---------- | ---------------------- |
| $ 0 $ to $ 1\sigma $       | 34.1%      | 34.1%                  |
| $ 1\sigma $ to $ 2\sigma $ | 13.6%      | 47.7%                  |
| $ 2\sigma $ to $ 3\sigma $ | 2.1%       | 49.8%                  |
| Beyond $ 3\sigma $         | 0.1%       | 50.0%                  |

Because the curve is symmetric, the same percentages appear on both sides of the mean.

**Totals:**

- $ \pm 1\sigma $: $ 34.1\% + 34.1\% = 68.2\% $
- $ \pm 2\sigma $: $ 68.2\% + 13.6\% + 13.6\% = 95.4\% $
- $ \pm 3\sigma $: $ 95.4\% + 2.1\% + 2.1\% \approx 99.7\% $

### Summary

| Topic              | Controlled by     | Key Point                                      |
|--------------------|-------------------|------------------------------------------------|
| **PDF Shape**      | $ \sigma^2 $      | Small → tall & narrow <br> Large → short & wide |
| **Location**       | $ \mu $           | Shifts the curve left or right                 |
| **68-95-99.7 Rule**| —                 | $ \mu \pm 1\sigma $ ≈ 68% <br> $ \mu \pm 2\sigma $ ≈ 95% <br> $ \mu \pm 3\sigma $ ≈ 99.7% |

> Practical Takeaway: Once you know $ \mu $ and $ \sigma $, you immediately know where the bulk of the data lies — without calculating complicated integrals.


Here’s a clean set of **Observations** you can append for the three new images:

### 05. Symmetric Distribution, Skewness, Kurtosis

> Symmetric Distribution

![Symmetric Distribution](./assets/05.%20Symmetric_distribution.jpg)

**Observations:**

- The **Standard Normal Distribution** is perfectly symmetric.
- The red dashed line is the **Line of Symmetry**, which passes through the mean ($\mu = 0$).
- Left side of the curve is a mirror image of the right side.
- Because of this symmetry:
  - Mean = Median = Mode
  - $P(X \leq -a) = P(X \geq a)$ for any value $a$
- This symmetry is one of the most important properties of the Normal distribution.

> Skewness

![Skewness](./assets/06.%20Skewness.jpg)

**Observations:**

| Type of Skew     | Shape Description                              | Tail Direction      | Mean vs Median          |
|------------------|------------------------------------------------|---------------------|-------------------------|
| **Negative Skew** (Left-skewed) | Long tail on the left side                    | Left tail longer    | Mean < Median           |
| **Symmetric** (Normal) | Both sides are mirror images                  | No long tail        | Mean = Median = Mode    |
| **Positive Skew** (Right-skewed) | Long tail on the right side                   | Right tail longer   | Mean > Median           |

**Key Points:**
- Skewness measures the **asymmetry** of a distribution.
- In a negatively skewed distribution, extreme low values pull the mean to the left.
- In a positively skewed distribution, extreme high values pull the mean to the right.
- The Normal distribution has **zero skewness** (perfectly symmetric).

> Kurtosis

![Kurtosis](./assets/07.%20Kurtosis.jpg)

**Observations:**

Kurtosis measures the **tailedness** and **peakedness** of a distribution (compared to the Normal distribution).

| Label | Kurtosis Value | Shape Characteristics                              | Type                  |
|-------|----------------|----------------------------------------------------|-----------------------|
| D     | 3              | Very sharp peak, heavy tails                       | Leptokurtic           |
| S     | 2              | Sharp peak, moderately heavy tails                 | Leptokurtic           |
| L     | 1.2            | Moderately peaked                                  | Slightly Leptokurtic  |
| N     | 0              | Standard Normal (reference)                        | Mesokurtic            |
| C     | -0.59          | Flatter peak, thinner tails                        | Platykurtic           |
| W     | -1             | Even flatter peak                                  | Platykurtic           |
| U     | -1.2           | Very flat peak, light tails                        | Platykurtic           |

**Key Points:**
- **Leptokurtic** (Kurtosis > 0): Tall peak + heavy tails → more outliers
- **Mesokurtic** (Kurtosis ≈ 0): Normal distribution
- **Platykurtic** (Kurtosis < 0): Flat peak + thin tails → fewer outliers
- The purple box highlights the central region where the differences in peakedness are most visible.


Here’s the clean lecture note version for this page:


## 06. Standard Normal Variate ($Z$) and Standardization
![Standardization](./assets/08.%20Standardization.jpg)

### What is a Standard Normal Variate?

A **Standard Normal Variate** (usually denoted by $Z$) is a random variable that follows the **Standard Normal Distribution**:

$$
Z \sim \mathcal{N}(0, 1)
$$

This means:
- Mean $\mu = 0$
- Variance $\sigma^2 = 1$
- Standard deviation $\sigma = 1$

---

### Standardization

Suppose we have any normal random variable:

$$
X \sim \mathcal{N}(\mu, \sigma^2)
$$

We can convert it into a standard normal variate using the formula:

$$
Z = \dfrac{X - \mu}{\sigma}
$$

After this transformation:

$$
Z \sim \mathcal{N}(0, 1)
$$

This process is called **Standardization** (or converting to $z$-scores).

### Why do we standardize?

- The 68-95-99.7 rule is defined for the **standard normal distribution**.
- By converting any normal variable $X$ into $Z$, we can directly apply the 68-95-99.7 rule.
- It allows us to compare values from different normal distributions on the same scale.


### Example of Standardization

If we have data points $x_1, x_2, \dots, x_{50}$ from $X \sim \mathcal{N}(\mu, \sigma^2)$, then each standardized value is:

$$
x_i' = \dfrac{x_i - \mu}{\sigma}
$$

And

$$
x_i' \sim \mathcal{N}(0, 1)
$$

### Visual Summary

After standardization, the distribution always looks like this:

- Centered at $0$
- Spread controlled by $\sigma = 1$
- We can directly use the `68-95-99.7` rule on the $Z$ values.

## 07. Kernel Density Estimation (KDE)

Kernel Density Estimation is a **non-parametric** way to estimate the probability density function of a continuous random variable from a sample of data.

### Visual Explanation

![Kernel Density Estimation](./assets/09.%20KDE.jpg)

**Left Plot – Histogram**  
- Shows the data using bars (bins).  
- Simple but depends heavily on bin width and starting point.  
- Gives a rough idea of the distribution.

**Right Plot – Kernel Density Estimate**  
- The **solid blue curve** is the final KDE.  
- The **red dashed curves** are individual kernels (usually Gaussian) centered at each data point (shown as white ticks on the x-axis).  
- The KDE is formed by **adding up** all the individual kernels.


### How KDE Works

1. Place a smooth kernel (most commonly a Gaussian curve) on top of every data point.
2. Add all these kernels together.
3. The resulting smooth curve is the estimated probability density function.

$$
\hat{f}(x) = \dfrac{1}{n h} \sum_{i=1}^{n} K\left( \dfrac{x - x_i}{h} \right)
$$

Where:
- $n$ = number of data points
- $h$ = bandwidth (controls smoothness)
- $K$ = kernel function (usually standard normal)

### Key Observations from the Plot

- The histogram is **blocky**, while the KDE is **smooth**.
- Each red dashed curve is a kernel centered at a data point.
- Where data points are dense (around $x = -1$), the KDE becomes higher.
- Where data points are sparse, the KDE becomes lower.
- The final blue curve is the sum of all the individual kernels.


### Advantages of KDE over Histogram

| Feature              | Histogram                  | KDE                          |
|----------------------|----------------------------|------------------------------|
| Smoothness           | Jagged / blocky            | Smooth continuous curve      |
| Dependence on bins   | Strongly depends on bin width & position | Depends mainly on bandwidth $h$ |
| Shape discovery      | Can hide true shape        | Better at revealing underlying distribution |
| Mathematical form    | Discrete                   | Continuous estimate of PDF   |


### Important Note

- Bandwidth $h$ is critical:  
  - Too small $h$ → very spiky (overfitting)  
  - Too large $h$ → over-smoothed (loses important features)

Would you like me to also add a short comparison between Histogram, PDF, and KDE in a summary card format?

## 08. Sampling Distribution & Central Limit Theorem (CLT)

![CLT](./assets/10.%20CLT.jpg)
### Sampling Distribution of the Sample Mean

Suppose we have a population with any distribution (not necessarily Gaussian):

- Population: $X$ (distribution of incomes, heights, etc.)
- We take many random samples of size $n$ (for example $n = 30$)

| Sample Number | Sample                  | Sample Mean     |
|---------------|-------------------------|-----------------|
| 1             | $S_1$                   | $\bar{x}_1$     |
| 2             | $S_2$                   | $\bar{x}_2$     |
| 3             | $S_3$                   | $\bar{x}_3$     |
| $\vdots$      | $\vdots$                | $\vdots$        |
| $m$           | $S_m$                   | $\bar{x}_m$     |

We now have a collection of sample means:

$$
\bar{x}_1,\ \bar{x}_2,\ \bar{x}_3,\ \dots,\ \bar{x}_m
$$

The distribution of these sample means is called the **Sampling Distribution of the Sample Mean**.

$$
\text{Distribution of }\bar{x}_i = \text{Sampling Distribution of Sample Means}
$$

### Central Limit Theorem (CLT)

**Statement of CLT:**

If we take random samples of size $n$ from **any** population (with finite mean $\mu$ and finite variance $\sigma^2$), then as the sample size $n$ becomes large:

$$
\bar{x} \;\sim\; \mathcal{N}\left(\mu,\ \dfrac{\sigma^2}{n}\right)
$$

In other words:

> The sampling distribution of the sample mean approaches a **Normal distribution**, regardless of the shape of the original population distribution.

### Key Points of CLT

| Condition                        | Result                                      |
|----------------------------------|---------------------------------------------|
| Population has mean $\mu$ and variance $\sigma^2$ | Sampling distribution has mean $\mu$ and variance $\dfrac{\sigma^2}{n}$ |
| Sample size $n$ is large         | Sampling distribution becomes approximately Normal |
| Original population can be anything | Even if the population is skewed or non-normal, $\bar{x}$ becomes normal |

### Rule of Thumb

- When $n \geq 30$, the sampling distribution of $\bar{x}$ is approximately Normal (even if the population is not Normal).
- If the population itself is Normal, then $\bar{x}$ is Normal for **any** sample size $n$.

### Summary of CLT

$$
\text{Any population} \xrightarrow{\text{large } n} \text{Sampling distribution of }\bar{x} \approx \text{Normal}
$$

$$
\bar{x} \sim \mathcal{N}\left(\mu,\ \dfrac{\sigma^2}{n}\right)
$$

- Mean of sample means $= \mu$
- Variance of sample means $= \dfrac{\sigma^2}{n}$
- Standard error of the mean $= \dfrac{\sigma}{\sqrt{n}}$


## 09. Q-Q Plot (Quantile-Quantile Plot)

### Purpose
How can we check whether a random variable $X$ is **Normally distributed** or not?

Two common techniques:
1. **Q-Q Plot** (Graphical method)
2. Statistical tests (e.g., Kolmogorov-Smirnov, Anderson-Darling)

### What is a Q-Q Plot?

A **Quantile-Quantile (Q-Q) Plot** compares the quantiles (percentiles) of our data with the quantiles of a theoretical distribution (usually the Standard Normal distribution).

> ### Steps to Create a Q-Q Plot

> **Step 1: Prepare the data**

Suppose we have a sample:
$$
X: x_1, x_2, x_3, \dots, x_{500}
$$

- Sort the data in ascending order:
$$
x'_1 \leq x'_2 \leq x'_3 \leq \dots \leq x'_{500}
$$

- Compute the percentiles (or quantiles) of the sorted data.

> **Step 2: Generate theoretical quantiles**

- Create a Standard Normal distribution: $Y \sim \mathcal{N}(0,1)$
- Generate a large number of observations (e.g., 1000) from $Y$
- Sort them and compute the corresponding percentiles:
$$
y'_1, y'_2, y'_3, \dots, y'_{100}
$$
(These are the **theoretical quantiles**)

> **Step 3: Plot the points**

Plot the pairs:
$$
(y'_i,\ x'_i)
$$

- Horizontal axis → Theoretical quantiles (from Standard Normal)
- Vertical axis → Sample quantiles (from our data)

![QQ](./assets/11.%20QQ.jpg)

### How to Interpret a Q-Q Plot

| Pattern in Q-Q Plot                          | Conclusion                                      |
|---------------------------------------------|-------------------------------------------------|
| Points lie approximately on a **straight line** | Data is approximately Normally distributed     |
| Points deviate systematically from the line | Data is **not** Normal                         |
| S-shaped curve                              | Data has heavier or lighter tails than Normal  |
| Curved pattern                              | Data is skewed                                 |

### Two Common Uses of Q-Q Plot

1. **Checking Normality**  
   Is $X \sim \mathcal{N}(\mu, \sigma^2)$?

2. **Comparing two distributions**  
   Do $X$ and $Y$ have the same distribution?

```py
#Q-Q plot
import numpy as np 
import pylab 
import scipy.stats as stats
import matplotlib.pyplot as plt

# N(0,1)
std_normal = np.random.normal(loc = 0, scale = 1, size=1000)

# 0 to 100th percentiles of std-normal
for i in range(0,101):
    print(i, np.percentile(std_normal,i))

# generate 100 sanples from N(20,5)
measurements = np.random.normal(loc = 0, scale = 1, size=10000) 
#try size=1000

plt.xlim(-1,1)

stats.probplot(measurements, dist="norm", plot=pylab)
pylab.show()

# generate 100 sanples from N(20,5)
measurements = np.random.normal(loc = 0, scale = 1, size=10000) 
#try size=1000
plt.xlim(-4, 4)

stats.probplot(measurements, dist="norm", plot=pylab)
pylab.show()

# generate 100 sanples from N(20,5)
measurements = np.random.uniform(low = -1, high = 1, size=10000) 
#try size=100, 1000, 10000

stats.probplot(measurements, dist="norm", plot=pylab)
pylab.show()

```

### Summary

> If the points in the Q-Q plot lie roughly on a straight line, we can conclude that the sample comes from a Normal distribution (or from the same distribution as the theoretical one).


## 10. How / Where to Use Distributions?

Distributions (especially the Normal distribution) are extremely useful for answering real-world business and data analysis questions.

### Example 1: T-Shirt Sizes for Employees

**Company size:** 1000 employees  

**Task:** Order T-shirts (S, M, L, XL) for all employees.

**Questions we can answer using distributions:**

1. How many XL T-shirts should we order?
2. Collect data of all 1000 employees’ heights.

**Given information:**
- Height range for XL: Height $> 180$ cm
- From domain knowledge / previous data: Heights follow a Normal distribution

$$
\text{Heights} \sim \mathcal{N}(\mu, \sigma^2)
$$

We can calculate:

$$
P(X > 180) = 1\%
$$

This means only about **1%** of employees need XL size.

Using the Normal distribution (PDF / CDF), we can estimate the required quantity of each size accurately instead of guessing.

### Example 2: Employee Salaries

Assume salaries follow a Normal distribution:

$$
S \sim \mathcal{N}(\mu, \sigma^2)
$$

**Questions:**

1. How many employees make a salary **greater than $100k**?
2. How many employees have salary in the range **[$50k, $70k]**?

From the CDF:

- Suppose $P(50k \leq S \leq 70k) \approx 30\%$

We can directly estimate the number of employees in any salary range using the Normal distribution.

### Why Distributions Are Useful

| Use Case                        | What Distribution Helps With                          |
|--------------------------------|-------------------------------------------------------|
| Inventory / Sizing decisions   | Estimate demand for each category (S, M, L, XL)      |
| Salary analysis                | Find percentage of people in different salary bands  |
| Quality control                | Detect unusual values (outliers)                      |
| Risk estimation                | Calculate probability of extreme events               |
| Forecasting                    | Make data-driven decisions instead of guessing        |


![Dist](./assets/12.%20Dist.jpg)
![Dist-PDF-CDF](./assets/12.%20Dist-PDF-CDF.jpg)

### Key Takeaway

> Once we know (or assume) that a variable follows a particular distribution (especially Normal), we can answer many practical questions using PDF, CDF, and the 68-95-99.7 rule — without collecting data for every single individual.


## 11. Chebyshev's Inequality

### Why do we need Chebyshev’s Inequality?

The **68-95-99.7 rule** works only when the data follows a **Normal (Gaussian)** distribution.

But what if:
- We **don’t know** the distribution of the data?
- We only know the mean $\mu$ and standard deviation $\sigma$?

In such cases, we use **Chebyshev’s Inequality**.

### Statement of Chebyshev’s Inequality

For **any** random variable $X$ (with finite mean $\mu$ and non-zero finite standard deviation $\sigma$):

$$
P\big(|X - \mu| \geq k\sigma\big) \leq \dfrac{1}{k^2}
$$

Equivalently:

$$
P\big(\mu - k\sigma < X < \mu + k\sigma\big) \geq 1 - \dfrac{1}{k^2}
$$

Where $k > 0$.

### Interpretation

- At least $1 - \dfrac{1}{k^2}$ proportion of the data lies within $k$ standard deviations from the mean.
- This result is true for **any distribution** (not just Normal).

| $k$   | Minimum Proportion of Data within $\mu \pm k\sigma$ |
|-------|------------------------------------------------------|
| $k=2$ | $1 - \dfrac{1}{4} = 75\%$                            |
| $k=3$ | $1 - \dfrac{1}{9} \approx 89\%$                      |
| $k=4$ | $1 - \dfrac{1}{16} = 93.75\%$                        |

### Example: Student Heights

Suppose heights of students follow a Normal distribution:

$$
X \sim \mathcal{N}(150,\ 10^2)
$$

Using the 68-95-99.7 rule:

$$
P(130 \leq X \leq 170) = 95\%
$$

(This is stronger because we assumed Normality.)

### Example: Salaries (Distribution Unknown)

We only know:
- Mean salary $\mu = 40k$
- Standard deviation $\sigma = 10k$

**Question 1:** What percentage of individuals have salary in the range $[20k,\ 60k]$?

$$
20k = \mu - 2\sigma, \quad 60k = \mu + 2\sigma
$$

Using Chebyshev’s Inequality ($k=2$):

$$
P(20k < X < 60k) \geq 1 - \dfrac{1}{2^2} = 1 - \dfrac{1}{4} = 0.75 = 75\%
$$

**Question 2:** What percentage of individuals have salary in the range $[10k,\ 70k]$?

$$
10k = \mu - 3\sigma, \quad 70k = \mu + 3\sigma
$$

$$
P(10k < X < 70k) \geq 1 - \dfrac{1}{9} \approx 89\%
$$

### Comparison: Normal Rule vs Chebyshev

| Rule                    | Assumption              | $k=2$ Result      | $k=3$ Result       |
|-------------------------|-------------------------|-------------------|--------------------|
| 68-95-99.7 Rule         | Data is Normal          | 95%               | 99.7%              |
| Chebyshev’s Inequality  | Any distribution        | At least 75%      | At least 89%       |

> **Note**: Chebyshev’s bound is weaker (more conservative) but much more general.

![Chebyshevs](./assets/13.%20Chebyshevs.jpg)

### Key Takeaway

- Use **68-95-99.7 rule** when data is approximately Normal.
- Use **Chebyshev’s Inequality** when you only know $\mu$ and $\sigma$, and the distribution is unknown.

## 12. Discrete and Continuous Uniform Distributions

> Discrete Uniform Distributions  

![PMF](./assets/14.%20Uniform_discrete_PMF.jpg)
![CDF](./assets/14.%20Uniform_discrete_CDF.jpg)

| Property | Formula / Value |
| --- | --- |
| **Notation** | $\mathcal{U}\{a,b\}$ or $\mathrm{unif}\{a,b\}$ |
| **Parameters** | $a,b$ integers with $b \ge a$<br><br>$n = b - a + 1$ |
| **Support** | $k \in \{a, a+1, \dots, b-1, b\}$ |
| **PMF** | $\frac{1}{n}$ |
| **CDF** | $\frac{\lfloor k \rfloor - a + 1}{n}$ |
| **Mean** | $\frac{a+b}{2}$ |
| **Median** | $\frac{a+b}{2}$ |
| **Mode** | N/A |
| **Variance** | $\frac{(b-a+1)^2 - 1}{12}$ |
| **Skewness** | $0$ |
| **Excess kurtosis** | $-\frac{6(n^2+1)}{5(n^2-1)}$ |
| **Entropy** | $\ln(n)$ |
| **MGF** | $\frac{e^{at} - e^{(b+1)t}}{n(1 - e^t)}$ |
| **CF** | $\frac{e^{iat} - e^{i(b+1)t}}{n(1 - e^{it})}$ |
| **PGF** | $\frac{z^a - z^{b+1}}{n(1-z)}$ |

**Use of Discrete Uniform Distribution in Machine Learning**

The discrete uniform distribution \(\mathcal{U}\{a, b\}\) is one of the simplest and most frequently used distributions in ML, mainly because it models **“every option is equally likely”**.

### Common Uses

| Use Case                        | How Discrete Uniform is Used                              | Example |
|--------------------------------|-----------------------------------------------------------|--------|
| **Random Sampling**            | Select data points, features, or indices with equal probability | Randomly pick a mini-batch or a subset of features |
| **Data Augmentation**          | Randomly choose transformations or samples                | Random crop location, random horizontal flip decision |
| **Exploration in RL**          | Uniform random action selection (ε-greedy baseline)       | Agent picks any action with probability \(1/|\mathcal{A}|\) |
| **Hyperparameter Search**      | Sample discrete hyperparameters uniformly                 | Number of layers, kernel size, number of trees |
| **Random Initialization**      | Initialize discrete structures randomly                   | Random permutation of features, random class assignment |
| **Baseline / Dummy Models**    | Random classifier that predicts each class equally        | Sanity-check baseline (accuracy ≈ \(1/C\)) |
| **Bootstrapping / Resampling** | Sample with equal probability (with or without replacement) | Creating bootstrap samples for bagging / uncertainty |
| **Synthetic Data Generation**  | Generate discrete labels or categorical features          | Creating balanced synthetic datasets |
| **Monte Carlo Methods**        | Generate uniform random integers for simulation           | Estimating expectations, randomized algorithms |

### Key Practical Points

- Whenever you write `np.random.randint(a, b+1)` or `random.choice(...)`, you are sampling from a discrete uniform distribution.
- It is the **default “no prior knowledge”** distribution for discrete choices.
- Because every value has the same probability \(1/n\), it is extremely easy to sample from and to reason about.
- In many algorithms it serves as the **null / random baseline** against which smarter methods are compared.

### Short Summary

In Machine Learning, the discrete uniform distribution is the mathematical model behind almost every “pick something completely at random” operation — from sampling data points and actions to choosing hyperparameters and creating random baselines.

> Continuous Uniform Distributions  

![PMF](./assets/14.%20Uniform_continuous_PDF.jpg)  
![CDF](./assets/14.%20Uniform_continuous_CDF.jpg)


| Property | Value / Formula |
| --- | --- |
| **Notation** | $\mathcal{U}_{[a,b]}$ |
| **Parameters** | $-\infty < a < b < \infty$ |
| **Support** | $[a, b]$ |
| **PDF** | $\begin{cases} \frac{1}{b-a} & \text{for } x \in [a, b] \\ 0 & \text{otherwise} \end{cases}$ |
| **CDF** | $\begin{cases} 0 & \text{for } x < a \\ \frac{x-a}{b-a} & \text{for } x \in [a, b] \\ 1 & \text{for } x > b \end{cases}$ |
| **Mean** | $\frac{1}{2}(a+b)$ |
| **Median** | $\frac{1}{2}(a+b)$ |
| **Mode** | any value in $(a, b)$ |
| **Variance** | $\frac{1}{12}(b-a)^2$ |
| **MAD** | $\frac{1}{4}(b-a)$ |
| **Skewness** | $0$ |
| **Excess kurtosis** | $-\frac{6}{5}$ |
| **Entropy** | $\log(b-a)$ |
| **MGF** | $\begin{cases} \frac{e^{tb} - e^{ta}}{t(b-a)} & \text{for } t \neq 0 \\ 1 & \text{for } t = 0 \end{cases}$ |
| **CF** | $\begin{cases} \frac{e^{itb} - e^{ita}}{it(b-a)} & \text{for } t \neq 0 \\ 1 & \text{for } t = 0 \end{cases}$ |

**Use of Continuous Uniform Distribution in Machine Learning**

The continuous uniform distribution \(\mathcal{U}_{[a,b]}\) models the idea that **every value in an interval is equally likely**. It is extremely common in ML for generating randomness in a bounded continuous range.

### Common Uses

| Use Case                          | How Continuous Uniform is Used                                      | Example |
|-----------------------------------|---------------------------------------------------------------------|--------|
| **Weight / Parameter Initialization** | Initialize neural network weights uniformly in a range             | Xavier / Glorot uniform initialization, He uniform |
| **Hyperparameter Sampling**       | Sample continuous hyperparameters uniformly                        | Learning rate, dropout rate, weight decay, batch size scaling |
| **Data Augmentation**             | Random continuous transformations                                  | Random rotation angle, brightness jitter, crop offset, shear |
| **Noise Injection**               | Add bounded random noise                                           | Input noise, label smoothing noise, adversarial perturbations |
| **Random Feature / Projection**   | Generate random continuous features or projection matrices         | Random Fourier features, random projections |
| **Monte Carlo & Simulation**      | Generate continuous random numbers in an interval                  | Estimating integrals, randomized algorithms |
| **Bayesian Priors**               | Flat (non-informative) prior over a bounded parameter              | Uniform prior on a probability or a scale parameter |
| **Exploration in Continuous Action Spaces** | Uniform random actions (baseline exploration)                   | Continuous control RL (before smarter policies) |
| **Synthetic Data Generation**     | Generate continuous features uniformly                             | Creating synthetic tabular data or random positions |
| **Regularization Techniques**     | Stochastic regularization with uniform noise                       | Dropout variants, dropblock, stochastic depth |

### Key Practical Points

- Whenever you write `np.random.uniform(a, b)` or `torch.rand(...) * (b-a) + a`, you are sampling from a continuous uniform distribution.
- It is the default “no preference” distribution for any continuous value that must stay inside a fixed interval \([a, b]\).
- Because the PDF is perfectly flat, every point inside \([a, b]\) has the same density \(\frac{1}{b-a}\).
- The CDF is a simple straight line from 0 to 1 between \(a\) and \(b\), making probabilities very easy to compute:
  \[
  P(X \le x) = \frac{x-a}{b-a} \quad \text{for } x \in [a,b]
  \]

### Short Summary

> In Machine Learning the continuous uniform distribution is the standard way to say “pick any real number between \(a\) and \(b\) with equal chance”. It appears in weight initialization, hyperparameter search, data augmentation, noise injection, and as a non-informative prior — essentially any time we need randomness inside a bounded continuous interval.

## 13. How to Randomly Sample Data Points (Uniform Distribution)

```py
import random
print(random.random())

#load IRIS dataset with 150 points.
from sklearn import datasets
iris = datasets.load_iris()
d = iris.data
d.shape
print(d[0])

# Sample 30 points randomly from the 150 point dataset
n=150
m=30
p = m/n
print(p)
sampled_data =[];

for i in range(0,n):
  a = random.random()
#   print(a)
  if  a <= p:
    sampled_data.append(d[i,:])
    
print(sampled_data)
```

## 14. Bernoulli and Binomial Distribution

### Bernoulli Distribution

A random variable $X$ follows a **Bernoulli distribution** if it has only **two possible outcomes**:

- Success → $1$ (with probability $p$)
- Failure → $0$ (with probability $1-p$)

$$
X \sim \text{Bernoulli}(p) \quad \text{where } 0 < p < 1
$$

**Example:** Tossing a fair coin once  
$$
X \sim \text{Bernoulli}(p = 0.5)
$$

- $P(X = 1) = p$ (Head)
- $P(X = 0) = 1-p$ (Tail)

### Binomial Distribution

When we repeat a Bernoulli trial **$n$ independent times**, the total number of successes follows a **Binomial distribution**.

$$
Y \sim \text{Binomial}(n, p)
$$

Where:
- $n$ = number of independent trials
- $p$ = probability of success in each trial
- $Y$ = number of successes

**Example:** Tossing a fair coin 10 times  
$$
Y = \text{Number of heads} \sim \text{Binomial}(n=10,\ p=0.5)
$$

$$
Y \in \{0, 1, 2, \dots, 10\}
$$

### Probability Mass Function (PMF)

The probability of getting exactly $k$ successes in $n$ trials is:

$$
P(Y = k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

Where:

$$
\binom{n}{k} = \dfrac{n!}{k!(n-k)!}
$$


### Visual Understanding

**Bernoulli Distribution** (only two possible values: 0 and 1)

![Bernoulli Distribution](./assets/15.%20Bernoulli_Distribution.jpg)

- Different colors show different values of $p$.

**Binomial Distribution – PDF (Probability Mass Function)**

![Binomial PDF](./assets/15.%20Binomial_distribution_pdf.jpg)

- Blue: $p=0.5$, $n=20$ (symmetric)
- Green: $p=0.7$, $n=20$ (right-skewed)
- Red: $p=0.5$, $n=40$ (more spread out and closer to Normal)

**Binomial Distribution – CDF**

![Binomial CDF](./assets/15.%20Binomial_distribution_cdf.jpg)

- Shows how the cumulative probability increases.
- Larger $n$ makes the CDF rise more gradually.


### Key Observations

| Feature                  | Bernoulli              | Binomial                          |
|--------------------------|------------------------|-----------------------------------|
| Number of trials         | 1                      | $n$ (multiple)                    |
| Possible values          | 0 or 1                 | $0, 1, 2, \dots, n$               |
| Parameter                | $p$                    | $n$ and $p$                       |
| Mean                     | $p$                    | $np$                              |
| Variance                 | $p(1-p)$               | $np(1-p)$                         |

### Important Notes

- Binomial distribution is the sum of $n$ independent Bernoulli random variables.
- When $n$ is large and $p$ is not too close to 0 or 1, the Binomial distribution can be approximated by a Normal distribution (this is related to the Central Limit Theorem).


## 15. Log-Normal Distribution

![Log-Normal PDF](./assets/16.%20Log-normal-pdfs.jpg)

![Log-Normal CDF](./assets/16.%20Log-normal-cdfs.jpg)

### Definition

A random variable $X$ follows a **Log-Normal distribution** if its natural logarithm is normally distributed.

$$
X \sim \text{Log-Normal}(\mu, \sigma^2)
\quad \Longleftrightarrow \quad
\ln(X) \sim \mathcal{N}(\mu, \sigma^2)
$$

Equivalently:

$$
Y = \ln(X) \quad \Rightarrow \quad Y \sim \mathcal{N}(\mu, \sigma^2)
$$

### Relationship

| Variable       | Distribution                      |
|----------------|-----------------------------------|
| $X$            | Log-Normal($\mu$, $\sigma^2$)     |
| $Y = \ln(X)$   | Normal($\mu$, $\sigma^2$)         |

### How to Check if Data is Log-Normal

Given observations $x_1, x_2, \dots, x_n$:

1. Compute the natural log of each value:
   $$
   y_i = \ln(x_i)
   $$

2. Test whether the $y_i$ values are normally distributed (using Q-Q plot or normality tests).

3. **Conclusion**:
   - If $y_i \sim \mathcal{N}(\mu, \sigma^2)$, then $X \sim \text{Log-Normal}(\mu, \sigma^2)$.

### Key Properties

| Property              | Formula / Value                                                                 |
|-----------------------|---------------------------------------------------------------------------------|
| **Notation**          | $\text{Lognormal}(\mu, \sigma^2)$                                               |
| **Parameters**        | $\mu \in \mathbb{R}$, $\sigma > 0$                                              |
| **Support**           | $x > 0$                                                                         |
| **PDF**               | $\dfrac{1}{x \sigma \sqrt{2\pi}} \exp\left( -\dfrac{(\ln x - \mu)^2}{2\sigma^2} \right)$ |
| **CDF**               | $\Phi\left( \dfrac{\ln x - \mu}{\sigma} \right)$                                 |
| **Mean**              | $\exp\left( \mu + \dfrac{\sigma^2}{2} \right)$                                   |
| **Median**            | $\exp(\mu)$                                                                     |
| **Mode**              | $\exp(\mu - \sigma^2)$                                                          |
| **Variance**          | $\left[ \exp(\sigma^2) - 1 \right] \exp(2\mu + \sigma^2)$                       |
| **Skewness**          | $\left[ \exp(\sigma^2) + 2 \right] \sqrt{\exp(\sigma^2) - 1}$                   |

### Common Applications

https://en.wikipedia.org/wiki/Log-normal_distribution#Occurrence_and_applications

The Log-Normal distribution commonly appears in data that is:

- Strictly positive
- Right-skewed

**Typical examples:**
- Stock prices and financial returns
- Income and wealth distribution
- City population sizes
- File sizes / comment lengths
- Biological measurements
- Time-to-failure / lifetime data

### Summary

> If a variable is **positive** and **right-skewed**, take the natural logarithm.  
> If the transformed data becomes approximately Normal, the original variable follows a **Log-Normal distribution**.

## 16. Power-Law Distribution

### What is a Power-Law Distribution?

A distribution follows a **Power Law** (also called **Pareto distribution**) when a small number of observations account for a large proportion of the total effect.

**Classic example – 80/20 Rule (Pareto Principle):**
- 20% of the items produce 80% of the impact
- 80% of the items produce only 20% of the impact

This pattern appears in wealth distribution, city sizes, word frequencies, website traffic, software bugs, customer revenue, etc.

### Visual Understanding

![PowerLaw](./assets/17.%20Power-Law.jpg)

**Observations:**
- A small proportion of items (the “vital few”) account for the majority of the impact.
- The remaining large proportion (the “useful many”) contribute only a small share.
- The curve shows the typical rapid decay followed by a long heavy tail.

### Probability Density Function (PDF)

![PDF](./assets/17.%20Pareto_PDF.jpg)

**Observations from the Pareto Type I PDF:**
- Fixed scale parameter $x_m = 1$, different shape parameters $\alpha$.
- Larger $\alpha$ → more peaked near $x_m$ and faster decay in the tail.
- Smaller $\alpha$ → heavier tail (more extreme values).
- As $\alpha \to \infty$, the distribution converges to a Dirac delta at $x_m$.

### Cumulative Distribution Function (CDF)

![CDF](./assets/17.%20Pareto_CDF.jpg)

**Observations from the Pareto Type I CDF:**
- All curves start at 0 for $x < x_m$ and rise toward 1.
- Larger $\alpha$ produces a steeper rise near $x_m$.
- As $\alpha \to \infty$, the CDF approaches a step function at $x = x_m$.

### Mathematical Summary (Pareto Type I)

| Property            | Expression                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Notation            | $\text{Pareto}(x_m, \alpha)$                                               |
| Parameters          | $x_m > 0$ (scale), $\alpha > 0$ (shape)                                    |
| Support             | $x \in [x_m, \infty)$                                                      |
| PDF                 | $\dfrac{\alpha x_m^\alpha}{x^{\alpha+1}}$                                  |
| CDF                 | $1 - \left(\dfrac{x_m}{x}\right)^\alpha$                                   |
| Mean                | $\dfrac{\alpha x_m}{\alpha-1}$ for $\alpha > 1$ (otherwise $\infty$)       |
| Median              | $x_m \cdot 2^{1/\alpha}$                                                   |
| Variance            | Finite only when $\alpha > 2$                                              |

### How to Check if Data Follows a Power Law

**Method 1: Log-Log Plot** (most common diagnostic)

1. Take data points $x_1, x_2, \dots, x_n$ and their frequencies/probabilities $y_i$.
2. Plot $\log(y)$ vs $\log(x)$.

![LogLog](./assets/17.%20Log-log_plot.jpg)

- If the points form an approximately **straight line** → Power Law is a good candidate.
- If not → data does not follow a Power Law.

**Method 2: Q-Q Plot**
- Compare your data against a theoretical Pareto distribution.
- Points lying roughly on a straight line support the Power Law assumption.

### Common Applications in Machine Learning & Real World

https://en.wikipedia.org/wiki/Pareto_distribution#Occurrence_and_applications

| Domain                        | How Power-Law Appears                                      |
|-------------------------------|------------------------------------------------------------|
| Networks / Graphs             | Degree distribution (scale-free networks)                  |
| Natural Language Processing   | Word frequencies (Zipf’s Law)                              |
| Recommendation Systems        | Item popularity (long-tail problem)                        |
| Anomaly Detection             | Modeling rare but extreme events                           |
| Wealth / Income               | Classic Pareto distribution                                |
| Web & Internet                | Website traffic, file sizes, link counts                   |
| Preferential Attachment       | Explains how power-law networks grow                       |

### Key Practical Takeaways

- When data has a **heavy right tail**, a Normal distribution is usually a poor fit.
- The **log-log plot** is the fastest visual check for power-law behavior.
- Recognizing power-law behavior helps us:
  - Choose better models
  - Avoid incorrect Normal assumptions
  - Handle extreme values properly
  - Understand long-tail phenomena in ML systems

> **Key Insight**: Power-law distributions are the natural model for situations where “a few items dominate, while the majority are rare.” This is the mathematical foundation of the famous 80/20 rule.

## 17. Box-Cox Transform

### Why do we need transformations?

Many statistical methods (especially those assuming Normality) work best when the data is approximately Gaussian.

However, real-world data is often:
- Right-skewed (e.g., income, city sizes)
- Follows a Power Law / Pareto distribution
- Log-Normal

In such cases, we apply a **transformation** to make the data closer to Normal.

### Common Transformations

| Original Distribution     | Transformation              | Resulting Distribution     |
|---------------------------|-----------------------------|----------------------------|
| Log-Normal                | $Y = \ln(X)$                | Normal                     |
| Power Law / Pareto        | Power transformation        | Sometimes closer to Normal |
| Skewed data               | Box-Cox transformation      | Approximately Normal       |

### Box-Cox Transformation

The **Box-Cox transformation** is a family of power transformations defined as:

$$
y_i =
\begin{cases}
\dfrac{x_i^\lambda - 1}{\lambda} & \text{if } \lambda \neq 0 \\[10pt]
\ln(x_i) & \text{if } \lambda = 0
\end{cases}
$$

Where:
- $x_i > 0$ (data must be positive)
- $\lambda$ is the transformation parameter

### Special Cases of Box-Cox

| Value of $\lambda$ | Transformation              | Name                  |
|--------------------|-----------------------------|-----------------------|
| $\lambda = 1$      | $y = x - 1$                 | No transformation     |
| $\lambda = 0$      | $y = \ln(x)$                | Log transformation    |
| $\lambda = 0.5$    | $y = \sqrt{x} - 1$          | Square root           |
| $\lambda = -1$     | $y = 1 - \dfrac{1}{x}$      | Reciprocal            |

### Python Example (using SciPy)
**Reference:** [SciPy Box-Cox Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.boxcox.html)

```python
from scipy import stats
import matplotlib.pyplot as plt

# Generate skewed data (log-gamma)
fig = plt.figure()
ax1 = fig.add_subplot(211)
x = stats.loggamma.rvs(5, size=500) + 5
prob = stats.probplot(x, dist=stats.norm, plot=ax1)
ax1.set_xlabel('')
ax1.set_title('Probplot against normal distribution')

# Apply Box-Cox transformation
ax2 = fig.add_subplot(212)
xt, _ = stats.boxcox(x)
prob = stats.probplot(xt, dist=stats.norm, plot=ax2)
ax2.set_title('Probplot after Box-Cox transformation')

plt.show()
```

### Important Note / Limitation

> **Box-Cox transformation is not guaranteed to work on all Pareto or Power-Law distributed data.**

It works well only on **some** of them.  
After applying the Box-Cox transformation, you **must** check the Q-Q plot of the transformed data to confirm whether it has become approximately Normal.

### How to Use Box-Cox in Practice

1. Ensure all data points are **positive**.
2. Apply `stats.boxcox()` (it automatically finds a good $\lambda$).
3. Plot the Q-Q plot of the transformed data.
4. Accept the transformation only if the Q-Q plot looks reasonably linear.

### Summary

| Goal                            | Recommended Tool                  |
|---------------------------------|-----------------------------------|
| Log-Normal → Normal             | Natural Log ($\ln$)               |
| Mild to moderate skewness       | Box-Cox Transformation            |
| Heavy-tailed Power Law / Pareto | Box-Cox (check Q-Q plot carefully)|

> **Key Insight**: Box-Cox is a powerful and flexible tool, but it is **not magic**. Always verify the result with a Q-Q plot.

## 18. Applications of Non-Gaussian Distributions

### Why do we need other distributions?

Not all real-world data follows a Gaussian (Normal) distribution.  
There are hundreds of other distributions (Uniform, Bernoulli, Binomial, Log-Normal, Pareto, Weibull, etc.).

**Question:** Why do we study them?

→ Because a well-chosen distribution gives us a **theoretical model** of how a random variable behaves.  
Once we have the model $X \sim D$, we can answer useful probability questions.

### Example: Daily Rainfall (Weibull Distribution)

**Problem:**  
How large should a water storage dam be?

We have 30–50 years of daily rainfall data.

Let:
$$
X = \text{maximum one-day rainfall}
$$

We want to know:

$$
P(X > 20\,\text{cm})
$$

If this probability is very small (e.g. $\leq 0.1\%$), then designing the dam for 20 cm may be sufficient.

### How to Answer This Question

1. **Collect data**: 30–50 years of daily rainfall.
2. **Store** hundreds of observations.
3. **Fit** a suitable distribution to the data.
4. Researchers have found that **maximum daily rainfall** often follows a **Weibull distribution**.

$$
X \sim \text{Weibull}(\text{parameters})
$$

5. Once we have the fitted Weibull distribution, we can compute:

$$
P(X > 20\,\text{cm}) = 1 - P(X \leq 20\,\text{cm}) = 1 - \text{CDF}(20)
$$

### General Process of Fitting a Distribution

| Step | Action |
|------|--------|
| 1    | Collect data |
| 2    | Visualize (histogram, density plot) |
| 3    | Try candidate distributions (Gaussian, Log-Normal, Weibull, Pareto, etc.) |
| 4    | Check goodness-of-fit using **Q-Q plot** and statistical tests (KS test, Anderson-Darling, etc.) |
| 5    | Select the best-fitting distribution |
| 6    | Use the CDF / PDF of the fitted distribution to answer probability questions |

### Important Notes

- If the data is **not Gaussian**, we can sometimes apply a transformation (e.g. Box-Cox) to make it closer to Normal, and then use Normal methods.
- However, in many cases (especially extreme value problems like rainfall, floods, wind speeds), it is better to directly use the appropriate non-Gaussian distribution (Weibull, Gumbel, Pareto, etc.).

### Common Non-Gaussian Distributions and Their Use Cases

| Distribution       | Typical Shape              | Common Real-World Applications                              | Key Characteristic                  |
|--------------------|----------------------------|-------------------------------------------------------------|-------------------------------------|
| **Bernoulli**      | Two outcomes (0 or 1)      | Coin toss, success/failure, click/no-click                  | Single trial                        |
| **Binomial**       | Discrete, can be skewed    | Number of successes in $n$ trials, defect counts            | Multiple independent Bernoulli trials |
| **Uniform**        | Flat                       | Random number generation, equal likelihood events           | All outcomes equally likely         |
| **Log-Normal**     | Right-skewed               | Stock prices, income, city sizes, file sizes                | $\ln(X)$ is Normal                  |
| **Pareto / Power Law** | Heavy right tail        | Wealth distribution, website traffic, word frequencies      | 80-20 rule, extreme inequality      |
| **Weibull**        | Flexible (can be skewed)   | Lifetime / reliability data, rainfall extremes, wind speeds | Excellent for extreme value modeling |
| **Exponential**    | Right-skewed               | Waiting times, time between events                          | Memoryless property                 |
| **Poisson**        | Discrete                   | Number of events in a fixed interval (calls, accidents)     | Rare events                         |

### General Process of Fitting a Distribution

1. Collect and clean the data  
2. Visualize (histogram / density plot)  
3. Candidate distributions based on domain knowledge  
4. Check fit using **Q-Q plot** and formal tests (KS, Anderson-Darling)  
5. Select the best distribution  
6. Use its CDF/PDF to answer probability questions  


### Key Takeaway

> Choosing the right distribution is often more powerful than forcing everything into a Normal distribution.  
> For extreme events (floods, maximum rainfall, system failures), distributions like **Weibull** or **Pareto** are usually much more appropriate than the Gaussian.

### Summary

> A good distributional model allows us to answer practical questions such as:
> - How large should a dam be?
> - What is the probability of an extreme event?
> - How much inventory should we keep?

Even if we have limited data, a well-fitted theoretical distribution gives us a powerful way to reason about rare events.

## 19. Covariance

We have two variables:
- $X$: Heights
- $Y$: Weights

Sample data:

| Sample | Height ($X$) | Weight ($Y$) |
|--------|--------------|--------------|
| $s_1$  | 160          | 62           |
| $s_2$  | 150          | 54           |
| $\vdots$ | $\vdots$   | $\vdots$     |
| $s_n$  | 190          | 48           |

**Question:** What is the relationship between $X$ and $Y$?

- Does $X \uparrow$ imply $Y \uparrow$?
- Does $X \uparrow$ imply $Y \downarrow$?
- Or is there no clear relationship?

To answer this, we use:
1. **Covariance**
2. **Pearson Correlation Coefficient**
3. **Spearman Rank Correlation Coefficient**

### Covariance Formula

$$
\text{Cov}(X, Y) = \dfrac{1}{n} \sum_{i=1}^{n} (x_i - \mu_x)(y_i - \mu_y)
$$

Where:
- $\mu_x$ = mean of $X$
- $\mu_y$ = mean of $Y$

**Variance** is a special case of covariance:

$$
\text{Var}(X) = \dfrac{1}{n} \sum_{i=1}^{n} (x_i - \mu_x)^2 = \text{Cov}(X, X)
$$


### Sign of Covariance

| Covariance Value       | Interpretation                          |
|------------------------|-----------------------------------------|
| $\text{Cov}(X,Y) > 0$  | Positive relationship ($X \uparrow$, $Y \uparrow$) |
| $\text{Cov}(X,Y) < 0$  | Negative relationship ($X \uparrow$, $Y \downarrow$) |
| $\text{Cov}(X,Y) = 0$  | No linear relationship                  |


### Visual Understanding (Scatter Plots)

![COV](./assets/19.%20covariance.jpg)

**1. Negative Covariance** ($\text{Cov}(X,Y) < 0$)

- As $X$ increases, $Y$ tends to decrease.
- Points form a downward trend.

**2. Zero Covariance** ($\text{Cov}(X,Y) = 0$)

- No clear upward or downward trend.
- Points are scattered randomly.

**3. Positive Covariance** ($\text{Cov}(X,Y) > 0$)

- As $X$ increases, $Y$ tends to increase.
- Points form an upward trend.

### Understanding the Sign using Deviations

We look at each point relative to the means $(\mu_x, \mu_y)$:

| Point Position relative to means | $(x_i - \mu_x)$ | $(y_i - \mu_y)$ | Product | Contribution to Cov |
|----------------------------------|------------------|------------------|---------|---------------------|
| Both above mean                  | $+$              | $+$              | $+$     | Positive            |
| $X$ above, $Y$ below             | $+$              | $-$              | $-$     | Negative            |
| $X$ below, $Y$ above             | $-$              | $+$              | $-$     | Negative            |
| Both below mean                  | $-$              | $-$              | $+$     | Positive            |

- If most products are **positive** → $\text{Cov}(X,Y) > 0$
- If most products are **negative** → $\text{Cov}(X,Y) < 0$

### Important Notes

- Covariance tells us the **direction** of the linear relationship (positive / negative / zero).
- Covariance does **not** tell us the **strength** of the relationship (because it depends on the scale of the variables).
- That is why we later use the **Pearson Correlation Coefficient**, which is a normalized version of covariance.

$$
\text{Cov}(X,Y) \neq \text{Correlation}(X,Y)
$$

### Summary

| Concept              | Meaning                                      |
|----------------------|----------------------------------------------|
| $\text{Cov}(X,Y) > 0$ | $X$ and $Y$ move in the same direction      |
| $\text{Cov}(X,Y) < 0$ | $X$ and $Y$ move in opposite directions     |
| $\text{Cov}(X,Y) = 0$ | No linear relationship                       |
| $\text{Cov}(X,X)$    | Equals $\text{Var}(X)$                       |

> Covariance is the foundation for understanding correlation.

## 20. Pearson Correlation Coefficient

### Definition



The **Pearson Correlation Coefficient** (also called Pearson’s $r$ or PCC) measures both the **strength** and **direction** of the linear relationship between two variables $X$ and $Y$.



$$

\rho_{X,Y} = \dfrac{\text{Cov}(X,Y)}{\sigma_X \, \sigma_Y}

$$



Where:

- $\text{Cov}(X,Y)$ = Covariance between $X$ and $Y$

- $\sigma_X = \sqrt{\text{Var}(X)}$ = Standard deviation of $X$

- $\sigma_Y = \sqrt{\text{Var}(Y)}$ = Standard deviation of $Y$

### Range of Pearson Correlation

![PCC](./assets/20.%20PCC.jpg)

$$
-1 \leq \rho_{X,Y} \leq +1
$$

| Value of $\rho$ | Interpretation                       |
| --------------- | ------------------------------------ |
| $\rho = +1$     | Perfect positive linear relationship |
| $0 < \rho < +1$ | Positive linear relationship         |
| $\rho = 0$      | No linear relationship               |
| $-1 < \rho < 0$ | Negative linear relationship         |
| $\rho = -1$     | Perfect negative linear relationship |

**Observations from the Pearson Correlation Coefficient (PCC)**

- The five panels show the relationship between two variables for different values of the Pearson correlation coefficient $\rho$.

- **$\rho = -1$**  
  Perfect negative linear relationship. All points lie exactly on a straight line with negative slope.

- **$-1 < \rho < 0$**  
  Negative linear relationship (but not perfect). As one variable increases, the other tends to decrease. The points are scattered around a downward-sloping line.

- **$\rho = 0$**  
  No linear relationship. The points are scattered randomly with no clear upward or downward trend.

- **$0 < \rho < +1$**  
  Positive linear relationship (but not perfect). As one variable increases, the other tends to increase. The points are scattered around an upward-sloping line.

- **$\rho = +1$**  
  Perfect positive linear relationship. All points lie exactly on a straight line with positive slope.

**Key Takeaways**

- $\rho$ only measures **linear** association.
- The closer $|\rho|$ is to 1, the stronger the linear relationship.
- $\rho = 0$ does **not** mean the variables are independent — it only means there is no *linear* correlation (they could still have a non-linear relationship).
- The sign of $\rho$ tells the direction (positive or negative), while the magnitude tells the strength.

### Why do we need Correlation if we already have Covariance?

- **Covariance** depends on the scale of the variables (e.g., height in cm vs meters changes the value).
- **Pearson Correlation** is **scale-invariant** (normalized version of covariance).
- Correlation is easier to interpret because it is always between $-1$ and $+1$.

![OBS](./assets/20.%20PCC-obs.jpg)

**Observations from the Pearson Correlation Coefficient (PCC) examples**

> ### 1st Row – Different strengths of linear correlation
- **$\rho = 1$**: Perfect positive linear relationship (all points lie on a straight line with positive slope).
- **$\rho = 0.8$**: Strong positive linear relationship (points tightly clustered around an upward line).
- **$\rho = 0.4$**: Moderate positive linear relationship (clear upward trend but with more scatter).
- **$\rho = 0$**: No linear relationship (cloud of points with no clear trend).
- **$\rho = -0.4$**: Moderate negative linear relationship.
- **$\rho = -0.8$**: Strong negative linear relationship.
- **$\rho = -1$**: Perfect negative linear relationship.

> ### 2nd Row – Effect of slope and perfect correlation
- Even when the slope is very small or the line is almost horizontal, as long as the points lie exactly on a straight line, $|\rho| = 1$.
- Pearson correlation measures the **strength of the linear relationship**, not the steepness of the slope.

> ### 3rd Row – Important limitation of Pearson correlation
- All these plots have **$\rho = 0$** (or very close to zero).
- However, the variables are clearly related through **non-linear** patterns:
  - Wavy / sinusoidal relationship
  - Random-looking but structured cloud
  - Diamond / square shapes
  - U-shaped (quadratic) relationship
  - X-shaped relationship
  - Circular relationship
  - Separate clusters

**Key Takeaways**

- Pearson correlation only detects **linear** associations.
- $\rho = 0$ does **not** mean the two variables are independent — it only means there is no linear correlation.
- Strong non-linear relationships can easily produce a Pearson correlation of zero.
- Always visualize the data (scatter plots) in addition to looking at the correlation value.

### Summary

| Concept                      | What it tells us                                  | Range                |
| ---------------------------- | ------------------------------------------------- | -------------------- |
| Covariance                   | Direction of linear relationship                  | $(-\infty, +\infty)$ |
| Pearson Correlation ($\rho$) | Direction **and** strength of linear relationship | $[-1, +1]$           |

> Pearson Correlation is one of the most widely used measures to quantify the linear association between two continuous variables.

## 21. Spearman Rank Correlation Coefficient

### Why do we need Spearman Correlation?

- **Pearson Correlation ($\rho$)** only measures **linear** relationships.
- If the relationship is strong but **non-linear** (e.g., curved), Pearson correlation may be low.
- **Spearman Rank Correlation ($r_s$)** measures the strength of a **monotonic** relationship (whether linear or not).

### How Spearman Correlation Works

Instead of using the original values, we convert both variables into **ranks**.

**Example:**

| Sample | $X$ (Height) | $Y$ (Weight) | Rank of $X$ ($r_x$) | Rank of $Y$ ($r_y$) |
|--------|--------------|--------------|---------------------|---------------------|
| $s_1$  | 160          | 52           | 4                   | 3                   |
| $s_2$  | 150          | 66           | 2                   | 4                   |
| $s_3$  | 170          | 68           | 5                   | 5                   |
| $s_4$  | 140          | 46           | 1                   | 1                   |
| $s_5$  | 158          | 51           | 3                   | 2                   |

- $r_x =$ rank of $X$ (ascending order)
- $r_y =$ rank of $Y$ (ascending order)

Then we compute the **Pearson correlation on the ranks**:

$$
\rho_{X,Y} = \dfrac{\text{Cov}(X,Y)}{\sigma_X \, \sigma_Y}
$$

$$
r_s = \rho_{r_x, r_y}
$$

$$
r_s = \dfrac{\text{Cov}(r_x,\ r_y)}{\sigma_{r_x} \, \sigma_{r_y}}
$$

> $r_x$ = ranks of $X$ & $r_y$ = ranks of $Y$


### Interpretation

| Spearman $r_s$ | Meaning                                      |
|----------------|----------------------------------------------|
| $r_s = +1$     | Perfect monotonic increasing relationship    |
| $r_s = -1$     | Perfect monotonic decreasing relationship    |
| $r_s \approx 0$| No monotonic relationship                    |

**Important Difference from Pearson:**

- Pearson $\rho = +1$ **only** if the relationship is perfectly linear.
- Spearman $r_s = +1$ if the relationship is perfectly monotonic (can be curved).

### Visual Examples

**Example 1: Perfect Monotonic (but non-linear)**

![Spearman = 1, Pearson = 0.88](./assets/21.%20SRCC-01.jpg)

- Clear increasing curved relationship.
- Spearman correlation = **1** (perfect monotonic)
- Pearson correlation = **0.88** (not perfect because it is not linear)

**Example 2: Weak Relationship**

![Spearman = 0.35, Pearson = 0.37](./assets/21.%20SRCC-02.jpg)

- Points are widely scattered.
- Both Spearman and Pearson give low values (around 0.35–0.37).

**Example 3: Strong Monotonic with some outliers**

![Spearman = 0.84, Pearson = 0.67](./assets/21.%20SRCC-03.jpg)

- Clear increasing trend but with some outliers on the right.
- Spearman (0.84) is higher than Pearson (0.67) because ranks are less affected by extreme values.

### Summary Comparison

| Feature                      | Pearson Correlation ($\rho$)      | Spearman Rank Correlation ($r_s$) |
|-----------------------------|-----------------------------------|-----------------------------------|
| Measures                    | Linear relationship               | Monotonic relationship            |
| Uses                        | Original values                   | Ranks of the values               |
| Sensitive to outliers       | Yes                               | Less sensitive                    |
| Perfect score (+1 or -1)    | Only if perfectly linear          | If perfectly monotonic (linear or curved) |
| Best used when              | Relationship is linear            | Relationship may be non-linear    |

> **Key Takeaway**:  
> Use **Pearson** when you expect a linear relationship.  
> Use **Spearman** when the relationship is monotonic but possibly non-linear, or when the data has outliers.

## 22. Correlation vs Causation

### Key Principle

> **Correlation does not mean/imply Causation**

Just because two variables are correlated does **not** mean that one causes the other.

### What Correlation Tells Us

- We can calculate the correlation between **any** two random variables $X$ and $Y$.
- A high correlation (positive or negative) only means that the two variables move together (or in opposite directions) in a linear way.
- It does **not** tell us anything about cause-and-effect.


### What Correlation Does *Not* Tell Us

- It does **not** mean $X$ causes $Y$
- It does **not** mean $Y$ causes $X$
- It does **not** mean there is a direct causal relationship

There could be:
- A third variable influencing both (confounding variable)
- Pure coincidence
- Reverse causation

### Causal Models

To claim that **$X$ causes $Y$**, we need more than just correlation. We need:

- Proper experimental design (e.g., randomized controlled trials)
- Causal inference techniques
- Domain knowledge
- Causal models / graphical models (e.g., Causal Graphs, do-calculus, etc.)

### Summary

| Concept              | What it means                              | Does it prove cause? |
|----------------------|--------------------------------------------|----------------------|
| Correlation          | Variables move together (or oppositely)    | No                   |
| Causation            | One variable directly influences the other | Needs stronger evidence |

> Always remember:  
> **Correlation ≠ Causation**

## 23. How to Use Correlations

### Applications of Correlation (Reminder: Correlation ≠ Causation)

We can calculate the **Pearson Correlation Coefficient (PCC)** between many pairs of variables.  
However, a strong correlation does **not** mean one variable causes the other.

---

### Practical Examples of Using Correlation

#### 1. Salary vs Square Footage of House
- Is a person’s salary correlated with the size (sq. ft.) of their home?
- Useful for real estate pricing models, affordability studies, etc.

#### 2. Years of Education vs Income
- Is the number of years of education correlated with income?
- Commonly studied in economics and sociology.

#### 3. E-commerce: Time Spent on Website vs Money Spent

| Time Spent on Site | Money Spent     |
|--------------------|-----------------|
| 29 hrs             | $20             |
| 30 min             | $100            |
| 60 min             | …               |

- Question: Is time spent on the website correlated with money spent in the next 24 hours?
- Useful for marketing, recommendation systems, and user behavior analysis.

#### 4. E-commerce: Number of Unique Visitors vs Sales

| Unique Visitors (per day) | Sales (per day) |
|---------------------------|-----------------|
| 100k                      | $1M             |
| 120k                      | $1.6M           |
| …                         | …               |

- Helps in forecasting revenue and understanding traffic-to-sales conversion.

#### 5. Medicine / Healthcare

| Dose of a Drug (mg) | Reduction in Blood Sugar |
|---------------------|---------------------------|
| 1 mg                | $x$                       |
| 2 mg                | $y$                       |
| 3 mg                | $z$                       |
| …                   | …                         |

- Is the dose of a medicine correlated with the reduction in blood sugar (or any health metric)?
- Important for dosage optimization and clinical studies.

### Important Reminder

Even if we find a strong correlation in any of the above examples:

- It does **not** automatically mean causation.
- There may be confounding factors.
- Proper causal analysis or controlled experiments are needed to claim cause-and-effect.

### Summary

| Domain          | Example of Correlation Use                          |
|-----------------|-----------------------------------------------------|
| Real Estate     | Salary ↔ House size                                 |
| Education       | Years of education ↔ Income                         |
| E-commerce      | Time on site ↔ Money spent                          |
| E-commerce      | Unique visitors ↔ Daily sales                       |
| Healthcare      | Drug dose ↔ Reduction in blood sugar / symptoms     |

> Correlation is a powerful exploratory tool, but it should always be interpreted with caution.

## 24. Confidence Interval Introduction

### What is a Confidence Interval?

A **Confidence Interval** gives a range of values within which we expect the true population parameter to lie, with a certain level of confidence.

### Example: Estimating Average Height

We want to estimate the **population mean height** ($\mu$) of people.

We take a **random sample** of size $n = 10$:

$$
\{x_1, x_2, \dots, x_{10}\}
$$

Example sample (heights in cm):

$$
\{180,\ 162,\ 158,\ 172,\ 168,\ 150,\ 171,\ 173,\ 165,\ 176\}
$$

### Point Estimate

The sample mean is used as a **point estimate** of the population mean:

$$
\bar{x} = \dfrac{1}{n} \sum_{i=1}^{n} x_i = 168.5\,\text{cm}
$$

So,

$$
\mu \approx \bar{x} = 168.5\,\text{cm}
$$

As the sample size $n$ increases, $\bar{x}$ gets closer to $\mu$.

### Confidence Interval

Instead of giving only a single number (point estimate), we give an **interval**:

$$
\mu \in [162.1,\ 174.9]
\quad \text{with } 95\% \text{ confidence}
$$

**Interpretation:**

> We are 95% confident that the true population mean height $\mu$ lies between 162.1 cm and 174.9 cm.

### Key Terms

| Term                  | Meaning                                          |
|-----------------------|--------------------------------------------------|
| Point Estimate        | Single best guess ($\bar{x}$)                    |
| Confidence Interval   | Range of plausible values for the parameter      |
| Confidence Level      | Probability that the interval contains the true parameter (e.g., 95%) |

### Summary

- A **point estimate** gives one number.
- A **confidence interval** gives a range and tells us how confident we are that the true parameter lies inside that range.
- Larger sample size → usually narrower (more precise) confidence interval.

## 25. Computing Confidence Interval Given the Underlying Distribution


### Setup

Assume the population follows a Normal distribution:

$$
X \sim \mathcal{N}(\mu, \sigma^2)
$$

Given:
- $\mu = 168$ cm (true mean — for illustration)
- $\sigma = 5$ cm

### Using the 68-95-99.7 Rule

For a Normal distribution:

| Interval                      | Probability |
|-------------------------------|-------------|
| $\mu \pm 1\sigma$             | $\approx 68\%$ |
| $\mu \pm 2\sigma$             | $\approx 95\%$ |
| $\mu \pm 3\sigma$             | $\approx 99.7\%$ |

![CI](./assets/25.%20CI-01.jpg)

**Example (95% interval):**

![CI](./assets/25.%20CI-02.jpg)

$$
\mu \pm 2\sigma = 168 \pm 2 \times 5 = 168 \pm 10
$$

$$
[158,\ 178]
$$

We can say:

> Approximately 95% of people’s heights lie between 158 cm and 178 cm.

### Confidence Interval Interpretation

If we want a **95% Confidence Interval** for the population mean (when we know $\sigma$):

$$
\left[ \bar{x} - 1.96 \cdot \dfrac{\sigma}{\sqrt{n}},\ 
\bar{x} + 1.96 \cdot \dfrac{\sigma}{\sqrt{n}} \right]
$$

(Using the more precise $z = 1.96$ instead of 2)

### Different Confidence Levels

| Confidence Level | $z$-value (approx) | Interval Width      | Interpretation                          |
|------------------|--------------------|---------------------|-----------------------------------------|
| 90%              | 1.645              | Narrower            | Less confident, smaller range           |
| 95%              | 1.96               | Medium              | Standard choice                         |
| 99%              | 2.58               | Wider               | More confident, larger range            |

**Trade-off:**
- Higher confidence level → wider interval
- Lower confidence level → narrower interval

### Key Visual Understanding

- The area under the Normal curve between the lower and upper limits equals the confidence level (e.g., 0.95 for 95% CI).
- The remaining probability is split equally in the two tails:
  - For 95% CI → 2.5% in each tail
  - For 90% CI → 5% in each tail

![CI](./assets/25.%20CI-03.jpg)

### Summary

- When the population is Normal and $\sigma$ is known, we can construct exact confidence intervals using $z$-values.
- 95% is the most commonly used confidence level.
- There is always a trade-off between **confidence** and **precision** (width of the interval).

## 26. Confidence Interval for the Mean of a Normal Random Variable

### Setup

We have a random variable $X$ with:
- Population mean $\mu$
- Population standard deviation $\sigma$

We take a random sample of size $n$:

$$
\{x_1, x_2, \dots, x_n\}
$$

Example sample (heights in cm, $n=10$):

$$
\{180,\ 162,\ 158,\ 172,\ 168,\ 150,\ 171,\ 173,\ 165,\ 176\}
$$

Sample mean:

$$
\bar{x} = 168.5\,\text{cm}
$$

**Goal:** Construct a 95% Confidence Interval for the population mean $\mu$.

### Case 1: Population Standard Deviation $\sigma$ is Known

**Assumption:** Someone tells us $\sigma = 5$ cm.

By the **Central Limit Theorem** (or exact Normality if the population is Normal):

$$
\bar{x} \sim \mathcal{N}\left(\mu,\ \dfrac{\sigma}{\sqrt{n}}\right)
$$

**95% Confidence Interval:**

$$
\mu \in \left[ \bar{x} - 1.96 \cdot \dfrac{\sigma}{\sqrt{n}},\ 
\bar{x} + 1.96 \cdot \dfrac{\sigma}{\sqrt{n}} \right]
$$

(Using $z_{0.025} \approx 1.96$; sometimes approximated as 2)

**Calculation:**

$$
\dfrac{\sigma}{\sqrt{n}} = \dfrac{5}{\sqrt{10}} \approx 1.58
$$

$$
\mu \in \left[ 168.5 - 1.96 \times 1.58,\ 
168.5 + 1.96 \times 1.58 \right]
$$

$$
\mu \in [165.39,\ 171.61]\,\text{cm}
\quad \text{with 95% confidence}
$$

### Case 2: Population Standard Deviation $\sigma$ is Unknown

In most real situations, we do **not** know $\sigma$.

We estimate it using the **sample standard deviation** $s$, and use the **Student’s t-distribution**.

$$
\bar{x} \sim t_{(n-1)}
$$

- Degrees of freedom = $n - 1$

**95% Confidence Interval (σ unknown):**

$$
\mu \in \left[ \bar{x} - t_{n-1,\ 0.025} \cdot \dfrac{s}{\sqrt{n}},\ 
\bar{x} + t_{n-1,\ 0.025} \cdot \dfrac{s}{\sqrt{n}} \right]
$$

![CI](./assets//26.%20CI-01.jpg)
![CI](./assets//26.%20CI-02.jpg)

https://en.wikipedia.org/wiki/Student%27s_t-distribution

### Summary of the Two Cases

| Situation                     | Distribution Used       | Critical Value      | Formula |
|-------------------------------|--------------------------|---------------------|---------|
| $\sigma$ **known**            | Standard Normal ($z$)    | $z_{0.025} \approx 1.96$ | $\bar{x} \pm z \cdot \dfrac{\sigma}{\sqrt{n}}$ |
| $\sigma$ **unknown**          | Student’s $t$            | $t_{n-1,\ 0.025}$   | $\bar{x} \pm t \cdot \dfrac{s}{\sqrt{n}}$ |

### Additional Notes

- When $n$ is large (usually $n \geq 30$), the $t$-distribution becomes very close to the Normal distribution.
- We can also construct confidence intervals for other parameters (e.g., median, 90th percentile, variance), but the method changes depending on the parameter.

### Key Takeaway

- If $\sigma$ is known → use **$z$-interval** (Normal).
- If $\sigma$ is unknown → use **$t$-interval** (Student’s t-distribution with $n-1$ degrees of freedom).


## 27. Confidence Interval Using Bootstrapping

### CI using Empirical Bootstrap

The empirical bootstrap allows us to construct confidence intervals for many statistics (median, variance, standard deviation, 90th percentile, etc.) **without making distributional assumptions**.

### Setup

Let $ X \sim F $.  
**Task:** Estimate a **95% CI** for the median of $ X $.

We observe a sample of size $ n = 10 $:

$$
S = \{x_1, x_2, x_3, \dots, x_n\}
$$

**Question:** Using *only* this sample, how can we obtain a CI for the median of $ X $?

### Bootstrap Procedure (Sampling with Replacement)

We generate new samples (bootstrap samples) from the original sample by **sampling with replacement**.

- Draw a uniform random index $ U(1,n) $
- Use that index to pick an observation from $ S $
- Repeat until we have a new sample of size $ n $

This produces bootstrap samples $ S_1, S_2, \dots, S_K $.

**Original Sample**  
$ S = \{x_1, x_2, \dots, x_n\} $

↓ Sampling with replacement using $ U(1,n) $

**Bootstrap Samples**  
$ S_1, S_2, \dots, S_K $

↓ Compute median of each

**Bootstrap Medians**  
$ m_1, m_2, \dots, m_K $

### Detailed Steps

$$
\begin{align*}
S_1 &: x_1^{(1)}, x_2^{(1)}, \dots, x_n^{(1)} \quad \rightarrow \quad m_1 \\
S_2 &: x_1^{(2)}, x_2^{(2)}, \dots, x_n^{(2)} \quad \rightarrow \quad m_2 \\
&\vdots \\
S_K &: x_1^{(K)}, x_2^{(K)}, \dots, x_n^{(K)} \quad \rightarrow \quad m_K
\end{align*}
$$

When $ K = 1000 $, we obtain 1000 bootstrap medians:

$$
m_1, m_2, m_3, \dots, m_{1000}
$$

### Constructing the 95% Confidence Interval

1. **Sort** the bootstrap medians in increasing order:

$$
m_1' \le m_2' \le m_3' \le \dots \le m_{1000}'
$$

2. The **95% CI** is given by the 2.5th and 97.5th percentiles of this ordered list:


For $K = 1000$:

$$
95\% \text{ CI for the median of } X = [m'_{25},\ m'_{975}]
$$

(i.e., the 25th and 975th ordered values)


### Key Properties

<div class="insight-item">
  <strong>Non-parametric technique</strong><br>
  Does <em>not</em> make any assumption about the distribution of the data.
</div>

<div class="insight-item">
  <strong>Versatility</strong><br>
  The same procedure works for variance, standard deviation, percentiles, or any other statistic — simply replace the median with the desired quantity.
</div>

## Code

```py
import numpy
from pandas import read_csv
from sklearn.utils import resample
from sklearn.metrics import accuracy_score
from matplotlib import pyplot

# load dataset
x = numpy.array([180,162,158,172,168,150,171,183,165,176])

# configure bootstrap
n_iterations = 1000
n_size = int(len(x))

# run bootstrap
medians = list()
for i in range(n_iterations):
    # prepare train and test sets
    s = resample(x, n_samples=n_size);
    m = numpy.median(s);
    #print(m)
    medians.append(m)

# plot scores
pyplot.hist(medians)
pyplot.show()

# confidence intervals
alpha = 0.95
p = ((1.0-alpha)/2.0) * 100
lower =  numpy.percentile(medians, p)

p = (alpha+((1.0-alpha)/2.0)) * 100
upper =  numpy.percentile(medians, p)
print('%.1f confidence interval %.1f and %.1f' % (alpha*100, lower, upper))
```

### Summary of the Method

| Step | Action |
|------|--------|
| 1 | Start with original sample $ S $ of size $ n $ |
| 2 | Generate $ K $ bootstrap samples by sampling **with replacement** |
| 3 | Compute the statistic (e.g., median) on each bootstrap sample |
| 4 | Sort the $ K $ bootstrap statistics |
| 5 | Take the appropriate percentiles (e.g., 2.5% and 97.5%) as the CI bounds |

> **Note:** This is the **percentile bootstrap** method (empirical bootstrap). It is simple, widely used, and distribution-free .

## 28. Hypothesis Testing Methodology

### Motivating Question

Is there a difference in the heights of students in Class 1 and Class 2?

| Class 1 | Class 2 |
|---------|---------|
| 150     | 162     |
| 152     | 156     |
| ...     | ...     |
| 193     | 182     |
| (50 students) | (50 students) |

We want to test whether the population means are different:

- $\mu_1$ = mean height of Class 1  
- $\mu_2$ = mean height of Class 2  

### Steps in Hypothesis Testing

#### 1. Choose a Test Statistic

$$
x = \mu_2 - \mu_1
$$

(or more commonly the difference of sample means $\bar{x}_2 - \bar{x}_1$)

#### 2. State the Hypotheses

- **Null Hypothesis ($H_0$)**: There is **no difference** between the two means.  
  $$
  H_0: \mu_1 = \mu_2 \quad \text{or} \quad \mu_2 - \mu_1 = 0
  $$

- **Alternative Hypothesis ($H_1$)**: There **is a difference** between the two means.  
  $$
  H_1: \mu_1 \neq \mu_2
  $$

This is an example of **proof by contradiction** style reasoning:
- Assume $H_0$ is true
- See how unusual the observed data is under that assumption

#### 3. Compute the p-value

The **p-value** is the probability of observing a test statistic as extreme as (or more extreme than) the one we got, **assuming the null hypothesis is true**.

Example:
- Suppose we observed a difference of 10 cm.
- If p-value = 0.9 → There is a 90% chance of seeing a 10 cm difference (or larger) even if $H_0$ is true → **not surprising** → Accept $H_0$
- If p-value = 0.05 → Only 5% chance of seeing such a difference if $H_0$ is true → **surprising** → Reject $H_0$

### Decision Rule

| p-value          | Interpretation                              | Decision              |
|------------------|---------------------------------------------|-----------------------|
| High (close to 1)| Data is consistent with $H_0$               | Fail to reject $H_0$  |
| Low (close to 0) | Data is unlikely under $H_0$                | Reject $H_0$          |
| Common threshold | $\alpha = 0.05$ (5%)                        | Reject $H_0$ if p < 0.05 |

### Summary

| Step | Action |
|------|--------|
| 1    | Choose a suitable test statistic |
| 2    | Define Null Hypothesis ($H_0$) and Alternative Hypothesis ($H_1$) |
| 3    | Calculate the p-value |
| 4    | Compare p-value with significance level ($\alpha$) and make a decision |

> **Key Idea**: We assume the null hypothesis is true and ask:  
> “How surprising is the data we observed?”  
> If it is very surprising (low p-value), we reject the null hypothesis.

## 29. Hypothesis Testing Intuition with a Coin Toss

### Problem

We are given a coin and want to determine whether it is **biased** or **fair**.

- Fair coin: $P(H) = 0.5$
- Biased towards Heads: $P(H) > 0.5$

### Experiment Design

**Experiment:** Flip the coin 5 times and count the number of Heads.

- Let $X$ = Number of Heads
- $X$ is a random variable (Binomial)

We perform the experiment and observe:

$$
X = 5 \quad \text{(all 5 flips are Heads)}
$$

### Hypotheses

- **Null Hypothesis ($H_0$)**: The coin is fair  
  $$
  H_0: P(H) = 0.5
  $$

- **Alternative Hypothesis ($H_1$)**: The coin is biased towards Heads  
  $$
  H_1: P(H) > 0.5
  $$

### Calculating the p-value

Under the assumption that $H_0$ is true (fair coin):

$$
P(X = 5 \mid H_0) = \left(\dfrac{1}{2}\right)^5 = \dfrac{1}{32} \approx 0.031 = 3.1\%
$$

This is the **p-value**.

**Interpretation:**
> If the coin is fair, there is only a **3.1% chance** of getting 5 Heads in 5 flips.

### Decision Rule (Rule of Thumb)

| p-value              | Decision                          | Conclusion                          |
|----------------------|-----------------------------------|-------------------------------------|
| p-value $< 5\%$      | Reject $H_0$                      | Accept $H_1$ (coin is biased)       |
| p-value $> 5\%$      | Fail to reject $H_0$              | Not enough evidence against fairness|

In this case:
- p-value ≈ 3.1% < 5%
- → **Reject $H_0$**
- → Conclude that the coin is **biased towards Heads**

### Important Notes

1. **Sample size matters**  
   - With only 3 flips, even getting 3 Heads gives:
     $$
     P(X=3 \mid H_0) = \dfrac{1}{8} = 12.5\% > 5\%
     $$
     → We would **not** reject $H_0$.

2. Hypothesis testing steps:
   1. Design the experiment
   2. Define Null Hypothesis ($H_0$) and Alternative Hypothesis ($H_1$)
   3. Choose a test statistic $X$ such that $P(\text{observation} \mid H_0)$ is easy to calculate
   4. Compute the p-value
   5. Make a decision based on a significance level (commonly 5%)

### Summary

| Concept              | Meaning in this example                          |
|----------------------|--------------------------------------------------|
| Null Hypothesis      | Coin is fair ($P(H)=0.5$)                        |
| Alternative          | Coin is biased towards Heads                     |
| Test Statistic       | Number of Heads in 5 flips                       |
| Observed value       | 5 Heads                                          |
| p-value              | 3.1%                                             |
| Decision             | Reject $H_0$ (coin appears biased)               |

> **Key Idea**: We assume the null hypothesis is true and ask how surprising the observed data is.  
> If it is sufficiently surprising (p-value < 5%), we reject the null hypothesis.

## 30. Resampling and Permutation Test

### Goal

We want to test whether there is a significant difference between the means of two groups (e.g., Class 1 and Class 2 heights).

- Observed difference:  
  $$
  \Delta = \bar{x}_{\text{Class 1}} - \bar{x}_{\text{Class 2}}
  $$

### Permutation Test (Resampling Approach)

**Idea:**  
Assume the Null Hypothesis $H_0$ is true (no real difference between the two groups).  
Then the group labels are meaningless, and we can randomly reassign the labels many times.

#### Steps:

1. **Pool** all the data from both classes (total 100 students).
2. **Randomly split** the 100 observations into two groups of 50 (this is sampling without replacement / permutation).
3. Compute the difference in means for this new random split:  
   $$
   \delta_i = \bar{x}_A - \bar{x}_B
   $$
4. Repeat this process many times (e.g., $K = 10,000$ times) to get:
   $$
   \delta_1, \delta_2, \dots, \delta_{10000}
   $$
5. Sort these differences.
6. See where the **original observed difference** $\Delta$ falls in this distribution.

### Calculating the p-value

- Count how many of the random differences $\delta_i$ are **as extreme as or more extreme than** the observed $\Delta$.
- 
$$
\text{p-value} = \dfrac{\text{Number of }\delta_i\text{ as extreme as }\Delta}{K}
$$

**Example interpretations:**
- p-value = 0.05 = 5%
- p-value = 0.02 = 2%
- p-value = 0.20 = 20%

### Decision Rule

| p-value     | Decision                          |
|-------------|-----------------------------------|
| p < 0.05    | Reject $H_0$ (significant difference) |
| p ≥ 0.05    | Fail to reject $H_0$              |

**Note:** The significance threshold (commonly 5%) can change depending on the domain. In some fields, 1% (0.01) is preferred.

### Connection to Normal Distribution (Pre-computing)

If the differences follow a Normal distribution approximately:

$$
\delta_i' \sim \mathcal{N}(0,1)
$$

Then we can compute the p-value using the tail probability of the Normal distribution (two-tailed test).

For example, if the standardized observed difference is 2:

$$
P(|Z| \ge 2) = 0.025 + 0.025 = 0.05
$$

### Key Advantages of Permutation Test

- It is a **non-parametric** method (does not assume the data follows a Normal distribution).
- It directly builds the null distribution by resampling.
- Very useful when sample sizes are small or distributional assumptions are doubtful.

### Summary

| Step | Action |
|------|--------|
| 1    | Compute observed difference $\Delta$ |
| 2    | Assume $H_0$ is true and randomly re-label the data many times |
| 3    | Compute difference for each random labeling |
| 4    | See how extreme the original $\Delta$ is among the random differences |
| 5    | Calculate p-value and make a decision |

> **Core Idea**: If the observed difference is very unusual even after randomly shuffling the labels thousands of times, then the difference is likely real (not due to chance).

## 31. Hypothesis Testing QA

### Setup

We have two classes:
- Class 1: 50 students
- Class 2: 50 students

We observe a difference in mean heights:

$$
\Delta = \bar{x}_2 - \bar{x}_1 = 10\,\text{cm}
$$

**Question:** Is this 10 cm difference real, or could it have happened just by chance?

### Step-by-step Reasoning

#### 1. What is the p-value here?

$$
\text{p-value} = P(X \ge 10\,\text{cm} \mid H_0)
$$

Where:
- $X$ = difference in means
- $H_0$: There is **no real difference** in the heights of the two classes

#### 2. Interpretation of p-value

- If p-value is **small** (e.g. 0.01 = 1% < 5%)  
  → Observing a 10 cm difference is very unlikely if $H_0$ is true  
  → We **reject** $H_0$

- If p-value is **large** (e.g. 0.20 = 20% > 5%)  
  → Observing a 10 cm difference is quite possible even if $H_0$ is true  
  → We **fail to reject** (accept) $H_0$

### How do we compute this p-value? (Permutation Test)

**Assume $H_0$ is true** (no real difference between classes).

1. Put all 100 students into one big pool.
2. Randomly split them into two groups of 50 (many times).
3. Each time, compute the difference in means:  
   $$
   \delta_1, \delta_2, \delta_3, \dots, \delta_{10000}
   $$
4. Sort these simulated differences.
5. Count how many of them are ≥ 10 cm.

**Example results:**

- Suppose 2000 out of 10,000 simulations gave difference ≥ 10 cm  
  $$
  \text{p-value} = \dfrac{2000}{10000} = 0.20 = 20\% > 5\%
  $$
  → **Accept $H_0$** (difference can easily happen by chance)

- Suppose only 100 out of 10,000 simulations gave difference ≥ 10 cm  
  $$
  \text{p-value} = \dfrac{100}{10000} = 0.01 = 1\% < 5\%
  $$
  → **Reject $H_0$** (difference is surprising under $H_0$)

### Key Insights

| Concept                        | Explanation |
|--------------------------------|-----------|
| Null Hypothesis ($H_0$)        | No real difference between the two classes |
| Test Statistic                 | Difference in means ($X = \bar{x}_2 - \bar{x}_1$) |
| p-value                        | Probability of seeing a difference as large as 10 cm **if $H_0$ is true** |
| Decision rule                  | Reject $H_0$ if p-value < 5% |
| Main challenge                 | Choosing a good $H_0$ that is easy to simulate |

### Summary

> We assume there is no real difference ($H_0$), randomly reshuffle the students many times, and see how often we get a difference as large as the one we actually observed.  
> If it rarely happens → the observed difference is significant → reject $H_0$.

## 32. K-S Test for Similarity of Two Distributions

### Goal

We have two samples:

- Sample 1: $X_1 = \{x_1, x_2, \dots, x_n\}$
- Sample 2: $X_2 = \{y_1, y_2, \dots, y_m\}$

**Question:** Do these two samples come from the **same distribution**?

![KS](./assets/32.%20KS.jpg)

$$
H_0: X_1 \text{ and } X_2 \text{ come from the same distribution}
$$

### Kolmogorov-Smirnov (KS) Test

The KS test compares the **Empirical Cumulative Distribution Functions (ECDFs)** of the two samples.

**Test Statistic:**

$$
D_{n,m} = \sup_x \left| F_{1,n}(x) - F_{2,m}(x) \right|
$$

Where:
- $F_{1,n}(x)$ = Empirical CDF of the first sample
- $F_{2,m}(x)$ = Empirical CDF of the second sample
- $D_{n,m}$ = Maximum vertical distance between the two ECDFs

### Decision Rule

We reject the null hypothesis $H_0$ if:

$$
D_{n,m} > c(\alpha) \sqrt{\dfrac{n+m}{n m}}
$$

Where $c(\alpha)$ depends on the significance level $\alpha$.

**Common values of $c(\alpha)$ with Significance Level $\alpha$ :**

| $\alpha$    | 0.10 | 0.05 | 0.025 | 0.01 | 0.005 | 0.001 |
| ----------- | ---: | ---: | ----: | ---: | ----: | ----: |
| $c(\alpha)$ | **1.22** | **1.36** |  **1.48** | **1.63** |  **1.73** |  ** ** |


**General formula:**

$$
c(\alpha) = \sqrt{-\dfrac{1}{2} \ln \alpha}
$$

### Examples

**Example 1:**  
$n = 1000$, $m = 5000$, $\alpha = 0.05$ → $c(\alpha) = 1.36$

$$
D_{n,m} > 1.36 \sqrt{\dfrac{1000+5000}{1000 \times 5000}} \approx 0.047
$$

If $D_{n,m} > 0.047$, reject $H_0$ at 5% significance level.

**Example 2:**  
$n = 50$, $m = 30$, $\alpha = 0.05$ → $c(\alpha) = 1.36$

$$
D_{n,m} > 1.36 \sqrt{\dfrac{50+30}{50 \times 30}} \approx 0.31
$$

If $D_{n,m} > 0.31$, reject $H_0$ at 5% significance level.

### Key Points

- The KS test is a **non-parametric** test (no assumption about the form of the distributions).
- It is sensitive to differences in both location and shape of the distributions.
- Larger sample sizes make the test more powerful (easier to detect small differences).
- The null hypothesis is rejected when the maximum difference between the two ECDFs is large.

### Summary

| Concept              | Description                                      |
|----------------------|--------------------------------------------------|
| Test                 | Two-sample Kolmogorov-Smirnov Test               |
| Null Hypothesis      | Both samples come from the same distribution     |
| Test Statistic       | $D_{n,m} = \sup |F_{1,n}(x) - F_{2,m}(x)|$     |
| Reject $H_0$ when    | $D_{n,m} > c(\alpha) \sqrt{\frac{n+m}{nm}}$     |
| Common $\alpha$      | 0.05 → $c(\alpha) = 1.36$                        |

> The KS test is one of the most widely used methods to check whether two samples come from the same underlying distribution.

## 33. K-S Test p-value

### Null Hypothesis

$$
H_0: X \text{ and } Y \text{ come from the same distribution}
$$

We reject $H_0$ at significance level $\alpha$ if:

$$
D_{n,m} > c(\alpha) \sqrt{\dfrac{n+m}{nm}}
$$

where

$$
c(\alpha) = \sqrt{-\dfrac{1}{2} \ln \alpha}
$$

### Deriving the Approximate p-value

Let $D = D_{n,m}$ (the observed KS statistic).

We reject $H_0$ when:

$$
D > c(\alpha) \sqrt{\dfrac{n+m}{nm}}
$$

Substitute $c(\alpha)$:

$$
D > \sqrt{-\dfrac{1}{2} \ln \alpha} \cdot \sqrt{\dfrac{n+m}{nm}}
$$

Square both sides:

$$
D^2 > \left(-\dfrac{1}{2} \ln \alpha\right) \cdot \dfrac{n+m}{nm}
$$

$$
D^2 \cdot \dfrac{nm}{n+m} > -\dfrac{1}{2} \ln \alpha
$$

Multiply both sides by $-2$:

$$
-2 D^2 \cdot \dfrac{nm}{n+m} < \ln \alpha
$$

Exponentiate both sides:

$$
\exp\left(-2 D^2 \cdot \dfrac{nm}{n+m}\right) < \alpha
$$

### Approximate p-value Formula

Since we reject $H_0$ when p-value $< \alpha$, we obtain the approximation:

$$
\text{p-value} \approx \exp\left(-2 D^2 \cdot \dfrac{nm}{n+m}\right)
$$

Where:
- $n$ = size of first sample
- $m$ = size of second sample
- $D$ = maximum difference between the two empirical CDFs

### Summary

| Quantity              | Formula / Meaning                                      |
|-----------------------|--------------------------------------------------------|
| Test Statistic        | $D_{n,m} = \sup |F_n(x) - G_m(x)|$                    |
| Critical value        | $c(\alpha)\sqrt{\frac{n+m}{nm}}$                       |
| $c(\alpha)$           | $\sqrt{-\frac{1}{2}\ln\alpha}$                         |
| Approximate p-value   | $\exp\left(-2D^2 \frac{nm}{n+m}\right)$                |

> This approximation is very useful in practice: once you compute the KS statistic $D$, you can quickly get an approximate p-value without looking up tables.

## 34. Code Snippet: K-S Test

```py
import numpy as np
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

#generate a gaussian r.v X
x = stats.norm.rvs(size=1000);
print(len(x),type(x))
sns.set_style('whitegrid')
sns.kdeplot(x, bw=0.5)
plt.show()

stats.kstest(x, 'norm')

# Y ~ Continous Uniform Distribution(0,1)
y = np.random.uniform(0,1,10000);
sns.kdeplot(np.array(y), bw=0.1)
plt.show()

# !pip3 install scipy==1.6.3
import scipy
np.__version__
scipy.__version__

stats.kstest(y, x)

```

## 35. Hypothesis Testing: Another Example

### Background

We previously saw the coin-toss example, which was easy to understand because $P(\text{observation} \mid H_0)$ was very simple to compute.

Now we look at a more practical example.

### Task

Determine whether the **population mean heights** of people in two cities are the same or different.

- City 1 population mean: $\mu_1$
- City 2 population mean: $\mu_2$

**Question:** Is $\mu_1 \approx \mu_2$ or are they different?

### Experiment

- Randomly sample 50 people from City 1 → heights $h_1, h_2, \dots, h_{50}$
- Randomly sample 50 people from City 2 → heights $h_1, h_2, \dots, h_{50}$

**Observed sample means:**

$$
\bar{x}_1 = 162\,\text{cm}, \quad \bar{x}_2 = 167\,\text{cm}
$$

**Test Statistic:**

$$
X = \bar{x}_2 - \bar{x}_1 = 5\,\text{cm}
$$

### Hypotheses

- **Null Hypothesis ($H_0$)**: There is **no difference** in the population mean heights.  
  $$
  H_0: \mu_1 = \mu_2
  $$

- **Alternative Hypothesis ($H_1$)**: There **is a difference**.

### p-value

We need to compute:

$$
P(X = 5\,\text{cm} \mid H_0)
$$

This is the probability of observing a difference of 5 cm (or more extreme) in sample means of size 50, **if there is truly no difference** in the population means.

### Two Possible Cases

#### Case 1: p-value is large

$$
P(X = 5 \mid H_0) = 0.20 = 20\% > 5\%
$$

- There is a 20% chance of seeing a 5 cm difference even if the population means are equal.
- This is **not surprising**.
- **Decision:** Accept $H_0$ (no strong evidence of a real difference).

#### Case 2: p-value is small

$$
P(X = 5 \mid H_0) = 0.03 = 3\% < 5\%
$$

- There is only a 3% chance of seeing a 5 cm difference if the population means are equal.
- This is **surprising**.
- **Decision:** Reject $H_0$ and accept $H_1$ (there is evidence of a real difference).

### Summary

| Step | Action |
|------|--------|
| 1    | Define the question (are the population means equal?) |
| 2    | Collect random samples and compute the observed difference |
| 3    | Set $H_0$: No difference in population means |
| 4    | Calculate $P(\text{observed difference} \mid H_0)$ |
| 5    | If p-value < 5% → Reject $H_0$ <br> If p-value > 5% → Accept $H_0$ |

> The key difficulty in real problems is computing $P(\text{observation} \mid H_0)$.  

> In the next sections we will see practical ways to calculate or approximate this probability (using CLT, t-distribution, or resampling).

## 36. Resampling and Permutation Test: Another Example

### Goal

We want to compute:

$$
P(X = 5\,\text{cm} \mid H_0)
$$

Where:
- $X = \bar{x}_2 - \bar{x}_1$ (difference in sample means)
- Observed difference = 5 cm
- $H_0$: There is **no difference** in the population mean heights of the two cities

### How to Compute the p-value using Resampling (Permutation Test)

**Assumption under $H_0$:**  
The two groups come from the same population → the city labels are meaningless.

#### Steps:

1. **Pool** all 100 height measurements (50 from City 1 + 50 from City 2).

2. **Randomly split** the 100 heights into two new groups of 50 (this simulates $H_0$).

3. Compute the difference in means for this random split:
   $$
   \delta = \bar{x}_A - \bar{x}_B
   $$

4. Repeat this process many times (e.g., 10,000 times) to get:
   $$
   \delta_1,\ \delta_2,\ \delta_3,\ \dots,\ \delta_{10000}
   $$

5. Count how many of these simulated differences are **as large as or larger than** the observed 5 cm.

### Interpreting the Results

#### Case 1: Large p-value

Suppose 20% of the simulated differences are ≥ 5 cm:

$$
P(X \ge 5 \mid H_0) = 0.20 = 20\% > 5\%
$$

- Seeing a 5 cm difference is quite common even when there is no real difference.
- **Decision:** Accept $H_0$

#### Case 2: Small p-value

Suppose only 3% of the simulated differences are ≥ 5 cm:

$$
P(X \ge 5 \mid H_0) = 0.03 = 3\% < 5\%
$$

- Seeing a 5 cm difference is rare if $H_0$ is true.
- **Decision:** Reject $H_0$ and conclude that the population means are different.

### Visual Summary of the Process

| Step | Action |
|------|--------|
| 1    | Pool all data (100 heights) |
| 2    | Randomly re-assign into two groups of 50 |
| 3    | Compute difference in means |
| 4    | Repeat thousands of times |
| 5    | See what fraction of simulations give difference ≥ observed difference (5 cm) |
| 6    | That fraction is the p-value |

### Key Takeaway

> By repeatedly randomly re-labeling the data under the assumption that $H_0$ is true, we build the distribution of the test statistic under the null.  
> The p-value is simply the proportion of random shuffles that produce a result as extreme as what we actually observed.

This is a powerful **non-parametric** method that does not require assuming normality.

## 37. How to Use Hypothesis Testing

### Connection to KS Test

The **Kolmogorov-Smirnov (KS) test** is itself a form of hypothesis testing.  
It checks whether two random variables come from the **same distribution** or not.

### Real-World Example: New Drug vs Existing Drug

**Situation:**
- Drug $D_1$ is already in the market. It reduces fever in **4 hours** on average.
- A new drug $D_2$ claims: “I reduce fever **faster** than $D_1$.”

**Experiment:**
- Give $D_1$ to 50 patients → Observed mean time $\bar{x}_1 = 4$ hours
- Give $D_2$ to 50 patients → Observed mean time $\bar{x}_2 = 2$ hours

**Observed difference:**
$$
X = \bar{x}_1 - \bar{x}_2 = 2 \text{ hours}
$$

### Hypothesis Testing Setup

- **Null Hypothesis ($H_0$)**: Both drugs take the same time to reduce fever (no real difference).
- **Alternative Hypothesis ($H_1$)**: $D_2$ is faster than $D_1$.
- **Test Statistic**: $X = \bar{x}_1 - \bar{x}_2$

### Pipeline: Resampling & Permutation Test

To compute the p-value $P(X \ge 2 \mid H_0)$, we use the following pipeline:

```text
┌─────────────────────────────────────────────────────┐
│  Step 1: Pool all the data                          │
│  Combine results of all 100 patients                │
│  (50 from D1 + 50 from D2)                          │
└──────────────────────┬──────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────┐
│  Step 2: Randomly split into two groups of 50       │
│                                                     │
│     ┌─────────────┐         ┌─────────────┐         │
│     │  Group A    │         │  Group B    │         │
│     │   (50)      │         │   (50)      │         │
│     └─────────────┘         └─────────────┘         │
└──────────────────────┬──────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────┐
│  Step 3: Compute difference in means                │
│  δ = mean(Group A) – mean(Group B)                  │
└──────────────────────┬──────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────┐
│  Step 4: Repeat Steps 2–3 many times (e.g. 10,000)  │
│  Obtain: δ₁, δ₂, δ₃, ..., δ₁₀₀₀₀                    │
└──────────────────────┬──────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────┐
│  Step 5: Calculate p-value                          │
│  p-value = (Number of δ ≥ 2 hours) / 10,000         │
└─────────────────────────────────────────────────────┘
```

### Decision Rule

| p-value          | Decision               | Conclusion                              |
|------------------|------------------------|-----------------------------------------|
| p-value < 0.05   | Reject $H_0$           | New drug $D_2$ is significantly faster  |
| p-value ≥ 0.05   | Fail to reject $H_0$   | Not enough evidence to support the claim|

### Significance Level ($\alpha$)

- Common choice: $\alpha = 0.05$ (5%)
- The more confident you want to be before rejecting $H_0$, the **smaller** you set $\alpha$.

### Summary of the Process

| Step | Action |
|------|--------|
| 1    | Define the practical question |
| 2    | Design a proper randomized experiment |
| 3    | Set $H_0$ (no difference) and $H_1$ |
| 4    | Choose a test statistic |
| 5    | Compute the p-value (using Permutation Test / KS Test, etc.) |
| 6    | Compare p-value with significance level and make a decision |

### Key Takeaway

> Hypothesis testing answers the question:  
> “If there was actually no difference, how often would we see a result as extreme as the one we observed just by chance?”

If that probability (p-value) is very small, we reject the null hypothesis and conclude that the observed difference is real.

![pipeline](./assets/37.%20pipeline.jpg)  
![pipeline](./assets/37.%20pipeline.png)

## 38. Proportional Sampling

### Problem

We have $n$ elements with associated weights (or scores):

$$
a = [a_1,\ a_2,\ a_3,\ a_4,\ a_5] = [2.0,\ 6.0,\ 1.2,\ 5.8,\ 20.0]
$$

**Task:**  
Pick one element such that the probability of selecting an element is **proportional** to its weight $a_i$.

(This is **not** uniform random sampling.)

### Step-by-Step Method

#### Step 1: Normalize the weights

1. Compute the total sum:
$$
S = \sum_{i=1}^{n} a_i = 2.0 + 6.0 + 1.2 + 5.8 + 20.0 = 35
$$

2. Normalize each weight:
$$
a_i' = \dfrac{a_i}{S}
$$

$$
\begin{align*}
a_1' &= 0.0571 \\
a_2' &= 0.1714 \\
a_3' &= 0.0343 \\
a_4' &= 0.1657 \\
a_5' &= 0.5714
\end{align*}
$$

(Note: $\sum a_i' = 1$)

#### Step 2: Compute Cumulative Sums

$$
\begin{align*}
\tilde{a}_1 &= a_1' = 0.0571 \\
\tilde{a}_2 &= \tilde{a}_1 + a_2' = 0.2285 \\
\tilde{a}_3 &= \tilde{a}_2 + a_3' = 0.2628 \\
\tilde{a}_4 &= \tilde{a}_3 + a_4' = 0.4285 \\
\tilde{a}_5 &= \tilde{a}_4 + a_5' = 1.0000
\end{align*}
$$

### Step 3: Sampling

1. Generate a random number $r$ from Uniform(0, 1):
$$
r \sim U(0,1)
$$

2. Find the smallest index $i$ such that:
$$
r \le \tilde{a}_i
$$

3. Return element $i$.

**Example:**
- If $r = 0.15$ → falls in the second interval → return element 2
- If $r = 0.50$ → falls in the fifth interval → return element 5

### Why This Works

The probability of selecting element $i$ is:

$$
P(\text{select } i) = \tilde{a}_i - \tilde{a}_{i-1} = a_i' = \dfrac{a_i}{S}
$$

Which is exactly proportional to the original weight $a_i$.

### Summary

| Step | Action |
|------|--------|
| 1    | Compute sum of all weights $S$ |
| 2    | Normalize: $a_i' = a_i / S$ |
| 3    | Compute cumulative sums $\tilde{a}_i$ |
| 4    | Sample $r \sim U(0,1)$ |
| 5    | Return the element corresponding to the interval where $r$ falls |

> This method is widely used in **Weighted Random Sampling**, **Roulette Wheel Selection** (Genetic Algorithms), and **Importance Sampling**.

## 39. Revision Questions

**Revision Questions**

1. [What is PDF?](#1-what-is-pdf)
2. [What is CDF?](#2-what-is-cdf)
3. [Explain about 1-std-dev, 2-std-dev, 3-std-dev range](#3-explain-about-1-std-dev-2-std-dev-3-std-dev-range)
4. [What is Symmetric distribution, Skewness and Kurtosis?](#4-what-is-symmetric-distribution-skewness-and-kurtosis)
5. [How to do Standard normal variate (Z) and standardization?](#5-how-to-do-standard-normal-variate-z-and-standardization)
6. [What is Kernel density estimation?](#6-what-is-kernel-density-estimation)
7. [Importance of Sampling distribution & Central Limit theorem](#7-importance-of-sampling-distribution--central-limit-theorem)
8. [Importance of Q-Q Plot: Is a given random variable Gaussian distributed?](#8-importance-of-q-q-plot-is-a-given-random-variable-gaussian-distributed)
9. [What is Uniform Distribution and random number generators?](#9-what-is-uniform-distribution-and-random-number-generators)
10. [What are Discrete and Continuous Uniform distributions?](#10-what-are-discrete-and-continuous-uniform-distributions)
11. [How to randomly sample data points?](#11-how-to-randomly-sample-data-points)
12. [Explain about Bernoulli and Binomial distribution](#12-explain-about-bernoulli-and-binomial-distribution)
13. [What is Log-normal and power law distribution?](#13-what-is-log-normal-and-power-law-distribution)
14. [What is Power-law & Pareto distributions: PDF, examples](#14-what-is-power-law--pareto-distributions-pdf-examples)
15. [Explain about Box-Cox / Power transform](#15-explain-about-box-cox--power-transform)
16. [What is Co-variance?](#16-what-is-co-variance)
17. [Importance of Pearson Correlation Coefficient](#17-importance-of-pearson-correlation-coefficient)
18. [Importance of Spearman Rank Correlation Coefficient](#18-importance-of-spearman-rank-correlation-coefficient)
19. [Correlation vs Causation?](#19-correlation-vs-causation)
20. [What is Confidence Intervals?](#20-what-is-confidence-intervals)
21. [Confidence Interval vs Point estimate?](#21-confidence-interval-vs-point-estimate)
22. [Explain about Hypothesis testing](#22-explain-about-hypothesis-testing)
23. [Define Hypothesis Testing methodology, Null-hypothesis, test-statistic, p-value](#23-define-hypothesis-testing-methodology-null-hypothesis-test-statistic-p-value)
24. [How to do K-S Test for similarity of two distributions?](#24-how-to-do-k-s-test-for-similarity-of-two-distributions)

#### 1. What is PDF?
PDF stands for **Probability Density Function**.  
For a continuous random variable $X$, the PDF $f(x)$ describes the relative likelihood of $X$ taking a particular value.  
Important properties:
- $f(x) \ge 0$ for all $x$
- $\int_{-\infty}^{\infty} f(x)\, dx = 1$
- $P(a \le X \le b) = \int_a^b f(x)\, dx$

#### 2. What is CDF?
CDF stands for **Cumulative Distribution Function**.  
It is defined as:
$$
F(x) = P(X \le x) = \int_{-\infty}^{x} f(t)\, dt
$$
Properties:
- $0 \le F(x) \le 1$
- Non-decreasing
- $\lim_{x \to -\infty} F(x) = 0$, $\lim_{x \to \infty} F(x) = 1$

#### 3. Explain about 1-std-dev, 2-std-dev, 3-std-dev range
This is the **Empirical Rule (68-95-99.7 Rule)** for a Normal distribution $X \sim \mathcal{N}(\mu, \sigma^2)$:

| Interval          | Approximate Probability |
| ----------------- | ----------------------- |
| $\mu \pm 1\sigma$ | ≈ 68.27%                |
| $\mu \pm 2\sigma$ | ≈ 95.45%                |
| $\mu \pm 3\sigma$ | ≈ 99.73%                |

#### 4. What is Symmetric distribution, Skewness and Kurtosis?
- **Symmetric distribution**: Left and right sides are mirror images (e.g., Normal). Mean = Median = Mode.  
- **Skewness**: Measures asymmetry.  
  - Positive skew → long right tail (Mean > Median)  
  - Negative skew → long left tail (Mean < Median)  
- **Kurtosis**: Measures tailedness / peakedness relative to Normal.  
  - Leptokurtic (Kurtosis > 0): heavy tails, sharp peak  
  - Mesokurtic (≈ 0): Normal  
  - Platykurtic (< 0): light tails, flat peak

#### 5. How to do Standard normal variate (Z) and standardization?
If $X \sim \mathcal{N}(\mu, \sigma^2)$, the standardized variable is:
$$
Z = \frac{X - \mu}{\sigma} \sim \mathcal{N}(0,1)
$$
This process is called **standardization**. It allows us to use the standard normal table / 68-95-99.7 rule for any normal variable.

#### 6. What is Kernel density estimation?
KDE is a **non-parametric** method to estimate the PDF of a continuous random variable from sample data.  
It places a smooth kernel (usually Gaussian) on each data point and sums them:
$$
\hat{f}(x) = \frac{1}{nh} \sum_{i=1}^{n} K\left(\frac{x - x_i}{h}\right)
$$
where $h$ is the bandwidth.

#### 7. Importance of Sampling distribution & Central Limit theorem
- The **sampling distribution** of the sample mean $\bar{x}$ is the distribution of $\bar{x}$ over many samples.  
- **Central Limit Theorem (CLT)**: For large $n$,
$$
\bar{x} \approx \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)
$$
even if the original population is not normal.  
This is the foundation of many inferential statistics techniques.

#### 8. Importance of Q-Q Plot: Is a given random variable Gaussian distributed?
A Q-Q plot compares the quantiles of the data against the quantiles of a theoretical Normal distribution.  
- If points lie approximately on a straight line → data is roughly Normal.  
- Systematic deviations → data is not Normal (skewed, heavy-tailed, etc.).

#### 9. What is Uniform Distribution and random number generators?
The Uniform distribution assigns equal probability to every value in an interval (continuous) or set (discrete).  
Most random number generators produce numbers that are approximately $\mathcal{U}[0,1]$.

#### 10. What are Discrete and Continuous Uniform distributions?
- **Discrete Uniform** $\mathcal{U}\{a,b\}$: equal probability $1/n$ on integers $a, a+1, \dots, b$.  
- **Continuous Uniform** $\mathcal{U}_{[a,b]}$: constant density $1/(b-a)$ on the interval $[a,b]$.

#### 11. How to randomly sample data points?
Using the Uniform distribution:  
- Discrete: `np.random.randint(a, b+1)` or `random.choice()`  
- Continuous: `np.random.uniform(a, b)`

#### 12. Explain about Bernoulli and Binomial distribution
- **Bernoulli**: Single trial with two outcomes (success/failure). $P(X=1)=p$, $P(X=0)=1-p$.  
- **Binomial**: Number of successes in $n$ independent Bernoulli trials.
$$
P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

#### 13. What is Log-normal and power law distribution?
- **Log-normal**: If $\log X \sim \mathcal{N}(\mu,\sigma^2)$, then $X$ is Log-normal. Right-skewed, used for quantities that are products of many positive factors.  
- **Power-law (Pareto)**: Heavy-tailed distribution where a few values dominate (80/20 rule).

#### 14. What is Power-law & Pareto distributions: PDF, examples
PDF of Pareto Type I:
$$
f(x) = \frac{\alpha x_m^\alpha}{x^{\alpha+1}}, \quad x \ge x_m
$$
Examples: wealth distribution, city sizes, word frequencies, website traffic, degree distribution in networks.

#### 15. Explain about Box-Cox / Power transform
Box-Cox is a family of power transformations used to make data more Normal / stabilize variance:
$$
y^{(\lambda)} = \begin{cases}
\dfrac{y^\lambda - 1}{\lambda} & \lambda \neq 0 \\
\log y & \lambda = 0
\end{cases}
$$

#### 16. What is Co-variance?
Covariance measures the joint variability of two random variables:
$$
\text{Cov}(X,Y) = E[(X-\mu_X)(Y-\mu_Y)]
$$
- Positive → variables tend to increase together  
- Negative → one increases while the other decreases  
- Zero → no linear relationship

#### 17. Importance of Pearson Correlation Coefficient
Pearson’s $\rho$ measures the **strength and direction of the linear relationship** between two variables.  
Range: $[-1, +1]$.  
It is scale-invariant (standardized covariance).

#### 18. Importance of Spearman Rank Correlation Coefficient
Spearman’s rank correlation measures the strength of a **monotonic** relationship (not necessarily linear).  
It is based on ranks and is more robust to outliers and non-linear but monotonic associations.

#### 19. Correlation vs Causation?
- **Correlation**: Two variables move together.  
- **Causation**: One variable directly causes the other.  
Correlation does **not** imply causation (confounding variables, reverse causality, coincidence possible).

#### 20. What is Confidence Intervals?
A confidence interval gives a range of plausible values for a population parameter.  
Example: 95% CI means that if we repeated the experiment many times, 95% of the intervals would contain the true parameter.

#### 21. Confidence Interval vs Point estimate?
- **Point estimate**: Single best guess (e.g., sample mean $\bar{x}$).  
- **Confidence Interval**: Range of values that quantifies uncertainty around the point estimate.

#### 22. Explain about Hypothesis testing
Hypothesis testing is a formal procedure to decide whether there is enough evidence to reject a claim (null hypothesis) about a population.

### 23. Define Hypothesis Testing methodology, Null-hypothesis, test-statistic, p-value
- **Null hypothesis ($H_0$)**: Default claim (usually “no effect” or “no difference”).  
- **Test statistic**: A number computed from the sample that measures how far the data is from $H_0$.  
- **p-value**: Probability of observing a test statistic at least as extreme as the one obtained, assuming $H_0$ is true.  
- Small p-value → evidence against $H_0$.

#### 24. How to do K-S Test for similarity of two distributions?
The Kolmogorov-Smirnov (K-S) test compares the empirical CDFs of two samples (or one sample vs a theoretical distribution).  
- Test statistic = maximum absolute difference between the two CDFs.  
- Small p-value → the two distributions are significantly different.