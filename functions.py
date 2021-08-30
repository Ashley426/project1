"""
What is a function and why we would want to use them
how to create a function
parameters
arguments
scope
recursion
"""

# #define give it a name():
# def say_what_i_say(words_to_say):
#     #code block
#     print(words_to_say)
# say_what_i_say("whooty whoo")
# say_what_i_say("bye felicia")

# create a function that takes one parameter
# the argument should be an integer
# the function should display the argument plus 10

# def number_three(add_number):
#     print(add_number)
# number_three(20 + 10)
# def add(x, y):
#     print(x + y)

# add(5, 3)

def place_order(items):
    count = 0

    while count < len(items):
        print(items[count])
        count += 1
my_order = ["salmon", "chips", "spinach"]

count = 25
print (count)

place_order(my_order)
#Assignment #1
#Create a function that takes two values
#that's equivalent to the two values multiplied by one another

#Add a condition bases on the value that 
# displays higher than 10 or less than 10

#Call the function you create

#Then try to display the variable you created within the function

# def one_number(add_number):
#     print(add_number)
#     if add_number > 10:
#         print("You got mail")
#     else
#         print('You have no mail')

#Part 2
def say_hello(name):
    if name == "Ash":
        print("hey")
    else:
        print("bye)")




 