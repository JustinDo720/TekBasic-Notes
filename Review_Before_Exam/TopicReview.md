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

### Jan 29 (T3)
- [String Interpolation](#string-interpolation-)
- [String Functions](#string-functions-)
- [Hashmap](#hashmap-)
  - Shallow vs Deep Copy
- [Overloading Arg](#overloading-function-arguments)
- [Anonymous Functions](#anonymous-function-)
- [Decorators](#decorators-)
- [Generators](#generators-)
- [Dictionary Comp](#dictionary-comp-)
- [Data Structures](#data-structures-)
- [Beginning OOP](#starting-python-oop-)

### Jan 30 (T4)
- [5 Pillars of OOP](#oop-concepts-)
- [MRO](#python-mro-method-resolution-order)
- [RegEX](#python-regular-expression-)
- [Starting Exceptions](#starting-exception-)

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

---

## String Interpolation 

Formatting strings with **F Strings**, using `.format(var1, var2)` or `% (var1,var2)`

```python
name, age = "justin", 20

print(f'I am an F string: {name} {age}')
print("I am formatting: {0} {1}".format(name, age))
print('I am interpolation s for string d for digits: %s %d' % (name, age))

```

---

## String Functions 

When in doubt use `dir(var)` to check all the built-in functions for it but here's a view:
1) `.title()` makes sure we have Upper case on all words
2) `.upper()` for full upper case 
3) `.lower()` for full lower case

---

## Hashmap 

A python **dictionary** with **keys:values** pair 

We could also combine dictionaries using the `d1 | d2` But it will be a **shallow copy**

### Shallow vs Deep Copy 

Shallow keeps the **reference** which means changing the new will change the **original**. Deep copy is **independent**
meaning it will not change/affect the **original**
- This only affects with **nested lists**

```python
d = {
    'name': 'Justin',
    'age': 20
}

d1 = {
    'fav_food': 'Chicken',
}

d2 = d | d1     # Shallow Copy meaning changing d2 will change d/d1

d2.popitem() # will give me fav_food because they're merged 
```

```python
# Shallow vs Deep 
import copy 

l1 = [[3,2],1,2,3,4]
l2 = copy.copy(l1)  # copies reference as well 
# Changing the original will affect the shallow copy too 
l1[0][0] = 2
# Changing the new will affect the original too 
l2[0][1] = 3

l2 = copy.deepcopy(l1)
# Changing the original will NOT affect the deep copy 
l1[0][0] = 2
# Changing the new will NOT affect the original. Only affecting the second copy
l2[0][1] = 3
```

---

## Overloading Function Arguments

**overloading** just means we could take in an endless amount of **positional** and **keyword** arguments using `*args*`
and `**kwargs`

```python

# *args is a tuple (we could access via index) 
def myFunc(*args):
    print(args[0])
    
# **kwargs is a dictionary 
def myFunc(**kwargs):
    print(kwargs.keys(), kwargs.values(), kwargs.get('key'))

```

--- 

## Anonymous Function 

**Lambda** is a quick function builder: `lambda arg1, arg2: return a+b` 

We could **reuse** a lambda function by setting a variable to it otherwise 

```python

people = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "San Francisco"},
    {"name": "Charlie", "age": 22, "city": "Chicago"},
    {"name": "David", "age": 35, "city": "Los Angeles"},
    {"name": "Eve", "age": 28, "city": "Miami"}
]

# Using lambda to sort 
# Sort in place if return new arry use sorted(people, key=lambda obj: obj['age'])
people.sort(key=lambda obj: obj['age'])

# The original way
def age(obj):
    return obj['age']

sorted(people, key=age)

# We could pass in some parameter on spot
print((lambda x,y : x+y)(2,3))  # 5
a = lambda x,y : x+y
print(a(2,3))
```

## Decorators 

The idea of *lambda* also introduces **callback functions** where we pass a function to be called **later**. 
- We create a **decorator function** that takes a **function** as an argument
- Inside the decorator function, we create a **wrapper** that uses the function in the argument 
- Return that wrapper 

```python

def myDecorator(func1):
    myVar = 'Decorator Scope'
    def wrapper():
        # To access myVar 
        nonlocal myVar
        myVar = 'Now Wrapper Scope'
        print(myVar)
        print('Doing something before running our function')
        func1()
        print('Doing something after our function')
    return wrapper()

@myDecorator
def simpFunc():
    print('My function')

simpFunc()  # "Doing something before..." "my Func.." "Doing something after..."
```

---

## Generators 

Similar to `range()`, but you can only use each value once, and they are produced one at a time, 
instead of all being stored in memory at once. **Lazy Loading**

```python
myObj = ['a','b','c']
def myGen():
    # Instead of storing all myObj into memory it yields (returns) a value one at a time 
    for obj in myObj:
        yield obj
    
# Don't forget to set my generator to a variable (ensures to get the next value) 
gen = myGen() 

for obj in gen:
    print(obj)

```

---

## Dictionary Comp 

We've seen **list comp** we could also make a dictionary comp. Also know that **nested dictionaries** exist

```python

myHashmap = {
    'age': 10,
    'num': 5,
}

# Let's double it 
secondHash = {key:value**2 for key,value in myHashmap.items()}

```

---

## Data Structures 

**NamedTuple** --> name a couple tuples with **fields**

```python
from collections import namedtuple

Game = namedtuple('Game', ['name', 'price', 'type'])

batman = Game('Batman V3', 12.50, 'action')
print(batman.name, batman.price, batman.type)

```

**Double Ended Queue** --> Queues we could work from the **left** side helping us achieve that **FIFO**

```python
from collections import deque

my_queue = deque([1,2,3])
# FIFO (1 is in so 1 should leave first) 
my_queue.popleft()
# We could also append left 
my_queue.appendleft(5)

```

**ChainMap** --> Combining Big Dictionaries 

```python
from collections import ChainMap

d1 = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3'
}

d2 = {
    'k4': 'v4',
    'k5': 'v5',
    'k6': 'v6'
}

cm = ChainMap(d1,d2)    # Use this to look at both dictionaries at once
cm['k6']
```

**Counter** --> Counting a certain occurrence 

```python
from collections import Counter

l = ['a', 'b', 'c', 'd' 'a', 'a', 'b', 'c']
cnt = Counter(l)
print(cnt)  # All occurrences of each element 
print(cnt['b'])     # Specific element 

# Most common?
print(cnt.most_common(2))

```

**Ordered Dictionary** --> Keeps track of order in which keys are pushed into dict 

```python
from collections import OrderedDict

od = OrderedDict([('k1','v1'), ('k2', 'v2')])
# od acts like a normal dictionary
```

**Default Dictionary** --> Doesn't raise KeyError by placing a **default** value 

```python
from collections import defaultdict

dd = defaultdict(int)
print(dd['A'])  # Default to 0 because int is our default

```

--- 

## Starting Python OOP 

Class are **blueprints** and objects are **instances** of that class meaning they carry *attributes* from that class.

```python
class Animal:
    # Constructor 
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed
        
    # Method 
    def make_sound(self):
        print(f'{self.name} is speaking...')
    
    # String representation 
    def __str__(self):
        return self.name + ' ' + self.breed
    
    # repr() for dev
    def __repr__(self):
        return f'Animal: {self.name} {self.breed}'

    # cleaning up references in memory 
    def __delete__(self, instance):
        self.name = None 
        self.breed = None 

# Creating the object
logan = Animal('Logan', 'Husky')
```

---

## OOP Concepts 

**Abstraction** is where we focus on the **essential** features by using the `ABC` class and `abstractmethod` to map
out what's necessary for our class.

```python
# Abstract class 
from abc import ABC, abstractmethod

class HouseABC(ABC):
    # No __init__ constructor because we're not using this to build an object 
    # Let's build getter and setter functions for House Name 
    @abstractmethod
    def setHouseName(self, house_name):
        pass
    
    @abstractmethod
    def getHouseName(self):
        pass 


class House(HouseABC):
    # Constructor because we're using this class to build objects 
    def __init__(self, name, size):
        # Private Variables is Encapsulation, we'll take a look later 
        self.__name = name
        self.size = size

    # This house CANNOT be completed without overriding our abstract methods 
    def getHouseName(self):
        return self.__name 

    def setHouseName(self, house_name):
        self.__name = house_name
        return self.getHouseName()
```

**Encapsulation** 

From the previous example we use `self.__name` which creates name as a **private variable** and could be accessed like:
`obj._ModelName__name` 

```python
def __init__(self, name, size):
        # Private Variables is Encapsulation, we'll take a look later 
        self.__name = name
        self.size = size
```

This helps use **protect** our data from being accessed directly. We also created **getter and setter functions**.

```python
# This house CANNOT be completed without overriding our abstract methods 
def getHouseName(self):
    return self.__name 

def setHouseName(self, house_name):
    self.__name = house_name
    return self.getHouseName()
```

**Inheritance** 

Our subclass (child class) gets properties/attributes from *Parent* including methods. This helps with **reusability**.
We use `super().__init__()` to initialize the parent class 

```python
class Animal:
    def __init__(self, name, breed):
        self.__name = name 
        self.breed = breed

    def make_sound(self):
        return self.__name + ' is making noise'

class Dog(Animal):
    def __init__(self, name, breed, age):
        # Initialize parent class
        super().__init__(name, breed)
        # Our child Property 
        self.age = age

muffin = Dog('Muff', 'German Shep', 3)
muffin.make_sound() # We have access to this method because Dog inherited by Animal
```

**Polymorphism**

The idea that objects could behave **differently** but have the **same** methods. We could also customize their function
based on what **class they belong to*. We could check with `isinstance(obj, Class)`

```python
class Animal:
    def __init__(self, name, breed):
        self.__name = name 
        self.breed = breed

    def make_sound(self):
        return self.__name + ' is making noise'
    
class Cat(Animal):
    def __init__(self, name, breed, age):
        # Initialize parent class
        super().__init__(name, breed)
        # Our child Property 
        self.age = age

Bean = Cat('Bean', 'tux', 2)

# Using muffin from last example 
both_animals = [muffin, Bean]
for animal in both_animals:
    # The idea is that, these are two different objects but we could loop through them to run the same function
    animal.make_sound()
```

---

## Python MRO (Method Resolution Order)

We don't go into-depth but `super()` is the key and `mro()` to see the inheritance order. But It mainly reads 
*Current* -> *Left* -> *Right* -> *Parent*

---

## Python Regular Expression 

We use **patterns** with **search functions**. Let's look at the search functions before patterns:
**Must import re** for regular expression
1) `re.match(pattern, str)` --> Match the beginning ONLY 
2) `re.search(pattern, str)` --> First occurrence ONLY 
3) `re.findall(pattern, str)` --> Lists of ALL occurrences (mostly used)

Constructing a pattern always start with a **raw string**: `r'pattern_here'`
- `[ ]` Look for certain characters within **range** 
  - `[a-zA-Z0-9]` Searches for any letter a-z lower and upper and any digits 0-9
- `+` is for **many** characters (group) while `.` is for **single**
  - `[a-zA-Z0-9]+` Mainly for **one or more** of these values 
- `{n}` for a **number** of these values 
  - `[a-zA-Z0-9]{6}` Mainly for **6** of these values 
- `|` for **or**
- `^` **Beginning**
- `$` **End**
- `\.` Escape character so like here we're **escaping** period 

```python
import re 

pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+'
result = re.findall(pattern, 'hello6 world1 hello554 admin@gmail.com JavaScript 12 ')
print(result)
```

---

## Starting Exception 

We use `try except else finally` block to catch errors in our code to **continue its runtime**

```python
def divide(a,b):
    return a//b

# Starting your try block
try:
    my_division = divide(1,0)
except ZeroDivisionError as e:
    # We know we cannot divide our 0 so we'll end up here
    print(e)
    

# Successful run 
try:
    my_division = divide(1,1)
except Exception as e:
    # We won't hit this block because 1/1 is fine
    print(e)
else:
    # Since our try block is successful 
    print(my_division)
finally:
    # Regardless of outcome 
    print('Printing regardless of outcome (Always hit this block of code)')
```

---
