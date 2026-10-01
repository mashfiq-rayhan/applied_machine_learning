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

### Dictionary

| **Operation**            | **Description**                      | **Example**                                      | **Output**                                    |                   |
| ------------------------ | ------------------------------------ | ------------------------------------------------ | --------------------------------------------- | ----------------- |
| Create dictionary        | Define with `{}`                     | `person = {"name": "Mashfiq", "age": 25}`        | `{'name': 'Mashfiq', 'age': 25}`              |                   |
| Access value             | Get value by key                     | `person["name"]`                                 | `'Mashfiq'`                                   |                   |
| Get with default         | Avoid KeyError if key not found      | `person.get("gender", "N/A")`                    | `'N/A'`                                       |                   |
| Add / Update value       | Assign new or existing key           | `person["city"] = "Dhaka"`                       | Adds/updates key                              |                   |
| Remove key               | Remove specific key                  | `person.pop("age")`                              | Returns removed value                         |                   |
| Remove last item         | Remove last inserted key-value pair  | `person.popitem()`                               | Returns tuple (key, value)                    |                   |
| Delete key               | Remove using `del`                   | `del person["name"]`                             | Deletes 'name'                                |                   |
| Clear dictionary         | Remove all items                     | `person.clear()`                                 | `{}`                                          |                   |
| Length                   | Count number of keys                 | `len(person)`                                    | `2`                                           |                   |
| Keys                     | Get all keys                         | `person.keys()`                                  | `dict_keys(['name','age'])`                   |                   |
| Values                   | Get all values                       | `person.values()`                                | `dict_values(['Mashfiq',25])`                 |                   |
| Items                    | Get key-value pairs                  | `person.items()`                                 | `dict_items([('name','Mashfiq'),('age',25)])` |                   |
| Check existence          | Test if key exists                   | `'name' in person`                               | `True`                                        |                   |
| Dictionary comprehension | Create dict with expression          | `{x: x**2 for x in (1,2,3)}`                     | `{1: 1, 2: 4, 3: 9}`                          |                   |
| Merge dictionaries       | Combine two dicts (Python 3.9+)      | \`dict1                                          | dict2\`                                       | Merged dictionary |
| Update dictionary        | Update with another dict             | `person.update({"age": 30})`                     | Updates 'age' to 30                           |                   |
| Copy dictionary          | Shallow copy                         | `new_dict = person.copy()`                       | Same dictionary copy                          |                   |
| Nested dictionary        | Dictionary inside another dictionary | `student = {"info": {"name": "Ali", "age": 22}}` | Nested dict structure                         |                   |

### Dictionary

```python
my_dict = {}

my_dict = {1: "abc", 2: "xyz"}
print(my_dict)

my_dict = {"name": "Mash", 1: ["abc", "xyz"]}
print(my_dict)

my_dict = dict()
my_dict = dict([(1, "abc"), (2, "xyz")])
print(my_dict)

my_dict = {'name': 'Mash', 'age': 31, 'address': 'Khulna'}
print(my_dict['name'])
print(my_dict)
print(my_dict.get('address'))
```

```python
my_dict = {'name': 'Mash', 'age': 31, 'address': 'Khulna'}
my_dict['name'] = 'Ray'
print(my_dict)
my_dict['degree'] = 'BSc CSE'
print(my_dict)
print(my_dict.get('address'))

print(my_dict.pop('age'))
print(my_dict)

my_dict = {'name': 'Mash', 'age': 31, 'address': 'Khulna'}
print(my_dict.popitem())
print(my_dict)

squares = {2: 4, 3:9, 4:16, 5:25}
del squares[2]
print(squares)

squares.clear()
print(squares)

del squares
# print(squares)
```

```python
squares = {2: 4, 3:9, 4:16, 5:25}

squares_c = squares.copy()
print(squares_c)

subjects = {}.fromkeys(['Math', 'English', 'Bangla'], 0)
print(subjects)

squares = {2: 4, 3:9, 4:16, 5:25}

print(squares.items())

print(squares.keys())

print(squares.values())
```
```python
d = {}
print(dir(d))
```
```python
d = {"a": 1, "b": 2, "c": 3, "d": 4}

dnew = {k: v for k, v in d.items() if (v > 2)}
print(dnew)
```
```python
d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
d = {k+'c':v for k,v in d.items() if v > 2}
print(d)
```

### String

| **Operation**     | **Description**                      | **Example**               | **Output**          |
| ----------------- | ------------------------------------ | ------------------------- | ------------------- |
| Create string     | Use single, double, or triple quotes | `s = "Hello"`             | `'Hello'`           |
| Multi-line string | Triple quotes                        | \`s = '''Hello            |                     |
| World'''\`        | Multi-line string                    |                           |                     |
| Access character  | Indexing (0-based)                   | `s[0]`                    | `'H'`               |
| Negative indexing | Access from end                      | `s[-1]`                   | `'o'`               |
| Slice string      | Substring                            | `s[0:5]`                  | `'Hello'`           |
| Length            | Count characters                     | `len(s)`                  | `5`                 |
| Concatenate       | Join strings                         | `s1 + s2`                 | `'HelloWorld'`      |
| Repeat            | Repeat string multiple times         | `s * 3`                   | `'HelloHelloHello'` |
| Check substring   | `in` keyword                         | `'ell' in s`              | `True`              |
| Uppercase         | Convert to uppercase                 | `s.upper()`               | `'HELLO'`           |
| Lowercase         | Convert to lowercase                 | `s.lower()`               | `'hello'`           |
| Title Case        | First letter uppercase               | `s.title()`               | `'Hello'`           |
| Capitalize        | First character uppercase            | `s.capitalize()`          | `'Hello'`           |
| Strip whitespace  | Remove leading/trailing spaces       | `s.strip()`               | `'Hello'`           |
| Replace           | Replace substring                    | `s.replace('H','J')`      | `'Jello'`           |
| Split             | Split into list                      | `s.split('l')`            | `['He', '', 'o']`   |
| Join              | Join iterable into string            | `'-'.join(['a','b','c'])` | `'a-b-c'`           |
| Find              | Find index of substring              | `s.find('l')`             | `2`                 |
| Count             | Count occurrences of substring       | `s.count('l')`            | `2`                 |
| Check start       | Starts with substring                | `s.startswith('He')`      | `True`              |
| Check end         | Ends with substring                  | `s.endswith('lo')`        | `True`              |
| Format            | Format strings                       | `f'Name: {name}'`         | `'Name: Mashfiq'`   |
| Escape characters | `\n`, `\t`, `\'`, `\"`, `\\`         | `s = 'Hello\nWorld'`      | Multi-line string   |
| Raw string        | Ignore escape characters             | `r'C:\path\file'`         | `'C:\path\file'`    |


```python
nstr = "Hello"

print(nstr[0])
print(nstr[-1])
print(nstr[2:5])
```

```python
count = 0
for l in 'Hello World':
    if l == 'o':
        count+=1
        
print(count)

print('l' in 'hello world')
print('or' in 'hello world')
```
```python
astr = "This is a String"

print(astr.lower())
print(astr.upper())
print(astr.split())
print(' '.join(['This', 'is', 'a', 'String']))
print('-'.join(['This', 'is', 'a', 'String']))
print(astr.find('Str'))
print(astr.replace('String', "Sentence"))

```
```python
myStr = "MadaM"

myStr = myStr.lower()

revStr = reversed(myStr)

if list(myStr) == list(revStr):
    print("This is a palindrome!")
else:
    print("This is not a palindrome!")
```
```python
myStr = "python Program to Sort words in Alphabetic Order"

words = myStr.split()

swords = sorted(words)
print(swords)

words.sort()
print(words)

for word in words:
    print(word)
```

### Functions

| **Function Type / Operation**     | **Description**                           | **Syntax / Example**                             | **Output / Notes**                               |
| --------------------------------- | ----------------------------------------- | ------------------------------------------------ | ------------------------------------------------ |
| Regular function                  | Define with `def`                         | `def greet(): return 'Hello'`                    | Function object; call with `greet()` → `'Hello'` |
| Function with parameters          | Accept input values                       | `def add(a, b): return a+b`                      | `add(2,3)` → `5`                                 |
| Default parameters                | Parameter has default value               | `def add(a, b=10): return a+b`                   | `add(5)` → `15`                                  |
| Keyword arguments                 | Specify parameter by name                 | `add(b=5,a=3)`                                   | `8`                                              |
| Arbitrary positional arguments    | Accept variable number of arguments       | `def func(*args): return sum(args)`              | `func(1,2,3)` → `6`                              |
| Arbitrary keyword arguments       | Accept variable number of named arguments | `def func(**kwargs): return kwargs`              | `func(a=1,b=2)` → `{'a':1,'b':2}`                |
| Return multiple values            | Return tuple of values                    | `def f(): return 1,2,3`                          | `(1,2,3)`                                        |
| Lambda (anonymous) function       | Inline single-expression function         | `f = lambda x: x*2`                              | `f(5)` → `10`                                    |
| Function annotations / type hints | Provide type hints                        | `def add(a:int,b:int)->int: return a+b`          | Type hints only                                  |
| Nested function                   | Define function inside another function   | `def outer(): def inner(): pass`                 | Inner accessible only within outer               |
| Recursion                         | Function calling itself                   | `def fact(n): return 1 if n==0 else n*fact(n-1)` | `fact(5)` → `120`                                |
| Higher-order function             | Function as argument or return value      | `map(lambda x:x*2,[1,2,3])`                      | `[2,4,6]`                                        |
| Decorator                         | Modify or enhance another function        | \`@decorator                                     |                                                  |
| def f(): pass\`                   | Modified function                         |                                                  |                                                  |
| Docstring                         | Documentation string for function         | `def f(): """Docs"""`                            | Access via `f.__doc__`                           |


```python
def print_name(name):
    """
    This Function prints a name
    """
    print(name)
    
print_name('Mash')

def add(a, b):
    return a + b

def add(a, b=10):
    return a + b

x = add(5, 6)
print(x)

x = add(5)
print(x)


def sums(*args):
    return sum(args)

x = sums(1, 2, 3, 4, 5, 6)
print(x)
```

```python
def computeHCF(a, b):
    smaller = b if a > b else a
    hcf = 1
    
    for i in range(1, smaller+1):
        if (a % i == 0) and (b % i == 0):
            hcf = i
    
    return hcf

x = computeHCF(50, 60)
print(x)
```

### Types of Functions

Python functions can be broadly classified into the following types:

| **Function Type**                 | **Description**                                                         | **Example**                                      |
| --------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------ |
| Built-in Functions                | Predefined functions provided by Python                                 | `len()`, `print()`, `type()`, `sum()`            |
| User-defined Functions            | Functions defined by the user using `def` keyword                       | `def greet(): return 'Hello'`                    |
| Anonymous / Lambda Functions      | Single-expression, unnamed functions                                    | `f = lambda x: x*2`                              |
| Recursive Functions               | Functions that call themselves                                          | `def fact(n): return 1 if n==0 else n*fact(n-1)` |
| Higher-order Functions            | Functions that take other functions as arguments or return functions    | `map(lambda x:x*2,[1,2,3])`                      |
| Nested / Inner Functions          | Functions defined inside another function                               | `def outer(): def inner(): pass`                 |
| Generator Functions               | Functions that yield values one at a time using `yield`                 | `def gen(): yield 1`                             |
| Decorator Functions               | Functions that modify/enhance other functions                           | \`@decorator                                     |
| def f(): pass\`                   |                                                                         |                                                  |
| Coroutine Functions               | Functions that can pause and resume execution using `async` and `await` | `async def fetch(): await task()`                |
| Class / Static / Instance Methods | Functions defined inside a class                                        | `class A: def method(self): pass`                |


### Built-in Functions

| **Category**         | **Function**                                         | **Description**                                            | **Example**                       | **Output**      |
| -------------------- | ---------------------------------------------------- | ---------------------------------------------------------- | --------------------------------- | --------------- |
| Type Conversion      | `int()`, `float()`, `str()`, `bool()`                | Convert values between types                               | `int('10')`                       | `10`            |
| Numeric              | `abs()`, `round()`, `pow()`, `divmod()`              | Absolute, rounding, power, division remainder              | `abs(-5)`                         | `5`             |
| Sequence             | `len()`, `max()`, `min()`, `sum()`, `sorted()`       | Work on sequences like list, tuple, string                 | `len([1,2,3])`                    | `3`             |
| Iterables            | `all()`, `any()`, `enumerate()`, `zip()`             | Check conditions, iterate with index, pair sequences       | `all([True, False])`              | `False`         |
| Object/Introspection | `type()`, `id()`, `isinstance()`, `dir()`, `help()`  | Inspect object type, memory, attributes                    | `type(5)`                         | `<class 'int'>` |
| Input/Output         | `print()`, `input()`, `open()`, `repr()`, `format()` | Output, read input, file operations                        | `print('Hello')`                  | `Hello`         |
| Functional           | `map()`, `filter()`, `reduce()`, `sorted()`          | Apply functions on iterables                               | `list(map(lambda x:x*2,[1,2,3]))` | `[2,4,6]`       |
| Others               | `range()`, `eval()`, `exec()`, `chr()`, `ord()`      | Generate sequences, evaluate strings, char code conversion | `range(3)`                        | `0,1,2`         |

```python
x = -100
print(abs(x))

lst = [1, 2, 3, 4]
print(all(lst))

lst = [0, 1, 2, 3, 4]
print(all(lst))

lst = []
print(all(lst))

lst = [False, 1, 2]
print(all(lst))
```
```python
numbers = [1, 2, 3]
print(dir(numbers))
```
```python
print(divmod(9,2))
```
```python
numbers = [10, 20, 30, 40, 50]
for index,num in enumerate(numbers):
    print(index, "---", num)

numbers = [10, 20, 30, 40, 50]
for index,num in enumerate(numbers, 10):
    print(index, "---", num)
```
```python
lst = [1, 2, 3, 4, 5]
print(isinstance(lst, list))

t = (1, 2, 3, 4, 5)
print(isinstance(t, list))
```

### Filter
```python
def posnum(x):
    if x > 0:
        return x
    
number_list = range(-10, 10)
print(list(number_list))

pos = list(filter(lambda x: x > 0, number_list))
print(pos)

pos = list(filter(posnum, number_list))
print(pos)
```

### Map
```python
numbers = [1, 2, 3, 4, 5]

def power2(num):
    return num**2

squared = list(map(power2, numbers))
print(squared)

squared = list(map(lambda x: x ** 2, numbers))
print(squared)
```

### Reduce
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]


def reducedsum(x, y):
    return x + y


squared = reduce(reducedsum, numbers)
print(squared)

squared = reduce(lambda x, y: x + y, numbers)
print(squared)
```

### Recursion
```python
def factorial(num):
    return 1 if num == 1 else (num * factorial(num-1))

result = factorial(10)
print(result)
```

### Fibonacci
```python
def fibonacci(num):
    return num if num <= 1 else fibonacci(num - 1) + fibonacci(num - 2)


nterms = 10
print(range(nterms))
print(list(range(nterms)))

print("Fibonacci Sequence: ")
for num in range(nterms):
    print(fibonacci(num))
```

### Lambda
```python
double = lambda x : x * 2
print(double(10))
square = lambda x : x ** 2
print(square(10))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evn = list(filter(lambda x: (x % 2 == 0), lst))
print(evn)

sqr = list(map(lambda x: x ** 2, lst))
print(sqr)

from functools import reduce
add = reduce(lambda x, y: x + y, lst)
print(add)

```

### Modules

| **Module**        | **Description**                                     | **Example Usage**                                                   |
| ----------------- | --------------------------------------------------- | ------------------------------------------------------------------- |
| `os`              | Interact with operating system (files, directories) | `import os; os.getcwd()`                                            |
| `sys`             | System-specific parameters and functions            | `import sys; sys.argv`                                              |
| `math`            | Mathematical functions                              | `import math; math.sqrt(16)`                                        |
| `random`          | Generate random numbers                             | `import random; random.randint(1,10)`                               |
| `datetime`        | Work with dates and times                           | `from datetime import date; date.today()`                           |
| `time`            | Time-related functions                              | `import time; time.sleep(2)`                                        |
| `re`              | Regular expressions                                 | `import re; re.findall(r'\d+', 'abc123')`                           |
| `json`            | Parse and generate JSON data                        | `import json; json.dumps({'a':1})`                                  |
| `csv`             | Read/write CSV files                                | `import csv; csv.reader(open('file.csv'))`                          |
| `collections`     | Specialized container datatypes                     | `from collections import Counter`                                   |
| `itertools`       | Functions creating iterators                        | `import itertools; itertools.permutations([1,2,3])`                 |
| `functools`       | Higher-order functions and operations               | `from functools import reduce`                                      |
| `os.path`         | Path manipulation                                   | `import os.path; os.path.join('a','b')`                             |
| `subprocess`      | Run and manage subprocesses                         | `import subprocess; subprocess.run(['ls'])`                         |
| `urllib`          | Work with URLs                                      | `from urllib import request; request.urlopen('http://example.com')` |
| `requests`        | HTTP requests (3rd-party library)                   | `import requests; requests.get('http://example.com')`               |
| `tkinter`         | GUI development                                     | `import tkinter; tkinter.Tk()`                                      |
| `socket`          | Network programming                                 | `import socket; socket.socket()`                                    |
| `logging`         | Logging facility                                    | `import logging; logging.info('message')`                           |
| `pickle`          | Object serialization                                | `import pickle; pickle.dump(obj, file)`                             |
| `threading`       | Multithreading                                      | `import threading; threading.Thread(target=func)`                   |
| `multiprocessing` | Multi-process parallelism                           | `import multiprocessing; multiprocessing.Process(target=func)`      |
| `math`            | Advanced math functions                             | `import math; math.factorial(5)`                                    |
| `statistics`      | Statistical functions                               | `import statistics; statistics.mean([1,2,3])`                       |

---

> **Tip:** Use `help(module_name) and dir(module_name)` in Python to see all functions and classes available in that module.


```python
import math
help(math)

import datetime
help(datetime)

from math import *
dir(math)
help(math)
```

### File I/O 

#### Opening a File

```python
f = open('file.txt', 'r')      # read (default)
f = open('file.txt', 'w')      # write (overwrite)
f = open('file.txt', 'a')      # append
f = open('file.txt', 'rb')     # read binary
f = open('file.txt', 'wb')     # write binary
```

#### Closing a File

```python
f.close()  # always close files when done
```

#### Using `with` Statement (Recommended)

```python
with open('file.txt', 'r') as f:
    data = f.read()  # automatically closes the file
```

#### Reading from a File

```python
f.read(size)          # read 'size' bytes, all if omitted
f.readline()          # read one line
f.readlines()         # read all lines as a list
```

##### Example:

```python
with open('file.txt', 'r') as f:
    for line in f:
        print(line, end='')
```

#### Writing to a File

```python
f.write('Hello')       # write string
f.writelines(list_of_strings)  # write multiple lines
```

##### Example:

```python
with open('file.txt', 'w') as f:
    f.write('Hello World\n')
    f.writelines(['Line1\n', 'Line2\n'])
```

#### File Methods

| Method                   | Description                 |
| ------------------------ | --------------------------- |
| `f.read(size)`           | Read 'size' bytes from file |
| `f.readline()`           | Read next line from file    |
| `f.readlines()`          | Read all lines into a list  |
| `f.write(str)`           | Write string to file        |
| `f.writelines(list)`     | Write list of strings       |
| `f.flush()`              | Flush internal buffer       |
| `f.seek(offset, whence)` | Move file cursor            |
| `f.tell()`               | Current file position       |

#### File Objects are Iterables

```python
with open('file.txt') as f:
    for line in f:
        print(line, end='')
```

#### Binary Files

```python
with open('file.bin', 'rb') as f:
    data = f.read()
with open('file.bin', 'wb') as f:
    f.write(b'Binary data')
```

#### File Buffering

```python
f = open('file.txt', 'w', buffering=1)  # line buffering
```

#### Misc Tips

* Always use `with` to handle files safely.
* Text mode `t` is default.
* Binary mode `b` is required for non-text files.
* Use `os` module for file operations like remove, rename, path checks.


### File I/O 

#### Opening a File

```python
f = open('file.txt', 'r')      # read (default)
f = open('file.txt', 'w')      # write (overwrite)
f = open('file.txt', 'a')      # append
f = open('file.txt', 'rb')     # read binary
f = open('file.txt', 'wb')     # write binary
```

#### Closing a File

```python
f.close()  # always close files when done
```

#### Using `with` Statement (Recommended)

```python
with open('file.txt', 'r') as f:
    data = f.read()  # automatically closes the file
```

#### Reading from a File

```python
f.read(size)          # read 'size' bytes, all if omitted
f.readline()          # read one line
f.readlines()         # read all lines as a list
```

##### Example:

```python
with open('file.txt', 'r') as f:
    for line in f:
        print(line, end='')
```

#### Writing to a File

```python
f.write('Hello')       # write string
f.writelines(list_of_strings)  # write multiple lines
```

##### Example:

```python
with open('file.txt', 'w') as f:
    f.write('Hello World\n')
    f.writelines(['Line1\n', 'Line2\n'])
```

#### File Methods

| Method                   | Description                 |
| ------------------------ | --------------------------- |
| `f.read(size)`           | Read 'size' bytes from file |
| `f.readline()`           | Read next line from file    |
| `f.readlines()`          | Read all lines into a list  |
| `f.write(str)`           | Write string to file        |
| `f.writelines(list)`     | Write list of strings       |
| `f.flush()`              | Flush internal buffer       |
| `f.seek(offset, whence)` | Move file cursor            |
| `f.tell()`               | Current file position       |

#### File Objects are Iterables

```python
with open('file.txt') as f:
    for line in f:
        print(line, end='')
```

#### Binary Files

```python
with open('file.bin', 'rb') as f:
    data = f.read()
with open('file.bin', 'wb') as f:
    f.write(b'Binary data')
```

#### File Buffering

```python
f = open('file.txt', 'w', buffering=1)  # line buffering
```

#### Misc Tips

* Always use `with` to handle files safely.
* Text mode `t` is default.
* Binary mode `b` is required for non-text files.
* Use `os` module for file operations like remove, rename, path checks.


```python
f = open('file.txt')
f = open('file.txt', 'r') # read (default)
f = open('file.txt', 'w') # write (overwrite)
f = open('file.txt', 'a') # append
f = open('file.txt', 'rb') # read binary
f = open('file.txt', 'wb') # write binary

f.read()
f.read(4)
f.tell()
f.seek(4)

f.seek(0)
for line in f:
    print(line)
    
f.readline()
f.readlines()
```
```python
import os

os.rename("test.txt", "file.txt")
os.remove("file.txt")
```

### OS File Operations

#### Rename a File

```python
import os
os.rename('old_name.txt', 'new_name.txt')
```

#### Remove/Delete a File

```python
import os
os.remove('file.txt')  # delete file
```

#### Check if File or Directory Exists

```python
import os
os.path.exists('file.txt')        # True if exists
os.path.isfile('file.txt')        # True if it's a file
os.path.isdir('folder')            # True if it's a directory
```

#### List Files in a Directory

```python
import os
os.listdir('.')  # list files and directories in current directory
```

#### Create a Directory

```python
import os
os.mkdir('new_folder')           # create single directory
os.makedirs('folder1/folder2')  # create nested directories
```

#### Remove a Directory

```python
import os
os.rmdir('folder')               # remove empty directory
os.removedirs('folder1/folder2') # remove nested empty directories
```

#### Get Current Working Directory

```python
import os
cwd = os.getcwd()
print(cwd)
```

#### Change Directory

```python
import os
os.chdir('new_folder')
```

#### Get Absolute Path

```python
import os
abs_path = os.path.abspath('file.txt')
print(abs_path)
```

#### Join Paths Safely

```python
import os
path = os.path.join('folder', 'file.txt')
```

#### File Size

```python
import os
size = os.path.getsize('file.txt')
```

#### Check Read/Write/Execute Permissions

```python
import os
os.access('file.txt', os.R_OK)  # read permission
os.access('file.txt', os.W_OK)  # write permission
os.access('file.txt', os.X_OK)  # execute permission
```

```python
import os 
os.getcwd()
os.chdir('the path')
os.listdir(os.getcwd())
os.mkdir()
os.rmdir()

import shutil

shutil.rmtree("test")
```

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')
```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
```python

```
