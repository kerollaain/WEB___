import math
import streamlit as st


def task1():
    """Задача 1: Обчислення виразу z"""
    a = st.number_input("Введіть значення кута a в радіанах:", format="%.2f", key="task1_a")
    if a is not None:
        z = math.cos(a) + math.sin(a) + math.cos(3 * a) + math.sin(3 * a)
        st.write("Значення виразу z =", z)


def fibonacci(n):
    """Задача 2: Обчислення n-го числа Фібоначчі"""
    if n < 0:
        return
    if n == 0 or n == 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def task2():
    """Задача 2: Обчислення числа Фібоначчі"""
    n = st.number_input("Введіть номер числа Фібоначчі:", min_value=0, step=1, key="task2_n")
    if n is not None:
        result = fibonacci(n)
        st.write(f"{n}-е число Фібоначчі: {result}")


def task3():
    """Задача 3: Заміна рядків у матриці"""
    def swap_rows(matrix, row1, row2):
        matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
        [17, 18, 19, 20]
    ]

    st.write("Початкова матриця:")
    st.table(matrix)

    # Виконуємо заміну рядків
    swap_rows(matrix, 0, 2)

    st.write("Матриця після заміни рядків:")
    st.table(matrix)


def main():
    st.title("Лабораторні роботи")
    st.sidebar.title("Меню")

    task_option = st.sidebar.radio("Оберіть задачу", ("Задача 1", "Задача 2", "Задача 3"))

    if task_option == "Задача 1":
        task1()
    elif task_option == "Задача 2":
        task2()
    elif task_option == "Задача 3":
        task3()


if __name__ == "__main__":
    main()
