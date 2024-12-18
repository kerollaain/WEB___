import streamlit as st

# Клас для книги
class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"Назва: {self.title}, Автор: {self.author}, Рік: {self.year}, Жанр: {self.genre}"

# Клас для домашньої бібліотеки
class HomeLibrary:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year, genre):
        book = Book(title, author, year, genre)
        self.books.append(book)
        st.write(f"Книга \"{title}\" додана до бібліотеки.")

    def remove_book(self, number):
        if 0 <= number < len(self.books):
            removed_book = self.books.pop(number)
            st.write(f"Книга \"{removed_book.title}\" видалена з бібліотеки.")
        else:
            st.write("Книга з таким номером не знайдена.")

    def search_books(self, **kwargs):
        results = self.books
        for key, value in kwargs.items():
            results = [book for book in results if getattr(book, key, None) == value]
        return results

    def get_book_by_number(self, number):
        if 0 <= number < len(self.books):
            return self.books[number]
        else:
            st.write("Книга з таким номером не знайдена.")
            return None

    def display_books(self):
        if not self.books:
            st.write("Бібліотека порожня.")
        else:
            for i, book in enumerate(self.books):
                st.write(f"{i}. {book}")

# Головна функція Streamlit
def main():
    st.title("Домашня бібліотека")

    library = HomeLibrary()

    # Додавання книг
    st.subheader("Додавання книг до бібліотеки")
    with st.form(key="add_book_form"):
        title = st.text_input("Назва книги")
        author = st.text_input("Автор книги")
        year = st.number_input("Рік видання", min_value=1500, max_value=2024, value=2000)
        genre = st.text_input("Жанр книги")
        submit_button = st.form_submit_button(label="Додати книгу")
        if submit_button:
            library.add_book(title, author, year, genre)

    # Пошук книг
    st.subheader("Пошук книг")
    search_author = st.text_input("Автор для пошуку")
    if search_author:
        found_books = library.search_books(author=search_author)
        if found_books:
            st.write(f"Знайдено книги автора {search_author}:")
            for book in found_books:
                st.write(book)
        else:
            st.write(f"Книги автора {search_author} не знайдено.")

    # Отримання книги за номером
    st.subheader("Отримання книги за номером")
    book_number = st.number_input("Номер книги", min_value=0, max_value=10, value=0)
    if book_number is not None:
        book = library.get_book_by_number(book_number)
        if book:
            st.write(book)

    # Видалення книги
    st.subheader("Видалення книги за номером")
    remove_number = st.number_input("Номер книги для видалення", min_value=0, max_value=10, value=0)
    if st.button("Видалити книгу"):
        library.remove_book(remove_number)

    # Виведення всіх книг
    st.subheader("Всі книги в бібліотеці")
    library.display_books()

if __name__ == "__main__":
    main()
