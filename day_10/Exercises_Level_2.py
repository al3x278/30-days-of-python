# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
total = 0
for num in range(101):
    total += num
print(total)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
even_sum = 0
odd_sum = 0
for num in range(101):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
print(even_sum)
print(odd_sum)
