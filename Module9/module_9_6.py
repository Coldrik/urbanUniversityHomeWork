import itertools


def all_variants(text):

    temp_list = []
    for lst_1 in range(1, len(text) + 1):
        temp_list.append(list(itertools.combinations(text, lst_1)))

    for lst_2 in temp_list:
        for lst_3 in lst_2:
            if ''.join(lst_3) in text:
                yield ''.join(lst_3)

a = all_variants("abc")
for i in a:
    print(i)