# Unpack siblings and parents from family_members
brothers = ('Greg', 'Mike', 'John')
sisters = ('Sarah', 'Emily', 'Lisa')
siblings = brothers + sisters
family_members = siblings + ('John', 'Mary')
siblings = family_members[0:6]
parents = family_members[6:8]

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'eggs', 'meat')
food_stuff_tp = fruits + vegetables + animal_products

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_lt) // 2
middle_items = food_stuff_lt[middle_index:middle_index + 1]

# Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country

# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
