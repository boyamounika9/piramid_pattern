class ATM :
    def __init__(self, balance,pin):
        self.__balance = balance
        self.__pin=pin
    def Deposit(self,pin):
        if len(pin)==6:
            print("depositing amount")
    def withdraw(self,pin):
        if len(pin)==6:
            print("withdrawing amount")
    def checkbalence(self,pin):
        if len(pin)==6:
            print("balence amount is:",self.__balance)

a=ATM(3000)
a.Deposit("123456")
a.withdraw("123456")
a.checkbalence("123456")