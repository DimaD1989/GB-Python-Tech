from card import BankCard
import text

class ATM:
    def __init__(self, index: int, bank: str, address: str, balance: float):
        self.index = index
        self.bank = bank
        self.address = address
        self._balance = balance
        self.card: BankCard = None

    def main_menu(self, line_1: str = '', line_2: str = '', line_3: str = '',
                  line_4: str = '', line_5: str = '', line_6: str = '',
                  line_7: str = '', line_8: str = '', line_9: str = ''):
        print('\n' * 20)
        print('-' * 33)
        print(f'|{line_1:^31}|')
        print(f'|{line_2:^31}|')
        print(f'|{line_3:^31}|')
        print(f'|{line_4:^31}|')
        print(f'|{line_5:^31}|')
        print(f'|{line_6:^31}|')
        print(f'|{line_7:^31}|')
        print(f'|{line_8:^31}|')
        print(f'|{line_9:^31}|')
        print('-' * 33)

    def insert(self, card: BankCard):
        pin = input(text.ENTER_PIN)
        if card.check_pin(pin):
            self.card = card
            return text.OPERATION_OK
        else:
            return text.WRONG_PIN

    def take_cash(self):
        if self.card:
            amount = float(input(text.CASH_AMOUNT))
            if amount < self._balance:
                if self.card.decrease(amount):
                    self._balance -= amount
                    return text.OPERATION_OK
            else:
                return text.NOT_ENOUGH_BALANCE
        else:
            return text.INSERT_CARD

    def check_balance(self):
        pass


    def replenish_balance(self):
        if self.card:
            amount = float(input(text.CASH_AMOUNT))
            if self.card.increase(amount):
                self._balance += amount
                return text.OPERATION_OK
        else:
            return text.INSERT_CARD

    def check_balance(self):
        return self.card.balance

    def __str__(self):
        return f'Банкомат: {self.bank} #{self.index}\nАдрес: {self.address}'
