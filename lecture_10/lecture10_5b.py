import urllib.request
import json
import var_dump as vd

# get internet data
url = 'https://edu.frostbit.fi/api/events/en'
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")

# convert the original raw JSON (text) format => Python data format
data = json.loads(raw_data)

# look at the data now
# vd.var_dump(data)

# [0] => dict(4)
#         ['name'] => str(29) "Miss Blomcreutz's House Tour "
#         ['date'] => str(8) "6.7.2026"
#         ['categories'] => list(4)
#             [0] => str(15) "cultural events"
#             [1] => str(8) "guidance"
#             [2] => str(17) "maritime helsinki"
#             [3] => str(19) "theatre (art forms)"
#         ['address'] => dict(2)
#             ['street_address'] => str(16) "Suomenlinna B 40"
#             ['postal_code'] => str(5) "00190"

# all set, loop through the events
for event in data:
    print(event['name'])

    # get the address info into separate variables
    street_address = event['address']['street_address']
    postal_code = event['address']['postal_code']

    # finally print the address info to the user
    print(f"{postal_code} {street_address}")

    # join the categories into a text and print
    categories = ", ".join(event['categories'])

    # you should notice that one of the events doesn't have
    # any categories => we have to catch that situation!:
    if len(event['categories']) > 0:
        print(f"CATEGORIES: {categories}")
    else:
        print("-- NO CATEGORIES --")

    print()