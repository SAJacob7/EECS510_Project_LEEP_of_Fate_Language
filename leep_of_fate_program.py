from stack import Stack
from node import Node

class Leep_of_Fate:
    def __init__(self, text_file):
        self.text_file = text_file
        self.all_states = None
        self.start_state = None
        self.accepting_state = None
        self.symbols = None
        self.transitions = None
        self.stack_symbols = None
    
    
    def parse_file(self):
        file = open(self.text_file, "r")
        transitions = []
        i = 0
        for line in file:
            line = line.strip()
            line = line.split(" ") # Strips and splits the lines by white space.
            if i==0:
                self.all_states = line
            elif i==1:
                self.symbols = line
            elif i==2:
                self.start_state = line
            elif i==3:
                self.accepting_state = line
            elif i==4:
                self.stack_symbols = line
            else:
                transitions.append(line)
            i = i+1
        self.transitions = transitions
        #print(self.all_states)
        #print(self.start_state)
        #print(self.accepting_state)
        #print(self.symbols)
        print(self.transitions)
        #print(self.stack_symbols)
    def accept_reject_string(self, w):
        pda_stack = Stack()
        pda_stack.push('Z')
        for i in range(0,len(w)):
            for transition in self.transitions:
                if transition[1] == w[i]:
                    if transition[5] in self.stack_symbols:
                        pda_stack.push(transition[5])
                        print("Pushing on: ", pda_stack.peek())
                    if transition[2] in self.stack_symbols:
                        if pda_stack.peek() == transition[2]:
                            print("Popping off: ", pda_stack.peek())
                            pda_stack.pop()
            
example = Leep_of_Fate("leep_of_fate_lang.txt")
example.parse_file()     
example.accept_reject_string("f*")