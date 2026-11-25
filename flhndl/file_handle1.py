import os
with open("rxt.txt", "r") as file:
    content = file.readline(3)
    print(type(content))
    print(content)
with open("rxt.txt", "w") as file2:
    content1=file2.write("Hello World")
    print(content1)

with open("rxt.txt", "a") as file3:
    content2=file3.write("Hello World")
    print(content2)  

os.remove("rxt.txt")