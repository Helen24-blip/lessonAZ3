import matplotlib.pyplot as plt
import numpy as np

# Генерация массива случайных чисел
random_array = np.random.rand(5)  # Массив из 5 случайных чисел
x = random_array  # Используем random_array как координаты X
y = np.random.rand(5)  # Создаем массив для Y

print("x (random_array):", x)
print("y:", y)

# Построение диаграммы рассеяния
plt.scatter(x, y)
plt.xlabel("Х ось")
plt.ylabel("Y ось")
plt.title("Диаграмма рассеивания с использованием random_array")
plt.show()
