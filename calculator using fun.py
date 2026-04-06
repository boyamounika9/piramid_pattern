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
a=int(input())
c=input()
b=int(input())
def fun(a,c,b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mul():
        print(a*b)
    def div():
        print(a/b)
    def mod():
        print(a%b)
    def non():
        print("not a valid symbol")
        if c=="+":
            add()
        elif c=="-":
            sub()
        elif c=="*":
            mul()
        elif c=="/":
            div()
        elif c=="%":
            mod()
        else:
            non()

fun(a,c,b)