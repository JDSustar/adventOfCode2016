class Player:
    def __init__(self):
        self.direction = "N"
        self.x = 0
        self.y = 0
        self.locations = []

    def turn(self, turnDirection):
        if self.direction == "N":
            self.direction = "W" if turnDirection == "L" else "E"
        elif self.direction == "E":
            self.direction = "N" if turnDirection == "L" else "S"
        elif self.direction == "S":
            self.direction = "E" if turnDirection == "L" else "W"
        elif self.direction == "W":
            self.direction = "S" if turnDirection == "L" else "N"

    def walk(self, distance):
        if not isinstance(distance, int):
            distance = int(distance)

        if self.direction == "N":
            for x in range(1, distance + 1):
                self.y += 1
                if (self.x, self.y) in self.locations:
                    print (self.x, self.y), self.getBlocksAway()
                self.locations.append((self.x, self.y))
        elif self.direction == "E":
            for x in range(1, distance + 1):
                self.x += 1
                if (self.x, self.y) in self.locations:
                    print (self.x, self.y), self.getBlocksAway()
                self.locations.append((self.x, self.y))
        elif self.direction == "S":
            for x in range(1, distance + 1):
                self.y -= 1
                if (self.x, self.y) in self.locations:
                    print (self.x, self.y), self.getBlocksAway()
                self.locations.append((self.x, self.y))
        elif self.direction == "W":
            for x in range(1, distance + 1):
                self.x -= 1
                if (self.x, self.y) in self.locations:
                    print (self.x, self.y), self.getBlocksAway()
                self.locations.append((self.x, self.y))

    def executeInstruction(self, instruction):
        turnCommand = instruction[0]
        distance = instruction[1:]
        self.turn(turnCommand)
        self.walk(distance)


    def getBlocksAway(self):
        return abs(self.x) + abs(self.y)