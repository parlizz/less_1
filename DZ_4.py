x = int(input('Введите число:'))
imax = 0
i = x

while i:
    if i % 10 > imax:
        imax = i % 10
    i //= 10
print('Максимальная цифра числа', imax)

