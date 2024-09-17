enter_task = input("Введите номер задачи по теме 'Управляющие конструкции' от 1 до 5: ")

match enter_task:

    case "1":
        print("\nЗадача 1: Пользователь вводит целое число, программа складывает все цифры числа,\n "
              "с полученным числом - то же самое и так до тех пор, пока не получится однозначное число.\n")

        enter_num = int(input("Введите число: "))

        while enter_num > 9:
            result = sum(int(x) for x in str(enter_num))
            enter_num = result

        print(result)

    case "2":
        print("\nЗадача 2: Кинотеатр. Дан список списков, каждый вложенный список состоит из 1 и 0,\n"
              "Количество вложенных списков - количество рядов. Пользователь вводит сколько билетов ему требуется.\n"
              "Программа должна найти ряд, где можно приобрести нужно количество билетов (места должны быть рядом).\n"
              "Если таких рядов несколько, то ближайший к экрану (ближайшим считается нулевой ряд).\n"
              "Ели таких мест нет, то вывести False\n")

        count_line = int(input("Введите количество рядов: "))
        count_seats = int(input("Введите количество сидений в ряду: "))

        list_line = []
        sub_list_line = []
        chk_enter = True
        chk_free = True
        a = 0
        c = 0
        num_line = -1
        num_seats = -1

        for a in range(count_line):
            list_seats = []
            for b in range(count_seats):
                enter_sits = int(input(f'Введите бронирование сидений в ряду {a}, № сидения - {b} \n'
                                       f'Ввод осуществляется поочередно по каждому сидению в виде параметра 0 или 1\n,'
                                       f'(0-место свободно, 1-место занято). Подтверждение через клавишу "Enter": '))
                if enter_sits in (0, 1):
                    element = enter_sits
                    list_seats.append(element)
                else:
                    print("Введен неверный формат бронирования сидений! Выход из программы")
                    chk_enter = False
                    break
            if chk_enter:
                list_line.append(list_seats)
            else:
                break
        if len(list_line) > 0 and chk_enter:
            print("\nСписок рядов и занятых сидений:", list_line)

        if chk_enter:
            enter_value = int(input("\nВведите количество мест для бронирования: "))

            while c < len(list_line):
                if isinstance(list_line[c], list):
                    sub_list_line = list_line[c]
                    d = 0
                    while d < len(sub_list_line):
                        if sub_list_line[d] == 0:
                            e = 1
                            while d + e < len(sub_list_line) and sub_list_line[d] == sub_list_line[d + e]:
                                e += 1
                            if e >= enter_value:
                                #print(f'Есть свободные места рядом в ряду {c} в количестве {e} шт')
                                chk_free = False
                                if num_line == -1:
                                    num_line = c
                                    num_seats = e
                            d += e
                        else:
                            d += 1
                    else:
                        c += 1
                else:
                    break
            if chk_free is True:
                print("\nНет свободных рядов")
            elif chk_free is False and num_line > -1:
                print(f'\nЕсть свободные места рядом в ряду {num_line} в количестве {num_seats} шт')

    case "3":
        print("\nЗадача 3: Написать упрощенную версию алгоритма RLE.\n"
              "Алгоритм RLE объединяет подряд идущие символы в коэффициент и символ\n")

        enter_text = input("Введите текст для объединения подряд идущих символов: ")

        rle = []
        symbol = enter_text[0]
        count = 1

        for elem in enter_text[1:]:
            if elem == symbol:
                count += 1
            else:
                rle.append(str(count))
                rle.append(symbol)
                symbol = elem
                count = 1
        else:
            rle.append(str(count))
            rle.append(symbol)
        print("".join(rle))

    case "4":
        print("\nЗадача 4: Шифр Цезаря. Пользователь вводит строку и ключ шифра,\n"
              "программа должна вывести зашифрованную строку (со сдвигом по ключу).\n"
              "Сдвиг циклический. Используем только латинский алфавит, пробелы не шифруются\n")

        import string

        enter_word = input("Введите слово для шифрования (английский язык): ")
        enter_shift = int(input("Введите значение сдвига: "))

        total_alpha = string.ascii_lowercase + string.ascii_uppercase + string.digits

        cript=""
        for elem in enter_word:
            if elem in total_alpha:
                cript += total_alpha[(total_alpha).index(elem) + enter_shift]
            else:
                cript += elem

        print("Оригинальный текст:",enter_word)
        print("Зашифрованный текст:",cript)

    case "5":
        print("\nЗадача 5: Табель успеваемости. Пользователь в бесконечном цикле (пока не будет введена пустая строка)\n"
              "вводит строки вида: 'название предмета' 'фамилия ученика' 'оценка'. После окончания ввода\n"
              "программа выводит в консоль Название предмета, далее список учеников и все их оценки в виде таблицы\n")

        list_jornal = []
        grouped_values = {}
        chk_enter = True
        a = 0
        c = 0
        enter_jornal = ""

        while chk_enter:
            for a in range(1):
                jornal = []
                for b in range(3):
                    if b == 0:
                        enter_jornal = input(f'Введите Предмет ученика {c}: ')
                    elif b == 1:
                        enter_jornal = input(f'Введите ФИО ученика {c}: ')
                    elif b == 2:
                        enter_jornal = input(f'Введите Оценку ученика {c}: ')
                    if len(enter_jornal) > 0:
                        element = enter_jornal
                        jornal.append(element)
                    else:
                        chk_enter = False
                        break
                if chk_enter:
                    list_jornal.append(jornal)
                else:
                    break
            c += 1
        if len(list_jornal) > 0:
            print("\nИтоговый журнал оценок:", list_jornal)

            for sublist in list_jornal:
                key = sublist[0]
                value = sublist[-2:]
                if key not in grouped_values:
                    grouped_values[key] = []
                grouped_values[key].append(value)
            for key, value in grouped_values.items():
                print(f"\n{key}:")
                value.sort()
                for i in value:
                    for j in i:
                        print(j, end=" ")
                    print("", sep='\n')

    case _:
        print("Невернный ввод. Выход из программы")
