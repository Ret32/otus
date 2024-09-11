#Пользователь вводит пятизначное число. Программа должна зеркально отразить центральные три цифры. Первая и последняя остаются на местах.
while True:

    enter_num = input ("Введите 5-ти значное число: ")

    if len(enter_num) == 5:
        revers_num = enter_num[0:1] + enter_num[-2:0:-1] + enter_num[4:5]
        enter_num = int(enter_num)
        revers_num = int(revers_num)
        print(f"Введено число с верной длинной. Ваше число: {enter_num}, реверсивное число в середине: {revers_num}")
        break
    else:
        user_enter = input ("Введено короткое число, попробуйте еще раз. Продолжить (да/нет)? ")
        if user_enter.lower() == 'нет':
            print("Выход из программы")
            break
        elif user_enter.lower() == 'да':
            continue
        else:
            print("Введено неизвестное значение. Выход из программы")
            break