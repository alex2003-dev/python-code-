import logic

def main():
    while True:
        print("\n1. Add expense")
        print("2. List all")
        print("3. Filter by category")
        print("4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            name = input("Name: ")
            amount = input("Amount: ")
            category = input("Category: ")
            logic.add_expense(name, amount, category)
        elif choice == "2":
            logic.list_expenses()
        elif choice == "3":
            cat = input("Category: ")
            logic.filter_expenses(cat)
        elif choice == "4":
            print("Bye")
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()
