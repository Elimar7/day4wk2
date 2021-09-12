shopping_list = []
while True:
    user_input = input("Would you like to: Show/Add/Del/Clear or Cancel?")
    if user_input == "Show".lower():
        print(shopping_list)
    elif user_input ==  "Add".lower():
        user_add = input("Which product would you like to add to your shopping cart?")
        print(f"Adding {user_add.title()} to shopping list.")
        shopping_list.append(user_add)
    elif user_input == "Del".lower():
        user_del = input("What product would you like to disgard?")
        print(f"Disgarding {user_del.title()} from shopping cart?")
        shopping_list.remove(user_del)
    elif user_input == "Clear".lower():
        user_clear = input("Are you sure you would like to clear your cart?(Y/N)")
        if user_clear == "Yes".lower():
            print(f"Your shopping cart has been emptied.")
            shopping_list.clear
    else:
        user_input == "quit".lower():
        
        