cart = []

while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Show Cart")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        if len(cart) == 0:
            print("Cart is empty")
        else:
            print("Items in cart:")
            for item in cart:
                print("-", item)

    elif choice == "2":
        item = input("Enter item name: ")
        cart.append(item)
        print(item, "added to cart")

    elif choice == "3":
        item = input("Enter item to update: ")

        if item in cart:
            new_item = input("Enter new item name: ")
            index = cart.index(item)
            cart[index] = new_item
            print("Item updated")
        else:
            print("Item not found")

    elif choice == "4":
        item = input("Enter item to remove: ")

        if item in cart:
            cart.remove(item)
            print("Item removed")
        else:
            print("Item not found")

    elif choice == "5":
        print("Exiting program")
        break

    else:
        print("Invalid choice")