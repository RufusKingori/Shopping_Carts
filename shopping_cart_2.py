#store = {product:[quantity,price]}
store = dict(orange=[150,30],banana=[200,20])
#products is a list of items. An item is a tupple tupe that includes quantity and price
def add_product(*products):
    for i in products:
        product_name = i[0]
        price = i[2]
        quantity = i[1]
        #if this product is already existing in store, we update the quantity and it's price
        if product_name in store:
            store[product_name][0] += quantity
            store[product_name][1] = price
        else: #create a new item in store
            store[product_name] = [quantity,price]


#products is a list of items. An item is a tupple type that includes product name and quantity
def remove_product(*products):
    for i in products:
        product_name = i[0]
        quantity = i[1]
        #if this product is already existing in store, we remove quantity
        if product_name in store:
            if store[product_name][0] >= quantity:
                store[product_name][0] -= quantity
            elif store[product_name][0] <= quantity: #remove it from the store
                del store[product_name]

# products is a list of items.
def calc_bill(*products):
    sum = 0
    for i in products:
        product_name = i[0]
        quantity = i[1]
        # if this product is already existing in store, we calculate the quantity * price
        if product_name in store:
            if store[product_name][0] >= quantity:
                sum += store[product_name][1] * quantity
                store[product_name][0] -= quantity
            elif store[product_name][0] <= 0:  # remove it from the store
                del store[product_name]
    return sum
def show_store():
    #this function show all products to screen
    for i in store:
        print(i,"quantity=",store[i][0],"price =",store[i][1])


#main program

add_product(("coconut",170,40),("plum",120,15))
add_product(("tomato",300,10))
show_store()

remove_product(("plum",30),("coconut",34))
print("after delete:")
show_store()

bill = calc_bill(("plum",3),("tomato",5))
print("you have to pay:",bill)
