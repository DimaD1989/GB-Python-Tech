triangle_sides = []
for i in ['a', 'b', 'c']:
    triangle_sides.append(int(input(f'Введите длину стороны {i}: ')))

for i in range(3):
    if triangle_sides[i] > triangle_sides[i - 1] + triangle_sides[(i + 1) % 3]:
        print('Такой треугольник не может существовать')
        break
else:
    if triangle_sides[0] == triangle_sides[1] == triangle_sides[2]:
        print('Этот треугольник равносторонний')
    elif triangle_sides[0] == triangle_sides[1] or \
            triangle_sides[1] == triangle_sides[2] or \
            triangle_sides[0] == triangle_sides[2]:
        print('Этот треугольник равнобедренный')
    else:
        print('Этот треугольник разносторонний')
