file=open('f.txt',"r")
count = len(file.readlines())
print("Number of lines:", count)
file.close

#Write a program to count number of words in a file.
try:
    with open("f.txt", "r") as file:
        data = file.read()
        words = data.split()
        count = len(words)

    print("Number of words:", count)

except FileNotFoundError:
    print("File not found")