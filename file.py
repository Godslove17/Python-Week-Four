 import os

# How to read files

file = open("mydata.txt", "r")
print(file.read())

# how to write a new file

newFile =open("filename.txt", "w")
print(newFile.write("the more you practice coding the better you become"))

# how to remove files

os.remove("filename.txt")

#  Error handling and exception
try:
    file = open("filename.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Oops! This files does not exist")
finally:
    print("It's was nice seeing you")