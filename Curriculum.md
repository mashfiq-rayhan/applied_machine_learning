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


# Applied Machine Learning Course — Full Curriculum

Source: AppliedAICourse (Applied Machine Learning course), extracted from the saved course page.

## Overview

Video time sums only lectures that list a duration; live sessions and some code walkthroughs have none listed.

| Module | Chapters | Lectures | Assignments | Video time |
|---|---:|---:|---:|---:|
| [Module 1: Fundamentals of Programming](#module-1-fundamentals-of-programming) | 10 | 87 | 3 | 15h 58m |
| [Module 2: Data Science: Exploratory Data Analysis and Data Visualization](#module-2-data-science-exploratory-data-analysis-and-data-visualization) | 10 | 140 | 1 | 20h 59m |
| [Module 3: Foundations of Natural Language Processing and Machine Learning](#module-3-foundations-of-natural-language-processing-and-machine-learning) | 12 | 143 | 5 | 33h 14m |
| [Module 4: Machine Learning - II( Supervised Learning Models)](#module-4-machine-learning---ii-supervised-learning-models) | 6 | 59 | 3 | 11h 32m |
| [Module 5: Feature Engineering, Productionization and deployment of ML Models](#module-5-feature-engineering-productionization-and-deployment-of-ml-models) | 3 | 52 | 0 | 28h 11m |
| [Module 6: Machine Learning Real-World Case Studies](#module-6-machine-learning-real-world-case-studies) | 7 | 127 | 5 | 16h 47m |
| [Module 7: Data Mining(Unsupervised Learning) and Recommender Systems + Real-World Case Studies](#module-7-data-miningunsupervised-learning-and-recommender-systems--real-world-case-studies) | 9 | 110 | 4 | 18h 0m |
| [Module 8: Neural Networks, Computer Vision and Deep Learning](#module-8-neural-networks-computer-vision-and-deep-learning) | 15 | 120 | 3 | 41h 11m |
| [Module 9: Deep Learning Real-World Case Studies](#module-9-deep-learning-real-world-case-studies) | 7 | 44 | 2 | 10h 58m |
| [Module 10: Misc Topics: Spark for ML, Big Data, Reinforcement Learning, ML Design](#module-10-misc-topics-spark-for-ml-big-data-reinforcement-learning-ml-design) | 4 | 28 | 0 | 2h 57m |
| **Total** | **83** | **910** | **26** | **199h 47m** |

---

## Module 1: Fundamentals of Programming

`10 chapters` · `87 lectures` · `3 assignments` · `15h 58m of video`

> ### How to utilise Applied AI Course

- **1.1** How to Learn from Appliedaicourse — 35 mins
- **1.2** How the Job Guarantee program works — 16 mins

> ### Python for Data Science Introduction

- **2.1** Python, Anaconda and relevant packages installations — 23 mins
- **2.2** Why learn Python? — 4 mins
- **2.3** Keywords and identifiers — 6 mins
- **2.4** comments, indentation and statements — 9 mins
- **2.5** Variables and data types in Python — 32 mins
- **2.6** Standard Input and Output — 7 mins
- **2.7** Operators — 14 mins
- **2.8** Control flow: if else — 10 mins
- **2.9** Control flow: while loop — 16 mins
- **2.10** Control flow: for loop — 15 mins
- **2.11** Control flow: break and continue — 10 mins

> ### Python for Data Science: Data Structures

- **3.1** Lists — 38 mins
- **3.2** Tuples part 1 — 10 mins
- **3.3** Tuples part-2 — 4 mins
- **3.4** Sets — 16 mins
- **3.5** Dictionary — 21 mins
- **3.6** Strings — 16 mins

> ### Python for Data Science: Functions

- **4.1** Introduction — 13 mins
- **4.2** Types of functions — 25 mins
- **4.3** Function arguments — 10 mins
- **4.4** Recursive functions — 16 mins
- **4.5** Lambda functions — 8 mins
- **4.6** Modules — 7 mins
- **4.7** Packages — 6 mins
- **4.8** File Handling — 23 mins
- **4.9** Exception Handling — 15 mins
- **4.10** Debugging Python — 15 mins

> ### Python for Data Science: Numpy

- **5.1** Numpy Introduction — 41 mins
- **5.2** Numerical operations on Numpy — 41 mins

> ### Python for Data Science: Matplotlib

- **6.1** Getting started with Matplotlib — 20 mins

> ### Python for Data Science: Pandas

- **7.1** Getting started with pandas — 8 mins
- **7.2** Data Frame Basics — 9 mins
- **7.3** Key Operations on Data Frames — 31 mins

> ### Python for Data Science: Computational Complexity

- **8.1** Space and Time Complexity: Searching for a number in a list — 20 mins
- **8.2** Binary search — 17 mins
- **8.3** Find elements common in two lists — 6 mins
- **8.4** Find elements common in two lists using a Hashtable/Dict — 12 mins

> ### SQL

- **9.1** Introduction to Databases — 22 mins
- **9.2** Why SQL? — 15 mins
- **9.3** Execution of an SQL statement. — 7 mins
- **9.4** IMDB dataset — 12 mins
- **9.5** Installing MySQL — 11 mins
- **9.6** Load IMDB data. — 4 mins
- **9.7** USE, DESCRIBE, SHOW TABLES — 15 mins
- **9.8** SELECT — 20 mins
- **9.9** LIMIT, OFFSET — 10 mins
- **9.10** ORDER BY — 6 mins
- **9.11** DISTINCT — 10 mins
- **9.12** WHERE, Comparison operators, NULL — 13 mins
- **9.13** Logical Operators — 27 mins
- **9.14** Aggregate Functions: COUNT, MIN, MAX, AVG, SUM — 8 mins
- **9.15** GROUP BY — 13 mins
- **9.16** HAVING — 12 mins
- **9.17** Order of keywords. — 4 mins
- **9.18** Join and Natural Join — 12 mins
- **9.19** Inner, Left, Right and Outer joins. — 23 mins
- **9.20** Sub Queries/Nested Queries/Inner Queries — 24 mins
- **9.21** DML:INSERT — 7 mins
- **9.22** DML:UPDATE , DELETE — 6 mins
- **9.23** DDL:CREATE TABLE — 12 mins
- **9.24** DDL:ALTER: ADD, MODIFY, DROP — 4 mins
- **9.25** DDL:DROP TABLE, TRUNCATE, DELETE — 3 mins
- **9.26** Data Control Language: GRANT, REVOKE — 10 mins
- **9.27** Learning resources — 3 mins

> ### Module 1: Live sessions

- **10.1** Code Walkthrough: Basic programming & bug-fixing in Python (for AI)
- **10.2** Code Walkthrough: Numerical algorithms using Python (for AI)
- **10.3** Code Walkthrough: Numerical methods in Python (for AI) -II
- **10.4** Code Walkthrough: Problems in Python [ Strings and Regex ]
- **10.5** Code Walkthrough: Problems in Python [ Strings and Regex -II]
- **10.6** Code Walkthrough: Dynamic Programming & Python in-built data-structures
- **10.7** Code Walkthrough: OOP in Python (for AI)- I
- **10.8** Code Walkthrough: OOP in Python for AI -II
- **10.9** Code Walkthrough: Pandas in Python
- **10.10** Code Walkthrough: Pandas& NumPy- II
- **10.11** How to code effectively and build a web-scraper
- **10.12** Using Web-APIs in Python for Machine Learning
- **10.13** How to use Github?
- **10.14** Multi-Processing & Multithreading in Python for AI/ML
- **10.15** Parallel programming for training and productionization of ML/AI systems [Flask & Gunicorn]
- **10.16** SQL: Importance and Sample Problems
- **10.17** Interactive Interview Session on Python programming for ML/AI
- **10.18** Programming problems for AI/ML/DataScience
- **10.19** Smart data acquisition for ML and AI
- **10.20** MongoDB for Documents (NoSQL)- Part 1
- **10.21** MongoDB for Documents (NoSQL)- Part 2

---

## Module 2: Data Science: Exploratory Data Analysis and Data Visualization

`10 chapters` · `140 lectures` · `1 assignments` · `20h 59m of video`

> ### Plotting for exploratory data analysis (EDA)

- **11.1** Introduction to IRIS dataset and 2D scatter plot — 26 mins
- **11.2** 3D scatter plot — 6 mins
- **11.3** Pair plots — 14 mins
- **11.4** Limitations of Pair Plots — 2 mins
- **11.5** Histogram and Introduction to PDF(Probability Density Function) — 17 mins
- **11.6** Univariate Analysis using PDF — 6 mins
- **11.7** CDF(Cumulative Distribution Function) — 15 mins
- **11.8** Mean, Variance and Standard Deviation — 17 mins
- **11.9** Median — 10 mins
- **11.10** Percentiles and Quantiles — 9 mins
- **11.11** IQR(Inter Quartile Range) and MAD(Median Absolute Deviation) — 6 mins
- **11.12** Box-plot with Whiskers — 9 mins
- **11.13** Violin Plots — 4 mins
- **11.14** Summarizing Plots, Univariate, Bivariate and Multivariate analysis — 6 mins
- **11.15** Multivariate Probability Density, Contour Plot — 9 mins
- **11.16** Assignment-1: Data Visualization with Haberman Dataset — 4 mins

> ### Linear Algebra

- **12.1** Why learn it ? — 4 mins
- **12.2** Introduction to Vectors(2-D, 3-D, n-D) , Row Vector and Column Vector — 14 mins
- **12.3** Dot Product and Angle between 2 Vectors — 14 mins
- **12.4** Projection and Unit Vector — 5 mins
- **12.5** Equation of a line (2-D), Plane(3-D) and Hyperplane (n-D), Plane Passing through origin, Normal to a Plane — 23 mins
- **12.6** Distance of a point from a Plane/Hyperplane, Half-Spaces — 10 mins
- **12.7** Equation of a Circle (2-D), Sphere (3-D) and Hypersphere (n-D) — 7 mins
- **12.8** Equation of an Ellipse (2-D), Ellipsoid (3-D) and Hyperellipsoid (n-D) — 6 mins
- **12.9** Square ,Rectangle — 6 mins
- **12.10** Hyper Cube,Hyper Cuboid — 3 mins
- **12.11** Revision Questions — 30 mins

> ### Probability and Statistics

- **13.1** Introduction to Probability and Statistics — 17 mins
- **13.2** Population and Sample — 7 mins
- **13.3** Gaussian/Normal Distribution and its PDF(Probability Density Function) — 27 mins
- **13.4** CDF(Cumulative Distribution function) of Gaussian/Normal distribution — 11 mins
- **13.5** Symmetric distribution, Skewness and Kurtosis — 25 mins
- **13.6** Standard normal variate (Z) and standardization — 6 mins
- **13.7** Kernel density estimation — 7 mins
- **13.8** Sampling distribution & Central Limit theorem — 19 mins
- **13.9** Q-Q plot:How to test if a random variable is normally distributed or not? — 23 mins
- **13.10** How distributions are used? — 17 mins
- **13.11** Chebyshev’s inequality — 20 mins
- **13.12** Discrete and Continuous Uniform distributions — 13 mins
- **13.13** How to randomly sample data points (Uniform Distribution) — 10 mins
- **13.14** Bernoulli and Binomial Distribution — 11 mins
- **13.15** Log Normal Distribution — 12 mins
- **13.16** Power law distribution — 12 mins
- **13.17** Box cox transform — 12 mins
- **13.18** Applications of non-gaussian distributions? — 26 mins
- **13.19** Co-variance — 14 mins
- **13.20** Pearson Correlation Coefficient — 13 mins
- **13.21** Spearman Rank Correlation Coefficient — 7 mins
- **13.22** Correlation vs Causation — 5 mins
- **13.23** How to use correlations? — 13 mins
- **13.24** Confidence interval (C.I) Introduction — 8 mins
- **13.25** Computing confidence interval given the underlying distribution — 11 mins
- **13.26** C.I for mean of a random variable — 14 mins
- **13.27** Confidence interval using bootstrapping — 18 mins
- **13.28** Hypothesis testing methodology, Null-hypothesis, p-value — 16 mins
- **13.29** Hypothesis Testing Intution with coin toss example — 27 mins
- **13.30** Resampling and permutation test — 15 mins
- **13.31** K-S Test for similarity of two distributions — 15 mins
- **13.32** Code Snippet K-S Test — 6 mins
- **13.33** Hypothesis testing: another example — 18 mins
- **13.34** Resampling and Permutation test: another example — 19 mins
- **13.35** How to use hypothesis testing? — 23 mins
- **13.36** Proportional Sampling — 18 mins
- **13.37** Revision Questions — 30 mins

> ### Interview Questions on Probability and statistics

- **14.1** Questions & Answers — 30 mins

> ### Dimensionality reduction and Visualization:

- **15.1** What is Dimensionality reduction? — 3 mins
- **15.2** Row Vector and Column Vector — 5 mins
- **15.3** How to represent a data set? — 4 mins
- **15.4** How to represent a dataset as a Matrix. — 7 mins
- **15.5** Data Preprocessing: Feature Normalisation — 20 mins
- **15.6** Mean of a data matrix — 6 mins
- **15.7** Data Preprocessing: Column Standardization — 16 mins
- **15.8** Co-variance of a Data Matrix — 24 mins
- **15.9** MNIST dataset (784 dimensional) — 20 mins
- **15.10** Code to Load MNIST Data Set — 12 mins

> ### PCA(principal component analysis)

- **16.1** Why learn PCA? — 4 mins
- **16.2** Geometric intuition of PCA — 14 mins
- **16.3** Mathematical objective function of PCA — 13 mins
- **16.4** Alternative formulation of PCA: Distance minimization — 10 mins
- **16.5** Eigen values and Eigen vectors (PCA): Dimensionality reduction — 23 mins
- **16.6** PCA for Dimensionality Reduction and Visualization — 10 mins
- **16.7** Visualize MNIST dataset — 5 mins
- **16.8** Limitations of PCA — 5 mins
- **16.9** PCA Code example — 19 mins
- **16.10** PCA for dimensionality reduction (not-visualization) — 15 mins

> ### (t-SNE)T-distributed Stochastic Neighbourhood Embedding

- **17.1** What is t-SNE? — 7 mins
- **17.2** Neighborhood of a point, Embedding — 7 mins
- **17.3** Geometric intuition of t-SNE — 9 mins
- **17.4** Crowding Problem — 8 mins
- **17.5** How to apply t-SNE and interpret its output — 38 mins
- **17.6** t-SNE on MNIST — 7 mins
- **17.7** Code example of t-SNE — 9 mins
- **17.8** Revision Questions — 30 mins

> ### Interview Questions on Dimensionality Reduction

- **18.1** Questions & Answers — 30 mins

> ### Statistical Testing and Experiments(Recorded LIVE Sessions)

- **19.1** Introduction to A/B Tests
- **19.2** How do we randomly split users ?
- **19.3** Metrics to compare Control and Treatment
- **19.4** Permutation-Resampling test
- **19.5** Q&A: Why permute/shuffle?
- **19.6** Q&A: How would shuffle programatically?
- **19.7** Quick Recap [till now]
- **19.8** Q&A + Polls with participants
- **19.9** Hypothesis testing: p-values, significance level & errors
- **19.10** Estimating the power of Permutation Tests
- **19.11** Code Walkthrough: Permutation Test from scratch.
- **19.12** Simulations using Code
- **19.13** Q&A with participants
- **19.14** Poll + Recap [till now]
- **19.15** Pros and Cons of Permutation Testing
- **19.16** Variation: Measuring clicks
- **19.17** Mann-Whitney-U Test
- **19.18** Code for Mann-Whitney-U test
- **19.19** Q&A with participants
- **19.20** Multiple testing and solutions
- **19.21** Remdesivir for Covid-19: Research Paper
- **19.22** Q&A with participants
- **19.23** Quick Recap (till now)
- **19.24** Bootstrapping for Confidence Intervals
- **19.25** Introduction to Multi-Arm-Bandits
- **19.26** Q&A with participants

> ### Module 2: Live Sessions

- **20.1** Exploratory Data Analysis
- **20.2** Which Plot to use when and where?
- **20.3** Interactive Interview Session on Data Analysis
- **20.4** Code Walkthrough: Seaborn module for plotting in AI/ML
- **20.5** Code Walkthrough: Live session on Basics of Linear Algebra for AI/ML
- **20.6** Hands on Probability and Stats
- **20.7** Code-Walkthrough: Probability and statistics- I
- **20.8** Code-Walkthrough: Probability and statistics-II
- **20.9** Q&A on Probability and Statistics
- **20.10** Code Walkthrough: Dimensionality Reduction for ML/AI
- **20.11** Tableau- Part 1
- **20.12** Tableau- Part 2
- **20.13** LIVE_ Interview Questions on Probability & Stats
- **20.14** Live Session (24th April 2022): Statistical Tests - Part 1
- **20.15** Live Session (01st May 2022): Statistical Tests - Part 2
- **20.16** Live Session (15th May 2022): Statistical Tests - Part 3
- **20.17** Live Session(07th August 2022): UMAP for visualising high dimensional data — 1 mins
- **20.18** Live Session(02nd Oct 2022): Recap of Math for ML
- **20.19** Live Session(16th Oct 2022): Recap of Probability and Statistics — 1 mins
- **20.20** Live Session (1st Jan 2023): Interview Session for Data Analyst roles

---

## Module 3: Foundations of Natural Language Processing and Machine Learning

`12 chapters` · `143 lectures` · `5 assignments` · `33h 14m of video`

> ### Real world problem: Predict rating given product reviews on Amazon

- **21.1** Dataset overview: Amazon Fine Food reviews(EDA) — 23 mins
- **21.2** Data Cleaning: Deduplication — 15 mins
- **21.3** Why convert text to a vector? — 14 mins
- **21.4** Bag of Words (BoW) — 18 mins
- **21.5** Text Preprocessing: Stemming, Stop-word removal, Tokenization, Lemmatization. — 15 mins
- **21.6** uni-gram, bi-gram, n-grams. — 9 mins
- **21.7** tf-idf (term frequency- inverse document frequency) — 22 mins
- **21.8** Why use log in IDF? — 14 mins
- **21.9** Word2Vec. — 16 mins
- **21.10** Avg-Word2Vec, tf-idf weighted Word2Vec — 9 mins
- **21.11** Bag of Words( Code Sample) — 19 mins
- **21.12** Text Preprocessing( Code Sample) — 11 mins
- **21.13** Bi-Grams and n-grams (Code Sample) — 5 mins
- **21.14** TF-IDF (Code Sample) — 6 mins
- **21.15** Word2Vec (Code Sample) — 12 mins
- **21.16** Avg-Word2Vec and TFIDF-Word2Vec (Code Sample) — 2 mins

> ### Classification And Regression Models: K-Nearest Neighbors

- **22.1** How “Classification” works? — 10 mins
- **22.2** Data matrix notation — 7 mins
- **22.3** Classification vs Regression (examples) — 6 mins
- **22.4** K-Nearest Neighbours Geometric intuition with a toy example — 12 mins
- **22.5** Failure cases of KNN — 7 mins
- **22.6** Distance measures: Euclidean(L2) , Manhattan(L1), Minkowski, Hamming — 20 mins
- **22.7** Cosine Distance & Cosine Similarity — 19 mins
- **22.8** How to measure the effectiveness of k-NN? — 16 mins
- **22.9** Test/Evaluation time and space complexity — 12 mins
- **22.10** KNN Limitations — 9 mins
- **22.11** Decision surface for K-NN as K changes — 23 mins
- **22.12** Overfitting and Underfitting — 12 mins
- **22.13** Need for Cross validation — 22 mins
- **22.14** K-fold cross validation — 18 mins
- **22.15** Visualizing train, validation and test datasets — 13 mins
- **22.16** How to determine overfitting and underfitting? — 19 mins
- **22.17** Time based splitting — 19 mins
- **22.18** k-NN for regression — 5 mins
- **22.19** Weighted k-NN — 8 mins
- **22.20** Voronoi diagram — 4 mins
- **22.21** Binary search tree — 16 mins
- **22.22** How to build a kd-tree — 17 mins
- **22.23** Find nearest neighbours using kd-tree — 13 mins
- **22.24** Limitations of Kd tree — 9 mins
- **22.25** Extensions — 3 mins
- **22.26** Hashing vs LSH — 10 mins
- **22.27** LSH for cosine similarity — 40 mins
- **22.28** LSH for euclidean distance — 13 mins
- **22.29** Probabilistic class label — 8 mins
- **22.30** Code Sample:Decision boundary . — 23 mins
- **22.31** Code Sample:Cross Validation — 13 mins
- **22.32** Revision Questions — 30 mins

> ### Interview Questions on K-NN(K Nearest Neighbour)

- **23.1** Questions & Answers — 30 mins

> ### Classification algorithms in various situations

- **24.1** Introduction — 5 mins
- **24.2** Imbalanced vs balanced dataset — 23 mins
- **24.3** Multi-class classification — 12 mins
- **24.4** k-NN, given a distance or similarity matrix — 9 mins
- **24.5** Train and test set differences — 22 mins
- **24.6** Impact of outliers — 7 mins
- **24.7** Local outlier Factor (Simple solution :Mean distance to Knn) — 13 mins
- **24.8** k distance — 4 mins
- **24.9** Reachability-Distance(A,B) — 8 mins
- **24.10** Local reachability-density(A) — 9 mins
- **24.11** Local outlier Factor(A) — 21 mins
- **24.12** Impact of Scale & Column standardization — 13 mins
- **24.13** Interpretability — 12 mins
- **24.14** Feature Importance and Forward Feature selection — 22 mins
- **24.15** Handling categorical and numerical features — 24 mins
- **24.16** Handling missing values by imputation — 21 mins
- **24.17** curse of dimensionality — 27 mins
- **24.18** Bias-Variance tradeoff — 24 mins
- **24.19** Intuitive understanding of bias-variance. — 7 mins
- **24.20** Revision Questions — 30 mins
- **24.21** best and worst case of algorithm — 6 mins

> ### Performance measurement of models

- **25.1** Accuracy — 15 mins
- **25.2** Confusion matrix, TPR, FPR, FNR, TNR — 25 mins
- **25.3** Precision and recall, F1-score — 10 mins
- **25.4** Receiver Operating Characteristic Curve (ROC) curve and AUC — 19 mins
- **25.5** Log-loss — 12 mins
- **25.6** R-Squared/Coefficient of determination — 14 mins
- **25.7** Median absolute deviation (MAD) — 5 mins
- **25.8** Distribution of errors — 7 mins
- **25.9** Revision Questions — 30 mins

> ### Interview Questions on Performance Measurement Models

- **26.1** Questions & Answers — 30 mins

> ### Naive Bayes

- **27.1** Conditional probability — 13 mins
- **27.2** Independent vs Mutually exclusive events — 7 mins
- **27.3** Bayes Theorem with examples — 18 mins
- **27.4** Exercise problems on Bayes Theorem — 30 mins
- **27.5** Naive Bayes algorithm — 26 mins
- **27.6** Toy example: Train and test stages — 26 mins
- **27.7** Naive Bayes on Text data — 16 mins
- **27.8** Laplace/Additive Smoothing — 24 mins
- **27.9** Log-probabilities for numerical stability — 11 mins
- **27.10** Bias and Variance tradeoff — 14 mins
- **27.11** Feature importance and interpretability — 10 mins
- **27.12** Imbalanced data — 14 mins
- **27.13** Outliers — 6 mins
- **27.14** Missing values — 3 mins
- **27.15** Handling Numerical features (Gaussian NB) — 13 mins
- **27.16** Multiclass classification — 2 mins
- **27.17** Similarity or Distance matrix — 3 mins
- **27.18** Large dimensionality — 3 mins
- **27.19** Best and worst cases — 8 mins
- **27.20** Code example — 8 mins
- **27.21** Revision Questions

> ### Logistic Regression

- **28.1** Geometric intuition of Logistic Regression — 31 mins
- **28.2** Sigmoid function: Squashing — 37 mins
- **28.3** Mathematical formulation of Objective function — 24 mins
- **28.4** Weight vector — 11 mins
- **28.5** L2 Regularization: Overfitting and Underfitting — 26 mins
- **28.6** L1 regularization and sparsity — 11 mins
- **28.7** Probabilistic Interpretation: Gaussian Naive Bayes — 20 mins
- **28.8** Loss minimization interpretation — 19 mins
- **28.9** hyperparameter Search: Grid search and random search — 16 mins
- **28.10** Column Standardization — 5 mins
- **28.11** Feature importance and Model interpretability — 14 mins
- **28.12** Collinearity of features — 14 mins
- **28.13** Train & Run time space & time complexity — 11 mins
- **28.14** Real world cases — 11 mins
- **28.15** Non-linearly separable data & feature engineering — 28 mins
- **28.16** Code sample: Logistic regression, GridSearchCV, RandomSearchCV — 23 mins
- **28.17** Extensions to Logistic Regression: Generalized linear models(GLM) — 8 mins

> ### Linear Regression

- **29.1** Geometric intuition of Linear Regression — 13 mins
- **29.2** Mathematical formulation — 14 mins
- **29.3** Real world Cases — 8 mins
- **29.4** Code sample for Linear Regression — 13 mins

> ### Solving Optimization Problems

- **30.1** Differentiation — 29 mins
- **30.2** Online differentiation tools — 8 mins
- **30.3** Maxima and Minima — 12 mins
- **30.4** Vector calculus: Grad — 10 mins
- **30.5** Gradient descent: geometric intuition — 19 mins
- **30.6** Learning rate — 8 mins
- **30.7** Gradient descent for linear regression — 8 mins
- **30.8** SGD algorithm — 9 mins
- **30.9** Constrained Optimization & PCA — 14 mins
- **30.10** Logistic regression formulation revisited — 6 mins
- **30.11** Why L1 regularization creates sparsity? — 17 mins
- **30.12** Revision questions — 30 mins

> ### Interview Questions on Logistic Regression and Linear Regression

- **31.1** Questions & Answers — 30 mins

> ### Module 3: Live Sessions

- **32.1** Code Walkthrough: Text Encodings for ML/AI
- **32.2** Dive deep into K-NN
- **32.3** Performance metrics Deep Dive
- **32.4** Interactive LIVE session: Logistic regression deep dive
- **32.5** Code Walkthrough: Optimization Methods for ML/AI
- **32.6** Code Walkthrough: Hyper-param Optimisation
- **32.7** Logistic Regression with Imbalanced data: A Geometric View
- **32.8** Linear Regression using Probability & Stats

---

## Module 4: Machine Learning - II( Supervised Learning Models)

`6 chapters` · `59 lectures` · `3 assignments` · `11h 32m of video`

> ### Support Vector Machines (SVM)

- **33.1** Geometric Intution — 20 mins
- **33.2** Mathematical derivation — 32 mins
- **33.3** Why we take values +1 and and -1 for Support vector planes — 9 mins
- **33.4** Loss function (Hinge Loss) based interpretation — 18 mins
- **33.5** Dual form of SVM formulation — 16 mins
- **33.6** kernel trick — 10 mins
- **33.7** Polynomial Kernel — 11 mins
- **33.8** RBF-Kernel — 22 mins
- **33.9** Domain specific Kernels — 6 mins
- **33.10** Train and run time complexities — 8 mins
- **33.11** nu-SVM: control errors and support vectors — 6 mins
- **33.12** SVM Regression — 8 mins
- **33.13** Cases — 9 mins
- **33.14** Code Sample — 14 mins
- **33.15** Revision Questions — 30 mins

> ### Interview Questions on Support Vector Machine

- **34.1** Questions & Answers — 30 mins

> ### Decision Trees

- **35.1** Geometric Intuition of decision tree: Axis parallel hyperplanes — 17 mins
- **35.2** Sample Decision tree — 8 mins
- **35.3** Building a decision Tree:Entropy — 19 mins
- **35.4** KL Divergence — 14 mins
- **35.5** Building a decision Tree:Information Gain — 10 mins
- **35.6** Building a decision Tree: Gini Impurity — 7 mins
- **35.7** Building a decision Tree: Constructing a DT — 21 mins
- **35.8** Building a decision Tree: Splitting numerical features — 8 mins
- **35.9** Feature standardization — 4 mins
- **35.10** Building a decision Tree:Categorical features with many possible values — 7 mins
- **35.11** Overfitting and Underfitting — 8 mins
- **35.12** Train and Run time complexity — 7 mins
- **35.13** Regression using Decision Trees — 9 mins
- **35.14** Cases — 12 mins
- **35.15** Code Samples — 9 mins
- **35.16** Revision Questions — 30 mins

> ### Interview Questions on decision Trees

- **36.1** Questions & Answers — 30 mins

> ### Ensemble Models

- **37.1** What are ensembles? — 6 mins
- **37.2** Bootstrapped Aggregation (Bagging) Intuition — 17 mins
- **37.3** Random Forest and their construction — 15 mins
- **37.4** Bias-Variance tradeoff — 7 mins
- **37.5** Bagging Train and run time complexity — 9 mins
- **37.6** Bagging:Code Sample — 4 mins
- **37.7** Extremely randomized trees — 8 mins
- **37.8** Random Forest :Cases — 6 mins
- **37.9** Boosting Intuition — 17 mins
- **37.10** Residuals, Loss functions and gradients — 13 mins
- **37.11** Gradient Boosting — 10 mins
- **37.12** Regularization by Shrinkage — 8 mins
- **37.13** Train and Run time complexity — 6 mins
- **37.14** XGBoost: Boosting + Randomization — 14 mins
- **37.15** AdaBoost: geometric intuition — 7 mins
- **37.16** Stacking models — 22 mins
- **37.17** Cascading classifiers — 15 mins
- **37.18** Kaggle competitions vs Real world — 9 mins
- **37.19** Revision Questions — 30 mins

> ### Module 4: Live Sessions

- **38.1** Code Walkthrough: Models in Scikit-Learn
- **38.2** Interview Questions on SVMs
- **38.3** Interview Questions on Boosting and Bagging
- **38.4** Attribution Models in Marketing
- **38.5** Attribution Models in Marketing-Part 2
- **38.6** LIVE_ Monte Carlo Simulations
- **38.7** Which ML/DL technique to use where?

---

## Module 5: Feature Engineering, Productionization and deployment of ML Models

`3 chapters` · `52 lectures` · `0 assignments` · `28h 11m of video`

> ### Featurization and Feature engineering.

- **39.1** Introduction — 15 mins
- **39.2** Moving window for Time Series Data — 15 mins
- **39.3** Fourier decomposition — 22 mins
- **39.4** Deep learning features: LSTM — 8 mins
- **39.5** Image histogram — 15 mins
- **39.6** Keypoints: SIFT. — 10 mins
- **39.7** Deep learning features: CNN — 4 mins
- **39.8** Relational data — 10 mins
- **39.9** Graph data — 12 mins
- **39.10** Indicator variables — 7 mins
- **39.11** Feature binning — 14 mins
- **39.12** Interaction variables — 9 mins
- **39.13** Mathematical transforms — 4 mins
- **39.14** Model specific featurizations — 9 mins
- **39.15** Feature orthogonality — 12 mins
- **39.16** Domain specific featurizations — 4 mins
- **39.17** Feature slicing — 10 mins
- **39.18** Kaggle Winners solutions — 7 mins

> ### Miscellaneous Topics

- **40.1** Calibration of Models:Need for calibration — 8 mins
- **40.2** Calibration Plots. — 17 mins
- **40.3** Platt’s Calibration/Scaling. — 8 mins
- **40.4** Isotonic Regression — 11 mins
- **40.5** Code Samples — 5 mins
- **40.6** Modeling in the presence of outliers: RANSAC — 13 mins
- **40.7** Retraining models periodically. — 8 mins
- **40.8** A/B testing. — 22 mins
- **40.9** VC dimension — 22 mins
- **40.10** Data Science Life cycle — 17 mins
- **40.11** Productionization and deployment of Machine Learning Models — 17 mins
- **40.12** Productionization and deployment + Spark — 96 mins
- **40.13** Hands on Live Session: Deploy an ML model using Flask APIs on AWS — 125 mins
- **40.14** Building web apps for ML/AI using StreamLit — 101 mins
- **40.15** Building web apps for ML/AI using StreamLit - II — 66 mins
- **40.16** ML Model productionization using Heroku — 120 mins
- **40.17** Amazon Sagemaker--Part 1 — 147 mins
- **40.18** Amazon sagemaker--part 2 — 161 mins
- **40.19** SageMaker Part 3: Distributed training and Deep Learning — 127 mins
- **40.20** SageMaker Part 4: Spark and Pipelines — 121 mins
- **40.21** Amazon SageMaker : Part 5 [Miscellaneous topics] — 97 mins
- **40.22** Design and Productionization of low latency ML systems — 93 mins

> ### Module 5: Live Sessions

- **41.1** Live session on Time Series Analysis and Forecasting
- **41.2** Testing and Debugging ML/AI systems end to end
- **41.3** Interview Questions on Productionization, Deployment
- **41.4** Interview Questions on Productionization and Deployment-PART II
- **41.5** KubeFlow: Architecture and Components
- **41.6** KubeFlow: Installation, Setup and Config
- **41.7** KubeFlow: Dashboard, Notebook Servers and Pipelines
- **41.8** KubeFlow: Pipelines using Kale, Rok, Katib and KfServing
- **41.9** Design and Productionization of low latency ML systems
- **41.10** Live Session(20th Feb 2022): Scenario based Interview Questions for ML engineer roles — 102 mins
- **41.11** Live Session(11th Sep 2022): ML Deployment Scenarios
- **41.12** Live Session(29th Nov 2022): Practical Time series Forecasting

---

## Module 6: Machine Learning Real-World Case Studies

`7 chapters` · `127 lectures` · `5 assignments` · `16h 47m of video`

> ### Case Study 1: Quora question Pair Similarity Problem

- **42.1** How to optimally learn from case-studies in the course? — 1 mins
- **42.2** Business/Real world problem : Problem definition — 6 mins
- **42.3** Business objectives and constraints. — 5 mins
- **42.4** Mapping to an ML problem : Data overview — 5 mins
- **42.5** Mapping to an ML problem : ML problem and performance metric. — 4 mins
- **42.6** Mapping to an ML problem : Train-test split — 5 mins
- **42.7** EDA: Basic Statistics. — 7 mins
- **42.8** EDA: Basic Feature Extraction — 10 mins
- **42.9** EDA: Text Preprocessing — 6 mins
- **42.10** EDA: Advanced Feature Extraction — 31 mins
- **42.11** EDA: Feature analysis. — 9 mins
- **42.12** EDA: Data Visualization: T-SNE. — 3 mins
- **42.13** EDA: TF-IDF weighted Word2Vec featurization. — 6 mins
- **42.14** ML Models :Loading Data — 6 mins
- **42.15** ML Models: Random Model — 7 mins
- **42.16** ML Models : Logistic Regression and Linear SVM — 11 mins
- **42.17** ML Models : XGBoost — 6 mins

> ### Case Study 2: Personalized Cancer Diagnosis

- **43.1** Business/Real world problem : Overview — 13 mins
- **43.2** Business objectives and constraints. — 11 mins
- **43.3** ML problem formulation :Data — 5 mins
- **43.4** ML problem formulation: Mapping real world to ML problem. — 19 mins
- **43.5** ML problem formulation :Train, CV and Test data construction — 4 mins
- **43.6** Exploratory Data Analysis:Reading data & preprocessing — 7 mins
- **43.7** Exploratory Data Analysis:Distribution of Class-labels — 7 mins
- **43.8** Exploratory Data Analysis: “Random” Model — 20 mins
- **43.9** Univariate Analysis:Gene feature — 34 mins
- **43.10** Univariate Analysis:Variation Feature — 19 mins
- **43.11** Univariate Analysis:Text feature — 15 mins
- **43.12** Machine Learning Models:Data preparation — 8 mins
- **43.13** Baseline Model: Naive Bayes — 23 mins
- **43.14** K-Nearest Neighbors Classification — 9 mins
- **43.15** Logistic Regression with class balancing — 10 mins
- **43.16** Logistic Regression without class balancing — 4 mins
- **43.17** Linear-SVM. — 6 mins
- **43.18** Random-Forest with one-hot encoded features — 7 mins
- **43.19** Random-Forest with response-coded features — 6 mins
- **43.20** Stacking Classifier — 8 mins
- **43.21** Majority Voting classifier — 5 mins

> ### Case Study 3:Facebook Friend Recommendation using Graph Mining

- **44.1** Problem definition. — 6 mins
- **44.2** Overview of Graphs: node/vertex, edge/link, directed-edge, path. — 11 mins
- **44.3** Data format & Limitations. — 9 mins
- **44.4** Mapping to a supervised classification problem. — 9 mins
- **44.5** Business constraints & Metrics. — 7 mins
- **44.6** EDA:Basic Stats — 12 mins
- **44.7** EDA:Follower and following stats. — 12 mins
- **44.8** EDA:Binary Classification Task — 16 mins
- **44.9** EDA:Train and test split. — 11 mins
- **44.10** Feature engineering on Graphs:Jaccard & Cosine Similarities — 15 mins
- **44.11** PageRank — 14 mins
- **44.12** Shortest Path — 4 mins
- **44.13** Connected-components — 12 mins
- **44.14** Adar Index — 12 mins
- **44.15** Kartz Centrality — 6 mins
- **44.16** HITS Score — 10 mins
- **44.17** SVD — 11 mins
- **44.18** Weight features — 6 mins
- **44.19** Modeling — 11 mins

> ### Case study 4:Taxi demand prediction in New York City

- **45.1** Business/Real world problem Overview — 9 mins
- **45.2** Objectives and Constraints — 11 mins
- **45.3** Mapping to ML problem :Data — 8 mins
- **45.4** Mapping to ML problem :dask dataframes — 12 mins
- **45.5** Mapping to ML problem :Fields/Features. — 6 mins
- **45.6** Mapping to ML problem :Time series forecasting/Regression — 8 mins
- **45.7** Mapping to ML problem :Performance metrics — 6 mins
- **45.8** Data Cleaning :Latitude and Longitude data — 4 mins
- **45.9** Data Cleaning :Trip Duration. — 7 mins
- **45.10** Data Cleaning :Speed. — 5 mins
- **45.11** Data Cleaning :Distance. — 2 mins
- **45.12** Data Cleaning :Fare — 6 mins
- **45.13** Data Cleaning :Remove all outliers/erroneous points — 3 mins
- **45.14** Data Preparation:Clustering/Segmentation — 19 mins
- **45.15** Data Preparation:Time binning — 5 mins
- **45.16** Data Preparation:Smoothing time-series data. — 5 mins
- **45.17** Data Preparation:Smoothing time-series data cont.. — 2 mins
- **45.18** Data Preparation: Time series and Fourier transforms. — 13 mins
- **45.19** Ratios and previous-time-bin values — 9 mins
- **45.20** Simple moving average — 8 mins
- **45.21** Weighted Moving average. — 5 mins
- **45.22** Exponential weighted moving average — 6 mins
- **45.23** Results. — 4 mins
- **45.24** Regression models :Train-Test split & Features — 8 mins
- **45.25** Linear regression. — 3 mins
- **45.26** Random Forest regression — 4 mins
- **45.27** Xgboost Regression — 2 mins
- **45.28** Model comparison — 6 mins

> ### Case study 5: Stackoverflow tag predictor

- **46.1** Business/Real world problem — 10 mins
- **46.2** Business objectives and constraints — 5 mins
- **46.3** Mapping to an ML problem: Data overview — 4 mins
- **46.4** Mapping to an ML problem:ML problem formulation. — 5 mins
- **46.5** Mapping to an ML problem:Performance metrics. — 21 mins
- **46.6** Hamming loss — 7 mins
- **46.7** EDA:Data Loading — 13 mins
- **46.8** EDA:Analysis of tags — 11 mins
- **46.9** EDA:Data Preprocessing — 11 mins
- **46.10** Data Modeling : Multi label Classification — 18 mins
- **46.11** Data preparation. — 8 mins
- **46.12** Train-Test Split — 2 mins
- **46.13** Featurization — 6 mins
- **46.14** Logistic regression: One VS Rest — 7 mins
- **46.15** Sampling data and tags+Weighted models. — 4 mins
- **46.16** Logistic regression revisited — 4 mins
- **46.17** Why not use advanced techniques — 3 mins

> ### Case Study 6: Microsoft Malware Detection

- **47.1** Business/real world problem :Problem definition — 6 mins
- **47.2** Business/real world problem :Objectives and constraints — 7 mins
- **47.3** Machine Learning problem mapping :Data overview. — 13 mins
- **47.4** Machine Learning problem mapping :ML problem — 12 mins
- **47.5** Machine Learning problem mapping :Train and test splitting — 4 mins
- **47.6** Exploratory Data Analysis :Class distribution. — 3 mins
- **47.7** Exploratory Data Analysis :Feature extraction from byte files — 8 mins
- **47.8** Exploratory Data Analysis :Multivariate analysis of features from byte files — 3 mins
- **47.9** Exploratory Data Analysis :Train-Test class distribution — 2 mins
- **47.10** ML models - using byte files only :Random Model — 11 mins
- **47.11** k-NN — 7 mins
- **47.12** Logistic regression — 5 mins
- **47.13** Random Forest and Xgboost — 7 mins
- **47.14** ASM Files :Feature extraction & Multiprocessing. — 11 mins
- **47.15** File-size feature — 2 mins
- **47.16** Univariate analysis — 3 mins
- **47.17** t-SNE analysis. — 2 mins
- **47.18** ML models on ASM file features — 8 mins
- **47.19** Models on all features :t-SNE — 2 mins
- **47.20** Models on all features :RandomForest and Xgboost — 4 mins

> ### Module 6: Live Sessions

- **48.1** Case Study 7: LIVE session on Ad Click Prediction
- **48.2** Case Study 7: Live Session: Ad-Click Prediction (contd.) and Performance metrics
- **48.3** Productionization of real-world ML systems
- **48.4** Scenario based Interview Questions for ML engineer roles
- **48.5** ML System Design For a Product Search Engine

---

## Module 7: Data Mining(Unsupervised Learning) and Recommender Systems + Real-World Case Studies

`9 chapters` · `110 lectures` · `4 assignments` · `18h 0m of video`

> ### Unsupervised learning/Clustering

- **49.1** What is Clustering? — 10 mins
- **49.2** Unsupervised learning — 4 mins
- **49.3** Applications — 16 mins
- **49.4** Metrics for Clustering — 19 mins
- **49.5** K-Means: Geometric intuition, Centroids — 8 mins
- **49.6** K-Means: Mathematical formulation: Objective function — 11 mins
- **49.7** K-Means Algorithm. — 11 mins
- **49.8** How to initialize: K-Means++ — 25 mins
- **49.9** Failure cases/Limitations — 11 mins
- **49.10** K-Medoids — 19 mins
- **49.11** Determining the right K — 5 mins
- **49.12** Code Samples — 7 mins
- **49.13** Time and space complexity — 4 mins

> ### Hierarchical clustering Technique

- **50.1** Agglomerative & Divisive, Dendrograms — 14 mins
- **50.2** Agglomerative Clustering — 9 mins
- **50.3** Proximity methods: Advantages and Limitations. — 24 mins
- **50.4** Time and Space Complexity — 4 mins
- **50.5** Limitations of Hierarchical Clustering — 5 mins
- **50.6** Code sample — 3 mins

> ### DBSCAN (Density based clustering) Technique

- **51.1** Density based clustering — 5 mins
- **51.2** MinPts and Eps: Density — 6 mins
- **51.3** Core, Border and Noise points — 7 mins
- **51.4** Density edge and Density connected points. — 6 mins
- **51.5** DBSCAN Algorithm — 11 mins
- **51.6** Hyper Parameters: MinPts and EpsA — 10 mins
- **51.7** Advantages and Limitations of DBSCAN — 9 mins
- **51.8** Time and Space Complexity — 3 mins
- **51.9** Code samples. — 3 mins
- **51.10** Revision Questions — 30 mins

> ### Recommender Systems and Matrix Factorization

- **52.1** Problem formulation: Movie reviews — 23 mins
- **52.2** Content based vs Collaborative Filtering — 11 mins
- **52.3** Similarity based Algorithms — 16 mins
- **52.4** Matrix Factorization: PCA, SVD — 23 mins
- **52.5** Matrix Factorization: NMF — 3 mins
- **52.6** Matrix Factorization for Collaborative filtering — 23 mins
- **52.7** Matrix Factorization for feature engineering — 9 mins
- **52.8** Clustering as MF — 21 mins
- **52.9** Hyperparameter tuning — 10 mins
- **52.10** Matrix Factorization for recommender systems: Netflix Prize Solution — 31 mins
- **52.11** Cold Start problem — 6 mins
- **52.12** Word vectors as MF — 20 mins
- **52.13** Eigen-Faces — 15 mins
- **52.14** Code example. — 11 mins
- **52.15** Revision Questions — 30 mins

> ### Interview Questions on Recommender Systems and Matrix Factorization.

- **53.1** Questions & Answers — 30 mins

> ### Case Study 8: Amazon fashion discovery engine(Content Based recommendation)

- **54.1** Problem Statement: Recommend similar apparel products in e-commerce using product descriptions and Images — 12 mins
- **54.2** Plan of action — 7 mins
- **54.3** Amazon product advertising API — 4 mins
- **54.4** Data folders and paths — 6 mins
- **54.5** Overview of the data and Terminology — 12 mins
- **54.6** Data cleaning and understanding:Missing data in various features — 22 mins
- **54.7** Understand duplicate rows — 9 mins
- **54.8** Remove duplicates : Part 1 — 12 mins
- **54.9** Remove duplicates: Part 2 — 15 mins
- **54.10** Text Pre-Processing: Tokenization and Stop-word removal — 10 mins
- **54.11** Stemming — 4 mins
- **54.12** Text based product similarity :Converting text to an n-D vector: bag of words — 14 mins
- **54.13** Code for bag of words based product similarity — 26 mins
- **54.14** TF-IDF: featurizing text based on word-importance — 17 mins
- **54.15** Code for TF-IDF based product similarity — 10 mins
- **54.16** Code for IDF based product similarity — 9 mins
- **54.17** Text Semantics based product similarity: Word2Vec(featurizing text based on semantic similarity) — 19 mins
- **54.18** Code for Average Word2Vec product similarity — 15 mins
- **54.19** TF-IDF weighted Word2Vec — 9 mins
- **54.20** Code for IDF weighted Word2Vec product similarity — 6 mins
- **54.21** Weighted similarity using brand and color — 9 mins
- **54.22** Code for weighted similarity — 7 mins
- **54.23** Building a real world solution — 5 mins
- **54.24** Deep learning based visual product similarity:ConvNets: How to featurize an image: edges, shapes, parts — 11 mins
- **54.25** Using Keras + Tensorflow to extract features — 8 mins
- **54.26** Visual similarity based product similarity — 6 mins
- **54.27** Measuring goodness of our solution :A/B testing — 7 mins
- **54.28** Assignment-24: Apparel Recommendation — 6 mins

> ### Case Study 9:Netflix Movie Recommendation System (Collaborative based recommendation)

- **55.1** Business/Real world problem:Problem definition — 6 mins
- **55.2** Objectives and constraints — 7 mins
- **55.3** Mapping to an ML problem:Data overview. — 4 mins
- **55.4** Mapping to an ML problem:ML problem formulation — 5 mins
- **55.5** Exploratory Data Analysis:Data preprocessing — 7 mins
- **55.6** Exploratory Data Analysis:Temporal Train-Test split. — 6 mins
- **55.7** Exploratory Data Analysis:Preliminary data analysis. — 15 mins
- **55.8** Exploratory Data Analysis:Sparse matrix representation — 8 mins
- **55.9** Exploratory Data Analysis:Average ratings for various slices — 7 mins
- **55.10** Exploratory Data Analysis:Cold start problem — 5 mins
- **55.11** Computing Similarity matrices:User-User similarity matrix — 20 mins
- **55.12** Computing Similarity matrices:Movie-Movie similarity — 6 mins
- **55.13** Computing Similarity matrices:Does movie-movie similarity work? — 6 mins
- **55.14** ML Models:Surprise library — 6 mins
- **55.15** Overview of the modelling strategy. — 8 mins
- **55.16** Data Sampling. — 5 mins
- **55.17** Google drive with intermediate files — 2 mins
- **55.18** Featurizations for regression. — 11 mins
- **55.19** Data transformation for Surprise. — 2 mins
- **55.20** Xgboost with 13 features — 6 mins
- **55.21** Surprise Baseline model. — 9 mins
- **55.22** Xgboost + 13 features +Surprise baseline model — 4 mins
- **55.23** Surprise KNN predictors — 15 mins
- **55.24** Matrix Factorization models using Surprise — 5 mins
- **55.25** SVD ++ with implicit feedback — 11 mins
- **55.26** Final models with all features and predictors. — 4 mins
- **55.27** Comparison between various models. — 4 mins
- **55.28** Assignment-18: Netflix prize — 5 mins

> ### High Level + End-End Design of a Music Recommendation system

- **56.1** High Level + End-End Design of a Music Recommendation system - I
- **56.2** High Level + End-End Design of a Music Recommendation system - II

> ### Module 7: Live Sessions

- **57.1** Building a simple Youtube recommendation using basic Math
- **57.2** Interview Questions on Clustering and Matrix Factorization
- **57.3** Live Session (22nd May 2022): Interview questions on Clustering
- **57.4** Live Session (29th May 2022): Interview Questions on Recommender Systems
- **57.5** Live Session(12th June 2022): Scenario based Interview Questions on RecSys — 1 mins
- **57.6** Live Session(21st August 2022): Design a Youtube Shorts/Reels/Tiktok feed recommender system — 1 mins
- **57.7** Live Session(21st August 2022): Design a Youtube Shorts/Reels/Tiktok feed recommender system — 1 mins

---

## Module 8: Neural Networks, Computer Vision and Deep Learning

`15 chapters` · `120 lectures` · `3 assignments` · `41h 11m of video`

> ### Deep Learning:Neural Networks.

- **58.1** History of Neural networks and Deep Learning. — 25 mins
- **58.2** How Biological Neurons work? — 8 mins
- **58.3** Growth of biological neural networks — 17 mins
- **58.4** Diagrammatic representation: Logistic Regression and Perceptron — 17 mins
- **58.5** Multi-Layered Perceptron (MLP). — 23 mins
- **58.6** Notation — 18 mins
- **58.7** Training a single-neuron model. — 28 mins
- **58.8** Training an MLP: Chain Rule — 40 mins
- **58.9** Training an MLP:Memoization — 14 mins
- **58.10** Backpropagation. — 26 mins
- **58.11** Activation functions — 17 mins
- **58.12** Vanishing Gradient problem. — 23 mins
- **58.13** Bias-Variance tradeoff. — 10 mins
- **58.14** Decision surfaces: Playground — 15 mins
- **58.15** Interview Questions — 30 mins

> ### Deep Learning: Deep Multi-layer perceptrons

- **59.1** Deep Multi-layer perceptrons:1980s to 2010s — 16 mins
- **59.2** Dropout layers & Regularization. — 21 mins
- **59.3** Rectified Linear Units (ReLU). — 28 mins
- **59.4** Weight initialization. — 24 mins
- **59.5** Batch Normalization. — 21 mins
- **59.6** Optimizers:Hill-descent analogy in 2D — 19 mins
- **59.7** Optimizers:Hill descent in 3D and contours. — 13 mins
- **59.8** SGD Recap — 18 mins
- **59.9** Batch SGD with momentum. — 25 mins
- **59.10** Nesterov Accelerated Gradient (NAG) — 8 mins
- **59.11** Optimizers:AdaGrad — 15 mins
- **59.12** Optimizers : Adadelta andRMSProp — 10 mins
- **59.13** Adam — 11 mins
- **59.14** Which algorithm to choose when? — 5 mins
- **59.15** Gradient Checking and clipping — 10 mins
- **59.16** Softmax and Cross-entropy for multi-class classification. — 25 mins
- **59.17** How to train a Deep MLP? — 8 mins
- **59.18** Auto Encoders. — 27 mins
- **59.19** Word2Vec :CBOW — 19 mins
- **59.20** Word2Vec: Skip-gram — 14 mins
- **59.21** Word2Vec :Algorithmic Optimizations. — 12 mins

> ### Deep Learning: Tensorflow and Keras.

- **60.1** Tensorflow and Keras overview — 23 mins
- **60.2** GPU vs CPU for Deep Learning. — 23 mins
- **60.3** Google Colaboratory. — 5 mins
- **60.4** Install TensorFlow — 6 mins
- **60.5** Online documentation and tutorials — 6 mins
- **60.6** Softmax Classifier on MNIST dataset. — 32 mins
- **60.7** MLP: Initialization — 11 mins
- **60.8** Model 1: Sigmoid activation — 22 mins
- **60.9** Model 2: ReLU activation. — 6 mins
- **60.10** Model 3: Batch Normalization. — 8 mins
- **60.11** Model 4 : Dropout. — 5 mins
- **60.12** MNIST classification in Keras. — 18 mins
- **60.13** Hyperparameter tuning in Keras. — 11 mins

> ### Deep Learning: Convolutional Neural Nets.

- **61.1** Biological inspiration: Visual Cortex — 18 mins
- **61.2** Convolution:Edge Detection on images. — 28 mins
- **61.3** Convolution:Padding and strides — 19 mins
- **61.4** Convolution over RGB images. — 11 mins
- **61.5** Convolutional layer. — 23 mins
- **61.6** Max-pooling. — 12 mins
- **61.7** CNN Training: Optimization — 9 mins
- **61.8** Receptive Fields and Effective Receptive Fields — 8 mins
- **61.9** Example CNN: LeNet [1998] — 10 mins
- **61.10** ImageNet dataset. — 6 mins
- **61.11** Data Augmentation. — 8 mins
- **61.12** Convolution Layers in Keras — 17 mins
- **61.13** AlexNet — 13 mins
- **61.14** VGGNet — 11 mins
- **61.15** Residual Network. — 22 mins
- **61.16** Inception Network. — 19 mins
- **61.17** What is Transfer learning. — 23 mins
- **61.18** Code example: Cats vs Dogs. — 15 mins
- **61.19** Code Example: MNIST dataset. — 6 mins
- **61.20** [Interview Question] How to build a face recognition system? — 1 mins

> ### Deep Learning: Long Short-term memory (LSTMs)

- **62.1** Why RNNs? — 23 mins
- **62.2** Recurrent Neural Network. — 29 mins
- **62.3** Training RNNs: Backprop. — 16 mins
- **62.4** Types of RNNs. — 14 mins
- **62.5** Need for LSTM/GRU. — 10 mins
- **62.6** LSTM. — 35 mins
- **62.7** GRUs. — 7 mins
- **62.8** Deep RNN. — 7 mins
- **62.9** Bidirectional RNN. — 12 mins
- **62.10** Code example : IMDB Sentiment classification — 33 mins

> ### Deep Learning: Generative Adversarial Networks (GANs)

- **63.1** Live session on Generative Adversarial Networks (GAN) — 124 mins

> ### Encoder-Decoder Models

- **64.1** LIVE: Encoder-Decoder Models — 82 mins

> ### Attention Models in Deep Learning

- **65.1** Attention Models in Deep Learning — 84 mins

> ### Deep Learning: Transformers and BERT

- **66.1** Transformers and BERT — 112 mins

> ### Deep Learning: Image Segmentation

- **67.1** Live session on Image Segmentation — 95 mins

> ### Deep Learning: Object Detection

- **68.1** Object Detection — 123 mins
- **68.2** Object Detection YOLO V3 — 103 mins

> ### Deep Learning: GPT-1, 2 and GPT-3 Models

- **69.1** GPT-1, 2 and GPT-3 Models — 130 mins

> ### OpenCV using Python

- **70.1** Code Walkthrough (OpenCV using Python)
- **70.2** Design and build a Smart Store

> ### Interview Questions on Deep Learning

- **71.1** Questions and Answers — 30 mins

> ### Module 8: Live Sessions

- **72.1** Code Walkthrough: Tensorflow 2.0 + Keras
- **72.2** Code Walkthrough: Tensorflow 2.0 + Keras --II
- **72.3** Code Walkthrough: DC-GANs and Gradient Tape
- **72.4** Code Walkthrough: Time Series forecasting using LSTMs/GRUs
- **72.5** Code Walkthrough Live Session: BERT and Fine-Tuning
- **72.6** Code Walkthrough: BERT- QuestionAnswering System
- **72.7** Code-Walkthrough: Transformers from scratch-I
- **72.8** Code-Walkthrough: Transformers from scratch-II
- **72.9** LIVE: Problem solving [Classification Algorithms]
- **72.10** Vision Transformers [from ICLR 2021]
- **72.11** Interview Questions on Deep Learning (NN, MLP, CNNs)
- **72.12** Interactive Interview Questions(from top product based companies)
- **72.13** Scenario based interview questions in AI/ML/DataScience
- **72.14** LIVE : Explainable AI [ LIME & SHAP ]
- **72.15** LIVE_ Explainable AI [ SHAP ]
- **72.16** Cutting-edge Recommender system for travel-booking by NVIDIA Engineers
- **72.17** Case-based Live: Deep Learning based Recommender Systems [ Algos + Design ]
- **72.18** Entity Embeddings @ LinkedIn, Amazon Session-1
- **72.19** Entity Embeddings @ LinkedIn, Amazon Session-2
- **72.20** Graph Neural Nets & Geometric Learning - PART 1
- **72.21** Graph Neural Nets & Geometric Learning --Part-2 — 112 mins
- **72.22** Live Session: Graph Neural Nets & Geometric Learning --Part-3 — 86 mins
- **72.23** Graph Neural Nets & Geometric Learning --Part-4 — 84 mins
- **72.24** Interactive Interview Session on NLP (Classical to SOTA)
- **72.25** Live Session(02nd July 2022): Interactive Interview Session on DL (MLPs) — 1 mins
- **72.26** Live Session(31st July 2022): Interview Session on CNNs — 1 mins
- **72.27** Live Session(28th Aug 2022): Knowledge Distillation in Deep Learning — 1 mins
- **72.28** Live Session(30th Oct 2022): Scenario based interview Questions — 1 mins
- **72.29** Live Session(04th Dec 2022): ML System Design of Image Search Engine — 1 mins
- **72.30** Live Session(22nd January 2023): Interview Session for ML Engineer roles

---

## Module 9: Deep Learning Real-World Case Studies

`7 chapters` · `44 lectures` · `2 assignments` · `10h 58m of video`

> ### Case Study 11: Human Activity Recognition

- **73.1** Human Activity Recognition Problem definition — 9 mins
- **73.2** Dataset understanding — 22 mins
- **73.3** Data cleaning & preprocessing — 4 mins
- **73.4** EDA:Univariate analysis. — 5 mins
- **73.5** EDA:Data visualization using t-SNE — 5 mins
- **73.6** Classical ML models. — 13 mins
- **73.7** Deep-learning Model. — 15 mins

> ### Case Study 10: Self Driving Car

- **74.1** Self Driving Car :Problem definition. — 14 mins
- **74.2** Datasets. — 9 mins
- **74.3** Data understanding & Analysis :Files and folders. — 5 mins
- **74.4** Dash-cam images and steering angles. — 6 mins
- **74.5** Split the dataset: Train vs Test — 3 mins
- **74.6** EDA: Steering angles — 6 mins
- **74.7** Mean Baseline model: simple — 5 mins
- **74.8** Deep-learning model:Deep Learning for regression: CNN, CNN+RNN — 10 mins
- **74.9** Batch load the dataset. — 6 mins
- **74.10** NVIDIA’s end to end CNN model. — 18 mins
- **74.11** Train the model. — 13 mins
- **74.12** Test and visualize the output. — 11 mins
- **74.13** Extensions. — 5 mins

> ### Case Study 12: Music Generation using Deep-Learning

- **75.1** Real-world problem — 15 mins
- **75.2** Music representation — 18 mins
- **75.3** Char-RNN with abc-notation :Char-RNN model — 23 mins
- **75.4** Char-RNN with abc-notation :Data preparation. — 41 mins
- **75.5** Char-RNN with abc-notation:Many to Many RNN ,TimeDistributed-Dense layer — 18 mins
- **75.6** Char-RNN with abc-notation : State full RNN — 12 mins
- **75.7** Char-RNN with abc-notation :Model architecture,Model training. — 13 mins
- **75.8** Char-RNN with abc-notation :Music generation. — 11 mins
- **75.9** Char-RNN with abc-notation :Generate tabla music — 3 mins
- **75.10** MIDI music generation. — 4 mins
- **75.11** Survey blog: — 5 mins

> ### Case Study 13: Semantic Search Engine for Q&A [Design + Code]

- **76.1** High Level Design of the Solution
- **76.2** Sentence Vectors and Docker Containerisation
- **76.3** Indexing using ElasticSearch
- **76.4** Deployment using Flask APIs, Docker and ElasticSearch

> ### Case Study 14: Building a Smart Gym Assistant from scratch

- **77.1** Building a Smart Gym Assistant from scratch- Part 1 — 130 mins
- **77.2** Building a Smart Gym Assistant from scratch- Part II — 121 mins

> ### Interview Questions

- **78.1** Revision Questions — 30 mins
- **78.2** External resources for Interview Questions — 30 mins

> ### Module 9: Live Sessions

- **79.1** High-level design of a self driving system
- **79.2** Music Recommendation System
- **79.3** Speaker identification using audio + Siamese Networks
- **79.4** Data Quality and Verification @ Uber, Netflix and Amazon
- **79.5** Data Quality and Verification @ Uber, Netflix and Amazon -- Part-2

---

## Module 10: Misc Topics: Spark for ML, Big Data, Reinforcement Learning, ML Design

`4 chapters` · `28 lectures` · `0 assignments` · `2h 57m of video`

> ### Machine Learning High-Level Design

- **80.1** Machine Learning design: Search engine for Q&A
- **80.2** ML System Design: Feature Store — 31 mins

> ### Sample Interview and Conceptual Questions [AUDIO]

- **81.1** Sample Interview and Conceptual Questions [AUDIO]

> ### Reinforcement Learning

- **82.1** Applications of RL — 10 mins
- **82.2** Problem Forumulation & Terminology — 8 mins
- **82.3** Bellman Equation — 20 mins
- **82.4** Dynamic Programming and RL — 11 mins
- **82.5** Markov Decision Process (MDP) — 12 mins
- **82.6** Q-function — 7 mins
- **82.7** Temporal Difference — 11 mins
- **82.8** Deep Q Learning: Intuition — 5 mins
- **82.9** Q&A — 37 mins

> ### Module 10: Live Sessions

- **83.1** An overview of AI Algorithms ( a 10,000 feet view)
- **83.2** Introduction to Big data for ML and AI
- **83.3** Big-Data & Cloud Storage for ML/AI Applications
- **83.4** Spark for Data Science and Machine Learning [Architecture and Programming model]- I
- **83.5** Spark for Data Science and Machine Learning [Setup + Code walkthroughs]-II
- **83.6** Spark for Data Science and Machine Learning [ML Lib and ML Pipelines]-III
- **83.7** How to Build a Chatbot?
- **83.8** Design and build a Chatbot from Scratch
- **83.9** Design and build a Chatbot from Scratch-Part 2
- **83.10** How to build IoT + AI systems
- **83.11** LIVE: How to Crack ML Competitions
- **83.12** Live: Effective communication for DS and MLEs
- **83.13** Sample Interview and Conceptual Questions [AUDIO]
- **83.14** Various roles in an ML/DataScience team — 13 mins
- **83.15** Client management for AI Projects — 11 mins
- **83.16** Live Session(17th July 2022): ML System design Interview session — 1 mins

---
