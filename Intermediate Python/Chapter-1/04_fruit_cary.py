# Set Defining

my_fruits = {'Mango', 'Orange', 'Kiwi', 'Orange'}

friend_fruits = {'Lichi', 'Apple', 'Orange', 'Peach'}

# Fruit is <in> both sets or not

print('apple' in friend_fruits)

set3 = {'Apple', 'Orange'}

print(set3.issubset(my_fruits))

# Methods of Sets

union_fruits = my_fruits.union(friend_fruits)

intersection_fruits = my_fruits.intersection(friend_fruits)

difference_fruits = my_fruits.difference(friend_fruits)




# Printing of Sets

print('Union Fruits: ', union_fruits)

print('Intersection Fruits: ', intersection_fruits)

print('Difference Fruits: ', difference_fruits)