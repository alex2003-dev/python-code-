import storage

def add_expense(name, amount, category):
    data = storage.load_expenses()
    try:
        amount = float(amount)
    except:
        print("Invalid amount")
        return
    item = {"name": name, "amount": amount, "category": category}
    data.append(item)
    storage.save_expenses(data)
    print("Expense added")

def list_expenses():
    data = storage.load_expenses()
    if not data:
        print("No expenses yet")
        return
    total = 0
    for i in data:
        print(i["name"], "-", i["amount"], "(", i["category"], ")")
        total += i["amount"]
    print("Total:", total)

def filter_expenses(category):
    data = storage.load_expenses()
    found = [x for x in data if x["category"].lower() == category.lower()]
    if not found:
        print("No expenses in this category")
        return
    total = 0
    for i in found:
        print(i["name"], "-", i["amount"])
        total += i["amount"]
    print("Total for", category + ":", total)
