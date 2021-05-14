import abc


class AbstractBasicAccount:

    @abc.abstractmethod
    def withdraw(self, value: int, user: str):
        raise NotImplementedError

    @abc.abstractmethod
    def transfer(self, value: int, user_sender: str, user_receiver: str):
        raise NotImplementedError

    @abc.abstractmethod
    def check_balance(self, user: str):
        raise NotImplementedError
