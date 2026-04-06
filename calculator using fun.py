def fun(a,b,c):
    if b=="+":
        print(a+c)
    elif b=="-":
        print(a-c)
    elif b=="*":
        print(a*c)
    elif b=="/":
        print(a/c)
    elif b=="%":
        print(a%c)
    else:
        print("invalid symbol")
a=int(input("enter first num"))
b=input("enter operator")
c=int(input("enter second num"))
fun(a,b,c)
