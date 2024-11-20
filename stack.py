#stack.py
from node import Node
class Stack:
    def __init__(self):
        """Creates the member variable top."""
        self._top = None

    def push(self, entry):
        """Pushes the newest entry to the top of the Stack."""
        cur_top = self._top
        self._top = Node(entry) # Makes the top the new entry.
        self._top.next = cur_top # Makes the old top the next of the new top. Links the two Nodes.
    def pop(self):
        """Returns and takes off the top of the Stack if the Stack is not empty."""
        if self._top != None: # Only runs if there is a top to pop.
            cur_top = self._top
            self._top = self._top.next # The new top is now the next of the old top, essentially disregarding the old top (popping it).
            return cur_top.entry
        else:
            raise RuntimeError # This happens if None is being popped off.
    def peek(self):
        """Returns the top of the Stack if its not empty."""
        if self._top != None: # Only runs if there is something in the Stack.
            return self._top.entry
        else:
            return None
            #raise RuntimeError # This happens if there is nothing in the Stack.
    def is_empty(self):
        """Returns True if the Stack is empty and False otherwise."""
        return self._top == None # Returns True when there is nothing in the Stack.