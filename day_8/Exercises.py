# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {
    "name": "Max",
    "color": "brown",
    "breed": "Labrador",
    "legs": 4,
    "age": 3
}

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Alex",
    "last_name": "Lee",
    "gender": "male",
    "age": 27,
    "marital_status": "single",
    "skills": ["Python", "Java"],
    "country": "USA",
    "city": "Seattle",
    "address": "Street 8"
}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student["skills"])
print(type(student["skills"]))

# Modify the skills values by adding one or two skills
student["skills"].extend(["SQL", "Git"])

# Get the dictionary keys as a list
print(list(student.keys()))

# Get the dictionary values as a list
print(list(student.values()))

# Change the dictionary to a list of tuples using items() method
print(list(student.items()))

# Delete one of the items in the dictionary
del student["marital_status"]

# Delete one of the dictionaries
del dog
