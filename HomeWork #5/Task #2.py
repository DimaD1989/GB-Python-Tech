from pprint import pprint

employee_list = [('Кирилл Панфилов', 100000, '2.5%'),
                 ('Андрей Беляев', 150000, '1.5%'),
                 ('Виталий Кузьмин', 1000, '5%')]

bonus = {name: salary + salary * (float(bonus[:-1]) / 100) for name, salary, bonus in employee_list}

pprint(bonus)
