carrying_capacity = int(input('Введите грузоподъемность рюкзака: '))

list_of_equipment = {'Провиант': 3,
                     'Вода': 2,
                     'Палатка': 6,
                     'Мяч': 0.5,
                     'Шампура': 1,
                     'Одежда': 5,
                     'Снасти': 2.5,
                     'Алкоголь': 7,
                     'Топор': 3.5,
                     'Телевизор': 25}


def sort_list(some_set: set):
    global global_list
    if len(some_set) == 1:
        return some_set
    else:
        for item in some_set:
            new_set = some_set.copy()
            new_set.remove(item)
            global_list.add(tuple(sort_list(new_set)))
    return some_set


list_of_equipment = dict(sorted(list_of_equipment.items(), key=lambda x: x[1]))
global_list = {tuple(list_of_equipment)}
sort_list(set(list_of_equipment))

print(f'В рюкзак грузоподъемностью {carrying_capacity}кг может влезть:')

for stack in global_list:
    summ_stack = 0
    for item in stack:
        summ_stack += list_of_equipment.get(item)
        if summ_stack > carrying_capacity:
            break
    else:
        print(*stack, 'весом', summ_stack, 'кг')
