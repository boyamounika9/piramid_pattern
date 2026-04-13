class ATM :
    def __init__(self, balance,pin):
        self.__balance = balance
        self.__pin=pin
    def Deposit(self):
        if self.__pin=="mounika@9":
            print("depositing amount")
        else:
            print("deny access")
    def withdraw(self):
        if self.__pin=="mounika@9":
            print("withdrawing amount")
        else:
            print("deny access")
    def checkbalence(self):
        if self.__pin=="mounika@9":
            print("balence amount is:",self.__balance)
        else:
            print("deny access")

a=ATM(3000,"mounika@9")
a.Deposit()
a.withdraw()
a.checkbalence()