# Steganography Project
## Purpose
To encode and read messages through the modification of LSDs in an image (must be formatted in BMP).

## Operation
It provides three functions: encryption, decryption, and cleaning.
Each is denoted by the operator input: -e, -d, and -c. 

1. Encryption - takes in an image file name to modify, an image output file name to store the altered photo, and an input ASCII text file to be encoded and embedded in the image file. 
  + Format  
    -e <original image name> <modified image name> [input ASCII text file name]
Or formatted as: -e <original image name> [input ASCII text file name]
In this second format, the inputted image is directly modified and no other files are created

3. Decryption - takes in a modified image and extracts the ASCII text from it, outputting
the plain text to a specified file or if one isn't provided, to the terminal

  + Format  
    -d <modified image name> [output ASCII text file name]

4. Cleaning - takes in a modified file and scrambles all the LSD so no previously stored
messages can be extracted from it
  + Format  
    for cleaning: -c <modified image name>

