# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

from day_10 import countries, countries_data

for country in countries:
    if 'land' in country.lower():
        print(country)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
for fruit in reversed(fruits):
    print(fruit)

# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
languages = set()
for country in countries_data:
    languages.update(country['languages'])
print(f'Total number of languages: {len(languages)}')

# Find the ten most spoken languages from the data
language_counts = {}
for country in countries_data:
    for language in country['languages']:
        language_counts[language] = language_counts.get(language, 0) + 1

most_spoken_languages = sorted(
    language_counts.items(), key=lambda item: item[1], reverse=True
)[:10]
for language, count in most_spoken_languages:
    print(f'{language}: {count}')

# Find the 10 most populated countries in the world
most_populated_countries = sorted(
    countries_data, key=lambda country: country['population'], reverse=True
)[:10]
for country in most_populated_countries:
    print(f"{country['name']}: {country['population']:,}")
