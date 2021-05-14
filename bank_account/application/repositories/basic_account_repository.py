from bank_account.application.repositories.interfaces.abstract_basic_account import AbstractBasicAccount


class BasicAccountRepository(AbstractBasicAccount):

    def withdraw(self, value: int, user: str):
        pass

    def transfer(self, value: int, user_sender: str, user_receiver: str):
        pass

    def check_balance(self, user: str):
        pass

