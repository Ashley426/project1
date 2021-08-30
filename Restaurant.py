#Make a wallet containing $100
wallet = 100
#Make a menu
menu =  ("Choose 1 Salad: $4.00, \n2 for hotdog: $2.00, \n3 for fries: 4.00, \n4 for coke: $2.00\
    \nWhat would you like to order today? ")

#ask user to order from the list

#True can be removed it will cause an infinite loop
while (True):

    choice = input(menu)
#This line can be removed its been accounted for already
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':

        if choice == '1':
            print("You have got salad")
            
            wallet -= 4
            if wallet < 0:
                print("you are out of money")
                break
            print("Your remaing balance is ", wallet)
            print()

        elif choice == '2':
            print("You have got hotdog")
            wallet -= 2
            if wallet < 0:
                print("you are out of money")
                break
            print("Your remaing balance is ", wallet)
            print()

        elif choice == '3':
            print("You have got fries")
            wallet -= 4
            if wallet < 0:
                print("you are out of money")
                break
            print("Your remaing balance is ", wallet)
            print()

        elif choice == '4':
            print("You have got the coke")
            wallet -= 2
            if wallet < 0:
                print("you are out of money")
                break
            print("Your remaing balance is ", wallet) 
            print()  

        elif wallet < 0:
            print("Get out") 
            print()
            break
#Our print() option can be replaced with \n.

    else:
        print("Please select from the menu")
        print()



    









#operation for balance on food
# if user_1 == menu1:
#     print(wallet - menu1)
# if user_1 == menu2: 
#     print(wallet - menu2)
# if user_1 == menu3:
#     print(wallet - menu3)
# if user_1 == menu4:
#     print(wallet - menu4)

#compares food to the prices 
# tuple_1 = ("salad","hotdog", "fries", "coke")
# tuple_2 = (4.00, 2.00, 4.00, 2.00)

# foodMenu = {
#     "salad":4,
#     "hotdog":2,
#     "fries":4,
#     "coke":2,
# }

# #food they want
# menu1 = "Salad"
# menu2 = "hotdog"
# menu3 = "fries"
# menu4 = "coke"




