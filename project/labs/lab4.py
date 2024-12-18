import streamlit as st
import random
from collections import Counter


# Функція для генерації випадкової фрази
def generate_random_phrase():
    list1 = ["Великий", "Маленький", "Швидкий", "Повільний"]
    list2 = ["собака", "кіт", "птах", "жираф"]
    list3 = ["бігає", "спить", "летить", "стрибає"]
    word1 = random.choice(list1)
    word2 = random.choice(list2)
    word3 = random.choice(list3)
    return f"{word1} {word2} {word3}"


# Функція для аналізу тексту з файлу
def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    total_chars_with_spaces = len(text)
    total_chars_without_spaces = len(text.replace(" ", "").replace("\n", ""))
    words = text.split()
    total_words = len(words)
    unique_words = set(words)
    total_unique_words = len(unique_words)
    word_counts = Counter(words)
    words_with_one_occurrence = sum(1 for count in word_counts.values() if count == 1)

    return {
        "total_chars_with_spaces": total_chars_with_spaces,
        "total_chars_without_spaces": total_chars_without_spaces,
        "total_words": total_words,
        "total_unique_words": total_unique_words,
        "words_with_one_occurrence": words_with_one_occurrence
    }


# Функція для пошуку найдовшої повторюваної послідовності
def find_longest_repeated_sequence(words, seq_length=3):
    sequences = [' '.join(words[i:i + seq_length]) for i in range(len(words) - seq_length + 1)]
    sequence_counts = Counter(sequences)
    repeated_sequences = {seq: count for seq, count in sequence_counts.items() if count > 1}
    if repeated_sequences:
        longest_sequence = max(repeated_sequences, key=len)
        return longest_sequence, repeated_sequences[longest_sequence]
    return None


# Основна функція Streamlit
def main():
    st.title("Лабораторна робота 4: Аналіз тексту")

    # Генерація випадкової фрази
    if st.button("Згенерувати випадкову фразу"):
        random_phrase = generate_random_phrase()
        st.write(f"Випадкова фраза: {random_phrase}")

    # Завантаження текстового файлу
    uploaded_file = st.file_uploader("Завантажте текстовий файл для аналізу", type="txt")

    if uploaded_file is not None:
        # Збереження завантаженого файлу
        file_path = f"temp_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Аналіз тексту
        analysis_results = analyze_text(file_path)
        st.write("Аналіз тексту:")
        st.write(f"Загальна кількість символів (включаючи пробіли): {analysis_results['total_chars_with_spaces']}")
        st.write(f"Загальна кількість символів (без пробілів): {analysis_results['total_chars_without_spaces']}")
        st.write(f"Загальна кількість слів: {analysis_results['total_words']}")
        st.write(f"Кількість унікальних слів: {analysis_results['total_unique_words']}")
        st.write(f"Кількість слів, що зустрічаються лише один раз: {analysis_results['words_with_one_occurrence']}")

        # Пошук найдовшої повторюваної послідовності
        words = open(file_path, 'r', encoding='utf-8').read().split()
        longest_sequence = find_longest_repeated_sequence(words)

        if longest_sequence:
            st.write(f"Найдовша повторювана послідовність: {longest_sequence[0]}")
            st.write(f"Кількість повторів: {longest_sequence[1]}")
        else:
            st.write("Повторюваних послідовностей немає.")


if __name__ == "__main__":
    main()
