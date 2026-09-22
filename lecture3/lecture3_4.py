from datetime import date, datetime, timedelta

# two timestamps
first = date(2026, 9, 22)
second = date(2026, 12, 31)

# calculate the difference
delta = second - first
days = delta.days

print(f"Days left this year: {days}")

# example 2, we have to create a bill for a customer TODAY
# what is the due date in 3 weeks, (21 days), also coulde be used
# to calculate product warranties etc.
today = datetime.now()
expires = today + timedelta(21)

# format nicely and print
date_text = expires.strftime("%d.%m.%Y")
print(date_text)