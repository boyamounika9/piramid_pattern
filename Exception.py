
# try:
#     a=int(input())
#     print(type(a))
# except ValueError:
#     print("invalid input")
# finally:
#     print("sucess")


try:
    a=int(input())
    b=int(input())
    print(a/b)
except ZeroDivisionError:
    print("cant divisible by zero")
except ValueError:
    print("invalid input")
except Exception as e:
    print("unexpected error" ,e)

    