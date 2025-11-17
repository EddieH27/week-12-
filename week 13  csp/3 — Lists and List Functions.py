# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# collections are used to store multiple items in a single variable
# lists are ordeed collections of items
# lists are mutable, meaning you can change their content
# lists are created using square brackets []

list_of_fruits = ['apple', 'banana', 'cherry', 'date']
print(list_of_fruits)
print(type(list_of_fruits))
print(list_of_fruits[0])
print(list_of_fruits[1])
print(list_of_fruits[-1])
print(list_of_fruits[1:3])
list_of_fruits.reverse()
print(list_of_fruits)
print(list_of_fruits[::-1])
list_of_fruits.append('Mango')
list_of_fruits.append('blueberry')
print(list_of_fruits)
popped_item = list_of_fruits.pop()
print(popped_item)
print(list_of_fruits)
list_of_fruits.insert(1, 'orange')
print(list_of_fruits)
list_of_fruits.remove('banana')
list_of_fruits.insert(3, 'peach')
list_of_fruits.sort()
print(list_of_fruits)
# list_of_items = list(range(1, 1001))
# print(list_of_items)
# print(len(list_of_items))

# instead of creating separate variables for each item, we can store them in a list which makes managing the code easier, and also makes the complexity easier to follow with multiple items in the code.
# Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.
list_of_foods = ['pizza', 'tacos', 'hot dog', 'cheeseburger', 'tamales']
# Print the second and last item.
print(list_of_foods[-1])
print(list_of_foods[-2])

# Add a new item using .append().
list_of_foods.append('pozole')
print(list_of_foods)
# Remove the first item using .pop(0).
list_of_foods.pop(0)

# Reverse your list using .reverse().
list_of_foods.reverse()
print(list_of_foods)
# Create a list of 3 lists (matrix), and access the middle element.\
