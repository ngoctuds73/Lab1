class Store:

    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}
        self.items_count = 0

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

    def can_add_item(self, count:int , capacity: int):
        return count < capacity

    def can_remove_item(self, items, item_name: str, amount: int):
        return item_name in items and amount <= items[item_name]

    def from_size(self, name, type, size):
        return self(name, type, size // 2)

    def add_item(self, item):
        if not self.can_add_item(self.items_count, self.capacity):
            return "Not enough capacity in the store"
        self.items_count += 1

        if item not in self.items:
            self.items[item] = 0
        self.items[item] += 1
        return f"{item} added to the store"

    def remove_item(self, item, amount):
        if not self.can_remove_item(self.items, item, amount):
            return f"Cannot remove {amount} {item}"

        self.items_count -= amount
        self.items[item] -= amount
        return f"{amount} {item} removed from the store"

first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)
print(first_store)
print(second_store)
print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))