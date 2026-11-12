# Write a code which gives grade to students according to theirs scores:
# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# ```
student_score = int(input("Enter your score: "))
if student_score >= 90 and student_score <= 100:
    print("A")
elif student_score >= 80:
    print("B")
elif student_score >= 70:
    print("C")
elif student_score >= 60:
    print("D")
elif student_score >= 0:
    print("F")
else:
    print("Invalid score")

# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
user_month = input("Enter a month: ").strip().title()
if user_month in ("September", "October", "November"):
    print("Autumn")
elif user_month in ("December", "January", "February"):
    print("Winter")
elif user_month in ("March", "April", "May"):
    print("Spring")
elif user_month in ("June", "July", "August"):
    print("Summer")
else:
    print("Invalid month")

# The following list contains some fruits:
# ```sh
# fruits = ['banana', 'orange', 'mango', 'lemon']
# ```

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruit = input("Enter a fruit: ").strip().lower()
if user_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(user_fruit)
    print(fruits)
