# Relative file path: relative to current working directory
# C:\Users\hp\Desktop\GitHub\100-Days-of-Code-Python\Day-24B\main2_angela.py
with open("../../../my_file.txt") as file:
    contents = file.read()
    print(contents)


# Absolute file path : relative to the root of file path
# C:\Users\hp\Desktop
with open("/Users/hp/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)
