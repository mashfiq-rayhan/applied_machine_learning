<style>
@import url('https://fonts.googleapis.com/css2?family=Play:wght@400;700&display=swap');

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

/* Keep displayed equations visually distinct without competing with the text. */
.katex-display,
.math,
.math-block {
  background: #00070e;
  border-left: 6px solid #2f005c;
  border-radius: 6px;
  padding: 0.6em 0.8em;
  overflow-x: auto;
  color: #c9c9c9 !important;
}

.katex,
.katex * {
  color: #9b9a9a !important;
}
</style>

# 4. Histogram, PDF, and CDF

> **A visual guide to distributions**
>
> Learn how observed data becomes a histogram, how probability density is represented by a PDF, and how probability accumulates in a CDF.

## At a Glance

| View          | What it shows                          | Visual form      |
| ------------- | -------------------------------------- | ---------------- |
| **Histogram** | Observed values grouped into intervals | Bars             |
| **PDF**       | Density across possible values         | Smooth curve     |
| **CDF**       | Probability accumulated up to a value  | Increasing curve |

### The Big Picture

Understanding **Histogram, Probability Density Function (PDF), and Cumulative Distribution Function (CDF)** is fundamental to understanding how numerical data is distributed.

These three concepts are closely related:

$$
\boxed{\text{Histogram} \approx \text{PDF} \rightarrow \text{CDF}}
$$

- **Histogram** shows how observations are distributed across intervals.
- **PDF** describes the probability density of a continuous random variable.
- **CDF** describes the accumulated probability up to a given value.

> **Reading path:** Start with the histogram to see the data, use the PDF to describe density, and use the CDF to answer cumulative probability questions.

---

<a id="histogram"></a>

## 4.1 Histogram

### Histogram Theory

A **histogram** is a graphical representation of the distribution of numerical data.

Unlike a bar chart, which is generally used for categorical data, a histogram is used for **continuous or numerical data**.

A histogram divides the range of values into intervals called **bins**.

For example, suppose we have:

$$
[12,15,17,21,22,24,26,28,31,35]
$$

We might divide the values into bins:

| Bin | Range |
| --- | ----- |
| 1   | 10–15 |
| 2   | 15–20 |
| 3   | 20–25 |
| 4   | 25–30 |
| 5   | 30–35 |

Each bin contains the observations that fall within its range.

The height of each bar represents the **frequency/count** of observations in that bin.

### Components of a Histogram

- **X-axis:** Value ranges or bins
- **Y-axis:** Frequency, relative frequency, or density
- **Bars:** Represent the number/density of observations in each interval
- **Bin width:** Width of each interval

---

### Mathematical Representation

Suppose we have \(n\) observations:

$$
x_1,x_2,x_3,\ldots,x_n
$$

If bin \(i\) is defined as:

$$
[x_i,x_i+h)
$$

where \(h\) is the bin width, then the number of observations inside that bin is:

$$
count_i=
\sum_{j=1}^{n}
I(x_j\in[x_i,x_i+h))
$$

where \(I\) is an **indicator function**:

$$
I(A)=
\begin{cases}
1 & \text{if }A\text{ is true}\\
0 & \text{if }A\text{ is false}
\end{cases}
$$

Therefore, every observation either contributes:

$$
1
$$

if it belongs to the bin, or:

$$
0
$$

if it does not.

---

### Relative Frequency

The **relative frequency** of a bin is:

$$
\text{Relative Frequency}_i
=
\frac{count_i}{n}
$$

It represents the proportion of observations contained within that bin.

For example, if there are 100 observations and 25 fall into a particular bin:

$$
\text{Relative Frequency}
=
\frac{25}{100}
=
0.25
$$

So, 25% of the observations are in that interval.

---

### Histogram Density

If we normalize the histogram by both the total number of observations and the bin width, we obtain a density estimate:

$$
\text{Density}_i
\approx
\frac{count_i}{n\cdot h}
$$

where:

- \(count_i\) = number of observations in bin \(i\)
- \(n\) = total number of observations
- \(h\) = bin width

This makes the histogram comparable to a **Probability Density Function (PDF)**.

The important idea is:

$$
\boxed{\text{Histogram density} \approx \text{PDF}}
$$

---

## 4.2 Why Histograms Are Useful

A histogram helps us understand the **shape and structure of a dataset**.

It can reveal:

<h3 class="insight-item"><strong>1. Distribution Shape :</strong> We can determine whether the data is approximately:</h3>

<ul class="insight-list">
<li>Symmetric</li>
<li>Left-skewed</li>
<li>Right-skewed</li>
<li>Uniform</li>
<li>Bell-shaped</li>
</ul>

<h3 class="insight-item"><strong>2. Modality :</strong> A histogram can show whether the distribution is:</h3>

<ul class="insight-list">
<li><strong>Unimodal</strong> → one major peak</li>
<li><strong>Bimodal</strong> → two major peaks</li>
<li><strong>Multimodal</strong> → multiple peaks</li>
</ul>

<h3 class="insight-item"><strong>3. Spread :</strong> It helps us understand how widely the observations are distributed.</h3>

<h3 class="insight-item"><strong>4. Outliers :</strong> Very distant observations may appear as isolated bars.</h3>

<h3 class="insight-item"><strong>5. Gaps :</strong> A histogram can reveal ranges where very few or no observations exist.</h3>

<h3 class="insight-item"><strong>6. Concentration :</strong> We can see where most of the observations are concentrated.</h3>

---

## 4.3 Choosing the Number of Bins

The number and width of bins significantly affect the appearance of a histogram.

### Too Few Bins

If there are too few bins:

- important patterns may disappear
- different groups may be merged
- the distribution may appear overly smooth

### Too Many Bins

If there are too many bins:

- the histogram can become noisy
- random fluctuations may look like meaningful patterns
- the underlying distribution can become difficult to interpret

Therefore:

$$
\boxed{\text{Bin width should be chosen carefully}}
$$

The goal is to reveal the underlying structure of the data rather than noise.

---

<a id="pdf"></a>

## 4.4 Probability Density Function (PDF)

### What is a PDF?

A **Probability Density Function (PDF)** describes how probability is distributed across the possible values of a **continuous random variable**.

The PDF is usually represented by:

$$
f(x)
$$

A PDF allows us to understand where values are more or less concentrated.

A region with a higher PDF value indicates **greater probability density**, while a lower PDF value indicates lower probability density.

However, an important point is:

$$
\boxed{\text{PDF value itself is not probability}}
$$

For a continuous random variable, probability is obtained from the **area under the PDF curve over an interval**.

---

## 4.5 Properties of a PDF

A valid PDF must satisfy:

$$
f(x)\ge0
$$

for all \(x\).

The total area under the PDF curve must equal 1:

$$
\boxed{
\int_{-\infty}^{\infty}f(x)\,dx=1
}
$$

This represents the fact that the total probability of all possible outcomes is 1.

---

## 4.6 Probability from a PDF

Suppose we want to find the probability that a continuous random variable \(X\) falls between \(a\) and \(b\).

The probability is:

$$
\boxed{
P(a\le X\le b)
=
\int_a^b f(x)\,dx
}
$$

Therefore:

$$
\text{Probability}
=
\text{Area under the PDF curve}
$$

between \(a\) and \(b\).

### Example

Suppose:

$$
P(10\le X\le20)
$$

is required.

Then:

$$
P(10\le X\le20)
=
\int_{10}^{20}f(x)\,dx
$$

The result is the area under the PDF between 10 and 20.

---

## 4.7 PDF and Continuous Variables

For a continuous random variable:

$$
\boxed{P(X=x)=0}
$$

for any exact single value \(x\).

This is an important distinction.

For example:

$$
P(X=10)=0
$$

but:

$$
P(9\le X\le11)>0
$$

may be positive.

Therefore, we use intervals and areas under the curve to calculate probabilities.

---

## 4.8 Relationship Between Histogram and PDF

A histogram is based on **observed sample data**, while a PDF represents the underlying **probability distribution** of a continuous random variable.

With a sufficiently large sample and an appropriate bin width:

$$
\boxed{\text{Histogram density} \approx f(x)}
$$

where \(f(x)\) is the PDF.

Conceptually:

<div class="concept-flow">
<div class="flow-step"><strong>Observed Data</strong></div>
<div class="flow-arrow">↓</div>
<div class="flow-step"><strong>Histogram</strong></div>
<div class="flow-arrow">↓</div>
<div class="flow-step"><strong>Approximation</strong></div>
<div class="flow-arrow">↓</div>
<div class="flow-step"><strong>Underlying PDF</strong></div>
</div>

The histogram gives us an empirical view of the data, while the PDF gives us a mathematical representation of a probability distribution.

---

<a id="cdf"></a>

## 4.9 Cumulative Distribution Function (CDF)

### What is a CDF?

The **Cumulative Distribution Function (CDF)** tells us the probability that a random variable \(X\) is less than or equal to a particular value \(x\).

It is defined as:

$$
\boxed{
F(x)=P(X\le x)
}
$$

For a continuous random variable with PDF \(f(x)\):

$$
\boxed{
F(x)=
\int_{-\infty}^{x}f(t)\,dt
}
$$

The CDF therefore represents the **accumulated probability** from \(-\infty\) up to \(x\).

---

## 4.10 Understanding CDF Intuitively

Suppose:

$$
F(50)=0.80
$$

This means:

$$
P(X\le50)=0.80
$$

In simple terms:

> **80% of the probability lies at or below 50.**

If the random variable represents exam scores, this could mean that 80% of the population has a score of 50 or less.

---

## 4.11 Properties of CDF

A CDF always satisfies:

$$
0\le F(x)\le1
$$

### Property 1: CDF is Non-Decreasing

As \(x\) increases, the CDF can increase or remain constant, but it cannot decrease.

$$
x_1<x_2
$$

implies:

$$
F(x_1)\le F(x_2)
$$

This makes sense because accumulated probability cannot decrease.

---

### Property 2: Lower Limit

As \(x\) approaches negative infinity:

$$
\boxed{
\lim_{x\to-\infty}F(x)=0
}
$$

There is essentially no probability accumulated before extremely small values.

---

### Property 3: Upper Limit

As \(x\) approaches positive infinity:

$$
\boxed{
\lim_{x\to\infty}F(x)=1
}
$$

Eventually, all probability has been accumulated.

---

## 4.12 Probability Using the CDF

The CDF makes calculating interval probabilities very convenient.

For a continuous random variable:

$$
\boxed{
P(a<X\le b)
=
F(b)-F(a)
}
$$

For continuous distributions, the distinction between \(<\) and \(\le\) does not affect the probability at individual points.

### Example

Suppose:

$$
F(20)=0.75
$$

and:

$$
F(10)=0.30
$$

Then:

$$
P(10<X\le20)
=
F(20)-F(10)
$$

$$
=0.75-0.30
$$

$$
=0.45
$$

Therefore:

$$
\boxed{P(10<X\le20)=0.45}
$$

So there is a **45% probability** that \(X\) falls between 10 and 20.

---

## 4.13 Relationship Between PDF and CDF

The PDF and CDF are directly related.

Starting with the CDF:

$$
F(x)
=
\int_{-\infty}^{x}f(t)\,dt
$$

If we differentiate the CDF:

$$
\boxed{
f(x)=\frac{dF(x)}{dx}
}
$$

Therefore:

$$
\boxed{
\text{PDF}=\text{Derivative of CDF}
}
$$

and:

$$
\boxed{
\text{CDF}=\text{Integral of PDF}
}
$$

Conceptually:

```text
              Integration
PDF  ─────────────────────────→  CDF
 ↑                                  │
 │                                  │
 └──────────── Derivative ──────────┘
```

---

## 4.14 Histogram vs PDF vs CDF

| Concept       | Meaning                       | Representation   | Main Question                                    |
| ------------- | ----------------------------- | ---------------- | ------------------------------------------------ |
| **Histogram** | Distribution of observed data | Bars             | How are the observations distributed?            |
| **PDF**       | Probability density           | Curve            | Where is probability concentrated?               |
| **CDF**       | Cumulative probability        | Increasing curve | How much probability is accumulated up to \(x\)? |

---

## 4.15 Simple Example

Consider the following observations:

$$
2,3,3,4,5,5,5,6,7,8
$$

There are:

$$
n=10
$$

observations.

A histogram might group the observations into bins.

For example:

| Value/Range | Count |
| ----------- | ----: |
| 2–3         |     3 |
| 4–5         |     4 |
| 6–7         |     2 |
| 8–9         |     1 |

The histogram tells us how many observations fall within each range.

A PDF would represent the corresponding **density** as a continuous curve if we model the data using a continuous distribution.

The CDF would answer questions such as:

$$
P(X\le5)
$$

From the data:

$$
2,3,3,4,5
$$

are 5 observations out of 10.

Therefore, the empirical cumulative probability is:

$$
\frac{5}{10}=0.5
$$

So:

$$
F(5)\approx0.5
$$

This means approximately 50% of the observations are less than or equal to 5.

---

## 4.16 Empirical CDF

When working with actual sample data, we can construct an **Empirical Cumulative Distribution Function (ECDF)**.

The ECDF is:

$$
\boxed{
\hat F(x)
=
\frac{1}{n}
\sum_{i=1}^{n}I(x_i\le x)
}
$$

where:

- \(n\) = number of observations
- \(I(x_i\le x)\) = 1 if \(x_i\le x\)
- \(I(x_i\le x)\) = 0 otherwise

The ECDF tells us the proportion of observed values that are less than or equal to \(x\).

---

## 4.17 Histogram, PDF, and CDF — Big Picture

These concepts can be understood as three different views of a distribution.

### Histogram

Works directly with observed data:

$$
\boxed{\text{Data}\rightarrow\text{Histogram}}
$$

It groups observations into bins.

### PDF

Describes probability density:

$$
\boxed{\text{PDF}\rightarrow\text{Density}}
$$

It tells us how probability is distributed across the range.

### CDF

Accumulates probability:

$$
\boxed{\text{PDF}\rightarrow\text{CDF}}
$$

It tells us how much probability has accumulated up to a particular value.

---

## 4.18 Visual Intuition

Think of the PDF and CDF as two views of the same distribution:

<div class="intuition-grid">
<div class="intuition-card pdf">
<h3>PDF: Density</h3>
<p>The height shows where observations are concentrated. A taller region means greater density, not probability at one exact point.</p>
<div class="intuition-chart" aria-label="A peaked PDF profile">
<span style="height: 20%"></span>
<span style="height: 35%"></span>
<span style="height: 55%"></span>
<span style="height: 80%"></span>
<span style="height: 100%"></span>
<span style="height: 80%"></span>
<span style="height: 55%"></span>
<span style="height: 35%"></span>
<span style="height: 20%"></span>
</div>
<div class="intuition-label">Density changes across the value range</div>
</div>

<div class="intuition-card cdf">
<h3>CDF: Accumulation</h3>
<p>The curve rises as probability accumulates from left to right. It begins near 0 and approaches 1.</p>
<div class="intuition-chart" aria-label="A rising CDF profile">
<span style="height: 10%"></span>
<span style="height: 18%"></span>
<span style="height: 28%"></span>
<span style="height: 42%"></span>
<span style="height: 58%"></span>
<span style="height: 72%"></span>
<span style="height: 83%"></span>
<span style="height: 92%"></span>
<span style="height: 98%"></span>
</div>
<div class="intuition-label">Accumulated probability increases toward 1</div>
</div>
</div>

> **Memory aid:** The PDF describes _where_ probability is concentrated; the CDF describes _how much_ probability has accumulated.

The CDF starts near:

$$
0
$$

and eventually approaches:

$$
1
$$

---

## 4.19 Key Mathematical Relationships

The most important formulas to remember are:

### Histogram Count

$$
\boxed{
count_i=
\sum_{j=1}^{n}
I(x_j\in\text{bin}_i)
}
$$

### Relative Frequency

$$
\boxed{
\text{Relative Frequency}_i
=
\frac{count_i}{n}
}
$$

### Histogram Density

$$
\boxed{
\text{Density}_i
\approx
\frac{count_i}{n h}
}
$$

### PDF Total Probability

$$
\boxed{
\int_{-\infty}^{\infty}f(x)\,dx=1
}
$$

### Probability from PDF

$$
\boxed{
P(a\le X\le b)
=
\int_a^b f(x)\,dx
}
$$

### CDF

$$
\boxed{
F(x)=P(X\le x)
}
$$

### CDF from PDF

$$
\boxed{
F(x)=
\int_{-\infty}^{x}f(t)\,dt
}
$$

### PDF from CDF

$$
\boxed{
f(x)=\frac{dF(x)}{dx}
}
$$

### Probability from CDF

$$
\boxed{
P(a<X\le b)=F(b)-F(a)
}
$$

---

## 4.20 Quick Summary

<div class="summary-grid">
<div class="summary-card histogram">
<div class="summary-tag">Observed data</div>
<h3>Histogram</h3>
<p><strong>Shows the distribution of observed numerical data using bins.</strong></p>
</div>

<div class="summary-card pdf">
<div class="summary-tag">Density</div>
<h3>PDF</h3>
<p><strong>Shows probability density across the possible values of a continuous random variable.</strong></p>
</div>

<div class="summary-card cdf">
<div class="summary-tag">Accumulation</div>
<h3>CDF</h3>
<p><strong>Shows the cumulative probability up to a particular value.</strong></p>
</div>
</div>

<div class="relationship-banner">
<strong>Histogram</strong>
<span class="arrow">≈</span>
<strong>PDF</strong>
<span class="arrow">→</span>
<strong>CDF</strong>
<span class="arrow">|</span>
<span>CDF = integral of PDF</span>
<span class="arrow">|</span>
<span>PDF = derivative of CDF</span>
</div>

### One-line intuition

$$
\boxed{
\text{Histogram = observed distribution}
}
$$

$$
\boxed{
\text{PDF = probability density}
}
$$

$$
\boxed{
\text{CDF = accumulated probability}
}
$$

---

## 4.21 ML Perspective

Before building a model, inspect the distribution of each feature. Histograms, PDFs, and CDFs help reveal the shape and behavior of the data before training begins.

<div class="ml-grid">
<div class="ml-card">
<h3>Features to Inspect</h3>
<p class="panel-kicker">Example numerical variables</p>
<ul class="feature-chips">
<li>Age</li>
<li>Salary</li>
<li>House price</li>
<li>Exam score</li>
<li>Temperature</li>
</ul>
</div>

<div class="ml-card diagnostics">
<h3>Questions to Ask</h3>
<ul>
<li>Is the feature skewed?</li>
<li>Are there outliers?</li>
<li>Where are values concentrated?</li>
<li>Would a transformation help?</li>
<li>Does it resemble a known distribution?</li>
</ul>
</div>
</div>

<div class="ml-workflow">
<strong>Inspect features</strong>
<span>→</span>
<strong>Understand distributions</strong>
<span>→</span>
<strong>Choose transformations</strong>
<span>→</span>
<strong>Build the model</strong>
</div>

CDFs are especially useful for understanding **percentiles and quantiles**. For example, if:

$$
F(x)=0.90
$$

then approximately 90% of the distribution lies at or below $x$.

<div class="percentile-callout">
<strong>ML interpretation:</strong> The CDF connects probability to percentiles and quantiles. A value where $F(x)=0.90$ is approximately the 90th percentile.
</div>

$$
\boxed{\text{CDF}\leftrightarrow\text{Percentiles}\leftrightarrow\text{Quantiles}}
$$

These ideas provide a foundation for **probability distributions, normal distribution, z-scores, variance, standard deviation, skewness, percentiles, quantiles, and statistical inference**.
