def multiplication_table():
    print("multiplication table from 1 to 10 ")
    for i in range(1, 11):
        for j in range(1, 11):
            value = i * j
            if value % 3 == 0 or value % 5 == 0:
                print(f"{str(value)+'*':>4}", end="")
            else:
                print(f"{value:>4}", end="")
        print()


multiplication_table()