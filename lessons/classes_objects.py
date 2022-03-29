"""EXample of a class and object instantiation."""


class Pizza:
    """Models the idea of pizza."""

    # Attribute Defintions
    size: str
    topping: int
    extra_cheese: bool = False

    def __init__(self, size: str, topping: int):
        """Init."""
        self.size = size
        self.topping = topping
    
    def price(self, tax: float) -> float:
        """Calculate the price of a pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0
        
        total += self.topping * 0.75

        if self.extra_cheese:
            total += 1.0

        total += tax

        return total


a_pizza: Pizza = Pizza("large", 3)
a_pizza.extra_cheese = False    
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price(1.05)}")

another_pizza = Pizza("small", 2)
print()