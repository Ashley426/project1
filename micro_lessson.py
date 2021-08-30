# #lists are zero-based and mutable (we cn change values)
# #if from left to right it will be negative position
# #How to create them and access values
#   #             0       1       2        3          4           5                
# groceries = ["milk", "eggs", "bread", "salmon", "Burgers", "rebel ice cream"]
#          #     -6         -5          -4        -3          -2             -1               
# print(groceries[1])
# print(groceries[2])
# print(groceries[-3])

# #to add to item to lists use append() fucntion 
# groceries.append("bacon")
# print(groceries)

# # .pop removes the last option from the list 
# # if position is not included
# groceries.pop(1)
# print(groceries)

# # .remove is to remover given item
# groceries.remove("salmon")
# print(groceries)
# fruit = ["apples," "oranges", "mangos"]
# for fruit in ['apples, oranges, mangos']:
#     print("I like",fruit)

#sequences
list_of_numbers = [123, 456]

list_of_numbers[0] = "abc"
print(list_of_numbers)

# #TUPLE are immutable(we cannot change value)has parenthesis
# coordinates = (12345.12345, 67890.67890)
# print(coordinates[0])

# #RANGE creates a sequence of values
# this_is_a_range_of_number = range(10)
# print(this_is_a_range_of_number)

#practice range
lovers_friends = range(20)
print(lovers_friends)