from math import isqrt

while True:
    print("\n1.Check prime\n2.Find divisors\n3.Primes up to N\n4.Exit")
    choice = input("Choose: ")

    if choice == "1":
        n = int(input("Enter number: "))
        if n < 2:
            print("Not prime")
            continue
        prime = True
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                prime = False
                break
        print("Prime" if prime else "Not prime")

    elif choice == "2":
        n = int(input("Enter number: "))
        divisors = [i for i in range(1, n + 1) if n % i == 0]
        print("Divisors:", divisors)

    elif choice == "3":
        n = int(input("Enter N: "))
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, isqrt(n) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        primes = [i for i in range(2, n + 1) if sieve[i]]
        print("Primes up to", n, ":", primes)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid input")

