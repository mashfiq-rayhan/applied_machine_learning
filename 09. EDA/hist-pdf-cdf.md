# 4. Histogram, PDF, and CDF

Understanding **Histogram, Probability Density Function (PDF), and Cumulative Distribution Function (CDF)** is fundamental to understanding how numerical data is distributed.

These three concepts are closely related:

$$
\boxed{\text{Histogram} \approx \text{PDF} \rightarrow \text{CDF}}
$$

* **Histogram** shows how observations are distributed across intervals.
* **PDF** describes the probability density of a continuous random variable.
* **CDF** describes the accumulated probability up to a given value.

---

<a id="histogram"></a>
# 4.1 Histogram

## Histogram Theory

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

* **X-axis:** Value ranges or bins
* **Y-axis:** Frequency, relative frequency, or density
* **Bars:** Represent the number/density of observations in each interval
* **Bin width:** Width of each interval

---

## Mathematical Representation

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

## Relative Frequency

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

## Histogram Density

If we normalize the histogram by both the total number of observations and the bin width, we obtain a density estimate:

$$
\text{Density}_i
\approx
\frac{count_i}{n\cdot h}
$$

where:

* \(count_i\) = number of observations in bin \(i\)
* \(n\) = total number of observations
* \(h\) = bin width

This makes the histogram comparable to a **Probability Density Function (PDF)**.

The important idea is:

$$
\boxed{\text{Histogram density} \approx \text{PDF}}
$$

---

# 4.2 Why Histograms Are Useful

A histogram helps us understand the **shape and structure of a dataset**.

It can reveal:

### 1. Distribution Shape

We can determine whether the data is approximately:

* symmetric
* left-skewed
* right-skewed
* uniform
* bell-shaped

### 2. Modality

A histogram can show whether the distribution is:

* **Unimodal** → one major peak
* **Bimodal** → two major peaks
* **Multimodal** → multiple peaks

### 3. Spread

It helps us understand how widely the observations are distributed.

### 4. Outliers

Very distant observations may appear as isolated bars.

### 5. Gaps

A histogram can reveal ranges where very few or no observations exist.

### 6. Concentration

We can see where most of the observations are concentrated.

---

# 4.3 Choosing the Number of Bins

The number and width of bins significantly affect the appearance of a histogram.

### Too Few Bins

If there are too few bins:

* important patterns may disappear
* different groups may be merged
* the distribution may appear overly smooth

### Too Many Bins

If there are too many bins:

* the histogram can become noisy
* random fluctuations may look like meaningful patterns
* the underlying distribution can become difficult to interpret

Therefore:

$$
\boxed{\text{Bin width should be chosen carefully}}
$$

The goal is to reveal the underlying structure of the data rather than noise.

---

<a id="pdf"></a>
# 4.4 Probability Density Function (PDF)

## What is a PDF?

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

# 4.5 Properties of a PDF

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

# 4.6 Probability from a PDF

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

# 4.7 PDF and Continuous Variables

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

# 4.8 Relationship Between Histogram and PDF

A histogram is based on **observed sample data**, while a PDF represents the underlying **probability distribution** of a continuous random variable.

With a sufficiently large sample and an appropriate bin width:

$$
\boxed{\text{Histogram density} \approx f(x)}
$$

where \(f(x)\) is the PDF.

Conceptually:

```text
Observed Data
     ↓
  Histogram
     ↓
Approximation
     ↓
Underlying PDF
```

The histogram gives us an empirical view of the data, while the PDF gives us a mathematical representation of a probability distribution.

---

<a id="cdf"></a>
# 4.9 Cumulative Distribution Function (CDF)

## What is a CDF?

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

# 4.10 Understanding CDF Intuitively

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

# 4.11 Properties of CDF

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

# 4.12 Probability Using the CDF

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

# 4.13 Relationship Between PDF and CDF

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

# 4.14 Histogram vs PDF vs CDF

| Concept       | Meaning                       | Representation   | Main Question                                    |
| ------------- | ----------------------------- | ---------------- | ------------------------------------------------ |
| **Histogram** | Distribution of observed data | Bars             | How are the observations distributed?            |
| **PDF**       | Probability density           | Curve            | Where is probability concentrated?               |
| **CDF**       | Cumulative probability        | Increasing curve | How much probability is accumulated up to \(x\)? |

---

# 4.15 Simple Example

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

# 4.16 Empirical CDF

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

* \(n\) = number of observations
* \(I(x_i\le x)\) = 1 if \(x_i\le x\)
* \(I(x_i\le x)\) = 0 otherwise

The ECDF tells us the proportion of observed values that are less than or equal to \(x\).

---

# 4.17 Histogram, PDF, and CDF — Big Picture

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

# 4.18 Visual Intuition

Think of a PDF as a **mountain landscape**.

The height of the mountain represents **density**.

The CDF represents how much area you have accumulated as you move from left to right.

```text
PDF

Density
  │
  │              /\
  │             /  \
  │           /      \
  │         /          \
  │_______/______________\________ Value
```

Now imagine accumulating the area from left to right:

```text
CDF

Probability
1.0 │                         ______
    │                     ___/
    │                  __/
    │               __/
    │            __/
    │        ___/
0.0 │_______/
    └────────────────────────────── Value
```

The CDF starts near:

$$
0
$$

and eventually approaches:

$$
1
$$

---

# 4.19 Key Mathematical Relationships

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

# 4.20 Quick Summary

### Histogram

> **Shows the distribution of observed numerical data using bins.**

### PDF

> **Shows probability density across the possible values of a continuous random variable.**

### CDF

> **Shows the cumulative probability up to a particular value.**

The relationship can be summarized as:

$$
\boxed{
\text{Histogram}
\approx
\text{PDF}
}
$$

and:

$$
\boxed{
\text{CDF}
=
\int \text{PDF}
}
$$

while:

$$
\boxed{
\text{PDF}
=
\frac{d}{dx}\text{CDF}
}
$$

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

# 4.21 ML Perspective

These concepts are useful in Machine Learning because they help us understand the **distribution of features** before building models.

For example, if a dataset contains:

* Age
* Salary
* House price
* Exam score
* Temperature

we can use histograms to inspect their distributions.

We can then reason about:

* skewness
* outliers
* concentration
* spread
* multimodality
* whether transformations may be useful
* whether a feature approximately follows a known distribution

CDFs are also useful for understanding **percentiles and quantiles**.

For example, if:

$$
F(x)=0.90
$$

then approximately 90% of the distribution lies at or below \(x\).

This provides a direct connection between:

$$
\boxed{\text{CDF}\leftrightarrow\text{Percentiles}\leftrightarrow\text{Quantiles}}
$$

Understanding Histogram, PDF, and CDF therefore provides an important foundation for later topics such as **probability distributions, normal distribution, z-scores, variance, standard deviation, skewness, percentiles, quantiles, and statistical inference**.
