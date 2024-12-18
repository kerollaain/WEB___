import streamlit as st
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

# Функція для отримання HTML контенту сторінки
def fetch_page(url):
    response = requests.get(url)
    if response.ok:
        return response.text
    else:
        st.error(f"Помилка отримання сторінки: {response.status_code}")
        return None

# Функція для аналізу HTML контенту сторінки
def analyze_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    words = re.findall(r'\w+', text.lower())
    word_frequency = Counter(words)

    tags = [tag.name for tag in soup.find_all()]
    tag_frequency = Counter(tags)

    links = soup.find_all('a', href=True)
    images = soup.find_all('img', src=True)

    return {
        "word_frequency": word_frequency,
        "tag_frequency": tag_frequency,
        "link_count": len(links),
        "image_count": len(images),
    }

# Функція для відображення результатів
def display_results(results):
    st.subheader("Частота слів:")
    for word, count in results["word_frequency"].most_common(10):
        st.write(f"{word}: {count}")

    st.subheader("Частота HTML-тегів:")
    for tag, count in results["tag_frequency"].most_common(10):
        st.write(f"<{tag}>: {count}")

    st.write(f"\nКількість посилань: {results['link_count']}")
    st.write(f"Кількість зображень: {results['image_count']}")

# Головна функція Streamlit
def main():
    st.title("Аналіз HTML-сторінки")

    # Введення URL сторінки
    url = st.text_input("Введіть URL сторінки новин:")
    if url:
        html_content = fetch_page(url)
        if html_content:
            results = analyze_page(html_content)
            display_results(results)

if __name__ == "__main__":
    main()
