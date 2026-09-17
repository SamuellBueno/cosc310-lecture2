"""Exercise 3: Enforce a business rule.

Extend your Cart so invalid operations are rejected by the CART.

  ValueError        when qty < 1
  OutOfStockError   when the item's "available" field is False
  KeyError          when removing an item that is not in the cart

Then demonstrate each one with try/except.
"""

from exercise1 import load_menu


class OutOfStockError(Exception):
    """Raised when a customer tries to order an item that is unavailable."""
    pass


class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []

    def add_item(self, item: dict, qty: int = 1) -> None:
        # TODO: validate FIRST, then mutate.
        #   if qty < 1:                 raise ValueError(...)
        #   if not item["available"]:   raise OutOfStockError(...)
        if qty<1:
            raise ValueError("cant add 0 or negative bro")
        if item["available"] == False:
            raise OutOfStockError("sorry we ran out of that")
        for i in self.lines: 
            if item["id"] == i["item_id"]:
                i["qty"] = i["qty"] + qty
                return 
        self.lines.append({
            "item_id": item["id"],
            "name": item["name"],
            "price": item["price"],
            "qty": qty,
        })
        return
        

    def remove_item(self, item_id: int) -> None:
        # TODO: raise KeyError if the item is not in the cart
        for i in self.lines: 
            if item_id == i["item_id"]:
                if i["qty"]==1:
                    self.lines.remove[i]
                    return
                i["qty"] = i["qty"] - 1
                return
        raise KeyError("item was never in the cart bro")

    def total(self) -> float:
        return round(sum(line["price"] * line["qty"] for line in self.lines), 2)

    def __repr__(self) -> str:
        return f"<Cart {len(self.lines)} items, ${self.total():.2f}>"


if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]           # available
    miso = menu[3]            # NOT available

    cart = Cart()

    # TODO: demonstrate each rejection with try/except and a readable message.
    # Example:
    try:
         cart.add_item(gyoza, 0)
    except Exception as e:
         print(f"Rejected: {e}")
    try:
         cart.add_item(gyoza, -10000)
    except Exception as e:
         print(f"Rejected: {e}")
    try:
         cart.add_item(miso, 1)
    except Exception as e:
         print(f"Rejected: {e}")
    try:
         cart.remove_item(miso)
    except Exception as e:
         print(f"Rejected: {e}")
   

