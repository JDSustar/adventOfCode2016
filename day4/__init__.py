import roomDecoder

with open('input.txt', 'r') as file:
    rooms = []

    for line in file:
        rooms.append(roomDecoder.room(line))

for r in rooms:
    if r.isReal():
        print r.getRoomName(), r.sectorId