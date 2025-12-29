class DiscountStrategy:
    def apply(self, price):
        pass

class NoDiscount(DiscountStrategy):
    def apply(self, price):
        return price 

class PercentDiscount(DiscountStrategy):
    def __init__(self, percent):
        self.percent = percent
    
    def apply(self, price):
        return price * (1 - self.percent / 100)

class FixedDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount
    
    def apply(self, price):
        return (price - self.amount)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.discount_strategy = NoDiscount() 
    
    def set_discount(self, strategy):
        self.discount_strategy = strategy
    
    def get_final_price(self):
        return self.discount_strategy.apply(self.price)

product = Product("Ноутбук", 50000)

print("Без скидки:", product.get_final_price())

product.set_discount(PercentDiscount(10)) 
print("Со скидкой 10%:", product.get_final_price())

product.set_discount(FixedDiscount(5000)) 
print("Со скидкой 5000 руб:", product.get_final_price())