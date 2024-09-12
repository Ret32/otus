enter_task = input("Введите номер задачи по теме 'Базовые типы данных' от 1 до 5: ")

match enter_task:
    case "1":
        print("Задача 1: Пользователь вводит пятизначное число. Программа должна зеркально отразить центральные три цифры.\n"
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
        print("Задача 2: Отпуск. Пользователь вводит сколько дней осталось до ближайшего отпуска.\n"
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
    case _:
        print("Невернный ввод. Выход из программы")