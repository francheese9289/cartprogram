def print_shopping_cart(items):
    if items:
        items == sorted(list(items))
        print('Your Cart: ')
        for count, item in enumerate(items, 1):
            print(str(count), "- ", item)
    else:
        print('Your cart is empty.')    


