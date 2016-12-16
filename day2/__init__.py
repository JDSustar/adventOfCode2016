import keypad

with open("input.txt", "r") as file:
    code = []
    last = None
    for line in file:
        k = keypad.Keypad(last)
        k.executeInstructions(line)
        code.append(k.current)
        last = k.current

print code