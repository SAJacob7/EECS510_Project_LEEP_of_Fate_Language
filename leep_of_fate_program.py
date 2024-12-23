from ascii_magic import AsciiArt

class Leep_of_Fate:
    def __init__(self, text_file):
        self.text_file = text_file
        self.all_states = None
        self.start_state = None
        self.accepting_state = None
        self.symbols = None
        self.transitions = None
        self.stack_symbols = None
        self.finished_trans = False
        self.visited_transition = []
    
    
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
       
    def accept_reject_string(self, w):
        if (len(w)==0):
            return (False, [])
        if (w[len(w)-1] != "*" or w.count("*") > 1):
            return (False, [])
        if(((w.count("f") + w.count("w")) % 2 == 0) and (w.count("f") + w.count("w")) != 0):
            return (False, [])
        if((w.count("a") + w.count("e")) % 2 == 1):
            return (False, [])

        count_of_ae = 0
        list_ae_counts = []
        for elem in w:
            if elem == "f" or elem == "w":
                if count_of_ae % 2 == 1:
                    return (False, [])
                else:
                    if count_of_ae != 0:
                        list_ae_counts.append(count_of_ae)
                    count_of_ae = 0
            elif elem == "a" or elem == "e":
                count_of_ae += 1
                
        if count_of_ae != 0:
            list_ae_counts.append(count_of_ae)

        count_fw = w.count("f") + w.count("w")
        temp_ae_count = 0
        temp_fw_count = 0
        start_ae_pop = 0
        start_fw_pop = 0
        current_state = "q0"
        accepting_transitions = []
        
        accepting_transitions.append(self.transitions[0])
        current_state = self.transitions[0][4] 

        for i in range(len(w)):
            if (len(w)==1 and w[0] == '*'):
                accepting_transitions.append(self.transitions[5])
            if (i != 0):
                if ((w[i - 1] == "e" or w[i - 1] == "a") and (w[i] == "f" or w[i] == "w")) or ((w[i - 1] == "f" or w[i - 1] == "w") and (w[i] == "a" or w[i] == "e")):
                    start_ae_pop = 0
                    accepting_transitions.append(self.transitions[12])
                    current_state = self.transitions[12][4]

            if w[i] == "a" or w[i] == "e":
                if (start_ae_pop == 0):
                    if (list_ae_counts[0] / 2 == temp_ae_count):
                        temp_ae_count = 0
                        start_ae_pop = 1 
                        accepting_transitions.append(self.transitions[5])
                        current_state = self.transitions[5][4]
                        list_ae_counts.pop(0)
                        
                    else:
                        for trans in self.transitions:
                            if (trans[1] == w[i] and trans[0] == "q1" and start_ae_pop == 0):
                                current_state = trans[4]
                                accepting_transitions.append(trans)
                                temp_ae_count += 1
                                break

                            elif (trans[1] == w[i] and trans[0] == "q2" and start_ae_pop == 1):
                                current_state = trans[4]
                                accepting_transitions.append(trans)
                                break

                if (start_ae_pop == 1):
                    for trans in self.transitions:
                        if (trans[1] == w[i] and trans[0] == "q2" and start_ae_pop == 1):
                            current_state = trans[4]
                            accepting_transitions.append(trans)
                            break

                
            elif w[i] == "f" or w[i] == "w":
                for trans in self.transitions:
                    if (trans[1] == w[i] and trans[0] == "q1" and start_fw_pop == 0):
                        current_state = trans[4]
                        accepting_transitions.append(trans)
                        temp_fw_count += 1

                    elif (trans[1] == w[i] and trans[0] == "q2" and start_fw_pop == 1):
                        if current_state != "q2":
                            accepting_transitions.append(self.transitions[5])
                        current_state = trans[4]
                        accepting_transitions.append(trans)

                if (count_fw // 2) + 1  == temp_fw_count:
                    temp_fw_count = 0
                    start_fw_pop = 1
                    accepting_transitions.append(self.transitions[6]) 
                    current_state = self.transitions[6][4]  
                    
        accepting_transitions.append(self.transitions[11])
        current_state = self.transitions[11][4] 
        return (True, accepting_transitions)
            
    
def main():
    example = Leep_of_Fate("leep_of_fate_lang.txt")
    example.parse_file()
    print("----------- LEEP of Fate: Rock Chalk Chronicles -----------\n")

    print("Cast your battle spell with these elements to defeat the Wildcat!")
    print("But beware as if the right spell is not casted the Jahawks will admit defeat to the Wild Beast of the West!\n")
    print("  Fire: f")
    print("  Water: w")
    print("  Air: a")
    print("  Earth: e")
    print("  *: Defeating Blow\n")
    user_input = input("Enter Your Battle Spell Jayhawk!: ")
    accept, transitions = (example.accept_reject_string(user_input.lower()))
    
    if accept:
        print("Accept\n")
        print("Transitions:")
        for trans in transitions:
            print(trans)

        print("\nRock Chalk Jayhwak, Go KU!\n")
        my_art = AsciiArt.from_image("jayhawk.png")
        my_art.to_terminal()

    else:
        print("Reject\n")
        my_art = AsciiArt.from_image("wildcat.jpg")
        my_art.to_terminal(columns=75)
    

main()