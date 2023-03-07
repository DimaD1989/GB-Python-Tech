def input_number() -> int:
    while True:
        try:
            number = int(input('Введите число от 1 до 100_000: '))
            if 0 < number <= 100_000:
                return number
            else:
                print('Число должно быть от 1 до 100_000')
        except ValueError:
            print('Введите целое число от 1 до 100_000')


def is_simple(number: int) -> bool:
    if not number % 2:
        return False
    for dev in range(3, number // 2 + 1, 2):
        if not number % dev:
            return False
    return True


num = input_number()
print(f'Число {num} ', end='')
print('простое' if is_simple(num) else 'составное')
