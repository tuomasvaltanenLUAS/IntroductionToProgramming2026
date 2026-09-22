# this is why it's a bit more sensible to use
# a specific import, because if we use the normal import:
# import datetime
# we would have to use it like this:
# today = datetime.datetime.now()
from datetime import datetime

# get current time and date
today = datetime.now()
print(today)