# Exercise 3

# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

import math

print("Integer: 5")
print("Float: 5.6")
print("Complex: 5 + 1j")
print("String: 'Coding is fun'")
print("Boolean: True")
print("List: [2,4,6,8]")
print("Tuple: (2,4,6,8)")
print("Set: {2,4,6,10}")
print("Dictionary: {'name': 'Alex', 'age': 25, 'country': 'United States'}")

# Find an Euclidean distance between (2, 3) and (10, 8)

point1 = (2, 3)
point2 = (10, 8)
dist = (point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2
distance = math.sqrt(dist)
print("Euclidean distance:", distance)
