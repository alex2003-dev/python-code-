<<<<<<< HEAD

=======
catalog = {"apple": 1.5, "banana": 0.8, "milk": 2.0, "bread": 2.5}
cart = []

def add(product, qty):
    for i, (p, q) in enumerate(cart):
        if p == product:
            cart[i] = (p, q + qty)
            return
    cart.append((product, qty))

def remove(product):
    global cart
    cart[:] = [item for item in cart if item[0] != product]

def total():
    return sum(catalog[p] * q for p, q in cart if p in catalog)

add("apple", 3)
add("apple", 2)
add("milk", 1)
remove("milk")

print("Cart:", cart)
print("Total:", total())
>>>>>>> 639a049 (Shopping Cart Simulator)
