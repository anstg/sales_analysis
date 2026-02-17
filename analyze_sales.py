import csv
from collections import defaultdict
import matplotlib.pyplot as plt


def read_sales(file_path="data/sales.csv"):
    sales = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['customerId'] = int(row['customerId'])
            row['age'] = int(row['age'])
            row['productId'] = int(row['productId'])
            row['cost'] = float(row['cost'])
            row['month'] = row['month']
            sales.append(row)
    return sales

def avg_monthly_spend(sales):
    spend_by_customer = defaultdict(lambda: defaultdict(float))
    for r in sales:
        spend_by_customer[r['customerId']][r['month']] += r['cost']

    age_groups = {'20-30': [], '31-45': [], '45+': []}

    for r in sales:
        cust_months = spend_by_customer[r['customerId']]
        avg_spend = sum(cust_months.values()) / len(cust_months)
        age = r['age']
        if 20 <= age <= 30:
            age_groups['20-30'].append(avg_spend)
        elif 31 <= age <= 45:
            age_groups['31-45'].append(avg_spend)
        elif age > 45:
            age_groups['45+'].append(avg_spend)

    result = {}
    for group, spends in age_groups.items():
        result[group] = round(sum(spends)/len(spends), 2) if spends else 0
    return result

def top_products(sales):
    income_by_product = defaultdict(float)
    total_income = 0
    for r in sales:
        income_by_product[r['productId']] += r['cost']
        total_income += r['cost']
    sorted_products = sorted(income_by_product.items(), key=lambda x: x[1], reverse=True)
    top5 = [(pid, round(income,2), round(income/total_income*100,2)) for pid, income in sorted_products[:5]]
    return top5

def plot_avg_spend(age_spend):
    groups = list(age_spend.keys())
    values = list(age_spend.values())
    plt.bar(groups, values, color=['skyblue','orange','green'])
    plt.title("Средние траты по возрастным группам")
    plt.ylabel("Средние траты")
    plt.show()

def plot_top_products(top5):
    products = [f"Product {pid}" for pid, _, _ in top5]
    incomes = [income for _, income, _ in top5]
    plt.bar(products, incomes, color='purple')
    plt.title("Топ-5 продуктов по доходу")
    plt.ylabel("Доход")
    plt.show()

def plot_monthly_trends(sales):
    month_groups = defaultdict(lambda: defaultdict(float))
    count_groups = defaultdict(lambda: defaultdict(int))
    
    for r in sales:
        age = r['age']
        month = r['month']
        cost = r['cost']
        if 20 <= age <= 30:
            group = '20-30'
        elif 31 <= age <= 45:
            group = '31-45'
        else:
            group = '45+'
        month_groups[group][month] += cost
        count_groups[group][month] += 1
    
    months = sorted({r['month'] for r in sales})
    for group in ['20-30','31-45','45+']:
        avg = [month_groups[group][m]/count_groups[group][m] if count_groups[group][m]>0 else 0 for m in months]
        plt.plot(months, avg, marker='o', label=group)
    
    plt.title("Средние траты по месяцам и возрастным группам")
    plt.xlabel("Месяц")
    plt.ylabel("Средние траты")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_age_group_share(sales):
    income_by_group = defaultdict(float)
    for r in sales:
        age = r['age']
        cost = r['cost']
        if 20 <= age <= 30:
            income_by_group['20-30'] += cost
        elif 31 <= age <= 45:
            income_by_group['31-45'] += cost
        else:
            income_by_group['45+'] += cost
    
    groups = list(income_by_group.keys())
    values = list(income_by_group.values())
    
    plt.pie(values, labels=groups, autopct='%1.1f%%', startangle=90, colors=['skyblue','orange','green'])
    plt.title("Доля дохода по возрастным группам")
    plt.show()
    
def plot_product_distribution(sales):
    from collections import Counter
    import matplotlib.pyplot as plt

    product_counts = Counter(r['productId'] for r in sales)
    
 
    product_counts = dict(sorted(product_counts.items(), key=lambda x: x[1], reverse=True))

    products = [f"Product {p}" for p in product_counts.keys()]
    counts = list(product_counts.values())

    plt.figure(figsize=(10,5))  
    plt.bar(products, counts, color='purple')
    plt.title("Количество покупок по продуктам")
    plt.ylabel("Количество")
    plt.xlabel("Продукты")
    plt.xticks(rotation=45, ha='right') 
    plt.tight_layout()  
    plt.show()

if __name__ == "__main__":
    sales = read_sales()
    age_spend = avg_monthly_spend(sales)
    top5 = top_products(sales)

    print("Средние траты по возрастным группам:")
    print(age_spend)
    print("\nТоп-5 продуктов по доходу:")
    for pid, income, share in top5:
        print(f"Product {pid}: income={income}, share={share}%")

    # Визуализация
    plot_avg_spend(age_spend)
    plot_top_products(top5)
    plot_monthly_trends(sales)
    plot_age_group_share(sales)
    plot_product_distribution(sales)


