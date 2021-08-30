# #Create a list with 5 values and assign it to
# #a variable for later use

my_colors = ["purple", "red", "blue", "green", "black"]

# for colors in my_colors:
#     if colors == "red":
#         print(colors)
    

# #Change the value of the item in the middle of 
# # the list to a tuple

my_colors[2] = tuple(("blue"))
print(my_colors)

# #Create a range of integers up to the number 7
# #  and add it to a variable for later use

my_count = range(8)
print(my_count)

# #Add the range of integers you just created to 
# # the end of the initial list you created

my_colors.append(my_count)
print(my_count)



#Display the middle value in the list

print(my_colors[2])

#Display the last value in the list
print(my_colors[-1])