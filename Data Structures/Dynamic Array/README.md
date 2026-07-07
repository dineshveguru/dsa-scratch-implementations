# Dynamic Array - Implementation

Arrays in python are by default dynamic -- we can add elements, remove elements or do any operations without ever specifying the size that array should hold unlike implementations in C/C++ (Vectors are of different concept though).

So, just for learning purposes, we use [ctypes](https://docs.python.org/3/library/ctypes.html) to mimic this behaviour. `ctypes` is a python library that let's us call functions in C source code or dynamic libraries.

For designing our dynamic array, we use ctypes `py_object` [More Here](https://docs.python.org/3/library/ctypes.html#ctypes.py_object) to store memory address of each element in py_object variable. Also, we want our array to be dynamic, so it should store multiple types of data (str, int etc.) in a single array. As `py_object` stores only pointers in those variables, we can represent any data type using them.

Our implementation covers these functionalities

- create dynamic list
- append element to the list
- get item from the list
- print the entire list

## Code 

### Initialize

Here, we create `_make_array()` function to create mulitiple contiguous `py_objects` which can be accessed using index just like in python arrays.

```python
def _make_array(self, capacity):
        """Instantiates array with capacity"""
        return (ctypes.py_object * capacity)()
```

> Notice: Why we used () here?

Let's assume you're creating a list in python using list type. For example:

```python
a = list([1, 2, 3]) 
```

When you run `ctypes.py_object * capacity`, Python doesn't allocate the array yet. Instead, it uses operator overloading to dynamically construct a new ctypes array class (a type) of that specific size.

Adding the () at the end instantiates that newly created class, allocating the actual block of contiguous memory.

This method will return the contiguous block, but we initialize them in the `__init__` method

```python
def __init__(self):
    self.capacity = 1
    self.n = 0
    self.A = self._make_array(self.capacity)    # <--
```

### Append

We use this method to append elements to the array.

```python
def append(self, val):
    """appends item to the array"""
    if self.n == self.capacity:
        temp = self._make_array(self.capacity + 1)
        for i in range(self.n):
            temp[i] = self.A[i]

        self.A = temp
        self.capacity += 1
    self.A[self.n] = val
    self.n += 1
```

The method checks if `self.n == self.capacity` just way of checking if the array is full. The `n` tracks the current no of elements and `capacity` tracks the total capacity of the current array.

If the array is full, we make a new array by increasing the capacity by 1 and then copying every element from the current array to new array and adding the new element to the last. Now, we update capacity & n respectively. 

### Get Item from Array

It's pretty straight-forward. We check if the given index is out of bounds to gracefully show an exception and if it's within the array, then we return the element at that index.

```python
def get_item(self, index):
    """returns the item at index from array"""
    if index < 0 or index >= self.n:
        return IndexError("index out of bounds!")

    return self.A[index]
```
