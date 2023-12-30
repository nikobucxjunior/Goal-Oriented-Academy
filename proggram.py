class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def __str__(self):
        return "\n".join(str(item) for item in self.items)

# example usage
def main():
    cart = ShoppingCart()

    apple = Product("Apple", 0.50)
    orange = Product("Orange", 0.60)
    bread = Product("Bread", 1.20)

    cart.add_item(apple)
    cart.add_item(orange)
    cart.add_item(bread)

    print("Your shopping cart contains:")
    print(cart)

    print(f"Total: ${cart.calculate_total()}")

if __name__ == "__main__":
    main()