cart_items = []
cart_total = 0
def add_item(item_name,item_price):
    cart_items.append(item_name)
    return (item_price)
cart_total += add_item("apple",0.5)
cart_total += add_item("apple",0.5)
cart_total += add_item("orange",4.5)
cart_total += add_item("mango",6.5)
cart_total += add_item("apple",0.5)
cart_total += add_item("mango",6.5)
cart_total += add_item("mango",6.5)
cart_total += add_item("mango",6.5)

cart_summary = dict((item,cart_items.count(item))for item in cart_items)
print(cart_summary)
print(cart_total)
