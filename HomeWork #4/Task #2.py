# пробовал сделать без try, через isinstance и перечислением хэшируемых типов,
# но потом подумал, что могут быть и пользовательские классы хэшируемые и применил try
# не нашел проверку объекта на хэшируемость :(

# def kwargs_to_dict(**kwargs):
#     return {value if isinstance(value, int | str | float | bool | tuple) else str(value): key for key, value in
#             kwargs.items()}


def kwargs_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result


print(kwargs_to_dict(name='Кирилл', age=38,
                     has_work=True, commands=['ККН', 'LM', 'DP'],
                     growth=1.87, nicks={'STONE', '17th'}))
