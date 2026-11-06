# sets
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(f"Length of the list: {len(age)}")
print(f"Length of the set: {len(age_set)}")
print(f"The set is bigger: {len(age_set) > len(age)}")
# Original list contains duplicate ages.
print(f"The list is bigger: {len(age) > len(age_set)}")

# Explain the difference between the following data types: string, list, tuple and set
# String is a collection of characters enclosed in quotes. Individual characters can be accessed using indexing.
# List is a collection of items that are ordered and mutable. Allows duplicate elements.
# Tuple is a collection of items that are ordered and immutable. Allows duplicate elements.
# Set is a collection of unique items that are unordered and mutable. Automatically eliminates duplicate elements.

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
sentence = sentence.rstrip('.')  # Removes '.'
unique_words = set(sentence.split())
print(f"Number of unique words: {len(unique_words)}")
