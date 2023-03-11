from fractions import Fraction


class SelfFraction:
    def __init__(self, fraction: str):
        fraction = fraction.split('/')
        if len(fraction) != 2 and isinstance(fraction[0], int) and isinstance(fraction[1], int):
            raise ValueError
        elif fraction[1] == 0:
            raise ZeroDivisionError
        else:
            self.num = int(fraction[0])
            self.den = int(fraction[1])
            num_devs = SelfFraction.general_div(self.num)
            den_devs = SelfFraction.general_div(self.den)
            main_dev = max(set(num_devs).intersection(den_devs))
            if main_dev:
                self.num //= main_dev
                self.den //= main_dev

    def __add__(self, other):
        main_den = self.den * other.den
        main_num = self.num * other.den + other.num * self.den
        return SelfFraction(f'{main_num}/{main_den}')

    def __mul__(self, other):
        main_num = self.num * other.num
        main_den = self.den * other.den
        return SelfFraction(f'{main_num}/{main_den}')

    @staticmethod
    def general_div(number: int):
        devs = [1]
        for i in range(1, number):
            if number % i == 0:
                devs.append(i)
        return devs

    def __str__(self):
        return f'{self.num}/{self.den}'


fract_1 = SelfFraction('7/8')
fract_2 = SelfFraction('1/2')

print(f'Свой класс {fract_1 + fract_2}')
print(f'Проверка {Fraction(3 / 4 + 1 / 2)}')

print(f'Свой класс {fract_1 * fract_2}')
print(f'Проверка {Fraction(3 / 4 * 1 / 2)}')
