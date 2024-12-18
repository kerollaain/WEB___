import os
import csv
import streamlit as st


def create_file(group_name, students):
    with open(f"{group_name}.txt", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(students)
    st.success(f"Файл '{group_name}.txt' створено.")


def read_file(file_name):
    if not os.path.exists(file_name):
        st.error(f"Файл '{file_name}' не існує.")
        return []
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        data = [(row[0], float(row[1])) for row in reader]
    return data


def append_to_file(file_name, students):
    if not os.path.exists(file_name):
        st.warning(f"Файл '{file_name}' не існує. Створюємо новий.")
        create_file(file_name.replace(".txt", ""), students)
        return
    with open(file_name, "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(students)
    st.success(f"Дані додано у файл '{file_name}'.")


def find_files_in_directory(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    st.write(f"Файли у каталозі '{directory}': {files}")
    return files


def search_in_file(file_name, student_name):
    students = read_file(file_name)
    for student, grade in students:
        if student == student_name:
            return student, grade
    return None


def sort_file(file_name):
    students = read_file(file_name)
    if not students:
        st.error(f"Файл '{file_name}' порожній або не існує.")
        return
    sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
    with open(file_name, "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(sorted_students)
    st.success(f"Дані у файлі '{file_name}' відсортовано.")


def main():
    st.title("Лабораторна робота 3: Робота з файлами")

    # Показуємо список лабораторних робіт
    students_group1 = [("Олена", 85.5), ("Андрій", 72.0), ("Марія", 95.3)]
    students_group2 = [("Василь", 65.4), ("Юлія", 88.8), ("Ігор", 74.5)]

    create_file_button = st.button("Створити файли для груп")
    if create_file_button:
        create_file("group1", students_group1)
        create_file("group2", students_group2)

    append_button = st.button("Додати студента до групи 1")
    if append_button:
        append_to_file("group1.txt", [("Олександр", 78.0)])

    read_button = st.button("Переглянути дані з файлу 'group1.txt'")
    if read_button:
        data = read_file("group1.txt")
        st.write("Дані з файлу 'group1.txt':")
        st.write(data)

    search_name = st.text_input("Введіть ім'я студента для пошуку")
    if search_name:
        student = search_in_file("group1.txt", search_name)
        if student:
            st.write(f"Студент: {student[0]}, Оцінка: {student[1]}")
        else:
            st.write("Студента не знайдено.")

    sort_button = st.button("Відсортувати дані в 'group1.txt'")
    if sort_button:
        sort_file("group1.txt")
        st.write("Дані після сортування:")
        sorted_data = read_file("group1.txt")
        st.write(sorted_data)

    list_files_button = st.button("Переглянути файли в каталозі")
    if list_files_button:
        files = find_files_in_directory(".")
        st.write(files)


if __name__ == "__main__":
    main()
