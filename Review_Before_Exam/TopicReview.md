# Ultimate Python Guide (TekBasic)

Here's everything you need to know before the Placement Exam...

### Jan 27 (T1)
- [Python Features](#python-features)
- [Interpreter vs Compiler](#interpreter-vs-compiler-)
- [Structure](#python-structure)
- [Variables](#python-variables-)
- [Object Memory Reference](#python-memory-reference-)
- [Strings](#python-strings-)
- [MemoryView](#memoryview)
- [Boolean and Python Operators](#python-boolean--operators)
- [Logical Conditions](#python-logical-conditions-)
- [While/For Loops](#python-loop)

### Jan 28 (T2)
- [Functions](#functions-)
- [Data Collections](#starting-data-collection)
- [Slicing](#slicing-)
- [DS Functions](#python-sequence-functions)


---

## Python Features

What makes Python **different/stand** out?
- No **Type Declaration**
- **Automatic** garbage collection 
- **OOP** concepts: *Inheritance*, *Polymorphism*, *Abstraction* and *Encapsulation* 
- Best for **Automation** 
- **Cross-platform** 
- **Multi-threading** and **Exception** handling 
- **Web** development (Django & Flask)


---

## Interpreter vs Compiler 

At core, Python is an **interpreted** language because it runs code right away without the need to *compile*. However, we could have multiple files causing Python to **compile** 

Compile just simply means we're changing **source code** (Human-readable) into **byte code** (machine-readable).

`python -m py_compile file_name.py` 
Forces Python to compile a **bytecode** file --> in **.pyc** extension

To sum it up:
Python is generally an **interpreted** language but there are some *compiling* in the background. Python does compile a **.pyc** file that's executed by the **interpreter**

---

## Python Structure

You could execute multiple **statements** on **one-line**:
`print('Hello'); python('World')`

**Indentations** are important to indicate the *block* that statement belongs to; therefore, Python is an **indentation langauge** (*PEP8* 4 for indentation)

We also have **text breaks** using `\`:

```python

text = "This " + \
        "Is " + \
        "Multiple Lines"
```

---

## Python Variables 

**Alias name** to hold/handle values to help us be more **dynamic**.

```python
c = 3 + 4j  # Imaginary I is J in programming 

# Different ways to declare int
a = 0b10    # Binary (0b), which is 2 in decimal
a2 = 0o31   # Octal (0o), which is 3×8 + 1 = 25 in decimal
a3 = 0xff   # Hexadecimal (0x), which is 15×16 + 15 = 255 in decimal
```

---

## Python Memory Reference 

Some objects might reference to the same *ID* (we could check with `id()`). This helps Python be more efficient if the *values are the same*

---

## Python Strings 

**Double** or **Single** quotes and we could use `\u` for **UTF-8** codes (special characters) or use the **char(decimal)** function instead. 

This is more useful with **Encoding/Decoding**

```python
# Binary Form
msg = b'Message to decode because it\'s in binary'
print(message.decode('utf-8'))

# Encoding regular string to binary 
reg_msg = 'Message to encode because it\'s regular string'
print(reg_msg.encode('utf-8'))
```

---

## MemoryView

Mainly useful to handle binary data by creating a *memoryview* from *bytearray* to avoid copying large data structures.

```python
mv = memoryview(bytearray([97, 98, 99]))  # Create a memory view of a bytearray
print(mv[0])  # Access the first byte
```

---

## Python Boolean & Operators

Useful when working with **conditional statements** because of **True/False** values. 

**Arithmatic**
- `+`, `-`, `*`, `/`, `//` (Whole division no remainders), `%` Divisible, `**`

**Comparison**
- `==`, `!=`, `>`, `<`, `>=`, `<=`

**Logical**
- `and`, `or`, `not`

**Assignments**
- `+=`, `-=`, `/=` (Floating), `//=` (Int), `%=` (remainders), `**` 

**Identity** vs **Membership**
- `is` checks for the same `id()` instead of value (`==`)
- `in` belonging to a certain **sequence** 

**Bitwise**
- Used to compare binaries
- Quick Binary Crash Course (e.g `0101`) 
    - Read from **right to left**
    - Each time we move we increase the **power** so starting at right-side **2^0** then **2^1** ... **2^n**
        - 1 means that we'll add that value to the next available 1
- `&` checks for 1 in both binary comparison (`0011` and `0101` will be `0001`)
-  `|` same as `&` except it will check for all positions with 1
- `^` returns 1 if bits are **different** 0 if same 
- `~` inverts bits 
- We also have `a<<1` to **multiple** by 2 & `a>>1` to **divide** by 2

---

## Python Logical Conditions 

**If Elif Else** blocks. We could use **if-else** on a oneliner

```python

if condition:
    # Do something if True
    pass
elif another_condition:
    # Do something if a different condition 
    pass
else:
    # Do something if none of our conditions match 
    pass 

print('Hello') if condition else 'World'

```

---

## Python Loop

It's important to understand some **control flow** methods:
- `break` will exit out the loop
- `continue` skip the current iteration 
- `pass` to do nothing in that scenario

**While Loop** continuous loop until a certain condition is **met** (or break case)

```python

counter = 0
while counter != 10:
    # Do something
    ...
    # Increment counter/condition 
    counter += 1 
    # or manually break
    break 

```

**For Loop** prepared loop

```python

a = 'str'
for string in a:
    print(string)

# Iterators/Range 
# 0-9
for i in range(10):
    print(i)
```

---

## Functions 

**Reusable** code with **parameters** to make our functions take in **arguments**. Functions could have a **return**
value.
- Takes in data, Manipulate it, Return something

**Positional and Keyword** arguments
- Positional comes first because they're **necessary** to maintain *order* in which the arguments are passed
- Keyword are at the **end** because *order does not matter*

```python
# Setting positional arguments first then keyword 
def arg_function(a,b,c=5,d=10):
    return 'something'  # Returning a value for an object

catch_something = arg_function(1,2)   # 1 is a and 2 is b => note: we don't need to add in c/d because they're keywords 
print(catch_something)  # using the returned value from the object
```

---

## Starting Data Collection

**Mutable vs Immutable** just means **dynamic vs static**. Mutable means we could *change* the structure.

Mutable DS (allowed to be modified):
- List: `mutable_list = [1,2,3,4]`

Immutable DS (cannot be modified):
- Strings: `"Hello"` 
- Tuples: `(1,2,3,4)`
- Range: `range(0,5)` Range Object must be looped (0-5) **excluding 5**

`len(ds)` could be used to find **how many elements** in that data structure.
`Indexing[int]` allows us to **retrieve** an element based on the *index* (Could use *-1* for reverse) 

---

## Slicing 

All DS could be sliced following: *Start*:*Stop*(Excluding):*Skip(Inclusive)*. Understand **slicing** does not **alter**
the original DS.

```python
l=[x for x in range(1,8)]
print(l[0::2]) # Output: 1,3,5,8 (Including the first element for a double skip)

# Step Backwards but NOT with a forward range 
print(l[8:1:-1]) # Will work but...
print(l[0:8:-1])    # Won't work
``` 

---

## Python Sequence Functions

Here are some functions we could use with *Data Structures*

**Arithmatic**
- `sum(l)`, `max(l)` and `min(l)`

**Conditionals**
- `any(l)` All `False` then returns *false*
- `all(l)` All must be `True` to return *true*

**Sorting**
- `sorted(l)`, `list(reversed(l))`, `l.sort()`

**Paring**
- `enumerate(l)` iterable object with pair **(index,element)**
- `zip(list1,list2)` pair of **tuple** from two list (key,value)

**Split & Joins**
- `l.split(' ')` split that string based on "spaces" (you could change the key) and returns a **list**
- `" ".join(l)` joins all elements into a **string**

**List Manipulation/Methods** 
- `l.append(new_element)`   Adds *new_element* to list 
- `l.extend([new,arry])`    Combines old arry with new arry
- `l.count('element')`     Counts amount of element in that list 
- `del l[index]`     Removes Specific Element from list based on index 
- `l.insert(index,'new_element')`    Inserts *new_element* at that index 
- `l.index('element', xrange, yrange)`   Finds index of element (could be based on range) 
- `l.pop(index)`    removes and returns that element 

**Nested** lists exist so we just keep chaining index:
`l[0][10]   # within the first array, we access the 10th element`

**Unpacking & Swapping** 
```python
list1 = list(range(0,3))    # 0, 1, 2
a1,a2,a3 = list1    # Unpacking 
a2,a3 = a3, a2  # Swapping
```

**Functions** with a **list/mutable** **parameter**
- If your parameter has a list/mutable, it will **continually** affect that list regardless of the times it's used



