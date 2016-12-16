class Keypad():
    def __init__(self, start):
        if start is not None:
            self.current = start
        else:
            self.current = "5"

    def executeInstructions(self, instructions):
        for i in instructions:
            self.update(i)

    def update(self, instruction):
        if self.current == "1":
            if instruction == "D":
                self.current = "3"
        elif self.current == "2":
            if instruction == "D":
                self.current = "6"
            elif instruction == "R":
                self.current = "3"
        elif self.current == "3":
            if instruction == "D":
                self.current = "7"
            elif instruction == "U":
                self.current = "1"
            elif instruction == "L":
                self.current = "2"
            elif instruction == "R":
                self.current = "4"
        elif self.current == "4":
            if instruction == "D":
                self.current = "8"
            elif instruction == "U":
                self.current = "8"
            elif instruction == "L":
                self.current = "3"
            elif instruction == "R":
                self.current = "4"
        elif self.current == "5":
            if instruction == "D":
                self.current = "5"
            elif instruction == "U":
                self.current = "5"
            elif instruction == "L":
                self.current = "5"
            elif instruction == "R":
                self.current = "6"
        elif self.current == "6":
            if instruction == "D":
                self.current = "A"
            elif instruction == "U":
                self.current = "2"
            elif instruction == "L":
                self.current = "5"
            elif instruction == "R":
                self.current = "7"
        elif self.current == "7":
            if instruction == "D":
                self.current = "B"
            elif instruction == "U":
                self.current = "3"
            elif instruction == "L":
                self.current = "6"
            elif instruction == "R":
                self.current = "8"
        elif self.current == "8":
            if instruction == "D":
                self.current = "C"
            elif instruction == "U":
                self.current = "4"
            elif instruction == "L":
                self.current = "7"
            elif instruction == "R":
                self.current = "9"
        elif self.current == "9":
            if instruction == "D":
                self.current = "9"
            elif instruction == "U":
                self.current = "9"
            elif instruction == "L":
                self.current = "8"
            elif instruction == "R":
                self.current = "9"
        elif self.current == "A":
            if instruction == "D":
                self.current = "A"
            elif instruction == "U":
                self.current = "6"
            elif instruction == "L":
                self.current = "A"
            elif instruction == "R":
                self.current = "B"
        elif self.current == "B":
            if instruction == "D":
                self.current = "D"
            elif instruction == "U":
                self.current = "7"
            elif instruction == "L":
                self.current = "A"
            elif instruction == "R":
                self.current = "C"
        elif self.current == "C":
            if instruction == "D":
                self.current = "C"
            elif instruction == "U":
                self.current = "8"
            elif instruction == "L":
                self.current = "B"
            elif instruction == "R":
                self.current = "C"
        elif self.current == "D":
            if instruction == "D":
                self.current = "D"
            elif instruction == "U":
                self.current = "B"
            elif instruction == "L":
                self.current = "D"
            elif instruction == "R":
                self.current = "D"
