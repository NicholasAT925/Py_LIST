Shopping_list = ["Pork", "Chicken", "Fish", "Fruits", "Vegetables"]

for food in Shopping_list:
    print(food)
print("\n")
print(Shopping_list[2])
print(Shopping_list[2][0])
print("\n")
# You can also slice the list like a string
print(Shopping_list[0:3]) # N otice how it produces another list
print(Shopping_list[-1])

Shopping_list.append("Ramen")
print(Shopping_list)