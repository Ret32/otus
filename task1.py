while True:

    enter_num = input ("Введите 5-ти значное число: ")

    if len(enter_num) == 5:
        print("Введено число с верной длинной. Ваше число: ", enter_num)
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