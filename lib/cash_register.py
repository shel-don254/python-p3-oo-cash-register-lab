#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total=0, items=None):
        self.discount = discount
        self.total = total
        self.items = items if items is not None else []

    def add_item(self, title, price, quantity=1):
        self.title = title
        self.price = price
        self.quantity = quantity

        self.total += self.price * quantity

        self.items.extend([title] * quantity)

        self.last_item_price = self.price * quantity
        
    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.price * (self.discount/100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_item_price            

    def reset_register_totals(self):
        self.items.clear()
        self.total = 0.0
        
          

new_register = CashRegister()
new_register.add_item("eggs", 100)
new_register.add_item("tomato", 200)
new_register.add_item("eggs", 100, 2)
new_register.add_item("tomato", 200, 3)
new_register.add_item("eggs", 100)
print(new_register.items)  # ['eggs', 'tomato', 'eggs', 'eggs', 'tomato', 'tomato', 'tomato', 'eggs']
print(new_register.total) # 1200
new_register.void_last_transaction()
print(new_register.total) # 1100
new_register.reset_register_totals()
print(new_register.items) # []
print(new_register.total) # 0.0