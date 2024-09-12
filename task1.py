enter_task = input("Введите номер задачи по теме 'Базовые типы данных' от 1 до 5: ")

match enter_task:

    case "1":
        print("\nЗадача 1: Пользователь вводит пятизначное число. Программа должна зеркально отразить центральные три цифры.\n"
                "Первая и последняя остаются на местах.\n")
        while True:

            enter_num = input("Введите 5-ти значное число: ")

            if len(enter_num) == 5:
                revers_num = enter_num[0:1] + enter_num[-2:0:-1] + enter_num[4:5]
                enter_num = int(enter_num)
                revers_num = int(revers_num)
                print(f"Введено число с верной длинной. Ваше число: {enter_num}, реверсивное число в середине: {revers_num}")
                break
            else:
                user_enter = input("Введено короткое число, попробуйте еще раз. Продолжить (да/нет)? ")
                if user_enter.lower() == 'нет':
                    print("Выход из программы")
                    break
                elif user_enter.lower() == 'да':
                    continue
                else:
                    print("Введено неизвестное значение. Выход из программы")
                    break

    case "2":
        print("\nЗадача 2: Отпуск. Пользователь вводит сколько дней осталось до ближайшего отпуска.\n"
              "Программа должна вывести количество выходных дней до отпуска, если учесть, что выходные\n"
              "это суббота и воскресенье, сегодня понедельник и праздники мы не учитываем.\n")
        from datetime import date, timedelta

        SAT = 5; SUN = 6

        enter_day = int(input("Введите количество дней до отпуска: "))
        date_now = date.today()
        start_date = date_now - timedelta(days=date_now.weekday())
        end_date = start_date + timedelta(enter_day)

        days = [date.fromordinal(d) for d in
                range(start_date.toordinal(),
                      end_date.toordinal())]
        weekend_days = [d for d in days if d.weekday() in (SAT, SUN)]

        num_weekends = len(weekend_days)

        print(f"Дата понедельника на текущей неделе - {start_date.strftime("%d.%m.%Y")}\n"
              f"Дата начала отпуска - {end_date.strftime("%d.%m.%Y")}\n"
              f"Количество выходных до отпуска: {num_weekends}")

    case "3":
        print("\nЗадача 3: Пользователь вводит длину и ширину плитки шоколада, а также размер куска, который хочет отломить.\n"
              "Программа должна вычислить - можно ли совершить подобный разлом или нет, \n"
              "если учесть, что ломать можно только по прямой\n")
        print("Введите размер шоколадки (Д*Ш): ")
        size_chocolate = []
        for i in range(2):
            x = int(input())
            size_chocolate.append(x)
        print(f"Введенный размер шоколадки: {size_chocolate}")

        flag = False
        enter_size = int(input("Введите размер кусочка шоколада: "))
        for size in size_chocolate:
            piece_choc = enter_size / size
            #    print(piece_choc)
            if piece_choc % 1 == 0:
                #    print(f"{piece_choc} - Целое")
                if piece_choc <= size_chocolate[1]:
                    # print("Можно разделить шоколадку на указанную ширину")
                    flag = True
            #     else:
            #         print("Не хватает ширины для выполнения деления")
            # elif piece_choc % 1 != 0 and flag == False:
            #     print(f"{piece_choc} - Дробное")
        if flag:
            print("Можно разделить шоколадку")
        else:
            print("Нельзя разделить шоколадку")

    case "4":
        print("\nЗадача 4: Пользователь вводит целое положительное число, программа должна вернуть строку в виде римского числа\n")
        while True:
            enter_dec = int(input("Введите положительное десятичное число: "))
            if enter_dec < 0:
                print("Введено отрицательное число, повторите ввод")
                continue
            Decimals = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
            Romans = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
            roman_total = []
            while enter_dec != 0:
                for val in range(len(Decimals)):
                    if enter_dec >= Decimals[val]:
                        dec = Decimals[val]
                        roman = Romans[val]
                diff = enter_dec - dec
                roman_total.append(roman)
                enter_dec = diff
            total = ''.join(roman_total)
            print(f"Римское число: {total}")
            break
    case "5":
        print("\nЗадача 5: Пользователь вводит данные, проверить - являются ли они положительным вещественным числом.\n"
              "Не использовать встроенные функции для проверки, только методы данных и конструкцию IF. \n"
              "(Дополнительное задание, по желанию - проверка на отрицательные вещественные числа)\n")
        enter_num = input("Введите число: ")
        if enter_num[-1] == ".":
            print(f"{enter_num} - число не вещественное")
        else:
            float(enter_num)
            if "." not in enter_num and "-" not in enter_num:
                print(f"{enter_num} - число вещественное целое положительное")
            if "." not in enter_num and "-" in enter_num:
                print(f"{enter_num} - число вещественное целое отрицательное")
            if "." in enter_num and "-" not in enter_num:
                print(f"{enter_num} - число вещественное дробное положительное")
            if "." in enter_num and "-" in enter_num:
                print(f"{enter_num} - число вещественное дробное отрицательное")
    case _:
        print("Невернный ввод. Выход из программы")