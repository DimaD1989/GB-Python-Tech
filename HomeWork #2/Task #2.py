from fractions import Fraction


class SelfFraction:
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int) and not isinstance(denominator, int):
            raise ValueError
        elif denominator == 0:
            raise ZeroDivisionError
        else:
            self.num = numerator
            self.den = denominator
            num_devs = SelfFraction.general_div(self.num)
            den_devs = SelfFraction.general_div(self.den)
            main_dev = max(set(num_devs).intersection(den_devs))
            if main_dev:
                self.num //= main_dev
                self.den //= main_dev

    def __add__(self, other):
        main_den = self.den * other.den
        main_num = self.num * other.den + other.num * self.den
        return SelfFraction(main_num, main_den)

    def __mul__(self, other):
        main_num = self.num * other.num
        main_den = self.den * other.den
        return SelfFraction(main_num, main_den)

    @staticmethod
    def general_div(number: int):
        devs = [1]
        for i in range(1, number):
            if number % i == 0:
                devs.append(i)
        return devs

    def __str__(self):
        return f'{self.num}/{self.den}'


first_fract = input('Введите первую дробь формата "a/b": ').split('/')
second_fract = input('Введите вторую дробь формата "a/b": ').split('/')

self_fract_1 = SelfFraction(int(first_fract[0]), int(first_fract[1]))
self_fract_2 = SelfFraction(int(second_fract[0]), int(second_fract[1]))
original_fract_1 = SelfFraction(int(first_fract[0]), int(first_fract[1]))
original_fract_2 = SelfFraction(int(second_fract[0]), int(second_fract[1]))

print(f'Свой класс {self_fract_1 + self_fract_2}')
print(f'Проверка {original_fract_1 + original_fract_2}')

print(f'Свой класс {self_fract_1 * self_fract_2}')
print(f'Проверка {original_fract_1 * original_fract_2}')
