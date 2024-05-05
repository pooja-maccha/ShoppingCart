from typing import List


class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        self.items: List[str] = []
        self.max_size = max_size

    def add(self, item: str):
        if self.size() == self.max_size:
            raise OverflowError("cannot add more items")
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self, price_map):
        total_price = 0
        for item in self.items:
            total_price += price_map.get(item)
        return total_price

    def remove_item(self, item: str):
        if item in self.items:
            self.items.remove(item)
        else:
            raise ValueError(f"{item} not found in the cart.")

    def clear_cart(self):
        self.items.clear()

    def check_item_in_cart(self, item: str):
        if item in self.items:
            raise ValueError("{item} already in cart.")
        else:
            self.add(item)