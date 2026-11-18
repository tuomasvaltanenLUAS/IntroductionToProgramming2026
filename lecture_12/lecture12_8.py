import json

# open our text file (create connection) in READ mode
# get raw JSON data from file (just text)
file_handle = open("cities.json", "r")
content = file_handle.read()
file_handle.close()

# convert the raw JSON => Python data format
# after this you can use the countries-variables
# as a list normally
countries = json.loads(content)

for country in countries:
    print(f"{country['name']} ({country['capital']})")
    print(f"Population: {country['population']}")
    print()