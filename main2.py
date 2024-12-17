from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import numpy as np
import matplotlib.pyplot as plt

# Путь к WebDriver
driver_path = "C:\\Users\\rebru\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

# Настройка Selenium
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Открываем сайт
    url = "https://www.divan.ru/category/divany-i-kresla"  # URL раздела с диванами
    driver.get(url)

    # Явное ожидание появления элементов с ценами
    wait = WebDriverWait(driver, 10)
    price_elements = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, 'span[data-testid="price"]')  # Селектор для цен
    ))

    # Сбор цен
    prices = []
    for price in price_elements:
        price_text = price.text.replace(' ', '').replace('руб.', '')
        if price_text.isdigit():  # Проверяем, что строка содержит только цифры
            prices.append(int(price_text))

    # Проверка на наличие данных
    if not prices:
        print("Цены не были распознаны. Проверьте селектор или структуру сайта.")
    else:
        # Сохранение данных в CSV
        with open('sofa_prices.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Цена'])
            for p in prices:
                writer.writerow([p])

        # Анализ данных
        prices_array = np.array(prices)
        mean_price = np.mean(prices_array)
        print(f"Средняя цена на диваны: {mean_price:.2f} ₽")

        # Построение гистограммы
        plt.figure(figsize=(8, 6))
        plt.hist(prices_array, bins=20, color='blue', alpha=0.7, edgecolor='black')
        plt.title('Гистограмма цен на диваны', fontsize=14)
        plt.xlabel('Цена (₽)', fontsize=12)
        plt.ylabel('Частота', fontsize=12)
        plt.grid(alpha=0.4)
        plt.show()

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрываем браузер
    driver.quit()
