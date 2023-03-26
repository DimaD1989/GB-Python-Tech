# def divine_path(abs_path: str) -> tuple:
#     result = []
#     for divine in ['.', ['\\', '/']]:
#         for i in range(len(abs_path) - 1, -1, -1):
#             if abs_path[i] in divine:
#                 result.insert(0, abs_path[i+1:])
#                 abs_path = abs_path[:i]
#                 break
#     result.insert(0, abs_path)
#     return tuple(result)

def divine_path(full_path: str):
    def divine(abs_path: str, div: str) -> tuple:
        abs_path = abs_path.split(div)
        file_name, extension = abs_path[-1].split('.')
        path = div.join(abs_path[:-1])
        return path, file_name, extension

    return divine(full_path, '/') if '/' in full_path else divine(full_path, '\\')


print(divine_path('C:/WorkShop/Python/GB-Python-Tech/HomeWork #5/Task #1.py'))
