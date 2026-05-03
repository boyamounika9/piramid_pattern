
# try:
#     a=int(input())
#     print(type(a))
# except ValueError:
#     print("invalid input")
# finally:
#     print("sucess")


# try:
#     a=int(input())
#     b=int(input())
#     print(a/b)
# except ZeroDivisionError:
#     print("cant divisible by zero")
# except ValueError:
#     print("invalid input")
# except Exception as e:
#     print("unexpected error" ,e)

    
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
    
#     result = a / b

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# except ValueError:
#     print("Invalid input")

# else:
#     print("Result:", result)



try:
    age = int(input("Enter age: "))
    
    if age < 18:
        raise ValueError("Age must be 18 or above")

except ValueError as e:
    print("Error:", e)

else:
    print("Valid age")