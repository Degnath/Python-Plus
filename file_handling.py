# Files

# Files are named locations on disk to store related information. They are used to permanently store data in a non-volatile memory (e.g. hard disk).

# Since Random Access Memory (RAM) is volatile (which loses its data when the computer is turned off), we use files for future use of the data by permanently storing them.

# When we want to read from or write to a file, we need to open it first. When we are done, it needs to be closed so that the resources that are tied with the file are freed.

# Hence, in Python, a file operation takes place in the following order:

#     Open a file
#     Read or write (perform operation)
#     Close the file

# Opening Files

# Python has a built-in open() function to open a file. This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.

# #### open(filename, mode)

# Default mode is read

# We can specify the mode while opening a file. In mode, we specify whether we want to read r, write w or append a to the file. We can also specify if we want to open the file in text mode or binary mode.

# The default is reading in text mode. In this mode, we get strings when reading from the file.

# On the other hand, binary mode returns bytes and this is the mode to be used when dealing with non-text files like images or executable files.

# Opening text file

file = open("C:\\Users\\ramana\\Documents\\PythonCourse\\FileHandling.txt")
print(file)
print(file.read())
# Closing a file
file.close()

# closing a file with 'with' statement
with open("C:\\Users\\ramana\\Documents\\PythonCourse\\FileHandling.txt", 'r') as file:
    print(file.read())
print("I have completed file reading")

print(file.read())


# File modes for operation.

#     “ r “, for reading.
#     “ w “, for writing.
#     “ a “, for appending.
#     “ r+ “, for both reading and writing

# Reading Files

# To read a file in Python, we must open the file in reading r mode.

# There are various methods available for this purpose. We can use the read(size) method to read in the size number of data. If the size parameter is not specified, it reads and returns up to the end of the file.

# we can use the readline() method to read individual lines of a file.

# The readlines() method returns a list of remaining lines of the entire file

# reading entire text from file
file = open("C:\\Users\\ramana\\Documents\\PythonCourse\\FileHandling.txt", 'r')
print(file.read())
file.close()

# reading all lines
file = open("C:\\Users\\ramana\\Documents\\PythonCourse\\FileHandling.txt", 'r')
print(file.readlines())
file.close()

# reading one line at a time
file = open("C:\\Users\\ramana\\Documents\\PythonCourse\\FileHandling.txt", 'r')
print(file.readline())
print(file.readline())

file.close()

# Reading first n characters of data
file = open("C:\\Users\\ramana\\Documents\\PythonCourse\\FileHandling.txt", 'r')
file.read(10)

print(file.read(4))
print(file.read(20))
file.close()

# We can change our current file cursor (position) using the seek() method. Similarly, the tell() method returns our current position (in number of bytes).
file = open("C:\\Users\\ramana\\Documents\\PythonCourse\\FileHandling.txt", 'r')
print(file.read(10))
print(file.read(20))
print(file.tell())

print(file.read(10))
print(file.read(20))
print(file.tell())

file = open("C:\\Users\\ramana\\Documents\\PythonCourse\\FileHandling.txt", 'r')
print(file.read(10))
print(file.read(20))
print(file.tell())
file.seek(0)
print(file.tell())
print(file.read(20))
file.close()

# Writing to Files

# In order to write into a file in Python, we need to open it in write w, append a or exclusive creation x mode.

# We need to be careful with the w mode, as it will overwrite into the file if it already exists. Due to this, all the previous data are erased.

# Writing a string or sequence of bytes (for binary files) is done using the write() method. This method returns the number of characters written to the file.

# Opening a file and write some text in that
with open("test.txt", 'w') as fileWrite:
    fileWrite.write("my first file\n")
    fileWrite.write("This file\n\n")
    fileWrite.write("contains three lines\n")

# opening same file and writing some more data in 'w' mode
with open("test.txt", 'w') as fileWrite:
    fileWrite.write("1. my first file\n")
    fileWrite.write("2. This file\n\n")
    fileWrite.write("3. contains three lines\n")

# reading not possible with 'W' mode
with open("test.txt", 'w') as fileWrite:
    fileWrite.write("1. my first file\n")
    fileWrite.write("2. This file\n\n")
    print(fileWrite.read())  # we get error stating not readable
    fileWrite.write("3. contains three lines\n")


# ['This file will open for both writing and readingThis file will open for both writing and readingThis file will open for both writing and reading']
with open("testWR.txt", 'r+') as fileWrite:
    fileWrite.write("This file will open for both writing and reading")
    print(fileWrite.readlines())
