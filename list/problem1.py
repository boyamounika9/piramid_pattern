#Create a list of 10 numbers and print all elements.
lis=[1,2,3,4,5,6,7,8,9,10]
print(lis)

#Find the sum of all elements in a list.
print(sum(lis))

# Find the maximum and minimum element in a list.
print(min(lis))
print(max(lis))

# Count how many even and odd numbers are in a list.
even=0
odd=0
for i in lis:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even:",even)
print("odd:",odd)

# Reverse a list without using built-in functions.
list=lis[:]
for i in range(0,len(lis)):
    list[-(i+1)]=lis[i]
print(list)

