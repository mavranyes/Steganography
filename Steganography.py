#Created by Micah Vranyes
#Date 3/28/2023
#Version 1.1

import sys
import random
import time

def extractBinary(fileName, msgLen):
    global offset
    with open(fileName, "rb") as imageFile:
        imageFile.read(offset)
        binaryMsg = ""
        for x in range(msgLen):
            byte = bytearray(imageFile.read(1))
            if (byte[0] % 2 == 1):
                binaryMsg += "1"
            else:
                binaryMsg += "0"
    offset += msgLen
    return binaryMsg

def replaceBinary(imageFileName, binaryMsg):
    with open(imageFileName, "r+b") as imageFile:
            imageFile.seek(offset)
            bytePlace = offset
            for diget in binaryMsg:  
                byte = bytearray(imageFile.read(1))
                #Modify LSD
                if (byte[0] % 2 == 1):
                    byte[0] -= 1
                if (diget == "1"):
                    byte[0] += 1
                #Replaces byte in image
                imageFile.seek(bytePlace)
                imageFile.write(byte)
                bytePlace += 1
                imageFile.seek(bytePlace)

try:
    global offset 
    offset = 100
    secret = ""
    msgLenInd = 16
    maxMsgCharSize = pow(2, msgLenInd) / 8
    operator = sys.argv[1]
    if operator == "-e":#If encrypt
        #Recieve user message input
        if len(sys.argv) >= 5:
            textFileName = sys.argv[4]
            testFile = open(textFileName, "r")
            asciiMsg = testFile.read()
        else:
            asciiMsg = input("Enter the secret message: ")
        #Convert ascii to binary
        binMsg = "".join(format(ord(x), "08b") for x in asciiMsg)
        #Find message length
        if len(binMsg) > maxMsgCharSize:
            print("Error: Message length cannot exceed %d characters!" % (int(maxMsgCharSize)))
            sys.exit()
        binMsg = format(len(binMsg), '0{}b'.format(msgLenInd)) + binMsg
        #Open image and replace each LSD
        imageFileName = sys.argv[2]
        replaceBinary(imageFileName, binMsg)
        
    elif operator == "-d":#If decrpyt
        #Find message length
        imageFileName = sys.argv[2]
        msgLenStr = extractBinary(imageFileName, msgLenInd)   
        decMsgLen = int(format(int(msgLenStr, 2), "d"))
        #Open image and grab each LSB
        binaryMsg = extractBinary(imageFileName, decMsgLen)
        #Binary string to ASCII
        for x in range(int(decMsgLen/8)):
            upBnd = int((x * 8) + 8)
            lwBnd = int(x * 8)
            secret = secret + format(int(format(int(binaryMsg[lwBnd:upBnd], 2), "d")), "c")
        #Insert into file or stdout
        if len(sys.argv) >= 4:
            textFileName = sys.argv[3]
            with open(textFileName, "w") as textFile:
                textFile.write(secret)
        else:
            print(secret)

    elif operator == "-c":#If cleaning
        imageFileName = sys.argv[2]
        #Create random binary string
        random.seed(round(time.time() * 1000))
        asciiMsg = "".join(chr(round(random.random()*100)) for x in range(int(maxMsgCharSize)))
        binMsg = "".join(format(ord(x), "08b") for x in asciiMsg)
        #Open image and replace each LSD
        replaceBinary(imageFileName, binMsg)
        
    print("Process Finished")
except OSError:
    print("Error: ASCII input file does not exist")
except IndexError:
    print("Error: Too few arguments")
    print("Format for encryption: -e <original file image name> <modified image name> [input ASCII text file name]")
    print("Format for decryption: -d <modified image name> [output ASCII text file name]")
    print("Format for cleaning: -d <modified image name>")