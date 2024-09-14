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
        pass

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

    case _:
        print("Невернный ввод. Выход из программы")
