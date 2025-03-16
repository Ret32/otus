enter_task = input("Введите номер задачи по теме 'Математический анализ' от 1 до 5: ")

match enter_task:

    case "1":
        print("\nЗадача 1\n")

        import sympy as sp

        # Определение переменных
        x1, x2 = sp.symbols('x1 x2')

        # Определение функции f(x)
        f = x1 ** 3 - 2 * x1 * x2 + x2 ** 2 - 3 * x1 - 2 * x2

        # Вычисление градиента функции f
        grad_f = sp.Matrix([sp.diff(f, var) for var in (x1, x2)])

        # Нахождение критических точек, решая систему уравнений grad_f = 0
        critical_points = sp.solve(grad_f, (x1, x2))

        # Вывод результатов
        print("Градиент функции f(x):")
        sp.pprint(grad_f, use_unicode=True)

        print("\nКритические точки функции f(x):")
        for point in critical_points:
            print(f"x1 = {point[0]}, x2 = {point[1]}")

    case "2":
        print("\nЗадача 2\n")

        import sympy as sp

        # Определение переменных
        x1, x2 = sp.symbols('x1 x2')

        # Определение функции f(x)
        f = sp.ln(sp.sqrt(x1) + sp.sqrt(x2))

        # Вычисление частных производных
        df_dx1 = sp.diff(f, x1)
        df_dx2 = sp.diff(f, x2)

        # Вычисление выражения x1 * df/dx1 + x2 * df/dx2
        expression = x1 * df_dx1 + x2 * df_dx2

        # Упростить выражение
        simplified_expression = sp.simplify(expression)

        # Проверка равенства 1/2
        is_equal = simplified_expression.equals(1 / 2)

        # Вывод результатов
        print("Частные производные:")
        print(f"df/dx1 = {df_dx1}")
        print(f"df/dx2 = {df_dx2}")
        print("\nВыражение x1 * df/dx1 + x2 * df/dx2:\n",simplified_expression)
        print("\nРавно ли выражение 1/2?\n",is_equal)

    case "3":
        print("\nЗадача 3\n")

        import sympy as sp

        # 1. Определение символьных переменных
        x, y, z = sp.symbols('x y z')

        # 2. Определение функции f(x, y, z)
        f = x + y + z + (x * y * z) ** 2

        # 3. Вычисление частных производных (компонентов градиента)
        df_dx = sp.diff(f, x)
        df_dy = sp.diff(f, y)
        df_dz = sp.diff(f, z)

        # 4. Формирование вектора градиента
        gradient_f = sp.Matrix([df_dx, df_dy, df_dz])

        # 5. Вычисление значения градиента в точке v = (1, 2, 3)
        gradient_at_v = gradient_f.subs({x: 1, y: 2, z: 3})

        # Вывод результатов
        print("Вектор градиента функции f:\n")
        sp.pprint(gradient_f, use_unicode=True)
        print("\nЗначение градиента в точке v = (1, 2, 3):\n")
        sp.pprint(gradient_at_v, use_unicode=True)

    case "4":
        print("\nЗадача 4\n")

        import sympy as sp

        # Определение символьных переменных
        n = 3  # Размерность пространства (например, R^3)
        x = sp.Matrix([sp.symbols(f'x{i + 1}') for i in range(n)]) # Создание вектора переменных x1, x2, ..., xn

        # Вычисление Евклидовой нормы ||x||
        norm_x = sp.sqrt(x.dot(x))

        # Определение функции f(x)
        f = (1 / 3) * norm_x ** 3

        # Вычисление градиента функции f
        gradient_f = sp.Matrix([sp.diff(f, xi) for xi in x])

        # Определение приращения dx
        dx = sp.Matrix([sp.symbols(f'dx{i + 1}') for i in range(n)])

        # Вычисление первого дифференциала df(x)
        df = gradient_f.dot(dx)

        # Вывод результатов
        print("Градиент функции f(x):\n")
        sp.pprint(gradient_f)
        print("\nПервый дифференциал df(x):\n")
        sp.pprint(df)


    case "5":
        print("\nЗадача 5\n")

        import numpy as np

        # Размерности
        n = 3  # Размерность вектора x
        m = 2  # Количество строк в матрице A

        # Генерация случайной матрицы A размером m x n и вектора x размером n
        A = np.random.randn(m, n)
        x = np.random.randn(n)

        # Вычисление функции f(x)
        f_x = np.linalg.norm(np.dot(A, x)) ** 2

        # Вычисление градиента
        gradient_f_x = 2 * np.dot(A.T, np.dot(A, x))

        # Определение приращения dx
        dx = np.random.randn(n)

        # Вычисление первого дифференциала
        df_x = np.dot(gradient_f_x, dx)

        print("Значение функции f(x):", f_x)
        print("Градиент функции f(x):", gradient_f_x)
        print("Первый дифференциал df(x):", df_x)



