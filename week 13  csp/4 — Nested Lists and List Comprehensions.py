

list1 = [1, 2, 3]
list2 = [4, 5, 6]
nested_list = [list1, list2]
print(nested_list[0])
print(nested_list [1] [0])

fruits = ["apple", 'orange', 'bananas', 'coconut']
vegetables = ['celery', 'carrrots', 'potatoes']
meats = ['chicken', 'fish', 'turkey']

groceries = [fruits, vegetables, meats]

for collection in groceries: 
    for food in collection: 
        print(food, end= '')

    
# for i in range(1,1001):
#     for j in range(1,1001):
#         if i > 0 and j > 0:
#             for k in range(1,1001):
#                 print('the number is ', i, j, k)
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ( -, 0, >),) 



for row in num_pad:
    for num in row: 
        print(num, end='')
    print()



# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[1][2])    # 6

# # List comprehension
# first_col = [row[0] for row in matrix]
# print(first_col)       # [1, 4, 7]



# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.
matrix = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
 ]

# Print the first list.
print(matrix[0])
# Print the second item from the third list.
sum_list = [row[-1] for row in matrix]
print(sum_list)
# Use a list comprehension to extract the last item from each sub-list.
squares = [x**2 for x in range(1,11)]
print(squares)
# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.