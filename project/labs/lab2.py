import streamlit as st

def find_min_five_elements(arr):
    """Функція для пошуку перших п'яти мінімальних елементів."""
    if len(arr) < 5:
        return sorted(arr)
    else:
        return sorted(arr)[:5]

def calculate_average(arr):
    """Функція для обчислення середнього арифметичного."""
    if not arr:
        return None
    return sum(arr) / len(arr)

def main():
    st.title("Лабораторна робота 2: Мінімальні елементи та середнє арифметичне")

    # Ввід числа для створення списку
    numbers_input = st.text_input("Введіть числа через кому (наприклад: 33, 10, 55):")

    if numbers_input:
        try:
            # Перетворення введених значень на список цілих чисел
            numbers = list(map(int, numbers_input.split(',')))

            if st.button("Запустити лабораторну роботу"):
                # Виклик функцій
                min_five = find_min_five_elements(numbers)
                average = calculate_average(numbers)

                # Виведення результатів
                st.write("Перші п'ять мінімальних елементів:", min_five)
                st.write("Середнє арифметичне:", average)

        except ValueError:
            st.error("Будь ласка, введіть правильний формат чисел.")
    else:
        st.warning("Будь ласка, введіть числа.")

if __name__ == "__main__":
    main()
