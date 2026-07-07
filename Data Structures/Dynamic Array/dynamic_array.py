import ctypes


class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.n = 0
        self.A = self._make_array(self.capacity)

    def _make_array(self, capacity):
        """Instantiates array with capacity"""
        return (ctypes.py_object * capacity)()

    def get_item(self, index):
        """returns the item at index from array"""
        if index < 0 or index >= self.n:
            return IndexError("index out of bounds!")

        return self.A[index]

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

    def print_items(self):
        """Print the current list of elements"""
        print("----------Current Items in the list------------")
        for i in range(self.n):
            print(self.A[i])


da = DynamicArray()

da.append(1)
da.append(3)
da.append(2)
da.append(6)

da.print_items()


da.append(4)

da.print_items()

print(f"current length of array is {da.n} and current capacity is {da.capacity}")

print(da.get_item(4))
print(da.get_item(5))
