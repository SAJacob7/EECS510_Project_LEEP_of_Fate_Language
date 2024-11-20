#node.py

class Node:
    def __init__(self, entry):
        """Creates the member variables entry and next."""
        self.entry = entry
        self.next = None # Sets this to None (nothing after it), unless otherwise changed.
