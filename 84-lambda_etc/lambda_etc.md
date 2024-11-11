---
title: 'Learn Coding'
author: 'ale66'
format: 
  revealjs:
    footer: '[github.com/ale66/learn-coding](https://github.com/ale66/learn-coding)&nbsp;&nbsp;&nbsp;'
    theme: [moon]
    preview-links: auto
    chalkboard: 
      boardmarker-width: 3
from: markdown+emoji
execute:
  echo: true
---

# Lambda etc.


---

## mapping function on sequences

```python
my_values = [1, 2, 3, 4, 5]
```

Compute the squares of the first five non-zero natural numbers

```python
l = len(my_values)

squared_values = []

for i in range(l):
    s = my_values[i]**2

    squared_values.append(s)

print(squared_values)

[1, 4, 9, 16, 25]
```


---

```python
my_values = [1, 2, 3, 4, 5]
```

Compute the squares of the first five non-zero natural numbers

```python
squared_values = list()

for val in my_values:
    squared_values.append(val**2)

print(squared_values)

[1, 4, 9, 16, 25]
```

A local, *list* activity

Functions won't add much

---

## Mapping

```python
def my_square(base: int)->int:
    return base**2

my_values = [1, 2, 3, 4, 5]

print(map(my_square, my_values))

[1, 4, 9, 16, 25]
```

here `my_square` is a *functor:* the name of the function itself


---

## List comprehensions

Extensional definition: explicit naming of the items that make up the list

Intensional definition: the formula/condition that item must satisfy to be into the list

In Maths:

$
\{1, 4, 9, 16, 25\}\ =\ \{x\ :\ \exists y. x = y^2 \wedge 0<y \leq 5\wedge y\in {\cal N}}
$


---

list comprehension brings list definition closer to natural language specification

```python
extensional = [1, 2, 3, 4, 5]

# create a new list
intensional = [x**2 for x in extensional]
```

A shorter notation, closer to Mathematics

(Data Science code tends to avoid nesting of `for` and `while` cycles)


---

## More examples


# lambda definitions


---

## Traditional function definition

Computes the $\mathrm{V}_{\circ} = \frac{4}{3}\pi r^3$ formula from school

```python
def my_vol(radius: int) -> float:
    '''Traditional function definition 
    to compute the volume of a sphere'''

    import math

    volume = 4/3 * math.pi * radius**3

    return volume
```

here `my_vol` is a *functor:* the name of the function itself

The function can be applied anywhere, and several times.

Sometimes a simpler, one-time formula application could do


---

## In-line functions

There is functor, the name of the function is the function itself

```python
lambda x: x**2
```

- `lambda` defines the input 

- the output is implicit with the evaluation of the formula`

```python
(lambda x: x**2)(3)
```

will return (or be substituted with) 9.

Look at the differences:

```python
print(my_square(3))

print((lambda x: x**2)(3))
```


---

## mapping lambdas

```python
my_values = [1, 2, 3, 4, 5]

map(lambda x: x**2, my_values)
```

applies (maps) the lambda definition on each element of the list

```python
def allSquares(input_list: list) -> list
    '''Squares all values of a given list'''

    squares = list()

    for el in input_list:
        square.append(el**2)

    return squares

print(allSquares(my_values))
```


---

## putting it all together

```python
list(map(lambda x: x**2, my_values))
```

makes the results into a list. 

This complex command is executed and *substituted with its own output.*

---

```python
my_values = [1, 2, 3, 4, 5]

print(list(map(lambda x: x**2, my_values)))

[1, 4, 9, 16, 25]
```


# Functions with variable args


---

Normally, argument passing is positional:

$\log_{10} 1000=3$

$\log_2 1024=10$

```python
def mylog(base: float, exponent: float)->float:
    ''' a wrap around the standard log function'''
    import math

    return math.log(base, exponent)

my_log(1000, 10)
my_log(1024, 2)
3
10
```


---

Python functions allow calls with a variable number of parameters

This gives great flexibility

Example: by *log* often the logarithm in base 10 is intended:

we save time and have better clarity by 

- assuming that 10 is the default base
   
- allow calls like *mylog(1000)*


## default values

Assumed values are described in the `def`

```python
def mylog(base = 10, argument):
    import math

    return math.log(argument, base)
```

```python
print(mylog(1000))

3

print(mylog(1024))

3.0103
```


---

# General rule for default values





---

## Inspecting the passed values

A function can examine the values received with the call and decide a course of action


```python
def myfunc(*args):
    ''' Study the received values '''

    for a in args:
        print(a)
```


# Data challenges


---

can you [get fresh data](https://data.spectator.co.uk/category/energy) and display it?

