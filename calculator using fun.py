# def fun(a,b,c):
#     if b=="+":
#         print(a+c)
#     elif b=="-":
#         print(a-c)
#     elif b=="*":
#         print(a*c)
#     elif b=="/":
#         print(a/c)
#     elif b=="%":
#         print(a%c)
#     else:
#         print("invalid symbol")
# a=int(input("enter first num"))
# b=input("enter operator")
# c=int(input("enter second num"))
# fun(a,b,c)

def add(c):
    print(a+b)
def sub(c):
    print(a-b)
def mul(c):
    print(a*b)
def div(c):
    print(a/b)
def mod(c):
    print(a%b)
def non(c):
    print("not a valid symbol")
def fun(a,c,b):
    if c=="+":
     add(c)
    elif c=="-":
     sub(c)
    elif c=="*":
     mul(c)
    elif c=="/":
     div(c)
    elif c=="%":
     mod(c)
    else:
     non()
a=int(input())
c=input()
b=int(input())
fun(a,c,b)