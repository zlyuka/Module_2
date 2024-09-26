
for int_ in range(3, 21):
    open_str = ''
    for i in range(1, int_):
        for j in range(i + 1, int_):
            if int_ % (i + j) == 0:
                open_str += str(i) + str(j)

    print(f'Вывод для значения {int_} - {open_str}')

