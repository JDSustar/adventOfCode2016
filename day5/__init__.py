import hashlib

doorId = "ojvtpuvg"
doorIdNumber = 0

password = ["", "", "", "", "" ,"", "", ""]
positionsFilled = []

while len(positionsFilled) < 8:
    doorHash = hashlib.md5(doorId + str(doorIdNumber)).hexdigest()
    if doorHash[0:5] == "00000":
        if doorHash[5].isdigit() and int(doorHash[5]) < 8 and doorHash[5] not in positionsFilled:
            password[int(doorHash[5])] = doorHash[6]
            positionsFilled.append(doorHash[5])
            print password

    doorIdNumber += 1

print password
