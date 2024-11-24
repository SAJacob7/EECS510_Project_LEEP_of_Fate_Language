#stack.py
from node import Node
class Stack:
    def __init__(self):
        """Creates the member variable top."""
        self.elems = []

    def push(self, entry):
        """Pushes the newest entry to the top of the Stack."""
        return self.elems.append(entry)
    def pop(self):
        """Returns and takes off the top of the Stack if the Stack is not empty."""
        return self.elems.pop()
    def peek(self):
        """Returns the top of the Stack if its not empty."""
        if self.is_empty() != True:
            return self.elems[-1]
        else:
            return None
            #raise RuntimeError # This happens if there is nothing in the Stack.
    def is_empty(self):
        """Returns True if the Stack is empty and False otherwise."""
        if len(self.elems) == 0:
            return True
        else:
            return False
    def copy_stack(self):
        new_stack = Stack()
        new_stack.elems = self.elems.copy()
        return new_stack