# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'
challenge = str1 + ' ' + str2 + ' ' + str3 + ' ' + str4
print(challenge)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
word_1 = 'Coding'
word_2 = 'For'
word_3 = 'All'
challenge2 = word_1 + ' ' + word_2 + ' ' + word_3
print(challenge2)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# Print the variable company using print().
company = 'Coding For All'
print(company)

# Print the length of the company string using len() method and print().
company = 'Coding For All'
print(len(company))

# Change all the characters to uppercase letters using upper() method.
company = 'Coding For All'
company_upper = company.upper()
print(company_upper)

# Change all the characters to lowercase letters using lower() method.
company = 'Coding For All'
company_lower = company.lower()
print(company_lower)

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
string = 'Coding For All'
string_capitalized = string.capitalize()
string_titled = string.title()
string_swapped = string.swapcase()
print("Capitalized:", string_capitalized)
print("Titled:", string_titled)
print("Swapped case:", string_swapped)

# Cut(slice) out the first word of Coding For All string.
string = 'Coding For All'
first_word = string[0:6]
print("First word: {}".format(first_word))

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
string = 'Coding For All'
print(string.find('Coding') != -1)  # True

# Replace the word coding in the string 'Coding For All' to Python.
string = 'Coding For All'
print(string.replace('Coding', 'Python'))  # 'Python For All'

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
string = "Python for Everyone"
print(string.replace("Everyone", "All"))

# Split the string 'Coding For All' using space as the separator (split()) .
string = 'Coding For All'
print(string.split())  # ['Coding', 'For', 'All']

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(string.split(', '))

# What is the character at index 0 in the string Coding For All.
string = 'Coding For All'
print(string[0])  # 'C'

# What is the last index of the string Coding For All.
string = 'Coding For All'
print(len(string) - 1)  # 13

# What character is at index 10 in "Coding For All" string.
string = 'Coding For All'
print(string[10])  # ' '

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
string = 'Python For Everyone'
words = string.split()
print(words[0][0] + words[1][0] + words[2][0])  # 'PFE'

# Create an acronym or an abbreviation for the name 'Coding For All'.
string = 'Coding For All'
words = string.split()
print(words[0][0] + words[1][0] + words[2][0])  # 'CFA'

# Use index to determine the position of the first occurrence of C in Coding For All.
string = 'Coding For All'
print(string.find('C'))  # 0

# Use index to determine the position of the first occurrence of F in Coding For All.
string = 'Coding For All'
print(string.index('F'))  # 7

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
string = 'Coding For All'
print(string.rfind('l'))  # 13

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.find('because'))  # 31

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.rindex('because'))  # 47

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
first_occurrence = string.find('because')
last_occurrence = string.rindex('because') + len('because')
sliced_phrase = string[first_occurrence:last_occurrence]
print(sliced_phrase)  # because because because

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.find('because'))  # 31

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
first_occurrence = string.find('because')
last_occurrence = string.rindex('because') + len('because')
sliced_phrase = string[first_occurrence:last_occurrence]
print(sliced_phrase)  # because because because

# Does 'Coding For All' start with a substring Coding?
print('Coding For All'.startswith('Coding'))  # True

# Does 'Coding For All' end with a substring coding?
print('Coding For All'.endswith('coding'))  # False

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
string = '   Coding For All      '
print(string.strip())  # 'Coding For All'

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
