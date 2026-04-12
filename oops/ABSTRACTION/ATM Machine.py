from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def check_balance(self):
        pass