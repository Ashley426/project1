"""
    Create a program with a Restaurant class that handles all of the 
    following dynamically:
    >   Can CRUD (create, read, update, delete) the following
        :: a menu
        :: a customer
        :: an order
    >   Should ask for info from customer to do everything, 
    no static / manually entered info
    
    >   MENU
        :: should have items
        :: those items should have names and prices
        :: items should be able to be added to the menu
        :: items should be able to be removed from the menu
        :: item prices should be able to be changed
    >   CUSTOMERS
        :: should have a name
        :: should have contact info like phone or email
        :: should have available funds so that we know if they can afford their order
    >   ORDER
        :: should have a name
        :: should have items
        :: should have a status like fulfilled, delivered, or something like that
        :: should be able to checkout or complete order based on customer info
"""
user_menu = {"Vegan Wrap: 13.99", "Roasted Califlower: 12.99",
"spicy eggplant: 22.99", "Vegan Alfredo: 24.99", 
"Butternut Squash: 22.99", "Quinoa: 14.99", "Veggie burger: 19.99",
"Sweet Potato fries: 12.99", "Cucmber salad: 12.99", "Organic Juice: 8.99"
   "What would you like to order today?"}

print(user_menu)



