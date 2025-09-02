![Python Logo](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

## Variable Types

| **Variable Type** | **Description** | **Example** | **Type Check** |
| --- | --- | --- | --- |
| Integer (`int`) | Whole numbers | `age = 25` | `type(age)` → `<class 'int'>` |
| Float (`float`) | Decimal numbers | `price = 99.99` | `<class 'float'>` |
| Complex (`complex`) | Complex numbers | `z = 2 + 3j` | `<class 'complex'>` |
| String (`str`) | Text | `name = "Mashfiq"` | `<class 'str'>` |
| Boolean (`bool`) | True/False | `is_active = True` | `<class 'bool'>` |
| List (`list`) | Ordered, mutable collection | `numbers = [1, 2, 3]` | `<class 'list'>` |
| Tuple (`tuple`) | Ordered, immutable collection | `coords = (10, 20)` | `<class 'tuple'>` |
| Range (`range`) | Sequence of numbers | `nums = range(5)` | `<class 'range'>` |
| Set (`set`) | Unordered, no duplicates | `unique = {1, 2, 3}` | `<class 'set'>` |
| Frozen Set (`frozenset`) | Immutable version of set | `fs = frozenset([1,2,3])` | `<class 'frozenset'>` |
| Dictionary (`dict`) | Key-value pairs | `person = {"name":"Mashfiq","age":25}` | `<class 'dict'>` |
| NoneType (`None`) | Absence of value | `result = None` | `<class 'NoneType'>` |
| Dynamic Variable | Can change type at runtime | `var = 10; var = "Ten"` | `type(var)` changes |
| Constant (by convention) | Value meant not to change | `PI = 3.14159` | `<class 'float'>` |
| Bytes (`bytes`) | Immutable sequence of bytes | `b = b"Hello"` | `<class 'bytes'>` |
| Bytearray (`bytearray`) | Mutable sequence of bytes | `ba = bytearray([65,66,67])` | `<class 'bytearray'>` |
| Memoryview (`memoryview`) | View of byte data | `mv = memoryview(b"Hello")` | `<class 'memoryview'>` |

---

## Variables and Data Types

### Numeric Types

```python
age = 25
print(age, type(age))

price = 99.99
print(price, type(price))

com = 2 + 3j
print(com, type(com))
```

### String

```python
name = "mashfiq"
gretting = "Hello Data Science"
multi = """this is a multiline text"""

print(name, type(name))
print(gretting, type(gretting))
print(multi, type(multi))
```

### Boolean

```python
is_active = True
is_admin = False

print(is_active, type(is_active))
print(is_admin, type(is_admin))
```

---

## Sequence Types

### List

```python
numbers = [1, 2, 3, 4, 5]
print(numbers, type(numbers))

fruits = ["apple", "banana", "mango"]
print(fruits, type(fruits))
```

### Tuple

```python
coordinates = (10.0, 20.0)
print(coordinates, type(coordinates))

colors = ("red", "green", "blue")
print(colors, type(colors))
```

### Range

```python
nums = range(0, 5)
print(nums, type(nums))
print(list(nums), type(nums))
```

### Set

```python
unique_nums = {1, 2, 3, 4, 5}
print(unique_nums, type(unique_nums))
```

### Dictionary

```python
person = {"name": "Mash", "age": 31, "city": "khulna"}
print(person, type(person))
print(person["name"])
```

### NoneType

```python
result = None
print(result, type(result))
```

### Dynamic Variables

```python
var = 10
var = "Ten"
var = [10]
print(var, type(var))
```

### Constants

```python
PI = 3.14159
GRAVITY = 9.8

print(PI, type(PI))
print(GRAVITY, type(GRAVITY))
```

---

## Type Conversion

```python
str(20)
int(20.6)
float(5)
```

---

## Output Formatting

```python
a = 10
b = 20

print("The value of a is {} and b is {}".format(a, b))
print("The value of b is {1} and a is {0}".format(a, b))
print("Hello {name}, {greeting}".format(name="Mash", greeting="Good Morning!"))
```

---

## Input and Membership

```python
num = input("Enter a number: ")
print(num)

x = 5
y = 5

print(x is y)
print(x is not y)

lst = [1, 2, 3, 4, 5]
print(1 in lst)
print(1 not in lst)
```

---

## Control Flow

### if...else

```python
num = 10
if num == 10:
    print("Number is positive")
print("this will always print")

if num > 0:
    print("Positive Number")
else:
    print("Negative Number")

num = 0
if num > 0:
    print("Positive Number")
elif num == 0:
    print("ZERO")
else:
    print("Negative Number")
```

### Nested if

```python
num = 10.5
if num >= 0:
    if num == 0:
        print("ZERO")
    else:
        print("Positive Number")
else:
    print("Negative Number")
```

### Largest of Three

```python
num1 = 10
num2 = 50
num3 = 15

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print(largest)
```

---

## Loops

### while loop

```python
lst = [10, 20, 30, 40, 50]
product = 1
index = 0

while index < len(lst):
    product *= lst[index]
    index += 1

print("Product is : {}".format(product))
```

### while loop with else

```python
numbers = [1, 2, 3, 4, 5]
index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1
else:
    print("No item left in the list")
```

### Is Prime

```python
num = int(input("Enter a number: "))
isDivisible = False
i = 2

while i < num:
    if num % i == 0:
        isDivisible = True
        print("{} is divisible by {}".format(num, i))
    i += 1

if isDivisible:
    print("{} is Not a Prime number.".format(num))
else:
    print("{} is a Prime number.".format(num))
```

### for loop

```python
lst = [10, 20, 30, 40, 50]
product = 1

for ele in lst:
    product *= ele

print(product)
```

### range()

```python
for i in range(10):
    print(i)
for i in range(1, 20, 2):
    print(i)
for i in range(0, 20, 5):
    print(i)

lst = ["Mash", "Safa", "Nosh", "Shad", "Rak", "Sham"]

for index in range(len(lst)):
    print(lst[index])
```

### for loop with else

```python
numbers = [1, 2, 3]

for item in numbers:
    print(item)
else:
    print("No more items")
```

### All The Prime Numbers in an Interval

```python
index1 = int(input("Enter Starting point of numbers: "))
index2 = int(input("Enter End point of numbers: "))

print("Prime numbers between {} and {} are: ".format(index1, index2))

for num in range(index1, index2 + 1):
    if num > 1:
        isDivisible = False
        for index in range(2, num):
            if num % index == 0:
                isDivisible = True
        if not isDivisible:
            print(num)
```

---

## List

| **Operation** | **Description** | **Example** | **Output** |
| --- | --- | --- | --- |
| Create a list | Define with `[]` | `fruits = ["apple", "banana", "mango"]` | `['apple', 'banana', 'mango']` |
| Access element | Use index (0-based) | `fruits[0]` | `'apple'` |
| Negative index | Access from end | `fruits[-1]` | `'mango'` |
| Slice list | Get sublist | `fruits[0:2]` | `['apple', 'banana']` |
| Append item | Add at end | `fruits.append("orange")` | `['apple','banana','mango','orange']` |
| Insert item | Add at specific index | `fruits.insert(1, "grape")` | `['apple','grape','banana','mango']` |
| Extend list | Add multiple items | `fruits.extend(["kiwi","melon"])` | `['apple','banana','mango','kiwi','melon']` |
| Remove item (by value) | Remove first matching element | `fruits.remove("banana")` | `['apple','mango']` |
| Pop item (by index) | Remove and return element | `fruits.pop(1)` | returns `'banana'` |
| Delete item | Remove by index with `del` | `del fruits[0]` | Removes first element |
| Clear list | Remove all items | `fruits.clear()` | `[]` |
| Length of list | Count items | `len(fruits)` | `3` |
| Check existence | Use `in` keyword | `"apple" in fruits` | `True` |
| Sort list | Sort ascending | `fruits.sort()` | Sorted list |
| Sort descending | Sort reverse | `fruits.sort(reverse=True)` | Reverse sorted |
| Reverse list | Reverse order | `fruits.reverse()` | Reversed list |
| Copy list | Create shallow copy | `copy_fruits = fruits.copy()` | Same list copy |
| Join lists | Concatenate lists | `list1 + list2` | Combined list |
| Repeat list | Duplicate items | `fruits * 2` | Repeated list |
| List comprehension | Create list with expression | `[x*2 for x in [1,2,3]]` | `[2, 4, 6]` |

---

## List Operations and Comprehensions

```python
lst0 = []
lst1 = ["one", "Two", "Three"]
lst2 = [1, 2, 3, 4]
lst3 = [[1, 2], [3, 4]]
lst4 = [1, 'str', 2, 3]
print(len(lst4))

lst = ["one", "Two", "Three"]
lst.append('Four')
print(lst)

lst.insert(3, "Four")
print(lst)

lst = ["one", "Two", "Two", "Three"]
lst.remove("Two")
print(lst)

lst1 = ["one", "Two", "Two", "Three"]
lst2 = ["Four", "Five"]
lst1.append(lst2)
print(lst1)

lst1 = ["one", "Two", "Two", "Three"]
lst2 = ["Four", "Five"]
lst1.extend(lst2)
print(lst1)

lst = ["one", "Two", "Three", "Four", "Five"]
del lst[1]
print(lst)

lst = ["one", "Two", "Three", "Four", "Five"]
a = lst.pop(1)
print(a)
print(lst)

lst = ["one", "Two", "Three", "Four", "Five"]
if "Two" in lst:
    print("AI")
if "Six" not in lst:
    print("ML")

numbers = [3, 1, 6, 2, 8]
sorted_lst = sorted(numbers)
reverse_sort_lst = sorted(numbers, reverse=True)

print(numbers)
numbers.sort()
print(sorted_lst)
print(reverse_sort_lst)
print(numbers)

lst = [1, 2, 3, 4, 5]
abc = lst
abc.append(6)
print(abc)
print(lst)

s = "one,Two,Three,Four,Five"
slst = s.split(',')
print(s)
print(slst)

s = "This is applied AI Course"
split_lst = s.split()
print(split_lst)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[:])
print(numbers[0:4])
print(numbers[::2])
print(numbers[2::2])

lst1 = [1, 2, 3, 4]
lst2 = ["Mash", "Safa"]
new_lst = lst1 + lst2
print(new_lst)

numbers = [1, 2, 3, 1, 3, 4, 2, 5]
print(numbers.count(1))
print(numbers.count(3))

for ele in new_lst:
    print(ele)
```

### List Comprehension

```python
sqrs = []

for i in range(10):
    sqrs.append(i**2)

print(sqrs)

sqrs = [i**2 for i in range(10)]
print(sqrs)

lst = [-10, -20, 10, 20, 50]
new_lst = [i * 2 for i in lst]
print(new_lst)

new_lst = [i * 2 for i in lst if i >= 0]
print(new_lst)

new_lst = [(i, i**2) for i in range(10)]
print(new_lst)
```

### Matrix Transpose Example

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

transposed = []

for i in range(4):
    lst = []
    for row in matrix:
        lst.append(row[i])
    transposed.append(lst)

print(transposed)

transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)
```

## Tuple

| **Operation**         | **Description**              | **Example**              | **Output**         |
| --------------------- | ---------------------------- | ------------------------ | ------------------ |
| Create a tuple        | Define with `()`             | `coords = (10, 20, 30)`  | `(10, 20, 30)`     |
| Single element tuple  | Add comma after single value | `single = (5,)`          | `(5,)`             |
| Access element        | Use index (0-based)          | `coords[0]`              | `10`               |
| Negative index        | Access from end              | `coords[-1]`             | `30`               |
| Slice tuple           | Get subtuple                 | `coords[0:2]`            | `(10, 20)`         |
| Concatenate tuples    | Combine two tuples           | `(1,2) + (3,4)`          | `(1, 2, 3, 4)`     |
| Repeat tuple          | Duplicate items              | `(1,2) * 2`              | `(1, 2, 1, 2)`     |
| Check existence       | Use `in` keyword             | `10 in coords`           | `True`             |
| Length of tuple       | Count items                  | `len(coords)`            | `3`                |
| Tuple unpacking       | Assign elements to variables | `x, y, z = coords`       | `x=10, y=20, z=30` |
| Count value           | Count occurrences of value   | `coords.count(10)`       | `1`                |
| Index of value        | Find first index of value    | `coords.index(20)`       | `1`                |
| Immutable             | Cannot modify after creation | `coords[0] = 5  # Error` | TypeError          |
| Convert list to tuple | Use `tuple()`                | `tuple([1,2,3])`         | `(1,2,3)`          |
| Nested tuple          | Tuples inside tuples         | `nested = (1,(2,3),4)`   | `(1,(2,3),4)`      |


### Tuple

```python
t = ()
t = (1, 2, 3)
t = (1, 2, 3, 'Mash')
t = ((1, 2, 3), ('Mash', 'Safa'))
t = ('Mash')
print(type(t))

t = ('Mash',)
print(type(t))

t = ('ABC', ('Mash', 'Safa'))
print(t[1][0])

t = (1,2,3,4,5,6, [1,2,3,4])
print(t)
print(t[1:4])
print(t[6][0])

del t

t = (1, 2, 3, 1, 3, 3, 4, 1)
print(t.count(1))
print(t.index(1))
print(1 in t)
```
```python
t = (1, 2, 3, 4, 5, 6)
print(len(t))

t = (4, 5, 3, 2, 1)
nt = sorted(t)
print(nt)

t = (4, 5, 3, 2, 1)
print(max(t))
print(min(t))
print(sum(t))

```

## Set

| **Operation**        | **Description**                        | **Example**                             | **Output**                     |                     |
| -------------------- | -------------------------------------- | --------------------------------------- | ------------------------------ | ------------------- |
| Create a set         | Define with `{}`                       | `fruits = {"apple", "banana", "mango"}` | `{'apple', 'banana', 'mango'}` |                     |
| Add element          | Add single item                        | `fruits.add("orange")`                  | Adds 'orange'                  |                     |
| Update set           | Add multiple items                     | `fruits.update(["kiwi", "melon"])`      | Adds multiple elements         |                     |
| Remove element       | Remove item; raises error if missing   | `fruits.remove("banana")`               | Removes 'banana'               |                     |
| Discard element      | Remove item; no error if missing       | `fruits.discard("banana")`              | Safe remove                    |                     |
| Pop element          | Remove arbitrary element               | `fruits.pop()`                          | Returns removed item           |                     |
| Clear set            | Remove all items                       | `fruits.clear()`                        | `set()`                        |                     |
| Length of set        | Count items                            | `len(fruits)`                           | `3`                            |                     |
| Union                | Combine sets                           | `A.union(B)` or \`A                     | B\`                            | All unique elements |
| Intersection         | Common elements                        | `A.intersection(B)` or `A & B`          | Elements in both sets          |                     |
| Difference           | Elements in A not in B                 | `A.difference(B)` or `A - B`            | Unique to A                    |                     |
| Symmetric Difference | Elements in either A or B but not both | `A.symmetric_difference(B)` or `A ^ B`  | Non-overlapping elements       |                     |
| Check existence      | Use `in` keyword                       | `'apple' in fruits`                     | `True`                         |                     |
| Immutable Set        | `frozenset()`                          | `fs = frozenset([1,2,3])`               | Immutable set                  |                     |
| Convert list to set  | Use `set()`                            | `set([1,2,2,3])`                        | `{1,2,3}`                      |                     |
| Iterate              | Loop through items                     | `for f in fruits: print(f)`             | Prints elements                |                     |


```python
s = {1, 2, 3}
print(type(s))
print(s)

s = set([1, 2, 3, 1])
print(s)

s.add(4)
print(s)

s.update([5, 6, 1])
print(s)

s.update([8, 9], {10, 2, 3})
print(s)

s.discard(1)
print(s)

s.remove(2)
print(s)

s.pop()
print(s)

s.clear()
print(s)

```

#### Set Operations
```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1 | set2)
print(set1.union(set2))

print(set1 & set2)
print(set1.intersection(set2))

print(set1 - set2)
print(set1.difference(set2))

print(set1 ^ set2)
print(set1.symmetric_difference(set2))

print(set1.issubset(set2))
print(set2.issubset(set1))

set1 = frozenset([1, 2, 3, 4, 5])
set2 = frozenset([4, 5, 6, 7, 8])

```


```python



```