# Here we have a person dictionary. Feel free to modify it!
#         person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    print(skills[len(skills) // 2])
    print('Python' in skills)

    if skills == ['JavaScript', 'React']:
        print('He is a front end developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(set(skills)):
        print('He is a fullstack developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(set(skills)):
        print('He is a backend developer')
    else:
        print('unknown title')

if person['is_married'] and person['country'] == 'Finland':
    print(
        f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
