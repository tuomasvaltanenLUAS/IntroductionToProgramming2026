# the logic is this:
# Bad weather: if temperature is less than +10C
# Bad weather: if humidity is over 80%
# Bad weather: if wind speed is over 2.5 m/s
# Bad weather: if it's dark outside
# In this case, we can assume it's dark outside
# if time is between 20-24 or 0-7

# initialize variables
temperature = 5
humidity = 65
wind_speed = 1.5
hour = 10

# helper variables
sun_down = 20
sun_rises = 7

# initialize the main boolean
good_weather = True

# if temperature < 10 or humidity > 80 or wind_speed > 2.5 or (hour > sun_....)
# this gets pretty complex easily, DOES THIS EVEN WORK?

if temperature < 10:
    good_weather = False

if humidity > 80:
    good_weather = False

if wind_speed > 2.5:
    good_weather = False

# the most difficult condition: time regarding dark
if hour > sun_down or hour < sun_rises:
    good_weather = False


if good_weather:
    print("Good weather outside!")
else:
    print("Bad weather...")