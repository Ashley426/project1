#get the total of the bill from the restaurant
print("Hello, I can help you calculate a tip based on your service!")

#the user types the amount of the bill
total_bill = float(input("What is the total on your bill? "))

#Depending on the service was good or bad the tip is lesser

# Ratings on your service good or bad?")
service = input("Was your service good, fair or bad? ")

#if the service is bad the will get a 5% tip if the service is good they get a 20% tip
if service == "good":
    tip = total_bill * 0.20
    gross_total = total_bill + tip
    print('Total bill amount: %.2f'  %total_bill)
    print(f'Level of service? good')
    print('Tip amount: %.2f' %tip)
    print('Total amount: %.2f' %gross_total)

elif service == "fair":
    tip = total_bill * 0.15
    gross_total = total_bill + tip
    print('Total bill amount: %.2f'  %total_bill)
    print(f'Level of service? fair')
    print('Tip amount: %.2f' %tip)
    print('Total amount: %.2f' %gross_total)

elif service == "bad":
    tip = total_bill * 0.10
    gross_total = total_bill + tip
    print('Total bill amount: %.2f'  %total_bill)
    print(f'Level of service? bad')
    print('Tip amount: %.2f' %tip)
    print('Total amount: %.2f' %gross_total)


else:
    print("IDIOT choose good, bad or fair!")
        