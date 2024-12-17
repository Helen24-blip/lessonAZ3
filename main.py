import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0  # Среднее значение
std_dev = 1  # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, density=True, alpha=0.7, color='blue', edgecolor='black')
plt.title('Гистограмма нормального распределения', fontsize=14)
plt.xlabel('Значения', fontsize=12)
plt.ylabel('Плотность вероятности', fontsize=12)
plt.grid(alpha=0.4)
plt.show()
