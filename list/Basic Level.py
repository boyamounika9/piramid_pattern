# #Create a list of 10 numbers and print all elements.
# lis=[1,2,3,4,5,1,2,3,4,5]
# print(lis)

# #Find the sum of all elements in a list.
# print(sum(lis))

# # Find the maximum and minimum element in a list.
# print(min(lis))
# print(max(lis))

# # Count how many even and odd numbers are in a list.
# even=0
# odd=0
# for i in lis:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print("even:",even)
# print("odd:",odd)

# # Reverse a list without using built-in functions.
# list=lis[:]
# for i in range(0,len(lis)):
#     list[-(i+1)]=lis[i]
# print(list)

# # Remove duplicates from a list.
# result = []
# for i in lis:
#     if i not in result:
#         result.append(i)

# print(result)

# # Find the length of a list without using len().
# length=0
# for i in lis:
#     length+=1
# print(length)


# list=[1,2,3,4,5]

# print(list)

# nums = list(map(int, input("Enter list: ").split()))

# print("First element:", nums[0])
# print("Last element:", nums[-1])
list=[1,2,3,4,5]
even=0
odd=0
for i in list:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even:",even)
print("odd:",odd)