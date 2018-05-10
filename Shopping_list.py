import os
from random import*
 

    

class Shopping_lists:
    def __init__(self, shopping_list, item_list, price_list):
        self.shopping_list = shopping_list
        self.item_list = item_list
        self.price_list = price_list
        
       

    def add_list(self, item, quantity, price):
        self.item_list.append{item: quantity}
        self.price_list.append{item: price}


def menu():
    print("""
        Press [v] to view shopping list. 
        Press [n] for new list.
        Press [a] to add item to list. 
        Press [d] to delete an item to list. 
        Press [q] to quit. 
        """)

    option = input('What would you like to do?').lower()

    if option == 'v':
        view_list()
        now_what()
    
    elif option == 'a':
        add_item()

    elif option == 'd':
        delete_item()

    else: 
        sys.exit()


def now_what():
    print("What do you want to do now?")
    print("Press (m) for menu or (q) to quit")
    option = input()
    if option == 'm':
        menu()
    else:
        sys.exit()


def view_list():
    shopping_list = input("Whats your shopping instance list name?")
    print(grocery_list.item_list)           

def add_list(shopping_list):
    option1 = input("You want to enter new list? y/n")
    if option1 == "y":
        #shopping_list = input"Enter name of new_list"
        grocery_list == input"Enter instance"
        instance = Shopping_lists(shopping_list, item_list = {}, price_list = {})
        
    else: 
        shopping_list= input("Enter shopping list name") 
        print(shopping_list)
        grocery_list = input"Enter instance"
        grocery_list = Shopping_lists(shopping_list, item_list = {}, price_list = {})
        while add_more = True:
            item = input("Enter item.")
            quantity = input("Enter Quantity")
            price = input("Enter price")
            grocery_list.add_list(item, quantity, price)
            option = input("Do you want to add more items to list? (y/n)")
            if option == "y":
                add_more = True
            else:
                add_more = False
    what_now()

def delete_item(shopping_list):
    while delete_more = True:
        item = input("Enter item to delete.")
        #quantity = input("Enter Quantity")
        #price = input("Enter price")
        for x in grocery_list.item_list:
            if x = item:
                del grocery_list.item_list['item']
                del grocery_list.price_list['item']
        option = input("Do you want to add more items to list? (y/n)")
        if option == "y":
            add_more = True
        else:
            add_more = False
    what_now()

    
menu()