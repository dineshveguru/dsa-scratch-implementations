class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LL:
    def __init__(self, val):
        self.head = Node(val=val)
        self.ll = self.head
        self.n = 1

    def add_element(self, val):
        """Adds element to end"""
        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = Node(val=val)
        self.n += 1

    def print_list(self):
        cur = self.head
        while cur.next:
            print(f"{cur.val}->", end=" ")
            cur = cur.next
        print(cur.val)

    # add element at index i
    def add_element_i(self, val, i):
        if i >= self.n:
            return IndexError("Check the length first!!")

        cur = self.head
        j = 0


linked_list = LL(1)
linked_list.add_element(2)
linked_list.add_element(3)
linked_list.print_list()
