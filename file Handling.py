# file=open('f.txt',"r")
# count = len(file.readlines())
# print("Number of lines:", count)
# file.close
try:
    with open("f.txt", "r") as file:
        data = file.read()
        words = data.split()
        count = len(words)

    print("Number of words:", count)

except FileNotFoundError:
    print("File not found")