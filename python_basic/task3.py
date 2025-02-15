enter_task = input("Введите номер задачи по теме 'Функции' от 1 до 4: ")

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
                    converted_string = ''.join(part.capitalize() for part in string.split('_'))
                else:
                    converted_string = ''.join(
                        ['_' + char.lower() if char.isupper() else char for char in string]).lstrip('_')

                if force_case:
                    if force_case == 'snake':
                        return f"Исходная строка: '{string}', параметр '{force_case}' | Преобразованная строка: '{converted_string}'"
                    elif force_case == 'camel':
                        return f"Исходная строка: '{string}', параметр '{force_case}' | Преобразованная строка: '{converted_string}'"
                else:
                    return f"Исходная строка: '{string}' | Преобразованная строка: '{converted_string}'"

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
                    return f"Ошибка: Неверный формат даты '{date_string}'. Ожидается 'DD.MM.YYYY'."

                try:
                    date_object = datetime.strptime(date_string, '%d.%m.%Y')

                    if date_string == date_object.strftime('%d.%m.%Y'):
                        return f"Дата '{date_string}' валидна."
                    else:
                        return f"Дата '{date_string}' не валидна."
                except ValueError:
                    return f"Дата '{date_string}' не валидна."

            test_date = ["29.02.2000", "29.02.2001", "31.04.1962", "15.08.2023", "31.12.2023", "32.01.2023", "01.13.2023",
                         "15-08-2023","15082023"]
            for date in test_date:
                print(is_valid_date(date))

    case "3":
            print("\nЗадача 3: Функция проверки на простое число. Простые числа – это такие числа, которые делятся на себя и на единицу.\n")

            import math

            def is_prime(n):
                if n < 2:
                    return f"Исходное число: {n} | Результат: False (число меньше 2 не является простым)"
                if n == 2:
                    return f"Исходное число: {n} | Результат: True (2 - единственное четное простое число)"
                if n % 2 == 0:
                    return f"Исходное число: {n} | Результат: False (четные числа больше 2 не являются простыми)"

                for i in range(3, int(math.sqrt(n)) + 1, 2):
                    if n % i == 0:
                        return f"Исходное число: {n} | Результат: False (делится на {i})"

                return f"Исходное число: {n} | Результат: True (число простое)"

            test_numbers = [1, 2, 3, 4, 5, 29, 30, 999]
            for number in test_numbers:
                print(is_prime(number))
    case "4":
            print("\nЗадача 4: Пользователь в бесконечном цикле вводит данные пользователей: имя, затем фамилию, возраст и ID. \n"
                  "Ввод продолжается до тех пор, пока не будет введено пустое поле. Пользователи заносятся в словарь, \n"
                  "где ключ это ID пользователя, а остальные данные записываются в виде кортежа. Так же программа должна проверять, \n"
                  "что имя и фамилия состоят только из символов и начинаются с большой буквы, если не с большой, то заменяет на большую, \n"
                  "возраст должен быть числом от 18 до 60, ID - целое число, дополненное до 8 знаков незначащими нолями, \n"
                  "ID должен быть уникальным. Дополнительно написать функцию, которая будет выводить полученный словарь в виде таблицы\n")


            def format_id(user_id):
                return str(user_id).zfill(8)


            def validate_name(name):
                if name and name.isalpha():
                    return name.capitalize()
                return None


            def validate_surname(surname):
                if surname and surname.isalpha():
                    return surname.capitalize()
                return None


            def validate_age(age):
                try:
                    age = int(age)
                    if 18 <= age <= 60:
                        return age
                except ValueError:
                    return None
                return None


            def validate_id(user_id, existing_ids):
                try:
                    user_id = int(user_id)
                    if format_id(user_id) not in existing_ids:
                        return format_id(user_id)
                except ValueError:
                    return None
                return None


            def print_users_table(users):
                print(f"{'ID':<10} {'Имя':<15} {'Фамилия':<15} {'Возраст':<10}")
                print("-" * 50)
                for user_id, (name, surname, age) in users.items():
                    print(f"{user_id:<10} {name:<15} {surname:<15} {age:<10}")


            def main():
                users = {}
                existing_ids = set()

                while True:
                    while True:
                        name = input("Введите имя (или оставьте пустым для выхода): ").strip()
                        if not name:
                            print("Выход из программы.\n")
                            if len(users) != 0:
                                print("Печать таблицы:")
                                print_users_table(users)
                            return
                        validated_name = validate_name(name)
                        if validated_name:
                            name = validated_name
                            break
                        else:
                            print("Ошибка: Имя должно содержать только буквы.")

                    while True:
                        surname = input("Введите фамилию: ").strip()
                        validated_surname = validate_surname(surname)
                        if validated_surname:
                            surname = validated_surname
                            break
                        else:
                            print("Ошибка: Фамилия должна содержать только буквы.")

                    while True:
                        age = input("Введите возраст: ").strip()
                        validated_age = validate_age(age)
                        if validated_age is not None:
                            age = validated_age
                            break
                        else:
                            print("Ошибка: Возраст должен быть числом от 18 до 60.")

                    while True:
                        user_id = input("Введите ID: ").strip()
                        validated_id = validate_id(user_id, existing_ids)
                        if validated_id:
                            user_id = validated_id
                            break
                        else:
                            print("Ошибка: ID должен быть уникальным и целым числом.")

                    users[user_id] = (name, surname, age)
                    existing_ids.add(user_id)

                print_users_table(users)


            if __name__ == "__main__":
                main()

    case _:
        print("Невернный ввод. Выход из программы")