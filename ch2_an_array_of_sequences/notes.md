Texts, lists and tables are together called trains, the FOR command works generically on them. 
Guido created Python, but before Python he was a contributor for the ABC language, that was a
ten year long research project to come up with a language for beginners. Comming from C++
background I can appreciate the fact that all types are not iterables. Generic operations on 
different types of sequences were present in the ABC language.
## Built-In Sequences
The standard library offers a rich selection of collections implemented in C. 
Based on memory usage they can be thought of as two types:
* Container: list, tuple etc
* flat: array, strings, bytes. These are more compact.
Based on mutability:
* Mutable: list
* Immutable: tuple
One thing to note is that, MutableSequence inherits all methods from immutable sequences and 
implement some more on top of it. Also, built-in concrete sequences (like list, tuple) do not
actually subclass the Sequence and MutableSequence classes, but they are virtual subclasses with
those (MutableSequencea and Sequence) ABCs. 
# Lists
## List Comprehensions and Generator Expressions
A for loop can have multiple intents: count, aggregate, and so on. But listcomps are explicity meant
to buidl a list. 
```
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors    # note how we did not need the \
                         for size in sizes]
>>> [('black', 'S'), ('black', 'M')...]         # note the order
```
*Genexps*
```
>>>
>>> # genexps
>>> symbols = '!@#$!@#$'
>>> (ord(symbol) for symbol in symbols)
<generator object <genexpr> at 0x100dc2500>
>>> gen =  ord(symbol) for symbol in symbols)
>>> next(gen)
33
```
These are similar to the listcomps just use '()' instead of '[]'. While passing genexps as single arg-
ument we can just omit the '()', but in case there are several arguments, '()' are required.
Advantage:
```
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in (f'{c} {s}' for c in colors
                          for s in sizes):
  print(tshirt)
```
If there are 1000 colors and 1000 sizes, listcomps create a list of a million items, making it a memory
intensive task. However, genexps yield just one item at a time, using the Cartesian product therefore 
saving lot of memory. Items are produced one-by-one.

## Tuples: the other fundamental sequence in Python
- not just immutable lists
- records with no field names as well. 
**Tuple hold records: each item inthe tuple holds the data for one field, and the position of the item gives
its meaning**
```
>>> city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)  # position decides the field, not need
                                                                      # to create a whole new class
```
