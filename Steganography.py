#Created by Micah Vranyes
#Date 3/28/2023
#Version 1.0

import sys

def extractBinary(fileName, msgLen, offset):
    with open(fileName, "rb") as imageFile:
        imageFile.read(OFF_SET + offset)
        binaryMsg = ""
        for x in range(msgLen):
            byte = bytearray(imageFile.read(1))
            if (byte[0] % 2 == 1):
                binaryMsg += "1"
            else:
                binaryMsg += "0"
    return binaryMsg

try:
    secret = ""
    OFF_SET = 100
    operator = sys.argv[1]
    if operator == "-e":#If encrypt
        #Recieve user message input
        if len(sys.argv) >= 5:
            textFileName = sys.argv[4]
            testFile = open(textFileName, "r")
            secret = testFile.read()
        else:
            secret = input("Enter the secret message: ")
        #Convert ascii to binary
        binaryForm = "".join(format(ord(x), "08b") for x in secret)
        msgLength = len(binaryForm)
        print(msgLength)
        binMsgLength = format(msgLength, '0{}b'.format(8))
        print(binMsgLength)
        binaryForm = binMsgLength + binaryForm
        #Open image and replace each LSB
        imageFileName = sys.argv[2]
        imageFile = open(imageFileName, "r+b")
        imageFile.seek(OFF_SET)
        bytePlace = OFF_SET
        for diget in binaryForm:  
            byte = bytearray(imageFile.read(1))
            #Modify LSD
            byte[0] -= 1
            if (byte[0] % 2 == 1):
                byte[0] -= 1
            if (diget == "1"):
                byte[0] += 1
            #Replaces byte in image
            imageFile.seek(bytePlace)
            imageFile.write(byte)
            bytePlace += 1
            imageFile.seek(bytePlace)

    elif operator == "-d":#If decrpyt
        # #Find message length
        imageFileName = sys.argv[2]
        msgLenStr = extractBinary(imageFileName, 8, 0)        
        msglen = int(format(int(msgLenStr, 2), "d"))
        print(msglen)
        #Open image and grab each LSB
        binaryMsg = extractBinary(imageFileName, msglen*8, 8)
        #Binary string to ASCII
        for x in range(int(msglen/8)):
            upBnd = int((x * 8) + 8)
            lwBnd = int(x * 8)
            secret = secret + format(int(format(int(binaryMsg[lwBnd:upBnd], 2), "d")), "c")
        #Insert into file
        textFileName = sys.argv[3]
        with open(textFileName, "w") as textFile:
            textFile.write(secret)

    print("Process Finished")
except OSError:
    print("Error: ASCII input file does not exist")
except IndexError:
    print("Error: Too few arguments")
    print("Format for encryption: -e <original file image name> <modified image name> [input ASCII text file name]")
    print("Format for decryption: -d <modified image name> [output ASCII text file name]")
