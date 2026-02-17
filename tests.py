from analyze_sales import avg_monthly_spend, top_products

# Простые тестовые данные
sales_test = [
    {'customerId':1,'age':25,'productId':101,'cost':100,'month':'202601'},
    {'customerId':1,'age':25,'productId':102,'cost':150,'month':'202601'},
    {'customerId':2,'age':35,'productId':103,'cost':200,'month':'202601'},
]

# Тест средних трат
result = avg_monthly_spend(sales_test)
assert result['20-30'] == 250
assert result['31-45'] == 200

# Тест топ-5 продуктов
top5 = top_products(sales_test)
assert top5[0][0] == 103
assert top5[0][1] == 200

print("Все тесты пройдены ✅")
