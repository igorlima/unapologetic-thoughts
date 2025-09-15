print(
'''
If you've ever worked with large datasets, nested loops, or complex iterations in Python, you've probably faced situations where regular loops feel too slow or clunky. This is where itertools comes to the rescue! Python's itertools module provides powerful functions that make working with iterators faster, memory-efficient, and more readable.

Python's itertools module is a hidden powerhouse for efficient iteration. If you haven’t explored itertools yet, now is the perfect time!
''')


print('`itertools.count()` – Infinite Counting Made Easy')
'''
If you need an infinite counter that keeps going? `count()` generates numbers indefinitely
'''
from itertools import count
for num in count(start=1, step=2):
  print(num, end=" ")
  if num > 10:
    break  # Stop the infinite loop
# output - 1 3 5 7 9 11


print('\n\n`itertools.cycle()` – Loop Over an Iterable Infinitely')
'''
When you need to cycle through a list indefinitely.
'''
from itertools import cycle
colors = ["red", "green", "blue"]
color_cycle = cycle(colors)
for _ in range(6):  # Print 6 colors
  print(next(color_cycle))


print('\n`itertools.repeat()` – Repeat a Value Efficiently')
'''
Instead of creating a list of repeated values, use `repeat()` to save memory.
'''
from itertools import repeat
for msg in repeat("Hello", 3):
  print(msg)


print('\n`itertools.accumulate()` – Running Totals in One Line')
'''
If you need a cumulative sum (or product) of numbers? `accumulate()` do it for you easily.
'''
from itertools import accumulate
nums = [1, 2, 3, 4, 5]
print(list(accumulate(nums)))  
# output - [1, 3, 6, 10, 15]
'''
OR you can also use `accumulate()` for multiplication:
'''
import operator
print(list(accumulate(nums, operator.mul)))  
# output - [1, 2, 6, 24, 120]


print('\n`itertools.chain()` – Flatten Nested Iterables')
'''
If you want to combine multiple lists into a single list ? `chain()` do it for you easily.
'''
from itertools import chain
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list(chain(list1, list2))
print(combined)  
# output - [1, 2, 3, 4, 5, 6]


print('\n`itertools.product()` – Cartesian Product (All Pair Combinations)')
'''
If you want to generate all possible pairs between two lists. `product()` function generate it for you.
'''
from itertools import product
sizes = ["S", "M", "L"]
colors = ["Red", "Blue"]
print(list(product(sizes, colors)))
# output
# [('S', 'Red'), ('S', 'Blue'), ('M', 'Red'), ('M', 'Blue'), ('L', 'Red'), ('L', 'Blue')]


print('\n`itertools.permutations()` – All Possible Orderings')
'''
If you need all orderings of elements in a sequence? permutations() function is perfect for this.
'''
from itertools import permutations
items = ["A", "B", "C"]
print(list(permutations(items)))
# output
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]


print('\n`itertools.combinations()` – Unique Groups of Items')
'''
If you want generate all unique combinations of elements without repetition.
'''
from itertools import combinations
letters = ["A", "B", "C"]
print(list(combinations(letters, 2)))  # Pick 2 elements at a time
# output
# [('A', 'B'), ('A', 'C'), ('B', 'C')]


print('\n`itertools.groupby()` – Group Elements Together')
'''
If you want to group consecutive similar items together.
'''
from itertools import groupby
data = "aaabbccccdaa"
grouped = [(key, list(group)) for key, group in groupby(data)]
print(grouped)
# output
# [('a', ['a', 'a', 'a']), ('b', ['b', 'b']), ('c', ['c', 'c', 'c', 'c']), ('d', ['d']), ('a', ['a', 'a'])]


print('\n`itertools.tee()` – Duplicate an Iterator')
'''
If you need to iterate over the same generator twice without consuming it? you can do it easily with `tee()`
'''
from itertools import tee
data = iter([1, 2, 3, 4])
iter1, iter2 = tee(data, 2)
print(list(iter1))  # output - [1, 2, 3, 4]
print(list(iter2))  # output - [1, 2, 3, 4]

'''
REFERENCE:
  - 10 Python itertools Tricks I Wish I Knew Sooner: https://medium.com/pythoneers/10-python-itertools-tricks-i-wish-i-knew-sooner-d97111f2959a
'''
