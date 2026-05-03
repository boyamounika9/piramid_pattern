# n=int(input())
# for i in range (1,n+1):
#     for j in range (1,i+1):
#         print("*",end=" ")
#     print()

# n=int(input())
# for i in range (1,n+1):
#     for j in range (i,n+1):
#         print(j,end=" ")
#     for j in range (1,i):
#         print(j,end=" ")
#     print()

# n=int(input())
# for i in range (1,n+1):
#     for j in range (i,n):
#         print(" ",end=" ")
#     for j in range (1,i+1):
#         print("*",end=" ")
#     print()

# n=5
# for i in range (n,0,-1):
#     for j in range (1,i+1):
#         print("*",end=" ")
#     print(" ")

n=5
for i in range (n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range (1,i+1):
        print("*",end=" ")
    print()


n=5
for i in range (1,n+1):
    for j in range (1,i+1):
        print(j,end=" ")
    print()