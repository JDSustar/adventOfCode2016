from collections import Counter
from collections import OrderedDict
import re

class room():
    def __init__(self, s):
        self.s = s
        match = re.match("(.*)-(\d+)\[(.....)\]", s)
        self.encrypedRoomName = match.group(1).replace("-", "")
        self.encrypedRoomNameWithSpaces = match.group(1).replace("-", " ")
        self.sectorId = int(match.group(2))
        self.checksum = match.group(3)

    def isReal(self):
        roomDict = Counter(list(self.encrypedRoomName))
        roomDictOrdered = OrderedDict(sorted(roomDict.items(), key=lambda t: (-t[1], t[0])))
        topChars = roomDictOrdered.keys()[:5]
        for x in range(0, 5):
            if self.checksum[x] != topChars[x]:
                return False

        return True

    def getRoomName(self):
        roomName = ""
        for c in self.encrypedRoomNameWithSpaces:
            if c == " ":
                roomName += " "
            else:
                d = ord(c)
                newD = (d - 97 + self.sectorId) % 26 + 97
                newC = chr(newD)
                roomName += newC

        return roomName