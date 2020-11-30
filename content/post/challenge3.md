+++
title = "Challenge 3: Python Stack Traces"
date = "2020-11-25"
author = "Stacy Bridges"
cover = "img/stacktrace.jpg"
description = "**Challenge 3**: Your task is to examine the stack traces and provide a brief response for each one..."
+++
## Problem Statement

Your task is to examine the stack traces and provide a brief response for each one that summarizes what the problem or likely problem is,
and the first line of code you would jump to in your code editor given the trace.

#
---
#

## My Response
### Contents: {#contents}
- **[Problem 1](#prob-1)** `TypeError: can only concatenate str (not "int") to str`
- **[Problem 2](#prob-2)** `TypeError: unsupported operand type(s) for +: 'int' and 'str`
- **[Problem 3](#prob-3)** `TypeError: can't multiply sequence by non-int of type 'str'`
- **[Problem 4](#prob-4)** `TypeError: can't multiply sequence by non-int of type 'list'`
- **[Problem 5](#prob-5)** `ValueError: Invalid`
- **[Problem 6](#prob-6)** `TypeError: zip argument #2 must support iteration`
- **[Problem 7](#prob-7)** `TypeError: can only concatenate list (not "int") to list`
- **[Problem 8](#prob-8)** `TypeError: unsupported operand type(s) for +: 'int' and 'str'`
- **[Problem 9](#prob-9)** `KeyError: 'one'`
#
---
# {#prob-1}
### Traceback Problem 1:
```
Traceback (most recent call last):
  File "stack_traces.py", line 36, in run_trace
    f()
  File "stack_traces.py", line 45, in <lambda>
    run_trace(1, lambda: perform_calculation(add, '1', 3))
  File "stack_traces.py", line 8, in perform_calculation
    calc(x, y)
  File "stack_traces.py", line 12, in add
    return x + y
TypeError: can only concatenate str (not "int") to str
```
### Answer:
Unlike JavaScript, the Python language won't attempt to dynamically cast variables when operands present a mixed bag to the **'+'** operator.
So, the issue in this trace is that the operands need to be of the same type.

It appears that **x** was cast as **string** and **y** was cast as a **number**. So, I'd say:
- if the calculation is supposed to be **arithmetic**, I would re-cast **x** as a **number**
- if the calculation is supposed to be **stringy**, I would re-cast **y** as a **string**
- in either case, I would make the adjustment in the caller at **line 45**

#
[`Go to Contents`](#contents)
#
---
# {#prob-2}
### Traceback Problem 2:{#a-name}
```
Traceback (most recent call last):
  File "stack_traces.py", line 36, in run_trace
    f()
  File "stack_traces.py", line 46, in <lambda>
    run_trace(2, lambda: perform_calculation(add, 7, '3'))
  File "stack_traces.py", line 8, in perform_calculation
    calc(x, y)
  File "stack_traces.py", line 12, in add
    return x + y
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
### Answer:
As with **Problem 1**, the operands need to be of the same type. The `TypeError` message is different, but the problem is essentially the same.

Again, I would decide if the operation is supposed to be **arithmetic** or **stringy**, and then I would recast the offending variable in the caller at **line 46**.  

#
[`Go to Contents`](#contents)
#
---
# {#prob-3}
### Traceback Problem 3:
```
Traceback (most recent call last):
  File "stack_traces.py", line 36, in run_trace
    f()
  File "stack_traces.py", line 47, in <lambda>
    run_trace(3, lambda: perform_calculation(mult, '3', '3'))
  File "stack_traces.py", line 8, in perform_calculation
    calc(x, y)
  File "stack_traces.py", line 15, in mult
    return x * y
TypeError: can't multiply sequence by non-int of type 'str'
```
### Answer:
Yes, Python lets you *'multiply'* strings if your use case requires it. However, you must multiply a string with a number. A string-on-string operation is not allowed with this operator.

If the intention here is only to return **x** number of strings, then the placement of the *number* and *string* operands is not important, but you must have one of each:

``` python
print(  3  * '3' )  # 333
print( '3' *  3  )  # 333
print( '3' * '3' )  # TypeError !
```

If you want to use a multiplier with other data types besides strings, the placement of the operands may become important.
My rule of thumb is to place the *multiplicand* in the *left operand* and the *multiplier* in the *right operand*.

So, to remedy the code, I would probably go to **line 47** and try casting one of the **'3'** arguments as a number (i.e., the *multiplier*)... preferably, the argument in the **y** position, i.e.:
```python
perform_calculation( mult, '3', 3 )
```
#
[`Go to Contents`](#contents)
#
---
# {#prob-4}
### Traceback Problem 4:
```
Traceback (most recent call last):
  File "stack_traces.py", line 36, in run_trace
    f()
  File "stack_traces.py", line 48, in <lambda>
    run_trace(4, lambda: perform_calculation(mult, [4], [3]))
  File "stack_traces.py", line 8, in perform_calculation
    calc(x, y)
  File "stack_traces.py", line 15, in mult
    return x * y
TypeError: can't multiply sequence by non-int of type 'list'
```
### Answer:
This problem is similar to **Problem 3** except that it uses a different data type.

To solve this problem, I would go to the caller at **line 48** and re-cast the argument in the **y** position as a number (the *multiplier*), i.e.:
```python
perform_calculation( mult, [4], 3 )
```

Of course, if the desired output is `[3,3,3,3]` instead of `[4,4,4]`, then I would swap the numbers as well as re-cast, i.e.:
```python
perform_calculation( mult, [3], 4 )
```
#
[`Go to Contents`](#contents)
#
---
# {#prob-5}
### Traceback Problem 5:
```
Traceback (most recent call last):
  File "stack_traces.py", line 36, in run_trace
    f()
  File "stack_traces.py", line 49, in <lambda>
    run_trace(5, lambda: perform_calculation(innoc, '1', 3))
  File "stack_traces.py", line 8, in perform_calculation
    calc(x, y)
  File "stack_traces.py", line 22, in innoc
    spelunk()
  File "stack_traces.py", line 21, in spelunk
    raise ValueError('Invalid')
ValueError: Invalid
```
### Answer:
I am guessing this error fell out of a `try: , except:` structure in the **spelunk()** method.

I would probably go to **line 21** to figure out which condition failed.

#
[`Go to Contents`](#contents)
#
---
# {#prob-6}
### Traceback Problem 6:
```
Traceback (most recent call last):
  File "stack_traces.py", line 36, in run_trace
    f()
  File "stack_traces.py", line 50, in <lambda>
    run_trace(6, lambda: comp_calc([1, 2, 3], 1, add))
  File "stack_traces.py", line 30, in comp_calc
    return [perform_calculation(calc, x_i, y_i) for x_i, y_i in zip(x, y)]
TypeError: zip argument #2 must support iteration
```
### Answer:
The `zip()` function in Python is an iterator, so it can be used with iterable data.
In this stack trace, it looks like we tried to pass non-iterable data to the `zip()` function.

Specifically, the argument **'1'** passed into the function per **line 50** is not iterable.

While the value **'1'** is itself not atomizable, it can still be made iterable by casting it
into an iterable context. For instance, you could wrap it in a list or tuple container,
which would *'band-aid'* the code to a certain extent... i.e., the
code should work with such a re-cast, but any parallelism that is typically achieved by the `zip()`
function would be lost because it would only be able to iterate the length of the shortest container.

To me, it would make sense to poke around **line 30** to understand what the calculation is supposed to achieve, and
then modify the caller at **line 50** to make sure the arguments can work properly with the calculation to get the job done.

#
[`Go to Contents`](#contents)
#
---
# {#prob-7}
### Traceback Problem 7:
```
Traceback (most recent call last):
  File "stack_traces.py", line 36, in run_trace
    f()
  File "stack_traces.py", line 51, in <lambda>
    run_trace(7, lambda: comp_calc([1, 2, [3]], [4, 5, 6], add))
  File "stack_traces.py", line 30, in comp_calc
    return [perform_calculation(calc, x_i, y_i) for x_i, y_i in zip(x, y)]
  File "stack_traces.py", line 30, in <listcomp>
    return [perform_calculation(calc, x_i, y_i) for x_i, y_i in zip(x, y)]
  File "stack_traces.py", line 8, in perform_calculation
    calc(x, y)
  File "stack_traces.py", line 12, in add
    return x + y
TypeError: can only concatenate list (not "int") to list
```
### Answer:
Similar to the previous problem, this stack trace has two iterables that use
the `zip()` function together with an adder function to iteratively add the values in
list **y** to the values in list **x**. This time, the final values of the iterables,
namely **[3]** and **6**, cannot be added together because the Python **'+'** operator is not
equipped to handle the data-type mismatch (i.e., *list + integer*).

Again, my inclination would be to inspect the calculation first, starting around
**lines 8 and 12**, to make sure that I haven't missed something--- I think we are dealing
with a simple adder function, but maybe there is a gremlin. Afterward, I would
want to update the arguments as appropriate at **line 51**.

Because we are using a `zip()` function, our interest must be in summing the
list contents at each index, not just concatenating the lists. As a result, my
updates to the arguments at **line 51** would probably look like:  

```python
comp_calc( [1, 2, 3], [4, 5, 6], add )
```

#
[`Go to Contents`](#contents)
#
---
# {#prob-8}
### Traceback Problem 8:
```
Traceback (most recent call last):
  File "stack_traces.py", line 36, in run_trace
    f()
  File "stack_traces.py", line 52, in <lambda>
    run_trace(8, lambda: calc_dict({'one': 1, 'two': '2'}, 'one', 'two', add))
  File "stack_traces.py", line 26, in calc_dict
    return perform_calculation(calc, d[k1], d[k2])
  File "stack_traces.py", line 8, in perform_calculation
    calc(x, y)
  File "stack_traces.py", line 12, in add
    return x + y
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
### Answer:
This problem is similar to **Problem 2** except that the `TypeError` is thrown
on values that were parsed from a dictionary object.  The error is caused by the
data types being mismatched for the dictionary keys *'one'* and *'two'*.

One way to fix the issue would be to decide if the operation is supposed to be
**arithmetic** or **stringy** and then update the argument inputs as needed at
**line 52**.

- For arithmetic: `dict = { 'one': 1, 'two': 2 }`
- For stringy: `dict = { 'one': '1', 'two': '2' }`

#
[`Go to Contents`](#contents)
#
---
# {#prob-9}
### Traceback Problem 9:
```
Traceback (most recent call last):
  File "stack_traces.py", line 36, in run_trace
    f()
  File "stack_traces.py", line 53, in <lambda>
    run_trace(9, lambda: calc_dict({}, 'one', 'two', add))
  File "stack_traces.py", line 26, in calc_dict
    return perform_calculation(calc, d[k1], d[k2])
KeyError: 'one'
```
### Answer:
For this problem, when Python goes to look up the key *'one'* in the dictionary, it cannot
find it because it is not there, which results in the `KeyError` being thrown.

It appears that the dictionary at **line 53** is indeed empty, so it should be populated with `key:value` pairs.
At a minimum, it needs to contain data for the keys *'one'* and *'two'*.

#
[`Go to Contents`](#contents)
#
