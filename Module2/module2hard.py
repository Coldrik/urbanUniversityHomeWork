def pair_searcher(a):  # функция подбирает пару чисел кратных числу а
    list_of_number = list(range(1, a + 1))
    list_of_pair = []
    for i in range(a):
        if int(a / 2) < i:
            break
        for j in range(i + 1, a):
            if a % (list_of_number[i] + list_of_number[j]) == 0:
                list_of_pair.extend([list_of_number[i], list_of_number[j]])
    print(*list_of_pair)


# передайте в функцию pair_searcher число от 3 до 20 необходимое к расшифровке
pair_searcher(20)
