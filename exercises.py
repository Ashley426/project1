# # You have one coin
print("You have one coin")

# Adding another coin



coin = 1

while(coin < 4):

    answer = input("Would you like another coin? ")

    if answer == "yes":
        coin += 1
        print("You have %d coins" % coin)
        if coin == 4:
            print("Thanks")

    elif answer == "no":
        print("Thanks for the bargain")
        break


# donuts_consumed = 0
# while (donuts_consumed < 4):
#     print("You have eaten %d donuts." % donuts_consumed)
#     donuts_consumed = donuts_consumed + 1