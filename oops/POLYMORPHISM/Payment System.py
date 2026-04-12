class CreditCardPayment:
    def pay(self,amount):
        print(amount, "CreditCardPayment")
class UPIPayment:
    def pay(self,amount):
        print(amount, "UPIPayment")
class CashPayment:
    def pay(self,amount):
        print(amount, "CashPayment") 
def show(obj) :
    obj.pay(300)  
c=CreditCardPayment()
u=UPIPayment()
p=CashPayment()

show(c)
show(u)
show(p)