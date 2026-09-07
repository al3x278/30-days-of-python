# Declare your age as integer variable
age = 27

# Declare your height as a float variable
height = 5.4

# Declare a variable that store a complex number
complex_num = 3 + 4j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100
base = float(input("Enter base of the triangle: "))
height = float(input("Enter height of the triangle: "))
area_of_triangle = 0.5 * base * height
print("The area of the triangle is", area_of_triangle)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12
perimeter = float(input("Enter side a of the triangle: ")) + float(input(
    "Enter side b of the triangle: ")) + float(input("Enter side c of the triangle: "))
print("The perimeter of the triangle is", perimeter)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print("The area of the rectangle is", area_of_rectangle)
print("The perimeter of the rectangle is", perimeter_of_rectangle)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter radius of the circle: "))
area_of_circle = 3.14 * radius ** 2
circumference_of_circle = 2 * 3.14 * radius
print("The area of the circle is", area_of_circle)
print("The circumference of the circle is", circumference_of_circle)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
x1 = 0
y1 = 2 * x1 - 2
x2 = 2
y2 = 2 * x2 - 2
slope8 = (y2 - y1) / (x2 - x1)
x_intercept = 1
y_intercept = -2
print("The slope is", slope8)
print("The x-intercept is", x_intercept)
print("The y-intercept is", y_intercept)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
slope9 = (10 - 2) / (6 - 2)
euclidean_distance = ((6 - 2) ** 2 + (10 - 2) ** 2) ** 0.5
print("The slope is", slope9)
print("The Euclidean distance is", euclidean_distance)

# Compare the slopes in tasks 8 and 9.
slope_comparison = slope8 == slope9
print("Are the slopes equal?", slope_comparison)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = -3  # One of the x values where y = 0
y = x**2 + 6*x + 9
print("At x =", x, ", y =", y)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python_length = len('python')
dragon_length = len('dragon')
falsy_comparison = python_length != dragon_length
print("Are the lengths equal?", not falsy_comparison)

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
on_in_python = 'on' in 'python'
on_in_dragon = 'on' in 'dragon'
both_contain_on = on_in_python and on_in_dragon
print("Is 'on' found in both strings?", both_contain_on)

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
jargon_in_sentence = 'jargon' in sentence
print("Is 'jargon' in the sentence?", jargon_in_sentence)

# There is no 'on' in both dragon and python
no_on_in_both = not on_in_python and not on_in_dragon
print("Is there no 'on' in either string?", no_on_in_both)

# Find the length of the text python and convert the value to float and convert it to string
python_length_float = float(python_length)
python_length_string = str(python_length_float)
print("Length of 'python' as float:", python_length_float)
print("Length of 'python' as string:", python_length_string)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
target_number = int(input("Enter a number to check if it's even: "))
divisible_by_2 = target_number // 2 == 2
remainder_is_zero = target_number % 2 == 0
print('Is ', target_number, ' even?', divisible_by_2 and remainder_is_zero)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# Check if type of '10' is equal to type of 10
# Check if int('9.8') is equal to 10
# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
