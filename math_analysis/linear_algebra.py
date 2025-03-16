enter_task = input("Введите номер задачи по теме 'Линейная алгебра' от 1 до 4: ")

match enter_task:

    case "1":
        print("\nЗадача 1\n")

        import numpy as np

        # Определение матриц A, B и C
        A = np.array([[2, -4],
                      [3, 5],
                      [-1, 0]])

        B = np.array([[1, 2, 7],
                      [-3, -4, 0],
                      [5, 2, 1]])

        C = np.array([[6, -3, 9],
                      [4, -5, 2],
                      [8, 1, 5]])

        # Транспонирование матриц A и B
        A_T = A.T
        B_T = B.T

        # Вычисление произведений A^T C и A^T B^T
        A_T_C = np.dot(A_T, C)
        A_T_B_T = np.dot(A_T, B_T)

        # Вычисление матрицы D
        D = A_T_C - 2 * A_T_B_T

        print("Матрица D:\n", D)

    case "2":
        print("\nЗадача 2\n")

        from sympy import symbols, Eq, Matrix, solve

        # Определение переменных
        x, y, z, v = symbols('x y z v')

        # Задание матриц
        A = Matrix([[x, 2, 3],
                    [-1, y, 4]])

        B = Matrix([[1, 2, -5],
                    [2, -6, z]])

        C = Matrix([[8, v, -1],
                    [1, 6, 4]])

        # Составление уравнения
        equation = Eq(3 * A + 2 * B, C)

        # Решение системы уравнений
        solution = solve(equation, (x, y, z, v))

        # Вывод решения
        for i in symbols('x y z v'):
            print (f"{i} = {solution[i]}")

    case "3":
        print("\nЗадача 3\n")

        import numpy as np

        # Определение строковых векторов
        a1_str = np.array([2, -5])
        a2_str = np.array([-1, 3])
        x_str = np.array([1, -4])

        # Преобразование строковых векторов в столбцовые
        a1 = a1_str.reshape(-1, 1)
        a2 = a2_str.reshape(-1, 1)
        x = x_str.reshape(-1, 1)

        # 1. Проверка линейной независимости векторов a1 и a2
        matrix_A = np.hstack((a1, a2))
        det_A = np.linalg.det(matrix_A)

        if det_A != 0:
            print("Векторы a1 и a2 линейно независимы и образуют базис B.")
        else:
            print("Векторы a1 и a2 линейно зависимы и не могут образовать базис B.")

        # 2. Нахождение координат [x]_B вектора x в базисе B
        # Решение системы A * [c1, c2]^T = x
        c = np.linalg.solve(matrix_A.T, x)
        c1, c2 = c[0][0], c[1][0]
        print(f"Координаты вектора x в базисе B: c1 = {c1}, c2 = {c2}")

        # 3. Преобразование координат вектора y из базиса B в стандартный базис
        y_B = np.array([1, 1]).reshape(-1, 1)
        y_standard = np.dot(matrix_A, y_B)
        print(f"Вектор y в стандартном базисе: {y_standard.T[0]}")

    case "4":
        print("\nЗадача 4\n")

        import numpy as np
        import matplotlib.pyplot as plt

        # 1. Генерация случайной матрицы A размером n x n
        n = 100  # Размерность матрицы
        A = np.random.randn(n, n)

        # 2. Сингулярное разложение матрицы A
        U, S, Vt = np.linalg.svd(A)

        # 3. Аппроксимация матрицы A с разным рангом r и вычисление ошибки
        errors = []
        for r in range(2, n + 1):
            # Создание диагональной матрицы S_r размером r x r
            S_r = np.diag(S[:r])
            # Аппроксимация матрицы A с рангом r
            A_r = U[:, :r] @ S_r @ Vt[:r, :]
            # Вычисление ошибки аппроксимации E(r) как нормы Фробениуса разности A и A_r
            error = np.linalg.norm(A - A_r, 'fro')
            errors.append(error)

        # 4. Построение графика зависимости ошибки от ранга
        plt.plot(range(2, n + 1), errors, marker='o', linestyle='-', color='b')
        plt.xlabel('Ранг r')
        plt.ylabel('Ошибка аппроксимации E(r)')
        plt.title('Зависимость ошибки аппроксимации от ранга матрицы')
        plt.grid(True)
        plt.show()