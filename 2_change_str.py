'''2. Имеется строка вида: AABABBAABBBAB. Необходимо написать функцию которая заменит буквы A на Bб
а B, на A. В результате применения функции к исходной строке, функция должна вернуть строку: BBABAABBAAABA'''

s = 'AABABBAABBBAB'

def change_str():
    # A_B = s.replace('A', 'B')
    # B_A = s.replace('B', 'A')
    # print(A_B + B_A)

    for l in s:
        if l == 'A':
            l ='B'
        else:
            l = 'A'
        print(l)




change_str()