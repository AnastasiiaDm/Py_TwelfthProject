'''2. Имеется строка вида: AABABBAABBBAB. Необходимо написать функцию которая заменит буквы A на Bб
а B, на A. В результате применения функции к исходной строке, функция должна вернуть строку: BBABAABBAAABA'''

s = 'AABABBAABBBAB'


def change_str():
    r = []
    # ?????????????как это впихнуть в list comprehension? почему результат none??????
    # print([(r.append('B') if k == 'A' else r.append('A')) for k in s])

    for k in s:
        if k == 'A':
            r.append('B')
        else:
            r.append('A')

    print(''.join((str(elem) for elem in r)))


change_str()
