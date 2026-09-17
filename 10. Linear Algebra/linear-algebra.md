<style>
@import url('https://fonts.googleapis.com/css2?family=Play:wght@400;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/latin-modern/1.1.0/css/latinmodern-math.min.css');

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

.relationship-item {
      background: #00070e;
      border-left: 5px solid var(--la-teal);
      border-radius: 5px;
      color: var(--la-ink);
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
      background: var(--la-amber-soft);
      border-left: 5px solid var(--la-teal) !important;
      color: var(--la-ink);
      padding: 0.75em 1em;
}

table {
      border: 1px solid var(--la-line);
      border-radius: 8px;
      overflow: hidden;
}

th {
      background: #00070e;
      color: #9e9d9d;
}

td {
      /* background: 3f6386; */
      color: #6080a0;
}

tr:nth-child(even) {
      background: var(--la-surface);
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
      font-family: 'Latin Modern Math', 'Cambria Math', 'STIX Two Math', serif !important;
}

.katex,
.katex * {
      color: #9b9a9a !important;
      font-family: 'Latin Modern Math', 'Cambria Math', 'STIX Two Math', serif !important;
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

---

## 10.2 Scalars

A **scalar** is a single numerical value.

Examples:

$$
5,\quad -3,\quad 2.5,\quad 100
$$

A scalar has magnitude but no direction.

For example:

$$
x=5
$$

is a scalar.

---

## 10.3 Introduction to Vectors

A **vector** is an ordered collection of numbers.

For example:

$$
\mathbf{x}
=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

This is a **2-dimensional vector**.

It can be interpreted geometrically as an arrow from the origin:

$$
(0,0)\rightarrow(3,4)
$$

---

### 10.3.1 2-D Vector

A 2-D vector has two components:

$$
\mathbf{x}
=
\begin{bmatrix}
x_1\\
x_2
\end{bmatrix}
$$

Example:

$$
\mathbf{x}
=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

---

### 10.3.2 3-D Vector

A 3-D vector has three components:

$$
\mathbf{x}
=
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}
$$

Example:

$$
\mathbf{x}
=
\begin{bmatrix}
2\\
5\\
7
\end{bmatrix}
$$

It can be represented as a point or direction in 3-dimensional space.

---

### 10.3.3 n-D Vector

A vector can contain any number of dimensions:

$$
\mathbf{x}
=
\begin{bmatrix}
x_1\\
x_2\\
x_3\\
\vdots\\
x_n
\end{bmatrix}
$$

This is an **n-dimensional vector**.

In Machine Learning, high-dimensional vectors are extremely common.

For example, a dataset with 100 features can represent one observation as:

$$
\mathbf{x}\in\mathbb{R}^{100}
$$

---

## 10.4 Row Vector and Column Vector

A vector can be written as either a **row vector** or a **column vector**.

### Row Vector

$$
\mathbf{x}
=
\begin{bmatrix}
x_1 & x_2 & x_3
\end{bmatrix}
$$

Shape:

$$
1\times3
$$

Example:

$$
\mathbf{x}
=
\begin{bmatrix}
2 & 4 & 6
\end{bmatrix}
$$

---

### Column Vector

$$
\mathbf{x}
=
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}
$$

Shape:

$$
3\times1
$$

Example:

$$
\mathbf{x}
=
\begin{bmatrix}
2\\
4\\
6
\end{bmatrix}
$$

A row vector is the transpose of a column vector:

$$
\mathbf{x}^T
=
\begin{bmatrix}
x_1 & x_2 & x_3
\end{bmatrix}
$$

---

## 10.5 Vector Addition

Two vectors of the same dimension can be added component-wise.

Let:

$$
\mathbf{a}
=
\begin{bmatrix}
2\\
3
\end{bmatrix}
$$

and

$$
\mathbf{b}
=
\begin{bmatrix}
4\\
1
\end{bmatrix}
$$

Then:

$$
\mathbf{a}+\mathbf{b}
=
\begin{bmatrix}
2+4\\
3+1
\end{bmatrix}
=
\begin{bmatrix}
6\\
4
\end{bmatrix}
$$

---

## 10.6 Scalar Multiplication

A vector can be multiplied by a scalar.

If:

$$
\mathbf{x}
=
\begin{bmatrix}
2\\
3
\end{bmatrix}
$$

then:

$$
3\mathbf{x}
=
3
\begin{bmatrix}
2\\
3
\end{bmatrix}
=
\begin{bmatrix}
6\\
9
\end{bmatrix}
$$

Scalar multiplication changes the magnitude of the vector.

---

## 10.7 Magnitude / Norm of a Vector

The magnitude or length of a vector is called its **norm**.

For:

$$
\mathbf{x}
=
\begin{bmatrix}
x_1\\
x_2
\end{bmatrix}
$$

the Euclidean norm is:

$$
\boxed{
\|\mathbf{x}\|
=
\sqrt{x_1^2+x_2^2}
}
$$

For an n-dimensional vector:

$$
\boxed{
\|\mathbf{x}\|
=
\sqrt{
\sum_{i=1}^{n}x_i^2
}
}
$$

Example:

$$
\mathbf{x}
=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

Therefore:

$$
\|\mathbf{x}\|
=
\sqrt{3^2+4^2}
=
5
$$

---

## 10.8 Dot Product

The **dot product** combines two vectors and produces a scalar.

For:

$$
\mathbf{a}
=
\begin{bmatrix}
a_1\\
a_2
\end{bmatrix}
$$

and

$$
\mathbf{b}
=
\begin{bmatrix}
b_1\\
b_2
\end{bmatrix}
$$

the dot product is:

$$
\boxed{
\mathbf{a}\cdot\mathbf{b}
=
a_1b_1+a_2b_2
}
$$

For n-dimensional vectors:

$$
\boxed{
\mathbf{a}\cdot\mathbf{b}
=
\sum_{i=1}^{n}a_ib_i
}
$$

---

### Example

$$
\mathbf{a}
=
\begin{bmatrix}
2\\
3
\end{bmatrix}
$$

$$
\mathbf{b}
=
\begin{bmatrix}
4\\
5
\end{bmatrix}
$$

Then:

$$
\mathbf{a}\cdot\mathbf{b}
=
2(4)+3(5)
=
8+15
=
23
$$

---

## 10.9 Dot Product and Angle Between Two Vectors

The dot product also tells us about the angle between two vectors.

The fundamental relationship is:

$$
\boxed{
\mathbf{a}\cdot\mathbf{b}
=
\|\mathbf{a}\|
\|\mathbf{b}\|
\cos\theta
}
$$

Therefore:

$$
\boxed{
\cos\theta
=
\frac{
\mathbf{a}\cdot\mathbf{b}
}{
\|\mathbf{a}\|\|\mathbf{b}\|
}
}
$$

and:

$$
\boxed{
\theta
=
\cos^{-1}
\left(
\frac{
\mathbf{a}\cdot\mathbf{b}
}{
\|\mathbf{a}\|\|\mathbf{b}\|
}
\right)
}
$$

This relationship is extremely important in Machine Learning.

### Interpretation

If:

$$
\mathbf{a}\cdot\mathbf{b}>0
$$

the angle is less than \(90^\circ\).

If:

$$
\mathbf{a}\cdot\mathbf{b}=0
$$

the vectors are perpendicular.

If:

$$
\mathbf{a}\cdot\mathbf{b}<0
$$

the angle is greater than \(90^\circ\).

---

## 10.10 Projection

Projection tells us how much of one vector lies in the direction of another vector.

The projection of \(\mathbf{a}\) onto \(\mathbf{b}\) is:

$$
\boxed{
\operatorname{proj}_{\mathbf b}\mathbf a
=
\frac{\mathbf a\cdot\mathbf b}
{\|\mathbf b\|^2}
\mathbf b
}
$$

The scalar projection is:

$$
\boxed{
\operatorname{comp}_{\mathbf b}\mathbf a
=
\frac{\mathbf a\cdot\mathbf b}
{\|\mathbf b\|}
}
$$

---

## 10.11 Unit Vector

A **unit vector** has magnitude equal to 1.

For a non-zero vector:

$$
\mathbf{x}
$$

its unit vector is:

$$
\boxed{
\hat{\mathbf{x}}
=
\frac{\mathbf{x}}
{\|\mathbf{x}\|}
}
$$

Example:

$$
\mathbf{x}
=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

Since:

$$
\|\mathbf{x}\|=5
$$

the unit vector is:

$$
\hat{\mathbf{x}}
=
\begin{bmatrix}
3/5\\
4/5
\end{bmatrix}
$$

and:

$$
\|\hat{\mathbf{x}}\|=1
$$

---

## 10.12 Equation of a Line in 2-D

A line can be represented using a point and a direction vector.

Suppose the line passes through:

$$
\mathbf{p}
=
\begin{bmatrix}
x_0\\
y_0
\end{bmatrix}
$$

with direction vector:

$$
\mathbf{d}
=
\begin{bmatrix}
a\\
b
\end{bmatrix}
$$

Then the vector equation of the line is:

$$
\boxed{
\mathbf{x}
=
\mathbf{p}+t\mathbf{d}
}
$$

where:

$$
t\in\mathbb{R}
$$

Expanding:

$$
\begin{bmatrix}
x\\
y
\end{bmatrix}
=
\begin{bmatrix}
x_0\\
y_0
\end{bmatrix}
+
t
\begin{bmatrix}
a\\
b
\end{bmatrix}
$$

Therefore:

$$
x=x_0+at
$$

$$
y=y_0+bt
$$

---

## 10.13 Line in Standard Form

A 2-D line can also be represented as:

$$
\boxed{
ax+by+c=0
}
$$

The vector:

$$
\begin{bmatrix}
a\\
b
\end{bmatrix}
$$

is **normal (perpendicular) to the line**.

---

## 10.14 Plane in 3-D

A plane in 3-D can be represented as:

$$
\boxed{
ax+by+cz+d=0
}
$$

The vector:

$$
\mathbf{n}
=
\begin{bmatrix}
a\\
b\\
c
\end{bmatrix}
$$

is the **normal vector** of the plane.

Therefore:

$$
\boxed{
\mathbf n\cdot\mathbf x+d=0
}
$$

where:

$$
\mathbf x=
\begin{bmatrix}
x\\y\\z
\end{bmatrix}
$$

---

## 10.15 Plane Passing Through the Origin

If the plane passes through the origin:

$$
(0,0,0)
$$

then:

$$
d=0
$$

Therefore:

$$
\boxed{
ax+by+cz=0
}
$$

or:

$$
\boxed{
\mathbf n\cdot\mathbf x=0
}
$$

This means every vector lying in the plane is perpendicular to the normal vector.

---

## 10.16 Normal to a Plane

For the plane:

$$
ax+by+cz+d=0
$$

the normal vector is:

$$
\boxed{
\mathbf n=
\begin{bmatrix}
a\\
b\\
c
\end{bmatrix}
}
$$

Example:

$$
2x+3y-4z+7=0
$$

has normal:

$$
\mathbf n=
\begin{bmatrix}
2\\
3\\
-4
\end{bmatrix}
$$

---

## 10.17 Hyperplane in n-D

A **hyperplane** is the generalization of a line and plane to higher dimensions.

The equation is:

$$
\boxed{
w_1x_1+w_2x_2+\cdots+w_nx_n+b=0
}
$$

Using vector notation:

$$
\boxed{
\mathbf w^T\mathbf x+b=0
}
$$

where:

- \(\mathbf{x}\) = input vector
- \(\mathbf{w}\) = normal vector
- \(b\) = bias/intercept

This equation is fundamental to Machine Learning.

For example, a linear classifier can use:

$$
\mathbf w^T\mathbf x+b=0
$$

to separate two classes.

---

## 10.18 Distance of a Point from a Plane / Hyperplane

For a plane:

$$
ax+by+cz+d=0
$$

and point:

$$
P=(x_0,y_0,z_0)
$$

the perpendicular distance is:

$$
\boxed{
D=
\frac{
|ax_0+by_0+cz_0+d|
}{
\sqrt{a^2+b^2+c^2}
}
}
$$

---

### General n-D Formula

For a hyperplane:

$$
\mathbf w^T\mathbf x+b=0
$$

the distance from a point \(\mathbf{x}\_0\) is:

$$
\boxed{
D=
\frac{
|\mathbf w^T\mathbf x_0+b|
}{
\|\mathbf w\|
}
}
$$

This formula is particularly important in:

- Support Vector Machines
- Linear classification
- Decision boundaries
- Maximum-margin optimization

---

## 10.19 Half-Spaces

A hyperplane divides space into two regions called **half-spaces**.

Given:

$$
\mathbf w^T\mathbf x+b=0
$$

the two half-spaces are:

$$
\boxed{
\mathbf w^T\mathbf x+b>0
}
$$

and:

$$
\boxed{
\mathbf w^T\mathbf x+b<0
}
$$

The hyperplane itself is:

$$
\mathbf w^T\mathbf x+b=0
$$

This is the geometric foundation of many linear classification algorithms.

---

## 10.20 Circle in 2-D

A circle consists of all points at a fixed distance \(r\) from a center.

If the center is:

$$
(h,k)
$$

then:

$$
\boxed{
(x-h)^2+(y-k)^2=r^2
}
$$

For a circle centered at the origin:

$$
\boxed{
x^2+y^2=r^2
}
$$

---

## 10.21 Sphere in 3-D

A sphere is the 3-D equivalent of a circle.

For center:

$$
(h,k,l)
$$

and radius \(r\):

$$
\boxed{
(x-h)^2+(y-k)^2+(z-l)^2=r^2
}
$$

For a sphere centered at the origin:

$$
\boxed{
x^2+y^2+z^2=r^2
}
$$

---

## 10.22 Hypersphere in n-D

The n-dimensional generalization is:

$$
\boxed{
\sum_{i=1}^{n}(x_i-c_i)^2=r^2
}
$$

where:

$$
\mathbf c=
\begin{bmatrix}
c_1\\
c_2\\
\vdots\\
c_n
\end{bmatrix}
$$

is the center.

Equivalently:

$$
\boxed{
\|\mathbf{x}-\mathbf{c}\|^2=r^2
}
$$

A hypersphere is therefore the set of all points whose Euclidean distance from the center is exactly \(r\).

---

## 10.23 Circle / Sphere / Hypersphere

| Dimension | Shape       | Equation                           |
| --------: | ----------- | ---------------------------------- |
|       2-D | Circle      | \((x-h)^2+(y-k)^2=r^2\)            |
|       3-D | Sphere      | \((x-h)^2+(y-k)^2+(z-l)^2=r^2\)    |
|       n-D | Hypersphere | \(\sum\_{i=1}^{n}(x_i-c_i)^2=r^2\) |

The common idea is:

$$
\boxed{
\|\mathbf{x}-\mathbf{c}\|=r
}
$$

---

## 10.24 Ellipse in 2-D

An ellipse is a generalization of a circle where the radius can differ along different axes.

For an ellipse centered at \((h,k)\):

$$
\boxed{
\frac{(x-h)^2}{a^2}
+
\frac{(y-k)^2}{b^2}
=
1
}
$$

where:

- \(a\) = semi-major axis
- \(b\) = semi-minor axis

If:

$$
a=b
$$

the ellipse becomes a circle.

---

## 10.25 Ellipsoid in 3-D

The 3-D equivalent is an ellipsoid:

$$
\boxed{
\frac{(x-h)^2}{a^2}
+
\frac{(y-k)^2}{b^2}
+
\frac{(z-l)^2}{c^2}
=
1
}
$$

where \(a,b,c\) determine the lengths of the three principal axes.

---

## 10.26 Hyperellipsoid in n-D

The n-dimensional generalization is:

$$
\boxed{
\sum_{i=1}^{n}
\frac{(x_i-c_i)^2}{a_i^2}
=
1
}
$$

where:

- \(c_i\) = center coordinate
- \(a_i\) = semi-axis length in dimension \(i\)

A hyperellipsoid can be viewed as a stretched or compressed hypersphere.

---

## 10.27 Circle vs Ellipse

A circle has the same radius in every direction.

$$
x^2+y^2=r^2
$$

An ellipse can have different scales along different axes.

$$
\frac{x^2}{a^2}+
\frac{y^2}{b^2}=1
$$

If:

$$
a=b=r
$$

then:

$$
\frac{x^2}{r^2}+\frac{y^2}{r^2}=1
$$

which gives:

$$
x^2+y^2=r^2
$$

Therefore:

> **A circle is a special case of an ellipse.**

---

## 10.28 Square

A square is a 2-D geometric object with:

- 4 equal sides
- 4 right angles
- Equal diagonals

For a square with side length \(s\):

### Area

$$
\boxed{
A=s^2
}
$$

### Perimeter

$$
\boxed{
P=4s
}
$$

### Diagonal

$$
\boxed{
d=s\sqrt{2}
}
$$

---

## 10.29 Rectangle

A rectangle has:

- 4 right angles
- Opposite sides equal
- Two independent side lengths

Let the side lengths be \(a\) and \(b\).

### Area

$$
\boxed{
A=ab
}
$$

### Perimeter

$$
\boxed{
P=2(a+b)
}
$$

### Diagonal

$$
\boxed{
d=\sqrt{a^2+b^2}
}
$$

A square is a special case of a rectangle where:

$$
a=b
$$

---

## 10.30 Hypercube

A **hypercube** is the n-dimensional generalization of a square and cube.

| Dimension | Hypercube    |
| --------: | ------------ |
|       1-D | Line segment |
|       2-D | Square       |
|       3-D | Cube         |
|       4-D | Tesseract    |
|       n-D | Hypercube    |

For side length \(s\), an n-dimensional hypercube has:

$$
\boxed{
V_n=s^n
}
$$

where \(V_n\) represents the n-dimensional hypervolume.

---

### Examples

### 1-D

$$
V_1=s
$$

Line segment.

### 2-D

$$
V_2=s^2
$$

Square area.

### 3-D

$$
V_3=s^3
$$

Cube volume.

### 4-D

$$
V_4=s^4
$$

Tesseract hypervolume.

---

## 10.31 Hypercuboid

A **hypercuboid** is the n-dimensional generalization of a rectangle and cuboid.

Suppose the side lengths are:

$$
a_1,a_2,\ldots,a_n
$$

Then its n-dimensional hypervolume is:

$$
\boxed{
V=
\prod_{i=1}^{n}a_i
}
$$

or:

$$
\boxed{
V=a_1a_2\cdots a_n
}
$$

---

### Relationship

```text
1-D
Line segment
      ↓
2-D
Rectangle
      ↓
3-D
Cuboid
      ↓
n-D
Hypercuboid
```

A hypercube is a special case of a hypercuboid where:

$$
a_1=a_2=\cdots=a_n=s
$$

Therefore:

$$
V=s^n
$$

---

## 10.32 Important Geometric Relationships

Many of the objects studied above are dimensional generalizations of one another.

<div class="relationship-item"><strong>Line:</strong> 1-D linear object.</div>

<div class="relationship-item"><strong>Plane:</strong> 2-D flat object inside 3-D space.</div>

<div class="relationship-item"><strong>Hyperplane:</strong> \((n-1)\)-dimensional flat object inside n-dimensional space.</div>

---

<div class="relationship-item"><strong>Circle:</strong> 2-D constant-distance boundary.</div>

<div class="relationship-item"><strong>Sphere:</strong> 3-D constant-distance boundary.</div>

<div class="relationship-item"><strong>Hypersphere:</strong> n-D constant-distance boundary.</div>

---

<div class="relationship-item"><strong>Square:</strong> 2-D equal-sided hyperrectangle.</div>

<div class="relationship-item"><strong>Cube:</strong> 3-D equal-sided hyperrectangle.</div>

<div class="relationship-item"><strong>Hypercube:</strong> n-D equal-sided hyperrectangle.</div>

---

## 10.33 Linear Algebra and Machine Learning

The concepts above appear directly in ML algorithms.

### Feature Vector

A sample can be represented as:

$$
\mathbf{x}
=
\begin{bmatrix}
x_1\\
x_2\\
\vdots\\
x_n
\end{bmatrix}
$$

where each \(x_i\) represents a feature.

---

### Linear Model

A linear model can be represented as:

$$
\boxed{
\hat y=\mathbf w^T\mathbf x+b
}
$$

Expanding:

$$
\hat y
=
w_1x_1+w_2x_2+\cdots+w_nx_n+b
$$

---

### Decision Boundary

For a binary linear classifier:

$$
\boxed{
\mathbf w^T\mathbf x+b=0
}
$$

This creates a hyperplane separating regions of the feature space.

---

### Distance from Decision Boundary

$$
\boxed{
D=
\frac{
|\mathbf w^T\mathbf x+b|
}{
\|\mathbf w\|
}
}
$$

This becomes particularly important in **Support Vector Machines**.

---

## 10.34 Geometry of High-Dimensional Data

One of the most important ideas in Machine Learning is that data does not need to exist in only 2-D or 3-D.

Suppose each observation has:

$$
100
$$

features.

Then:

$$
\mathbf{x}\in\mathbb{R}^{100}
$$

We cannot directly visualize the 100-dimensional space, but the mathematical operations remain the same.

For example:

### Distance

$$
\|\mathbf{x}-\mathbf{y}\|
$$

### Similarity

$$
\mathbf{x}\cdot\mathbf{y}
$$

### Hyperplane

$$
\mathbf{w}^T\mathbf{x}+b=0
$$

### Hypersphere

$$
\|\mathbf{x}-\mathbf{c}\|=r
$$

This is why understanding 2-D and 3-D geometry provides intuition for higher-dimensional Machine Learning.

---

## 10.35 Important Formula Summary

### Vector Norm

$$
\boxed{
\|\mathbf{x}\|
=
\sqrt{\sum_{i=1}^{n}x_i^2}
}
$$

### Dot Product

$$
\boxed{
\mathbf a\cdot\mathbf b
=
\sum_{i=1}^{n}a_ib_i
}
$$

### Angle

$$
\boxed{
\cos\theta
=
\frac{\mathbf a\cdot\mathbf b}
{\|\mathbf a\|\|\mathbf b\|}
}
$$

### Unit Vector

$$
\boxed{
\hat{\mathbf x}
=
\frac{\mathbf x}{\|\mathbf x\|}
}
$$

### Projection

$$
\boxed{
\operatorname{proj}_{\mathbf b}\mathbf a
=
\frac{\mathbf a\cdot\mathbf b}
{\|\mathbf b\|^2}\mathbf b
}
$$

### Line

$$
\boxed{
\mathbf{x}
=
\mathbf{p}+t\mathbf{d}
}
$$

### Plane

$$
\boxed{
ax+by+cz+d=0
}
$$

### Hyperplane

$$
\boxed{
\mathbf w^T\mathbf x+b=0
}
$$

### Point-to-Hyperplane Distance

$$
\boxed{
D=
\frac{
|\mathbf w^T\mathbf x+b|
}{
\|\mathbf w\|
}
}
$$

### Circle

$$
\boxed{
(x-h)^2+(y-k)^2=r^2
}
$$

### Sphere

$$
\boxed{
(x-h)^2+(y-k)^2+(z-l)^2=r^2
}
$$

### Hypersphere

$$
\boxed{
\|\mathbf{x}-\mathbf{c}\|^2=r^2
}
$$

### Ellipse

$$
\boxed{
\frac{(x-h)^2}{a^2}
+
\frac{(y-k)^2}{b^2}
=1
}
$$

### Ellipsoid

$$
\boxed{
\frac{(x-h)^2}{a^2}
+
\frac{(y-k)^2}{b^2}
+
\frac{(z-l)^2}{c^2}
=1
}
$$

### Hyperellipsoid

$$
\boxed{
\sum_{i=1}^{n}
\frac{(x_i-c_i)^2}{a_i^2}
=1
}
$$

### Hypercube

$$
\boxed{
V=s^n
}
$$

### Hypercuboid

$$
\boxed{
V=\prod_{i=1}^{n}a_i
}
$$

---

## 10.36 Revision Questions

### Conceptual Questions

### <span class="revision-question">Q1. What is a vector?</span>

Explain the difference between a scalar and a vector.

### <span class="revision-question">Q2. What is the difference between a row vector and a column vector?</span>

Give their dimensions for a vector containing 5 elements.

### <span class="revision-question">Q3. What does the magnitude of a vector represent geometrically?</span>

### <span class="revision-question">Q4. What does the dot product of two vectors produce?</span>

### <span class="revision-question">Q5. What does it mean when $\mathbf a\cdot\mathbf b=0$ ?</span>

### <span class="revision-question">Q6. What is a unit vector?</span>

### <span class="revision-question">Q7. Why do we normalize vectors?</span>

### <span class="revision-question">Q8. What does vector projection represent geometrically?</span>

### <span class="revision-question">Q9. What is the difference between a line, plane, and hyperplane?</span>

### <span class="revision-question">Q10. What is the normal vector of a plane?</span>

### <span class="revision-question">Q11. What is a half-space?</span>

### <span class="revision-question">Q12. What is the difference between a circle and an ellipse?</span>

### <span class="revision-question">Q13. What is the difference between a sphere and a hypersphere?</span>

### <span class="revision-question">Q14. What is a hypercube?</span>

### <span class="revision-question">Q15. What is the difference between a hypercube and a hypercuboid?</span>

---

## 10.37 Numerical Revision Questions

### Q1. Vector Norm

Given:

$$
\mathbf{x}
=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

calculate:

$$
\|\mathbf{x}\|
$$

---

### Q2. Dot Product

Given:

$$
\mathbf a=
\begin{bmatrix}
2\\
3
\end{bmatrix}
$$

and:

$$
\mathbf b=
\begin{bmatrix}
4\\
5
\end{bmatrix}
$$

calculate:

$$
\mathbf a\cdot\mathbf b
$$

---

### Q3. Angle Between Vectors

Given:

$$
\mathbf a=
\begin{bmatrix}
1\\
0
\end{bmatrix}
$$

and:

$$
\mathbf b=
\begin{bmatrix}
0\\
1
\end{bmatrix}
$$

find the angle between them.

---

### Q4. Unit Vector

Find the unit vector of:

$$
\mathbf{x}
=
\begin{bmatrix}
6\\
8
\end{bmatrix}
$$

---

### Q5. Projection

Find the projection of:

$$
\mathbf a=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

onto:

$$
\mathbf b=
\begin{bmatrix}
1\\
0
\end{bmatrix}
$$

---

### Q6. Hyperplane

Given:

$$
2x+3y-4z+5=0
$$

identify its normal vector.

---

### Q7. Distance from Plane

Find the distance between:

$$
P=(1,2,3)
$$

and:

$$
2x+3y+6z-10=0
$$

---

### Q8. Circle

Find the center and radius of:

$$
(x-3)^2+(y+2)^2=25
$$

---

### Q9. Sphere

Find the center and radius of:

$$
(x-1)^2+(y-2)^2+(z+3)^2=16
$$

---

### Q10. Hypercube

What is the 5-dimensional hypervolume of a hypercube with side length:

$$
s=2
$$

?

---

## 10.38 ML-Oriented Revision Questions

### Q1.

Why can a dataset with 100 features be represented as vectors in:

$$
\mathbb R^{100}
$$

?

### Q2.

Explain why:

$$
\mathbf w^T\mathbf x+b=0
$$

represents a decision boundary.

### Q3.

Why is the vector \(\mathbf w\) normal to the hyperplane?

### Q4.

Why is the distance:

$$
\frac{|\mathbf w^T\mathbf x+b|}{\|\mathbf w\|}
$$

useful in classification?

### Q5.

What is the relationship between dot product and cosine similarity?

### Q6.

Why are vectors fundamental to neural networks?

### Q7.

How can an image be represented using matrices and vectors?

### Q8.

Why does increasing the number of features increase the dimensionality of the feature space?

---

## 10.39 Big Picture

The most important conceptual chain to remember is:

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

Geometrically:

$$
\boxed{
\text{Line}
\rightarrow
\text{Plane}
\rightarrow
\text{Hyperplane}
}
$$

Shapes:

$$
\boxed{
\text{Circle}
\rightarrow
\text{Sphere}
\rightarrow
\text{Hypersphere}
}
$$

and:

$$
\boxed{
\text{Square}
\rightarrow
\text{Cube}
\rightarrow
\text{Hypercube}
}
$$

The central ML idea is:

$$
\boxed{
\text{Data}
\rightarrow
\text{Vectors}
\rightarrow
\text{Geometric Space}
\rightarrow
\text{Linear Algebra Operations}
\rightarrow
\text{ML Model}
}
$$

Once vectors, dot products, projections, norms, hyperplanes, and distances become intuitive, many Machine Learning algorithms become much easier to understand.
