def fill_cart():
    from printcart import print_shopping_cart as psc
    shopping_cart = []
    print ('Welcome to the store!Let\'s fill your cart!')
    print ("To access your cart select: 'a' to add an item,'d' to delete an item, 's' to show or review your cart")
    print ("'c' to clear the cart and start over, or 'q' to quit shopping. ")
    while True:
        action = input ('What would you like to do? Add (a), Delete (d), Show (s), Clear(c) or Quit (q)? ')
        if action == 'a':
            item = input('Add item: ')
            shopping_cart.append(item)
            psc(shopping_cart)
        elif action == 'd':
            item = input('Which item would you like to delete? ')
            shopping_cart.remove(item)
            psc(shopping_cart)
            continue
        elif action == 's':
            psc (shopping_cart)
            continue
        elif action == 'c':
            shopping_cart.clear()
            psc (shopping_cart)
            continue
        elif action == 'q':
            break
    return shopping_cart

fill_cart()


    