enter_task = input("Введите номер задачи по теме 'Функции' от 1 до 5: ")

match enter_task:

    case "1":
            print("\nЗадача 1: Написать функцию, которая будет перводит снейк_кейс в КэмелКейс и наоборот.\n"
                  "Функция сама определяет - какой формат ей передали. Можно добавить ключевой аргумент, \n"
                  "который будет принудительно возвращать один из форматов.\n")


            def convert_case(string, force_case=None):

                if not string:
                    raise ValueError("Строка не должна быть пустой!")

                if '_' in string:
                    is_snake_case = all(part.islower() for part in string.split('_'))
                    is_screaming_snake_case = all(part.isupper() for part in string.split('_'))

                    if not (is_snake_case or is_screaming_snake_case):
                        raise ValueError("Строка должна быть формата snake_case или SCREAMING_SNAKE_CASE!")

                    is_snake_case = True
                elif string[0].isupper() and string.isalnum() and '_' not in string:
                    is_snake_case = False
                else:
                    raise ValueError("Строка должна быть формата snake_case или CamelCase")

                if force_case:
                    if force_case == 'snake':
                        is_snake_case = True
                    elif force_case == 'camel':
                        is_snake_case = False
                    else:
                        raise ValueError("Параметр force_case должен содержать ключ 'snake' или 'camel'")

                if is_snake_case:
                    return ''.join(part.capitalize() for part in string.split('_'))
                else:
                    return ''.join(['_' + char.lower() if char.isupper() else char for char in string]).lstrip('_')


            print(convert_case("привет_мир"))
            print(convert_case("ПриветМир"))
            print(convert_case("привет_мир", force_case='snake'))
            print(convert_case("ПриветМир", force_case='camel'))
            print(convert_case("ПРИВЕТ_МИР"))
    case "2":
            print("\nЗадача 2: Написать функцию проверяющую валидность введенной даты.\n")

            from datetime import datetime
            import re

            def is_valid_date(date_string):

                date_format_pattern = r'^\d{2}\.\d{2}\.\d{4}$'
                if not re.match(date_format_pattern, date_string):
                    print("Ошибка: Неверный формат даты. Ожидается 'DD.MM.YYYY'.")
                    return False

                try:

                    date_object = datetime.strptime(date_string, '%d.%m.%Y')
                    return date_string == date_object.strftime('%d.%m.%Y')
                except ValueError:
                    return False

            print(is_valid_date("29.02.2000"))
            print(is_valid_date("29.02.2001"))
            print(is_valid_date("31.04.1962"))
            print(is_valid_date("15.08.2023"))
            print(is_valid_date("31.12.2023"))
            print(is_valid_date("32.01.2023"))
            print(is_valid_date("01.13.2023"))
            print(is_valid_date("15-08-2023"))
            print(is_valid_date("15082023"))
    case _:
        print("Невернный ввод. Выход из программы")