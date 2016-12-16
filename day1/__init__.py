import io
import player

with open("input.txt", 'r') as file:
    wholeFile = file.read()

instructions = wholeFile.split(",")

instructions = [x.strip() for x in instructions]

p = player.Player()

for i in instructions:
    p.executeInstruction(i)

print p.getBlocksAway()