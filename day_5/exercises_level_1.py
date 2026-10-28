# Declare an empty list
empty_list = []
# Declare a list with more than 5 items
items_list = ['ball', 1, 3.14, True, 'pie', 'banana']
# Find the length of your list
length = len(items_list)
# Get the first item, the middle item and the last item of the list
first_item = items_list[0]
middle_item = items_list[length // 2]
last_item = items_list[length - 1]
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Alex Lee', 27, 5.4, 'Single', '123 Main St']
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']
# Print the list using print()
print(it_companies)
# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
print('first: ' + it_companies[0] + ', middle: ' +
      it_companies[len(it_companies) // 2] + ', last: ' + it_companies[-1])
# Print the list after modifying one of the companies
it_companies[6] = 'Meta'
print(it_companies)
# Add an IT company to it_companies
it_companies.append('Tesla')
# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, 'SpaceX')
# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = it_companies[3].upper()
# Join the it_companies with a string '#;  '
it_companies_str = '#;  '.join(it_companies)
# Check if a certain company exists in the it_companies list.
it_companies_exists = 'Google' in it_companies
# Sort the list using sort() method
it_companies.sort()
# Reverse the list in descending order using reverse() method
it_companies.reverse()
# Slice out the first 3 companies from the list

# Slice out the last 3 companies from the list

# Slice out the middle IT company or companies from the list

# Remove the first IT company from the list

# Remove the middle IT company or companies from the list

# Remove the last IT company from the list

# Remove all IT companies from the list

# Destroy the IT companies list

# Join the following lists:

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
