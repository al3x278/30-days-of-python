# sets
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Join A and B
A_and_B = A | B

# Find A intersection B
A_intersection_B = A & B

# Is A subset of B
print('Is A a subset of B? ' + str(A.issubset(B)))

# Are A and B disjoint sets
print('Are A and B disjoint sets? ' + str(A.isdisjoint(B)))

# Join A with B and B with A
A_join_B = A | B
B_join_A = B | A

# What is the symmetric difference between A and B
symmetric_difference = A.symmetric_difference(B)

# Delete the sets completely
del A
del B
