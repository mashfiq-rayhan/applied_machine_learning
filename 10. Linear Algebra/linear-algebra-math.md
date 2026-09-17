<style>
@import url('https://fonts.googleapis.com/css2?family=Play:wght@400;700&display=swap');

:root {
  --la-ink: #3f6386;
  --la-teal: #3f6386;
  --la-teal-soft: #e8f6f7;
  --la-coral: #9333ea;
  --la-coral-soft: #fff1ed;
  --la-amber: #9a6b16;
  --la-amber-soft: #fff8e6;
  --la-line: #5b5c5c;
  --la-surface: #f7faf9;
  --la-text: #c9c9c9;
}

*,
*::before,
*::after {
  font-family: 'Play', sans-serif !important;
}

pre,
pre code {
  font-family: Consolas, 'Courier New', monospace !important;
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

blockquote {
  background: #00070e;
  border-left: 5px solid var(--la-teal) !important;
  color: var(--la-text);
  padding: 0.75em 1em;
}

table {
  border: 1px solid var(--la-line);
  border-radius: 8px;
  overflow: hidden;
}

th {
  background: #00070e;
  color: var(--la-text);
}

td {
  color: var(--la-text);
}

tr:nth-child(even) {
  background: #17283a;
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
}

.katex,
.katex * {
  color: #9b9a9a !important;
}
</style>

# Linear Algebra

> **A geometric and mathematical toolkit for Machine Learning**
>
> Linear algebra gives us a language for representing data, measuring relationships, and describing the spaces where ML models operate.

## At a Glance

| Idea       | Intuition                  | ML connection                               |
| ---------- | -------------------------- | ------------------------------------------- |
| **Scalar** | One number                 | A single value or parameter                 |
| **Vector** | An ordered list of values  | One observation or feature embedding        |
| **Matrix** | A table of values          | A dataset, transformation, or layer weights |
| **Tensor** | A higher-dimensional array | Images, batches, and deep-learning data     |

### The Core Progression

$$
\boxed{
\text{Scalar}
\rightarrow
\text{Vector}
\rightarrow
\text{Matrix}
\rightarrow
\text{Higher-Dimensional Space}
}
$$

### How to Read These Notes

1. **Build the objects:** scalars, vectors, matrices, and geometric shapes.
2. **Learn the operations:** norms, dot products, projections, and distances.
3. **Connect geometry to ML:** hyperplanes, decision boundaries, and feature spaces.
4. **Finish with practice:** formula summaries and revision questions.

> **Study tip:** For each formula, ask what it measures geometrically and where it appears in an ML model.

Linear Algebra is one of the fundamental mathematical foundations of **Machine Learning, Deep Learning, Computer Vision, Optimization, and Data Science**.

In Machine Learning, data is frequently represented using:

- **Scalars** → single numbers
- **Vectors** → lists of numbers
- **Matrices** → collections of vectors
- **Tensors** → higher-dimensional arrays

Many ML operations can ultimately be expressed using **vector and matrix operations**.

---

## 10.1 Why Learn Linear Algebra?

Linear Algebra allows us to represent and manipulate data mathematically.

For example, a person's features can be represented as:

$$
\mathbf{x} =
\begin{bmatrix}
\text{age}\\
\text{height}\\
\text{weight}\\
\text{income}
\end{bmatrix}
$$

A dataset containing many observations can then be represented as a matrix:

$$
X =
\begin{bmatrix}
x_{11} & x_{12} & x_{13} \\
x_{21} & x_{22} & x_{23} \\
\vdots & \vdots & \vdots \\
x_{n1} & x_{n2} & x_{n3}
\end{bmatrix}
$$

Linear Algebra is used throughout ML:

| ML Concept        | Linear Algebra                   |
| ----------------- | -------------------------------- |
| Dataset           | Matrix                           |
| Features          | Vectors / Matrix columns         |
| Linear Regression | Matrix operations                |
| Neural Networks   | Matrix multiplication            |
| PCA               | Eigenvectors / matrices          |
| Computer Vision   | Image matrices / tensors         |
| Embeddings        | High-dimensional vectors         |
| Optimization      | Vector calculus + linear algebra |
| Similarity        | Dot product / cosine similarity  |

The goal is therefore not simply to memorize formulas, but to understand **how geometric objects and data are represented mathematically**.


## 10.2 Introduction to Vectors (2D, 3D, nD)

**Row Vector and Column Vector**

### Point / Vector

A point (or vector) in space can be represented by an ordered list of numbers called its **coordinates**.

### 2-Dimensional Vector (2D)

$$
\mathbf{p} =
\begin{bmatrix}
2 & 3
\end{bmatrix}
$$

$$
\begin{bmatrix}
x_1 & x_2
\end{bmatrix}
$$

**Geometrical interpretation:**

```
        x₂
         ↑
         |
       3 |        • P(2, 3)
         |
         |
         +---------------→ x₁
        (0,0)   2
```

The vector $\mathbf{p}$ starts at the origin $(0,0)$ and ends at the point $P(2,3)$.

### 3-Dimensional Vector (3D)

$$
\mathbf{q} =
\begin{bmatrix}
2 & 3 & 5
\end{bmatrix}
$$

$$
\begin{bmatrix}
x_1 & x_2 & x_3
\end{bmatrix}
$$

**Geometrical interpretation:**

```
            x₂
             ↑
             |
             |     • q(2,3,5)
             |
             +--------→ x₁
            /
           /
          /
         ↙
         x₃
```

The vector $\mathbf{q}$ lives in three-dimensional space and has components along the $x_1$, $x_2$, and $x_3$ axes.

### n-Dimensional Vector (nD)

In general, an $n$-dimensional vector is written as:

$$
\mathbf{x} =
\begin{bmatrix}
x_1 & x_2 & x_3 & \dots & x_n
\end{bmatrix}
$$

**Example:**

$$
\mathbf{x} =
\begin{bmatrix}
2 & 3 & 9 & 1 & 5 & \dots & n
\end{bmatrix}
$$

Even though we cannot visualize dimensions higher than 3, the mathematical rules for vectors remain the same in any number of dimensions.

The vector $\mathbf{p}$ starts at the origin $(0,0)$ and ends at the point $P(2,3)$.

**Note:**  
The notation used above ($[ \cdot ]$) represents a **row vector**.  
A **column vector** is written vertically:

$$
\mathbf{p} =
\begin{bmatrix}
2 \\
3
\end{bmatrix},
\qquad
\mathbf{q} =
\begin{bmatrix}
2 \\
3 \\
5
\end{bmatrix},
\qquad
\mathbf{x} =
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{bmatrix}
$$

Both forms are common; the choice depends on the context (especially in matrix multiplication).

### Distance of a Point from the Origin

The **distance** (or **magnitude** / **length** / **norm**) of a vector is the straight-line distance from the origin to the point represented by that vector.

### 2-Dimensional (2D)

Consider the point $ P(a, b) $.

$$
d = \text{distance from origin to } P = \sqrt{a^2 + b^2}
$$

**Geometric illustration:**

```
        x₂
         ↑
         |
         |
         |         • P(a, b)
       b |       /
         |     / d
         |   /
         | /
         +---------`-----------→ x₁
    (0,0)     a
```

This is simply the **Pythagorean theorem** applied to the right triangle formed by the coordinates.

### 3-Dimensional Case (3D)

Consider the point $ P(a, b, c) $.

$$
d' = \sqrt{a^2 + b^2 + c^2}
$$

**Geometric illustration:**

```
            x₂
             ↑
             |
             |
             |     • P(a, b, c)
             |    /
             |   /
             |  / d'
             | /
             +------------------→ x₁
            /
           /
          /
         /
        /
      ↙ x₃
```

The formula is the natural extension of the 2D case into three dimensions.

### n-Dimensional Case (nD)

For a general point (or vector) in $ n $-dimensional space:

$$
\mathbf{P} = [a_1,\ a_2,\ \dots,\ a_n]
$$

the distance from the origin is:

$$
Q = \sqrt{a_1^2 + a_2^2 + \cdots + a_n^2} = \sqrt{\sum_{i=1}^{n} a_i^2}
$$

This is called the **Euclidean norm** (or $\ell_2$-norm) of the vector.

**Summary Table**

| Dimension | Point / Vector                   | Distance from Origin           |
| --------- | -------------------------------- | ------------------------------ |
| 2D        | $ P(a,b) $                       | $ \sqrt{a^2 + b^2} $           |
| 3D        | $ P(a,b,c) $                     | $ \sqrt{a^2 + b^2 + c^2} $     |
| nD        | $ \mathbf{P} = [a_1,\dots,a_n] $ | $ \sqrt{\sum\_{i=1}^n a_i^2} $ |

This quantity is extremely important — it is the foundation for defining unit vectors, angles between vectors, and many operations in linear algebra and machine learning.

### Distance Between Two Points

The distance between two points is the length of the straight line connecting them. It is calculated using the **Euclidean distance** formula.

### 2-Dimensional Case (2D)

Let the two points be:

- $ P(a_1, a_2) $
- $ Q(b_1, b_2) $

$$
d = \sqrt{(a_1 - b_1)^2 + (a_2 - b_2)^2}
$$

**Geometric illustration:**

```
        x₂
         ↑
         |
         |
    a₂   |  • P(a₁, a₂)
         |    \
         |      \ d
         |        \
    b₂   |          • Q(b₁, b₂)
         |
         +-----------------------→ x₁
    (0,0)   a₁      b₁
```

(The horizontal difference is $ a_1 - b_1 $ and the vertical difference is $ a_2 - b_2 $.)

### 3-Dimensional Case (3D)

Let the two points be:

- $ P(a_1, a_2, a_3) $
- $ Q(b_1, b_2, b_3) $

$$
d = \sqrt{(a_1 - b_1)^2 + (a_2 - b_2)^2 + (a_3 - b_3)^2}
$$

### n-Dimensional Case (nD)

In general, for two points in $ n $-dimensional space:

$$
\begin{align*}
P &= (a_1, a_2, \dots, a_n) \\
Q &= (b_1, b_2, \dots, b_n)
\end{align*}
$$

the distance is:

$$
d = \sqrt{\sum_{i=1}^{n} (a_i - b_i)^2}
$$

### Row Vector and Column Vector

A vector can be written in two common forms:

**Row Vector** (written horizontally):

$$
A_1 = [a_1,\ a_2,\ \dots,\ a_n]_{1 \times n}
$$

**Column Vector** (written vertically):

$$
A_2 = \begin{bmatrix}
a_1 \\
a_2 \\
\vdots \\
a_n
\end{bmatrix}_{n \times 1}
$$

**Note:**

- A row vector is a $ 1 \times n $ matrix.
- A column vector is an $ n \times 1 $ matrix.
- In most mathematical contexts (especially linear algebra), **column vectors** are preferred by default.

### Matrix

A general matrix with $ m $ rows and $ n $ columns is written as:

$$
A_{m \times n} =
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}_{m \times n}
$$

### 10.3 Dot Product and Angle Between Two Vectors

Let two vectors in $ n $-dimensional space be:

$$
\mathbf{a} = [a_1,\ a_2,\ \dots,\ a_n], \qquad
\mathbf{b} = [b_1,\ b_2,\ \dots,\ b_n]
$$

### Vector Addition

$$
\mathbf{a} + \mathbf{b} = [(a_1 + b_1),\ (a_2 + b_2),\ \dots,\ (a_n + b_n)]
$$

### Dot Product (Scalar Product)

The **dot product** of two vectors is defined as:

$$
\mathbf{a} \cdot \mathbf{b} = a_1 b_1 + a_2 b_2 + \cdots + a_n b_n = \sum_{i=1}^{n} a_i b_i
$$

**Matrix notation:**

If we treat $\mathbf{a}$ as a row vector and $\mathbf{b}$ as a column vector, then:

$$
\mathbf{a} = \begin{bmatrix}
a_1 \\
a_2 \\
\vdots \\
a_n
\end{bmatrix} \qquad

\mathbf{a}^\top = [a_1\ a_2\ \dots\ a_n] \qquad

\mathbf{b} = \begin{bmatrix}
b_1 \\
b_2 \\
\vdots \\
b_n
\end{bmatrix}
$$

$$
\mathbf{a} \cdot \mathbf{b}
= [a_1\ a_2\ \dots\ a_n]
\begin{bmatrix}
b_1 \\
b_2 \\
\vdots \\
b_n
\end{bmatrix}
= \mathbf{a}^\top \mathbf{b}
$$

(where $\mathbf{a}^\top$ means the transpose of $\mathbf{a}$).

### Important Convention

> **By default, if anyone mentions a vector, it is assumed to be a column vector.**

That is:

$$
\mathbf{a} =
\begin{bmatrix}
a_1 \\
a_2 \\
\vdots \\
a_n
\end{bmatrix}
$$

This is the standard convention in linear algebra and most mathematical literature.

### Dot Product – Matrix Form & Geometric Meaning

Let two column vectors be:

$$
\mathbf{a} =
\begin{bmatrix}
a_1 \\
a_2 \\
\vdots \\
a_n
\end{bmatrix},
\qquad
\mathbf{b} =
\begin{bmatrix}
b_1 \\
b_2 \\
\vdots \\
b_n
\end{bmatrix}
$$

Then the transpose of $\mathbf{a}$ is the row vector:

$$
\mathbf{a}^\top = [a_1,\ a_2,\ \dots,\ a_n]
$$

**Dot product in matrix form:**

$$
\mathbf{a} \cdot \mathbf{b} = \mathbf{a}^\top \mathbf{b} = \sum_{i=1}^{n} a_i b_i
$$

### Geometric Interpretation of the Dot Product

$$
\mathbf{a} \cdot \mathbf{b} = \|\mathbf{a}\| \|\mathbf{b}\| \cos\theta
$$

where:

- $\|\mathbf{a}\|$ = length (magnitude) of vector $\mathbf{a}$
- $\|\mathbf{b}\|$ = length of vector $\mathbf{b}$
- $\theta$ = angle between the two vectors

**Length of a vector (2D example):**

$$
\|\mathbf{a}\| = \sqrt{a_1^2 + a_2^2}
$$

**Diagram (2D):**

```
        x₂
         ↑
         |
         |     a (a₁, a₂)
         |    /
         |   /  ||a||
         |  / θ
         | /________→ b (b₁, b₂)
         |/   ||b||
         +-------------------------→ x₁
        (0,0)
```

### Formula for the Angle Between Two Vectors

From the geometric definition:

$$
\mathbf{a} \cdot \mathbf{b} = a_1 b_1 + a_2 b_2 = \|\mathbf{a}\| \|\mathbf{b}\| \cos\theta
$$

Solving for $\theta$:

$$
\theta = \cos^{-1}\left( \frac{a_1 b_1 + a_2 b_2}{\|\mathbf{a}\| \|\mathbf{b}\|} \right)
$$

**General n-dimensional formula:**

$$
\theta_{(\mathbf{a},\mathbf{b})} = \cos^{-1}\left(
\frac{\displaystyle\sum_{i=1}^{n} a_i b_i}{\|\mathbf{a}\| \|\mathbf{b}\|}
\right)
= \cos^{-1}\left(
\frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}
\right)
$$

### Special Case: Orthogonal (Perpendicular) Vectors

If the angle $\theta = 90^\circ$, then $\cos 90^\circ = 0$, so:

$$
\mathbf{a} \cdot \mathbf{b} = 0
$$

**Conclusion:**

$$
\mathbf{a} \cdot \mathbf{b} = 0 \quad \Longleftrightarrow \quad \mathbf{a} \perp \mathbf{b}
$$

(In n dimensions this is written as $\displaystyle\sum_{i=1}^{n} a_i b_i = 0$.)

**Key Formulas at a Glance**

| Concept                 | Formula                                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------------------ |
| Dot product (algebraic) | $\mathbf{a}\cdot\mathbf{b} = \sum a_i b_i = \mathbf{a}^\top\mathbf{b}$                           |
| Dot product (geometric) | $\mathbf{a}\cdot\mathbf{b} = \|\mathbf{a}\|\|\mathbf{b}\|\cos\theta$                             |
| Angle between vectors   | $\theta = \cos^{-1}\left(\dfrac{\mathbf{a}\cdot\mathbf{b}}{\|\mathbf{a}\|\|\mathbf{b}\|}\right)$ |
| Perpendicular condition | $\mathbf{a}\cdot\mathbf{b} = 0 \implies \mathbf{a} \perp \mathbf{b}$                             |

**This is the next page of your lecture notes.**

**Topics:**

- Squared length of a vector ($\mathbf{a} \cdot \mathbf{a}$)
- Section **10.4 – Projection and Unit Vector**
- Scalar projection of one vector onto another

Here is a clean and polished Markdown version:

### Length (Norm) of a Vector Revisited

$$
\mathbf{a} \cdot \mathbf{a} = a_1^2 + a_2^2 + \cdots + a_n^2 = \|\mathbf{a}\|^2
$$

Therefore the length (Euclidean norm) of the vector is:

$$
\|\mathbf{a}\| = \sqrt{a_1^2 + a_2^2 + \cdots + a_n^2} = \sqrt{\mathbf{a} \cdot \mathbf{a}}
$$

```
          ↑
          |     a
          |    /
          |   /  ||a||
          |  /
          | /
          +--------→
```

### 10.4 Projection and Unit Vector

#### Scalar Projection of Vector $\mathbf{a}$ onto Vector $\mathbf{b}$

The **scalar projection** (or component) of $\mathbf{a}$ onto $\mathbf{b}$ is the length of the shadow of $\mathbf{a}$ when light shines perpendicular to $\mathbf{b}$.

**Diagram:**

```
              a
             /
            / θ
           /
          /________→ b
         /
        d (projection)
```

Let $ d $ be the scalar projection of $\mathbf{a}$ onto $\mathbf{b}$.

From trigonometry:

$$
d = \|\mathbf{a}\| \cos\theta
$$

Using the geometric definition of the dot product:

$$
\cos\theta = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}
$$

Substitute:

$$
d = \|\mathbf{a}\| \cdot \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|} = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{b}\|}
$$

**Final formula for the scalar projection of $\mathbf{a}$ onto $\mathbf{b}$:**

$$
\text{proj}_{\mathbf{b}} \mathbf{a}
= d
= \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{b}\|}
= \frac{\displaystyle\sum_{i=1}^{n} a_i b_i}{\|\mathbf{b}\|}
= \frac{\|\mathbf{a}\| \|\mathbf{b}\| \cos\theta}{\|\mathbf{b}\|}
= \|\mathbf{a}\| \cos\theta
$$

**Summary of Important Relations**

| Quantity                                          | Formula                                             |
| ------------------------------------------------- | --------------------------------------------------- |
| Squared length                                    | $\|\mathbf{a}\|^2 = \mathbf{a}\cdot\mathbf{a}$      |
| Length of vector                                  | $\|\mathbf{a}\| = \sqrt{\mathbf{a}\cdot\mathbf{a}}$ |
| Scalar projection of $\mathbf{a}$ on $\mathbf{b}$ | $\dfrac{\mathbf{a}\cdot\mathbf{b}}{\|\mathbf{b}\|}$ |

### Unit Vector

A **unit vector** $\hat{\mathbf{a}}$ in the direction of a vector $\mathbf{a}$ has two properties:

1. It has the **same direction** as $\mathbf{a}$
2. Its length is **exactly 1**: $\|\hat{\mathbf{a}}\| = 1$

```
        x₂
         ↑
         |
         |
         |     a (a₁, a₂)
         |    /
         |   /  ||a||
         |  /
         | /  â  (unit vector)
         +------------------------→ x₁
```

## 10.5 Equation of a Line (2D), Plane (3D) and Hyperplane (nD)

### 2D – Equation of a Line

Standard forms:

$$
y = mx + c
$$

$$
ax + by + c = 0
$$

$$
\omega_1 x_1 + \omega_2 x_2 + \omega_0 = 0
$$

Solving for $x_2$:

$$
x_2 = \left(-\frac{\omega_1}{\omega_2}\right)x_1 + \left(-\frac{\omega_0}{\omega_2}\right)
$$

which is the familiar slope-intercept form $y = mx + c$.

### 3D – Equation of a Plane

$$
ax + by + cz + d = 0
$$

or

$$
\omega_1 x_1 + \omega_2 x_2 + \omega_3 x_3 + \omega_0 = 0
$$

### nD – Equation of a Hyperplane

$$
\omega_0 + \omega_1 x_1 + \omega_2 x_2 + \cdots + \omega_n x_n = 0
$$

In compact form:

$$
\omega_0 + \sum_{i=1}^{n} \omega_i x_i = 0
$$

**Matrix / Vector form:**

$$
\boldsymbol{\omega} =
\begin{bmatrix}
\omega_1 \\
\omega_2 \\
\vdots \\
\omega_n
\end{bmatrix},
\quad
\mathbf{x} =
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{bmatrix}
$$

$$
\omega_0 + \boldsymbol{\omega}^\top \mathbf{x}
= \omega_0 + [\omega_1\ \omega_2\ \dots\ \omega_n]
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{bmatrix}
= 0
$$

$$
\omega_0 + \boldsymbol{\omega}^\top \mathbf{x} = 0
$$

### Special Case: Hyperplane Passing Through the Origin

If the hyperplane passes through the origin, then $\omega_0 = 0$:

$$
\boldsymbol{\omega}^\top \mathbf{x} = 0
$$

| Dimension | Equation through origin                                   |
| --------- | --------------------------------------------------------- |
| 2D        | $\omega_1 x_1 + \omega_2 x_2 = 0$                         |
| 3D        | $\omega_1 x_1 + \omega_2 x_2 + \omega_3 x_3 = 0$          |
| nD        | $\omega_1 x_1 + \omega_2 x_2 + \cdots + \omega_n x_n = 0$ |
|           | $\boldsymbol{\omega}^\top \mathbf{x} = 0$                 |

If it does **not** pass through the origin:

$$
\boldsymbol{\omega}^\top \mathbf{x} + \omega_0 = 0
$$

### Normal Vector to a Hyperplane

The vector $\boldsymbol{\omega}$ is **normal** (perpendicular) to the hyperplane $\pi$.

$$
\boldsymbol{\omega} \cdot \mathbf{x} = \boldsymbol{\omega}^\top \mathbf{x} = \|\boldsymbol{\omega}\| \|\mathbf{x}\| \cos\theta = 0
$$

$$
\Rightarrow \quad \boldsymbol{\omega} \perp \mathbf{x} \quad \text{for every point } \mathbf{x} \text{ on the hyperplane}
$$

**Unit normal vector:**

$$
\hat{\boldsymbol{\omega}} = \frac{\boldsymbol{\omega}}{\|\boldsymbol{\omega}\|}
$$

Then for any point $\mathbf{x}_i$ on the hyperplane:

$$
\hat{\boldsymbol{\omega}} \cdot \mathbf{x}_i = 0
$$

```
          ω̂
          ↑
          |
          |   π (hyperplane)
          +----------------→
         (0,0)
```

## 10.6 Distance of a Point from a Plane / Hyperplane & Half-Spaces

### Distance Formula

Let the hyperplane be $\boldsymbol{\omega}^\top \mathbf{x} = 0$ (or $\boldsymbol{\omega}^\top \mathbf{x} + \omega_0 = 0$).

The **signed distance** from a point $\mathbf{p}$ to the hyperplane is:

$$
d = \frac{\boldsymbol{\omega}^\top \mathbf{p}}{\|\boldsymbol{\omega}\|}
$$

If $\|\boldsymbol{\omega}\| = 1$ (unit normal), this simplifies to:

$$
d = \boldsymbol{\omega}^\top \mathbf{p}
$$

#### Geometric Meaning & Half-Spaces

```
                               P (positive side)
                               •
                               |
                               | d
          ↑                    |
          |                    |
          |                    |
          ω̂                    |
          +--------------------•---------------------→ π
         (0,0)                 |
                               |
                               |
                               |
                               |
                               •
                               P' (negative side)
```

- If $\dfrac{\boldsymbol{\omega}^\top \mathbf{p}}{\|\boldsymbol{\omega}\|} > 0$ → point is on the **positive** side of the hyperplane, $\boldsymbol{\omega}⬆ : \mathbf{p}⬆$
- If $\dfrac{\boldsymbol{\omega}^\top \mathbf{p}}{\|\boldsymbol{\omega}\|} < 0$ → point is on the **negative** side, $\boldsymbol{\omega}⬆ : \mathbf{p}⬇$
- If $= 0$ → point lies **on** the hyperplane

The two sides are called **half-spaces**.

The sign of the dot product $\boldsymbol{\omega}^\top \mathbf{p}$ tells us on which side of the hyperplane the point lies.

---

**Quick Reference Summary**

| Concept                          | Formula / Statement                                                       |
| -------------------------------- | ------------------------------------------------------------------------- |
| Unit vector                      | $\hat{\mathbf{a}} = \mathbf{a}/\|\mathbf{a}\|$, $\|\hat{\mathbf{a}}\|=1$  |
| Hyperplane equation              | $\omega_0 + \boldsymbol{\omega}^\top\mathbf{x} = 0$                       |
| Through origin                   | $\boldsymbol{\omega}^\top\mathbf{x} = 0$                                  |
| Normal vector                    | $\boldsymbol{\omega} \perp$ hyperplane                                    |
| Distance from point $\mathbf{p}$ | $d = \dfrac{\boldsymbol{\omega}^\top\mathbf{p}}{\|\boldsymbol{\omega}\|}$ |
| Half-space test                  | Sign of $\boldsymbol{\omega}^\top\mathbf{p}$                              |

### 10.7 Equation of a Circle (2D), Sphere (3D) and Hypersphere (nD)

### Circle (2D)

**Centered at the origin:**

$$
x^2 + y^2 = r^2
\quad \text{or} \quad
x_1^2 + x_2^2 = r^2
$$

**Centered at $(h,k)$:**

$$
(x - h)^2 + (y - k)^2 = r^2
$$

**Point location test** for $P(x_1, x_2)$:

| Condition             | Location                             |
| --------------------- | ------------------------------------ |
| $x_1^2 + x_2^2 < r^2$ | $P(x_1, x_2)$ **Inside** the circle  |
| $x_1^2 + x_2^2 = r^2$ | $P(x_1, x_2)$ **On** the circle      |
| $x_1^2 + x_2^2 > r^2$ | $P(x_1, x_2)$ **Outside** the circle |

```
          y = x₂
            ↑
            |     • P'
            |   ╭───╮
            |  ╱     ╲
            | │   r   │
            |  ╲     ╱
            |   ╰───╯
            +--------→ x = x₁
                 (0,0)
```

#### Sphere (3D)

$$
x_1^2 + x_2^2 + x_3^2 = r^2
$$

**Point location test** for $P(x_1,x_2,x_3)$:

| Condition                     | Location                                |
| ----------------------------- | --------------------------------------- |
| $x_1^2 + x_2^2 + x_3^2 < r^2$ | $P(x_1,x_2,x_3)$ **Inside** the sphere  |
| $x_1^2 + x_2^2 + x_3^2 = r^2$ | $P(x_1,x_2,x_3)$ **On** the sphere      |
| $x_1^2 + x_2^2 + x_3^2 > r^2$ | $P(x_1,x_2,x_3)$ **Outside** the sphere |

#### Hypersphere (nD)

$$
x_1^2 + x_2^2 + \cdots + x_n^2 = r^2
\quad \text{or} \quad
\sum_{i=1}^{n} x_i^2 = r^2
$$

**Point location test:** for $P(x_1,x_2,x_3,\cdots,x_n)$:

| Condition          | Location                   |
| ------------------ | -------------------------- |
| $\sum x_i^2 < r^2$ | $P$ **Inside**             |
| $\sum x_i^2 = r^2$ | $P$ **On** the hypersphere |
| $\sum x_i^2 > r^2$ | $P$ **Outside**            |

## 10.8 Equation of an Ellipse (2D), Ellipsoid (3D) and Hyperellipsoid (nD)

### Ellipse (2D)

$$
\frac{x_1^2}{a^2} + \frac{x_2^2}{b^2} = 1
$$

**Point location test** for $P(x_1,x_2)$:

| Condition                                     | Location                             |
| --------------------------------------------- | ------------------------------------ |
| $\dfrac{x_1^2}{a^2} + \dfrac{x_2^2}{b^2} < 1$ | $P(x_1,x_2)$ **Inside** the ellipse  |
| $\dfrac{x_1^2}{a^2} + \dfrac{x_2^2}{b^2} = 1$ | $P(x_1,x_2)$ **On** the ellipse      |
| $\dfrac{x_1^2}{a^2} + \dfrac{x_2^2}{b^2} > 1$ | $P(x_1,x_2)$ **Outside** the ellipse |

```
          x₂
           ↑
           |     b
           |   ╭───╮
           |  ╱     ╲
           | │   a   │
           |  ╲     ╱
           |   ╰───╯
           +--------→ x₁
                (0,0)
```

---

### Ellipsoid (3D)

$$
\frac{x_1^2}{a^2} + \frac{x_2^2}{b^2} + \frac{x_3^2}{c^2} = 1
$$

**Point location test:** for $P(x_1,x_2,x_3)$:

| Condition                                                          | Location                              |
| ------------------------------------------------------------------ | ------------------------------------- |
| $\dfrac{x_1^2}{a^2} + \dfrac{x_2^2}{b^2} + \dfrac{x_3^2}{c^2} < 1$ | $P(x_1,x_2,x_3)$ **Inside**           |
| $\dfrac{x_1^2}{a^2} + \dfrac{x_2^2}{b^2} + \dfrac{x_3^2}{c^2} = 1$ | $P(x_1,x_2,x_3)$ **On** the ellipsoid |
| $\dfrac{x_1^2}{a^2} + \dfrac{x_2^2}{b^2} + \dfrac{x_3^2}{c^2} > 1$ | $P(x_1,x_2,x_3)$ **Outside**          |

### Hyperellipsoid (nD)

$$
\frac{x_1^2}{a_1^2} + \frac{x_2^2}{a_2^2} + \cdots + \frac{x_n^2}{a_n^2} = 1
$$

**Point location test:** for $P(x_1,x_2,x_3,\cdots,x_n)$:

| Condition                               | Location                      |
| --------------------------------------- | ----------------------------- |
| $\sum_{i=1}^n \dfrac{x_i^2}{a_i^2} < 1$ | $P$ **Inside**                |
| $\sum_{i=1}^n \dfrac{x_i^2}{a_i^2} = 1$ | $P$ **On** the hyperellipsoid |
| $\sum_{i=1}^n \dfrac{x_i^2}{a_i^2} > 1$ | $P$ **Outside**               |

**Append this content right after the existing section `### 10.9 Square and Rectangle (2D)`** (just before `### 10.10 Hypercube and Hypercuboid (nD)`).

It matches the lecture screenshot and expands the axis-aligned rectangle example with the exact conditions, diagram description, and the hyperplane representation of the boundary lines that appear in the image.


### 10.9 Square and Rectangle (2D)

**Squares / Rectangles (axis-parallel)**

In 2-D an axis-aligned (axis-parallel) rectangle is defined by independent bounds on each coordinate.

**Example from the board**

A point $P(p_1,p_2)$ lies **inside** the rectangle when

$$
p_1 \le 5 \quad\text{and}\quad p_1 > 2
$$
$$
p_2 > 3 \quad\text{and}\quad p_2 < 4
$$

i.e.

$$
2 < p_1 \le 5 \qquad\text{and}\qquad 3 < p_2 < 4.
$$

**Geometric picture**

```
          x₂
           ↑
         4 |  ┌─────────┐   ← x₂ = 4
           |  │         │
           |  │  • P    │
         3 |  └─────────┘   ← x₂ = 3
           +--2---------5--→ x₁
              ↑         ↑
            x₁=2      x₁=5
```

**Boundary lines as hyperplanes**

Each vertical or horizontal side is itself a 1-dimensional hyperplane.

For the left boundary $x_1 = 2$:

$$
\omega_0 + \omega_1 x_1 + \omega_2 x_2 = 0
$$

with the concrete coefficients

$$
\omega_0 = -2,\qquad \omega_1 = 1,\qquad \omega_2 = 0
\qquad\Rightarrow\qquad
-2 + 1\cdot x_1 + 0\cdot x_2 = 0
\qquad\Rightarrow\qquad x_1 = 2.
$$

The two half-spaces created by this line are simply

$$
p_1 < 5 \qquad\text{and}\qquad p_1 > 5
$$

(and likewise for the other three sides).

A point lies inside the rectangle if and only if it satisfies **all four** half-space inequalities at the same time.

**General form (axis-aligned rectangle)**

$$
x_{\min} < x_1 < x_{\max}
\qquad\text{and}\qquad
y_{\min} < x_2 < y_{\max}.
$$

(The same idea extends immediately to a hyper-rectangle / hypercuboid in $n$ dimensions — see the next section.)


### 10.10 Hypercube and Hypercuboid (nD)

#### Hypercube / Hypercuboid in 3D

A rectangular box (cuboid) aligned with the axes.

```
          x₂
           ↑
           |    ┌───┐
           |   /   /|
           |  └───┘ |
           |  │   │ /
           +--│───│/→ x₁
              └───┘
             ↙
            x₃
```

#### Hypercuboid in n Dimensions

An axis-aligned box in $n$-dimensional space is defined by independent bounds on each coordinate:

$$
a_i < x_i < b_i \quad \text{for } i = 1,2,\dots,n
$$

A point lies inside the hypercuboid if **all** of these inequalities are satisfied simultaneously.

**Summary of Geometric Objects**

| Object              | Equation (centered at origin)                                   | Inside test           |
| ------------------- | --------------------------------------------------------------- | --------------------- |
| Circle (2D)         | $x_1^2 + x_2^2 = r^2$                                           | $< r^2$               |
| Sphere (3D)         | $x_1^2 + x_2^2 + x_3^2 = r^2$                                   | $< r^2$               |
| Hypersphere (nD)    | $\sum x_i^2 = r^2$                                              | $< r^2$               |
| Ellipse (2D)        | $\frac{x_1^2}{a^2} + \frac{x_2^2}{b^2} = 1$                     | $< 1$                 |
| Ellipsoid (3D)      | $\frac{x_1^2}{a^2} + \frac{x_2^2}{b^2} + \frac{x_3^2}{c^2} = 1$ | $< 1$                 |
| Hyperellipsoid (nD) | $\sum \frac{x_i^2}{a_i^2} = 1$                                  | $< 1$                 |
| Rectangle / Cuboid  | Axis-aligned bounds on each coordinate                          | All inequalities true |
