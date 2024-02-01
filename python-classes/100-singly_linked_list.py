#!/usr/bin/python3
"""Document for module"""


class Node:
    """Document for class"""
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def __str__(self):
        current = self._head
        output = ""
        while current:
            output += f"{current}\n"
            current = current.next_node
        return output.strip()

    def sorted_insert(self, value):
        new_node = Node(value)
        if self._head is None or self._head.data >= value:
            new_node.next_node = self._head
            self._head = new_node
            return
        current = self._head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
