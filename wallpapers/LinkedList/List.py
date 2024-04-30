class Node:
    def __init__(self, valor):
        self.val = valor
        self.next = None
        self.prev = None


class ListNode:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert(self, pos: int, val):
        if pos < 0:
            raise IndexError("pos must be greater than or equal to 0")

        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.count += 1
        elif pos < self.count:
            puntero = self.head

            for cont in range(pos - 1):
                puntero = puntero.next

            new_node.next = puntero.next
            puntero.next = new_node
            self.count += 1
        else:
            self.append(val)

    def append(self, valor):
        new_node = Node(valor)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.count += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.count += 1

    def delete(self, pos: int):
        if pos < 0:
            raise IndexError("Position cannot be negative.")

        if pos >= self.count:
            return

        if pos == 0:
            primer = self.head
            self.head = self.head.next
            primer.next = None
            self.count -= 1

        elif self.head is not None:
            puntero = self.head

            for _ in range(pos - 1):
                puntero = puntero.next

            temp = puntero.next
            puntero.next = temp.next
            temp.next = None
            self.count -= 1

    def pop(self):
        """
        Remove and return the value of the last node in the list.
        """
        if self.head is None:
            raise IndexError("Cannot pop from an empty list")
        elif self.head.next is None:
            temp = self.head
            self.head = None
            self.tail = None
            self.count -= 1
            return temp.val
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            temp = current.next
            current.next = None
            self.tail = current
            self.count -= 1
            return temp.val

    def get(self, pos: int):
        if pos < 0:
            raise IndexError("Position must be a non-negative integer.")
        if self.head is None or pos >= self.count:
            return None
        else:
            puntero = self.head

            for _ in range(pos):
                puntero = puntero.next

            return puntero.val
