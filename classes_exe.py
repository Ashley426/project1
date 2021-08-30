# '''what they are and why they're  '''


# class Pizza:
#     def __init_(self, size, crust="thin", sauce="tomato"):
#         self.size = size
#         self.crust = crust
#         self.sauce = sauce

# troys_pizza = Pizza("large", "thin", "marinara")
# armonis_pizza = Pizza()
# print(armonis_pizza.sauce)

# Exercise 
'''Based off of what you see under vehicles on toyota.com
create a class and several instances of it'''

# class suvs_crossovers:
#     def __init__(self, color="Red", seats=5, backupcamera="Integrated backup camera",
#      mpg=40, roof="Panoramic roof"):
#         self.color = color
#         self.seats = seats
#         self.backupcamera= backupcamera
#         self.mpg=mpg
#         self.roof= roof

# # new_car = suvs_crossovers("Blue", 8, "No camera", 39, "no roof")
# new_car= suvs_crossovers()
# print(new_car.color)

# class Car:
#     def __init__(self, make, model, color, current_speed = 0):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.current_speed = current_speed

#     def increase_speed(self, speed_increase):
#         self.current_speed += speed_increase

#     def decrease_speed(self, speed_decrease):
#         self.current_speed -= speed_decrease

# troys_car = Car("toyota", "corolla", "red")

# troys_car.increase_speed(20)
# troys_car.decrease_speed(10)
# print(troys_car.current_speed)

class order:
    def __init__(self, is_delivery, customer={}, items=[], total_price=0, fulfilled= False):
        self.is_delivery = is_delivery
        self.customer = customer
        self.items = items
        self.total_price = total_price
        self.fulfilled = fulfilled

    def add_customer_name(self, name):
        self.customer["name"] = name

    def add_items(self, item):
        self.items.append(item)

    def get_total_price(self):
        index = 0
        total = 0
        while index is < len(self.item):
        self.total_price += self.items[index]["price"]
        index += 1

        new_order = order(True)
        new_order.add_customer_name("troy")
        new_order.add_item({
        "name": "Pizza", 
        "price": 10
    })
        print(new_order.customer)
        print(new_order.items)

