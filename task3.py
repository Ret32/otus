enter_task = input("Введите номер задачи по теме 'Функции' от 1 до 5: ")

match enter_task:

    case "1":
            print("\nЗадача 1: Написать функцию, которая будет перводит снейк_кейс в КэмелКейс и наоборот.\n"
                  "Функция сама определяет - какой формат ей передали. Можно добавить ключевой аргумент, \n"
                  "который будет принудительно возвращать один из форматов.\n")


            def convert_case(string, force_case=None):

                if not string:
                    raise ValueError("Строка не должна быть пустой!")

                is_snake_case = False
                is_camel_case = False

                if '_' in string:
                    if all(part.islower() for part in string.split('_')):
                        is_snake_case = True
                    elif all(part.isupper() for part in string.split('_')):
                        is_snake_case = True
                    else:
                        raise ValueError("Строка должна быть формата snake_case или SCREAMING_SNAKE_CASE!")
                elif string[0].isupper() and string[1:].isalnum() and not any(char == '_' for char in string):
                    is_camel_case = True
                else:
                    raise ValueError("Строка должна быть формата snake_case или CamelCase")

                if force_case:
                    if force_case == 'snake':
                        is_snake_case = True
                        is_camel_case = False
                    elif force_case == 'camel':
                        is_snake_case = False
                        is_camel_case = True
                    else:
                        raise ValueError("Параметр force_case должен содержать ключ 'snake' или 'camel'")

                if is_snake_case:
                    components = string.split('_')
                    return ''.join(word.capitalize() for word in components)
                else:
                    snake_case = ''.join(['_' + char.lower() if char.isupper() else char for char in string])
                    return snake_case.lstrip('_')


            print(convert_case("привет_мир"))
            print(convert_case("ПриветМир"))
            print(convert_case("привет_мир", force_case='snake'))
            print(convert_case("ПриветМир", force_case='camel'))
            print(convert_case("ПРИВЕТ_МИР"))

    case _:
        print("Невернный ввод. Выход из программы")