<style>
@import url('https://fonts.googleapis.com/css2?family=Play:wght@400;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/latin-modern/1.1.0/css/latinmodern-math.min.css');

:root {
  --la-ink: #3f6386;
  --la-teal: #3f6386;
  --la-teal-soft: #e8f6f7;
  --la-coral: #9333ea;
  --la-coral-soft: #fff1ed;
  --la-cdf: #6f9fb8;
  --la-line: #5b5c5c;
  --la-surface: #f7faf9;
  --la-text: #c9c9c9;
  --la-panel: #00070e;
  --la-chip: #17283a;
}

*,
*::before,
*::after {
  font-family: 'Play', sans-serif !important;
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

h3 {
  color: var(--la-coral);
}

.insight-item {
  background: var(--la-panel);
  border-left: 5px solid var(--la-coral);
  border-radius: 5px;
  color: var(--la-text);
  font-size: 1.05em;
  margin: 0.7em 0;
  padding: 0.65em 0.9em;
}

.insight-item strong {
  color: var(--la-coral);
}

.insight-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.55em;
  list-style: none;
  margin: 0.5em 0 1em;
  padding: 0;
}

.insight-list li {
  background: var(--la-chip);
  border: 1px solid var(--la-teal);
  border-radius: 999px;
  color: var(--la-text);
  padding: 0.35em 0.75em;
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

.summary-grid {
  display: flex;
  gap: 1em;
  margin: 1.25em 0;
}

.summary-card {
  background: var(--la-panel);
  border-top: 5px solid var(--la-teal);
  border-radius: 7px;
  color: var(--la-text);
  flex: 1 1 0;
  min-width: 0;
  padding: 1em;
}

.summary-card.pdf {
  border-top-color: var(--la-coral);
}

.summary-card.cdf {
  border-top-color: var(--la-cdf);
}

.summary-card h3 {
  margin-top: 0;
}

.summary-card p {
  margin-bottom: 0;
}

.summary-tag {
  color: var(--la-teal);
  font-size: 0.82em;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.relationship-banner {
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

.relationship-banner strong {
  color: var(--la-coral);
}

.relationship-banner .arrow {
  color: var(--la-teal);
  font-size: 1.2em;
}

.ml-grid {
  display: flex;
  gap: 1em;
  margin: 1.25em 0;
}

.ml-card {
  background: var(--la-panel);
  border-left: 5px solid var(--la-teal);
  border-radius: 7px;
  color: var(--la-text);
  flex: 1 1 0;
  padding: 1em;
}

.ml-card.diagnostics {
  border-left-color: var(--la-coral);
}

.ml-card h3 {
  margin-top: 0;
}

.feature-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45em;
  list-style: none;
  margin: 0;
  padding: 0;
}

.feature-chips li {
  background: var(--la-chip);
  border-left: 3px solid var(--la-coral);
  border-radius: 4px;
  color: var(--la-text);
  flex: 1 1 calc(50% - 0.45em);
  padding: 0.55em 0.7em;
}

.panel-kicker {
  color: var(--la-teal);
  font-size: 0.82em;
  font-weight: 700;
  letter-spacing: 0.04em;
  margin-top: -0.6em;
  text-transform: uppercase;
}

.ml-workflow {
  align-items: center;
  background: var(--la-panel);
  border: 1px solid var(--la-teal);
  border-radius: 7px;
  color: var(--la-text);
  display: flex;
  flex-wrap: wrap;
  gap: 0.55em;
  justify-content: center;
  margin: 1.25em 0;
  padding: 0.85em 1em;
  text-align: center;
}

.ml-workflow strong {
  color: var(--la-coral);
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

@media (max-width: 700px) {
  .summary-grid,
  .ml-grid {
    flex-direction: column;
  }
}

.intuition-grid {
  display: flex;
  gap: 1em;
  margin: 1.25em 0;
}

.intuition-card {
  background: var(--la-panel);
  border-radius: 7px;
  color: var(--la-text);
  flex: 1 1 0;
  min-width: 0;
  padding: 1em;
}

.intuition-card.pdf {
  border-top: 5px solid var(--la-coral);
}

.intuition-card.cdf {
  border-top: 5px solid var(--la-cdf);
}

.intuition-card h3 {
  margin-top: 0;
}

.intuition-chart {
  align-items: end;
  border-bottom: 2px solid var(--la-teal);
  display: flex;
  gap: 0.35em;
  height: 9em;
  justify-content: center;
  margin: 1em 0;
  padding: 0 0.75em;
}

.intuition-chart span {
  background: var(--la-coral);
  border-radius: 4px 4px 0 0;
  display: block;
  flex: 1;
  max-width: 2.5em;
}

.intuition-card.cdf .intuition-chart span {
  background: var(--la-cdf);
}

.intuition-label {
  color: var(--la-teal);
  font-size: 0.9em;
  text-align: center;
}

@media (max-width: 760px) {
  .intuition-grid {
    flex-direction: column;
  }
}

.relationship-item {
  background: var(--la-panel);
  border-left: 5px solid var(--la-teal);
  border-radius: 5px;
  color: var(--la-text);
  margin: 0.65em 0;
  padding: 0.55em 0.85em;
}

.relationship-item strong {
  color: var(--la-coral);
  margin-right: 0.35em;
}

.revision-question {
  color: #c0392b;
}

blockquote {
  background: var(--la-panel);
  border-left: 5px solid var(--la-cdf) !important;
  color: var(--la-text);
  padding: 0.75em 1em;
}

table {
  border: 1px solid var(--la-line);
  border-radius: 8px;
  overflow: hidden;
}

th {
  background: var(--la-panel);
  color: var(--la-text);
}

td {
  color: var(--la-text);
}

tr:nth-child(even) {
  background: var(--la-chip);
}

hr {
  border: 0;
  border-top: 2px solid var(--la-line);
  margin: 2.2em 0;
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
  font-family: 'Latin Modern Math', 'Cambria Math', 'STIX Two Math', serif !important;
}

.katex,
.katex * {
  color: #9b9a9a !important;
  font-family: 'Latin Modern Math', 'Cambria Math', 'STIX Two Math', serif !important;
}
</style>

# Descriptive Statistics

> **A concise guide to descriptive statistics**
>
> Learn the center, spread, and relative position of data with the most important summary measures used in EDA and machine learning.

## At a Glance

<div class="summary-grid">
  <div class="summary-card">
    <div class="summary-tag">Center</div>
    <h3>Mean, Median, Mode</h3>
    <p>These describe where the data tends to sit.</p>
  </div>
  <div class="summary-card pdf">
    <div class="summary-tag">Spread</div>
    <h3>Variance, Std Dev, IQR, MAD</h3>
    <p>These measure how far values typically deviate from the center.</p>
  </div>
  <div class="summary-card cdf">
    <div class="summary-tag">Position</div>
    <h3>Percentile, Quantile</h3>
    <p>These place an observation within the full distribution.</p>
  </div>
</div>

## Table of Contents

- [1. Mean](#1-mean)
- [2. Variance](#2-variance)
- [3. Standard Deviation](#3-standard-deviation)
- [4. Mean vs Variance vs Standard Deviation](#4-mean-vs-variance-vs-standard-deviation)
- [5. Median](#5-median)
- [6. Mean vs Median](#6-mean-vs-median)
- [7. Mode](#7-mode)
- [8. Percentile](#8-percentile)
- [9. Quantile](#9-quantile)
- [10. Quartiles](#10-quartiles)
- [11. Interquartile Range (IQR)](#11-interquartile-range-iqr)
- [12. IQR and Outlier Detection](#12-iqr-and-outlier-detection)
- [13. MAD — Median Absolute Deviation](#13-mad--median-absolute-deviation)
- [14. Why Is MAD Robust?](#14-why-is-mad-robust)
- [15. Standard Deviation vs IQR vs MAD](#15-standard-deviation-vs-iqr-vs-mad)
- [16. Complete Summary](#16-complete-summary)
- [17. A Useful Mental Model](#17-a-useful-mental-model)
- [18. Robust vs Non-Robust Statistics](#18-robust-vs-non-robust-statistics)
- [19. Connection to Machine Learning](#19-connection-to-machine-learning)
- [20. Final Takeaways](#20-final-takeaways)

Descriptive statistics help us **summarize, understand, and describe a dataset** using numerical measures.

In Machine Learning and Data Science, these measures are useful for:

- Understanding the distribution of data
- Measuring the center of data
- Measuring the spread/variability of data
- Detecting outliers
- Comparing different datasets/features
- Understanding feature distributions before building models
- Performing data preprocessing and exploratory data analysis (EDA)

<div class="relationship-banner">
  <span><strong>Center</strong></span>
  <span class="arrow">→</span>
  <span>Mean / Median / Mode</span>
  <span class="arrow">→</span>
  <span><strong>Spread</strong></span>
  <span class="arrow">→</span>
  <span>Variance / Std Dev / IQR / MAD</span>
</div>

# 1. Mean

The **mean** is the arithmetic average of a set of observations.

For a dataset:

$$
x_1, x_2, x_3, \dots, x_n
$$

the mean is:

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i
$$

Where:

- $\bar{x}$ = sample mean
- $x_i$ = individual observation
- $n$ = number of observations

## Example

Consider:

$$
2,\ 4,\ 6,\ 8,\ 10
$$

Mean:

$$
\bar{x} = \frac{2+4+6+8+10}{5}
$$

$$
\bar{x} = 6
$$

Therefore:

> **Mean = 6**

## Intuition

The mean represents the **balance point** of the data.

If we think of every observation as having the same weight, the mean is the point at which the data would balance.

## Mean and Outliers

The mean is **sensitive to outliers**.

Consider:

$$
2,\ 4,\ 6,\ 8,\ 10
$$

Mean:

$$
6
$$

Now add an extreme value:

$$
2,\ 4,\ 6,\ 8,\ 10,\ 100
$$

New mean:

$$
\frac{2+4+6+8+10+100}{6}=21.67
$$

The mean moved from:

$$
6 \rightarrow 21.67
$$

even though most of the observations are still between 2 and 10.

### Key Point

> **Mean is useful, but it can be strongly affected by extreme values.**

# 2. Variance

Variance measures **how spread out the observations are around the mean**.

The basic idea is:

1. Calculate the mean.
2. Calculate the difference between each observation and the mean.
3. Square those differences.
4. Take their average.

For a population:

$$
\sigma^2 = \frac{1}{N}\sum_{i=1}^{N}(x_i-\mu)^2
$$

For a sample:

$$
s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2
$$

Where:

- $\mu$ = population mean
- $\bar{x}$ = sample mean
- $N$ = population size
- $n$ = sample size
- $\sigma^2$ = population variance
- $s^2$ = sample variance

## Why Do We Square the Differences?

Suppose the mean is 5.

For observations:

$$
3,\ 7
$$

The deviations are:

$$
3-5=-2
$$

and

$$
7-5=2
$$

If we simply added them:

$$
-2+2=0
$$

The positive and negative deviations would cancel each other.

So we square the deviations:

$$
(-2)^2=4
$$

$$
(2)^2=4
$$

This allows us to measure the magnitude of the deviations without cancellation.

## Example

Consider:

$$
2,\ 4,\ 6,\ 8,\ 10
$$

Mean:

$$
\bar{x}=6
$$

| $x$ | $x-\bar{x}$ | $(x-\bar{x})^2$ |
| --: | ----------: | --------------: |
|   2 |          -4 |              16 |
|   4 |          -2 |               4 |
|   6 |           0 |               0 |
|   8 |           2 |               4 |
|  10 |           4 |              16 |

Sum of squared deviations:

$$
16+4+0+4+16=40
$$

Population variance:

$$
\frac{40}{5}=8
$$

So:

> **Variance = 8**

## Important Property

Variance is measured in **squared units**.

For example:

- Height → meters
- Variance of height → meters²

This makes variance mathematically useful but sometimes difficult to interpret directly.

# 3. Standard Deviation

The **standard deviation** is the square root of the variance.

$$
\sigma = \sqrt{\sigma^2}
$$

For a sample:

$$
s=\sqrt{s^2}
$$

If:

$$
\text{Variance}=8
$$

then:

$$
\text{Standard Deviation}=\sqrt{8}\approx2.83
$$

## Why Use Standard Deviation?

Variance is expressed in squared units.

Standard deviation returns the measurement to the **original unit of the data**.

For example:

> If height is measured in centimeters, standard deviation is also measured in centimeters.

This makes standard deviation easier to interpret.

## Intuition

A small standard deviation means:

> Data points are generally close to the mean.

A large standard deviation means:

> Data points are generally farther from the mean.

### Example

Dataset A:

$$
49,\ 50,\ 51,\ 50,\ 50
$$

Dataset B:

$$
20,\ 40,\ 50,\ 60,\ 80
$$

Both may have similar means, but Dataset B has much greater variability.

# 4. Mean vs Variance vs Standard Deviation

| Measure            | What it tells us                         |
| ------------------ | ---------------------------------------- |
| Mean               | Center of the data                       |
| Variance           | Spread around the mean                   |
| Standard Deviation | Spread around the mean in original units |

### Simple intuition

```text
Mean              → Where is the center?
Variance          → How spread out is the data?
Standard Deviation → How spread out is the data, in original units?
```

# 5. Median

The **median** is the middle value after sorting the observations.

## Example

Consider:

$$
2,\ 4,\ 6,\ 8,\ 10
$$

The middle value is:

$$
6
$$

Therefore:

> **Median = 6**

## Even Number of Observations

Consider:

$$
2,\ 4,\ 6,\ 8
$$

There are two middle values:

$$
4,\ 6
$$

The median is their average:

$$
\frac{4+6}{2}=5
$$

Therefore:

> **Median = 5**

## Median and Outliers

The median is much less sensitive to extreme values than the mean.

Consider:

$$
2,\ 4,\ 6,\ 8,\ 10
$$

Mean:

$$
6
$$

Median:

$$
6
$$

Now replace 10 with 100:

$$
2,\ 4,\ 6,\ 8,\ 100
$$

Mean:

$$
24
$$

Median:

$$
6
$$

The median remains unchanged.

### Key Point

> **Median is a robust measure of central tendency.**

# 6. Mean vs Median

| Property               | Mean        | Median      |
| ---------------------- | ----------- | ----------- |
| Measures center        | ✅          | ✅          |
| Sensitive to outliers  | High        | Low         |
| Requires sorting       | No          | Yes         |
| Useful for skewed data | Less robust | More robust |

## When Mean and Median Differ

For a symmetric distribution:

$$
\text{Mean} \approx \text{Median}
$$

For a right-skewed distribution:

$$
\text{Mean} > \text{Median}
$$

For a left-skewed distribution:

$$
\text{Mean} < \text{Median}
$$

# 7. Mode

The **mode** is the value that occurs most frequently in a dataset.

## Example

Consider:

$$
2,\ 3,\ 3,\ 4,\ 5,\ 3,\ 6
$$

The value `3` occurs most frequently.

Therefore:

> **Mode = 3**

## Multiple Modes

A dataset can have more than one mode.

Example:

$$
1,\ 1,\ 2,\ 2,\ 3
$$

Both `1` and `2` occur twice.

Therefore, the dataset is **bimodal**.

A dataset can also be:

- Unimodal → one mode
- Bimodal → two modes
- Multimodal → multiple modes

## Mode for Categorical Data

Unlike mean and median, mode can be used with **categorical data**.

Example:

```text
Red
Blue
Blue
Green
Blue
Red
```

Mode:

```text
Blue
```

# 8. Percentile

A **percentile** tells us the value below which a certain percentage of observations falls.

For example:

> The 90th percentile is the value below which approximately 90% of the observations fall.

## Examples

### 50th Percentile

The 50th percentile corresponds to the **median**.

$$
P_{50} = \text{Median}
$$

### 25th Percentile

The 25th percentile is also called:

$$
Q_1
$$

### 75th Percentile

The 75th percentile is:

$$
Q_3
$$

## Percentile Interpretation

Suppose the 80th percentile of exam scores is:

$$
85
$$

This means:

> Approximately 80% of students scored at or below 85.

It does **not** mean that the student scored 80%.

# 9. Quantile

A **quantile** divides ordered data into groups containing approximately equal proportions of observations.

The term **quantile** is more general than percentile.

### Common Quantiles

| Quantile      | Equivalent               |
| ------------- | ------------------------ |
| 0.25 quantile | 25th percentile          |
| 0.50 quantile | 50th percentile / Median |
| 0.75 quantile | 75th percentile          |

For example:

$$
Q(0.50)=\text{Median}
$$

## Quantile vs Percentile

The concepts are closely related.

A percentile usually uses a percentage:

$$
25\%,\ 50\%,\ 75\%
$$

A quantile often uses a proportion:

$$
0.25,\ 0.50,\ 0.75
$$

Therefore:

$$
25\text{th percentile}=0.25\text{ quantile}
$$

# 10. Quartiles

Quartiles divide sorted data into **four parts**.

### First Quartile

$$
Q_1 = 25\text{th percentile}
$$

Approximately 25% of observations are below $Q_1$.

### Second Quartile

$$
Q_2 = 50\text{th percentile}
$$

This is the median.

### Third Quartile

$$
Q_3 = 75\text{th percentile}
$$

Approximately 75% of observations are below $Q_3$.

# 11. Interquartile Range (IQR)

The **Interquartile Range (IQR)** measures the spread of the **middle 50%** of the data.

It is defined as:

$$
IQR = Q_3-Q_1
$$

Where:

- $Q_1$ = 25th percentile
- $Q_3$ = 75th percentile

## Example

Suppose:

$$
Q_1=10
$$

and

$$
Q_3=30
$$

Then:

$$
IQR=30-10=20
$$

Therefore:

> **IQR = 20**

## Why Is IQR Useful?

IQR is resistant to extreme values.

It focuses only on the middle 50% of the observations.

This makes it particularly useful for:

- Skewed distributions
- Data containing outliers
- Robust statistical analysis
- Box plots

# 12. IQR and Outlier Detection

A common rule for detecting outliers is the **1.5 × IQR rule**.

Calculate:

$$
IQR=Q_3-Q_1
$$

Then calculate the lower and upper fences:

$$
\text{Lower Fence}=Q_1-1.5(IQR)
$$

$$
\text{Upper Fence}=Q_3+1.5(IQR)
$$

Observations outside these boundaries are commonly flagged as potential outliers.

## Example

Suppose:

$$
Q_1=10
$$

$$
Q_3=30
$$

Then:

$$
IQR=20
$$

Lower fence:

$$
10-1.5(20)=-20
$$

Upper fence:

$$
30+1.5(20)=60
$$

Therefore, observations below `-20` or above `60` would be flagged as potential outliers under this rule.

> **Important:** An observation flagged by the IQR rule is a statistical outlier candidate, not automatically an error.

# 13. MAD — Median Absolute Deviation

**MAD** stands for **Median Absolute Deviation**.

It is a robust measure of variability based on the median rather than the mean.

The procedure is:

1. Calculate the median.
2. Calculate the absolute deviation of every observation from the median.
3. Find the median of those absolute deviations.

## Formula

Let the median of the dataset be:

$$
m=\text{median}(X)
$$

Then:

$$
MAD=\text{median}(|x_i-m|)
$$

## Example

Consider:

$$
2,\ 4,\ 6,\ 8,\ 10
$$

Median:

$$
m=6
$$

Calculate absolute deviations:

| $x$ |   $ | x-m | $   |
| --: | --: | --- | --- |
|   2 |   4 |
|   4 |   2 |
|   6 |   0 |
|   8 |   2 |
|  10 |   4 |

The absolute deviations are:

$$
4,\ 2,\ 0,\ 2,\ 4
$$

Their median is:

$$
2
$$

Therefore:

> **MAD = 2**

# 14. Why Is MAD Robust?

Consider:

$$
2,\ 4,\ 6,\ 8,\ 10
$$

Now introduce a large outlier:

$$
2,\ 4,\ 6,\ 8,\ 100
$$

The median is still:

$$
6
$$

Absolute deviations:

$$
4,\ 2,\ 0,\ 2,\ 94
$$

Median absolute deviation:

$$
2
$$

The extreme value `100` has very little influence on the MAD.

### Key Point

> **MAD is a robust measure of spread and is much less sensitive to extreme observations than variance or standard deviation.**

# 15. Standard Deviation vs IQR vs MAD

| Measure            | Based on        | Sensitive to outliers? | Main use                  |
| ------------------ | --------------- | ---------------------: | ------------------------- |
| Standard Deviation | Mean            |                    Yes | General measure of spread |
| IQR                | $Q_1$ and $Q_3$ |                    Low | Spread of middle 50%      |
| MAD                | Median          |                    Low | Robust measure of spread  |

# 16. Complete Summary

| Statistic              | Measures          | Key idea                              |
| ---------------------- | ----------------- | ------------------------------------- |
| **Mean**               | Central tendency  | Arithmetic average                    |
| **Median**             | Central tendency  | Middle value                          |
| **Mode**               | Central tendency  | Most frequent value                   |
| **Variance**           | Spread            | Average squared deviation from mean   |
| **Standard Deviation** | Spread            | Square root of variance               |
| **Percentile**         | Relative position | Value below which a percentage falls  |
| **Quantile**           | Relative position | Divides data into proportions         |
| **IQR**                | Spread            | $Q_3-Q_1$, middle 50%                 |
| **MAD**                | Spread            | Median absolute deviation from median |

# 17. A Useful Mental Model

When looking at a new dataset, ask:

### Where is the center?

- **Mean**
- **Median**
- **Mode**

### How spread out is the data?

- **Variance**
- **Standard Deviation**
- **IQR**
- **MAD**

### Where does an observation lie within the distribution?

- **Percentile**
- **Quantile**

### Are there potential outliers?

- **IQR rule**
- **MAD-based methods**

# 18. Robust vs Non-Robust Statistics

A useful distinction in statistics is **robustness**.

### Less Robust to Outliers

- Mean
- Variance
- Standard deviation

### More Robust to Outliers

- Median
- IQR
- MAD

This distinction becomes particularly important when working with **real-world datasets**, because real-world data frequently contains extreme observations.

# 19. Connection to Machine Learning

These statistics are heavily used during **Exploratory Data Analysis (EDA)** and preprocessing.

For example:

### Mean and Median

Used to understand the center of a feature and to help with missing-value imputation.

### Standard Deviation

Useful for understanding feature scale and for **standardization**.

### Percentiles and Quantiles

Useful for understanding the relative position of observations and the shape of a distribution.

### IQR

Useful for identifying potential outliers and understanding the spread of the middle 50%.

### MAD

Useful when a robust measure of variability is needed.

# 20. Final Takeaways

> **Mean** → Average value

> **Median** → Middle value

> **Mode** → Most frequent value

> **Variance** → Average squared distance from the mean

> **Standard Deviation** → Typical spread around the mean, in original units

> **Percentile** → Value below which a given percentage of observations fall

> **Quantile** → Value dividing data according to a specified proportion

> **IQR** → Spread of the middle 50%

> **MAD** → Median absolute distance from the median

### The most important distinction

$$
\boxed{\text{Mean/Median/Mode} \rightarrow \text{Center}}
$$

$$
\boxed{\text{Variance/Std-dev/IQR/MAD} \rightarrow \text{Spread}}
$$

$$
\boxed{\text{Percentile/Quantile} \rightarrow \text{Position}}
$$
