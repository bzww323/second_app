import streamlit as st
import matplotlib.pyplot as plt
from numpy import * # извините

st.title("Графический калькулятор")
# боковое меню, в которое удобно будет внести все функции:
with st.sidebar:
    x_min = st.number_input("Выберите минимум по горизонтальной оси", value=0)
    x_max = st.number_input("Выберите максимум по горизонтальной оси", value=10)
    # даем пользователю возможность выбрать функцию
    function = st.text_input("Формула", "x") # "x" - значение по умолчанию, чтобы изначально строился график y = x  (более наивная реализация с готовым выбором функций:  # function = st.selectbox("Функция", ["log", "sin", "cos", "arcsin", "arccos", "tan"]))
    # слайдер для выбора количества точек
    steps = st.slider("Количество точек", 50, 500)
    grid = st.checkbox("Сетка")

x = linspace(x_min, x_max, steps)
y = eval(function) #y = getattr(np, function)(x) # getattr(np, function) выдает функцию: log, cos, sin; (x) - сразу же передаем аргумент этой функции
# y = x ** 2
figure = plt.figure(figsize=(8,8))
plt.plot(x, y, color="green")
if grid:
    plt.grid()

st.pyplot(figure)
