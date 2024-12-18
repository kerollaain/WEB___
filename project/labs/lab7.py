import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import re


# Задача 1: Графік функції Y(x) = x * sin(5x)
def task1():
    x = np.linspace(-2, 5, 500)
    y = x * np.sin(5 * x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=r'$Y(x) = x \cdot \sin(5x)$', color='blue')
    plt.xlabel('x')
    plt.ylabel('Y(x)')
    plt.title('Графік функції $Y(x) = x \\cdot \\sin(5x)$')
    plt.legend()
    plt.grid(True)

    # Вивести графік у Streamlit
    st.pyplot(plt)


# Задача 2: Гістограма частоти появи літер
def task2():
    text = "Приклад тексту для аналізу частоти появи літер у Python"
    processed_text = ''.join(filter(str.isalpha, text.lower()))
    letter_counts = Counter(processed_text)
    letters = list(letter_counts.keys())
    frequencies = list(letter_counts.values())

    plt.figure(figsize=(8, 6))
    plt.bar(letters, frequencies, color='skyblue', edgecolor='black')
    plt.xlabel('Літери')
    plt.ylabel('Частота')
    plt.title('Гістограма частоти появи літер у тексті')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Вивести графік у Streamlit
    st.pyplot(plt)


# Задача 3: Гістограма частоти типів речень
def task3():
    text = """
    Що це таке? Це приклад тексту! Текст може містити різні речення...
    Ось ще кілька: як ти? Це звичайне речення. А це — окличне!
    """

    normal_sentences = len(re.findall(r'[^.!?]+\.', text))
    question_sentences = len(re.findall(r'[^.!?]+\?', text))
    exclamatory_sentences = len(re.findall(r'[^.!?]+!', text))
    ellipsis_sentences = len(re.findall(r'[^.!?]+\.\.\.', text))

    categories = ["Звичайні", "Питальні", "Окличні", "З трикрапкою"]
    frequencies = [normal_sentences, question_sentences, exclamatory_sentences, ellipsis_sentences]

    plt.figure(figsize=(8, 6))
    plt.bar(categories, frequencies, color=['blue', 'green', 'red', 'purple'])
    plt.xlabel("Типи речень")
    plt.ylabel("Частота")
    plt.title("Частота різних типів речень у тексті")

    # Вивести графік у Streamlit
    st.pyplot(plt)


# Основна функція
def main():
    st.title("Лабораторна робота 7")

    st.header("Задача 1: Графік функції")
    task1()

    st.header("Задача 2: Гістограма частоти появи літер")
    task2()

    st.header("Задача 3: Гістограма частоти типів речень")
    task3()


if __name__ == "__main__":
    main()
