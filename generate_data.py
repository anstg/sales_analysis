import csv
import random

customers = [
    {"customerId": 1, "age": 25},
    {"customerId": 2, "age": 32},
    {"customerId": 3, "age": 38},
    {"customerId": 4, "age": 50},
    {"customerId": 5, "age": 28},
]

products = [
    {"productId": 101, "base_cost": 100},
    {"productId": 102, "base_cost": 150},
    {"productId": 103, "base_cost": 200},
    {"productId": 104, "base_cost": 120},
    {"productId": 105, "base_cost": 130},
]

months = [f"2026{str(m).zfill(2)}" for m in range(1, 13)]

sales = []

for month in months:
    for cust in customers:
        # каждый клиент покупает 1-3 продукта в месяц
        for _ in range(random.randint(1, 3)):
            prod = random.choice(products)
            # цена может меняться на ±20%
            cost = round(prod["base_cost"] * random.uniform(0.8, 1.2), 2)
            sales.append({
                "customerId": cust["customerId"],
                "age": cust["age"],
                "productId": prod["productId"],
                "cost": cost,
                "month": month
            })

# Сохраняем CSV
with open("data/sales.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["customerId","age","productId","cost","month"])
    writer.writeheader()
    for row in sales:
        writer.writerow(row)

print("Сгенерировано", len(sales), "записей")
