#1)Write a Python program to list only directories, files and all directories, files in a specified path.
"""
import os
path = r"C:\Users\Iskander\Desktop\git_tutorial\work\hello"
directories = [direc for direc in os.listdir(path) if os.path.isdir(os.path.join(path, direc))]
print("Directories in path:")
print(directories)
files = [fil for fil in os.listdir(path) if os.path.isfile(os.path.join(path, fil))]
print("Files in path:")
print(files)
all = os.listdir(path)
print("All contents in path:")
print(all)
"""

#2)Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
"""
import os
path = input("Enter path to checking: ")
if os.path.exists(path):
    print(f"{path} exist")
    if os.access(path, os.R_OK):
      print(f"{path} readable")
    else:
        print(f"{path} not readable")
    if os.access(path, os.W_OK):
        print(f"{path} writable")
    else:
       print(f"{path} not writable")
    if os.access(path, os.X_OK):
        print(f"{path} executable")
    else:
        print(f"{path} not executable")
else:
   print(f"{path} doesn't exist!")
"""

 
#  3)Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os
path = input("Enter path: ")
if os.path.exists(path):
    print("Path to directory:", os.path.dirname(path))
    print("Directory name:", os.path.basename(path))
else:
    print("Path does not exist!")

# 4)Write a Python program to count the number of lines in a text file.
f = "test.txt"
cnt = 0
with open(f, "r") as file:
    for line in file:
         cnt += 1
print("Number of lines in", f, ":", cnt)

# 5)Write a Python program to write a list to a file.
l = input().split()
with open("testing.txt", "w") as file:
    for i in l:
        file.write(i + "\n")

#6)Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string
l = list(string.ascii_uppercase)
for letter in l:
    n = letter + ".txt"
    with open(n, "w") as file:
      file.write("This is file " + n)

#7)Write a Python program to copy the contents of a file to another file
path1 = input("Enter first path: ")
path2 = input("Enter second path: ")
with open(path1, "r") as s, open(path2, "w") as d:
    contents = s.read()
    d.write(contents)
print("File copied successfully!")

#8)Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or notimport os
path = input("Enter path: ")
if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted successfully")
    else:
       print("You don't have permission to delete the file")
else:
    print("File does not exist!")