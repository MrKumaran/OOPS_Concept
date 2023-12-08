import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    @classmethod  # Function using this decorator can be called even before instanced usually used for getting data from
    # other files like csv format in this instance
    def instantiate_from_csv(cls):
        with open("Details.csv", "r") as c:
            reader = csv.DictReader(c)
            items = list(reader)
        for item in items:
            Item(name=item.get('name'), price=int(item.get('price')), quantity=int(item.get('quantity')))

    @staticmethod  # just like function declared outside class but diff is it's declared inside class
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity}\n)"
