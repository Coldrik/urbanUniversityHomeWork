def length_of_element(symb):
    if isinstance(symb, int):
        return symb
    elif isinstance(symb, str):
        return len(symb)


def unpack_func(s):
    if not s:
        return s

    if isinstance(s[0], list):
        return unpack_func(s[0]) + unpack_func(s[1:])

    if isinstance(s[0], tuple):
        return unpack_func(list(s[0])) + unpack_func(list(s[1:]))

    if isinstance(s[0], dict):
        return unpack_func(list(s[0].items())) + unpack_func(s[1:])

    if isinstance(s[0], set):
        return unpack_func(list(s[0])) + unpack_func(list(s[1:]))

    return s[:1] + unpack_func(s[1:])


def calculate_structure_sum(data):
    work_list = unpack_func(data)
    print(work_list)
    lenght_data = 0
    for i in work_list:
        lenght_data += length_of_element(i)
    return lenght_data


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
