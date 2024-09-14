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
    case _:
        print("Невернный ввод. Выход из программы")
