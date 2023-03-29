The purpsoe of this application is to encode a message by modify the LSD of an image (formated in BMP)
It provides three functions of use: encryption, decryption, and cleaning. 
Each is denoted by the opertor input: -e, -d, and -c. 

The first, encryption, takes in a image file name to modify, an image output file name to
store the altered photo, and an input ASCII text file to be encoded and embedded in the
image file. 
Format for encryption: -e <original image name> <modified image name> [input ASCII text file name]

The second, decryption, takes in a modified image and extracts the ASCII text from it, outputting
the plain text to a specified file or if one isn't provided, to the terminal
Format for decryption: -d <modified image name> [output ASCII text file name]

The third, cleaing, takes in a modified file and scrambles all the LSD so no previously stored
messages can be extracted from it
Format for cleaning: -c <modified image name>

