import csv
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import date, datetime

# Создаем наши данные
with open('stepik.csv', 'w', encoding='utf-8', newline='') as file:
    sales_data = [
        {'product_name': 'яблоки', 'quantity': 10, 'price': 15, 'date': '2024-06-21'},
        {'product_name': 'груши', 'quantity': 16, 'price': 11, 'date': '2024-06-22'},
        {'product_name': 'сливы', 'quantity': 20, 'price': 15, 'date': '2024-06-19'},
        {'product_name': 'печенье', 'quantity': 16, 'price': 23, 'date': '2024-06-20'},
        {'product_name': 'сливы', 'quantity': 21, 'price': 15, 'date': '2024-06-16'},
        {'product_name': 'яблоки', 'quantity': 16, 'price': 15, 'date': '2024-06-20'},
        {'product_name': 'конфеты Рот-Фронт', 'quantity': 11, 'price': 22, 'date': '2024-06-24'},
        {'product_name': 'сливы', 'quantity': 6, 'price': 15, 'date': '2024-06-20'},
    ]

    columns = ['product_name', 'quantity', 'price', 'date']
    writer = csv.DictWriter(file, fieldnames=columns, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    for i in sales_data:
        writer.writerow(i)

def read_sales_data(file_path):
    sales_data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            product_name, quantity, price, date = row['product_name'], int(row['quantity']), float(row['price']), datetime.strptime(row['date'], '%Y-%m-%d').date()
            sales_data.append({
                'product_name': product_name,
                'quantity': quantity,
                'price': price,
                'date': date
            })
    return sales_data
def total_sales_per_product(file_path):
    sales_data = read_sales_data(file_path)
    total_sales = defaultdict(float)
    for sale in sales_data:
        total_sales[sale['product_name']] += sale['quantity'] * sale['price']
    return total_sales


def sales_over_time(file_path):
    sales_data = read_sales_data(file_path)
    sales_by_date = defaultdict(float)
    for sale in sales_data:
        sales_by_date[sale['date']] += sale['quantity'] * sale['price']
    return sales_by_date

total_sales = total_sales_per_product('stepik.csv')
sales_by_date = sales_over_time('stepik.csv')


max_product = max(total_sales, key=total_sales.get)
max_product_value = total_sales[max_product]


max_day = max(sales_by_date, key=sales_by_date.get)
max_day_value = sales_by_date[max_day]

print(f"Продукт с наибольшей выручкой: {max_product}, общая выручка: {max_product_value}")
print(f"День с наибольшей выручкой: {max_day}, общая выручка: {max_day_value}")

plt.figure(figsize=(10, 5))
plt.bar(total_sales.keys(), total_sales.values(), color='skyblue')
plt.title('Total Sales Per Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(sales_by_date.keys(), sales_by_date.values(), color='salmon')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
