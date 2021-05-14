
class BankAccount:

    def __init__(self, holder, balance, limit):
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    @property
    def holder(self):
        return self.__holder.title()

    @holder.setter
    def holder(self, holder):
        self.__holder = holder

    @property
    def balance(self):
        return self.__balance.title()

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    @property
    def limit(self):
        return self.__limit.title()

    @limit.setter
    def limit(self, limit):
        self.__limit = limit
