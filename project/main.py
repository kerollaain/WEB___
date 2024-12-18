import streamlit as st
import importlib
import traceback

def load_labs():
    labs = {
        "Lab 1": "labs.lab1",
        "Lab 2": "labs.lab2",
        "Lab 3": "labs.lab3",
        "Lab 4": "labs.lab4",
        "Lab 5": "labs.lab5",
        "Lab 6": "labs.lab6",
        "Lab 7": "labs.lab7",
        "README": "README.md",
    }
    return labs

def run_lab(module_name):
    try:
        lab_module = importlib.import_module(module_name)
        if hasattr(lab_module, "task1"):
            lab_module.task1()
        if hasattr(lab_module, "task2"):
            lab_module.task2()
        if hasattr(lab_module, "task3"):
            lab_module.task3()
    except ModuleNotFoundError:
        st.error(f"Модуль {module_name} не знайдено!")
    except Exception as e:
        st.error(f"Сталася помилка: {str(e)}")
        st.text(traceback.format_exc())  # Вивести подробиці помилки для налагодження

def main():
    st.title("Лабораторні роботи")
    st.sidebar.title("Меню")

    labs = load_labs()
    lab_name = st.sidebar.selectbox("Оберіть лабораторну роботу", list(labs.keys()))

    if lab_name:
        st.header(lab_name)
        if st.button("Запустити лабораторну роботу"):
            run_lab(labs[lab_name])

if __name__ == "__main__":
    main()
