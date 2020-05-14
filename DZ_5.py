vyruchka = int(input("выручка:"))
izdergka = int(input("издержка:"))
i = 0
i = vyruchka - izdergka
while vyruchka > izdergka:
    print("фирма в прибыли")
    pers = int(input("количество сотрудников:"))
    prib = i / pers
    print("Прибыль фирмы:", f'{prib:.2f}')
    break
if vyruchka < izdergka:
    print("Фирма в убытке")
    pers = int(input("количество сотрудников:"))
    prib = i / pers
    print("Прибыль фирмы:", f'{prib:.2f}')
