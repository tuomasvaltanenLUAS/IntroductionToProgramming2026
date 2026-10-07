# the logic of the weather is this:

# Bad weather: if temperature is less than +10C
# Bad weather: if humidity is over 80%
# Bad weather: if wind speed is over 2.5 m/s
# Bad weather: if it's dark outside
# In this case, we can assume it's dark outside
# if time (hour) is between 20-24 or 0-7

# initialize variables
temperature = 5
humidity = 65
wind_speed = 1.5
hour = 10

# helper variables
sun_down = 20
sun_rises = 7

# initialize the main boolean, this only keeps track of the weather
# => is it good or bad
# we assume in the beginning the weather is good, and try to prove
# it wrong with subsequent if-statements
good_weather = True

# let's try to formulate this condition somehow
# if you start to have a condition like this, CONSIDER A HELPER BOOLEAN VARIABLE
# to make the logic easier and manageable

# this gets pretty complex easily, DOES THIS EVEN WORK?
# if temperature < 10 or humidity > 80 or wind_speed > 2.5 or (time > sun_down ...)

# if temperature less than 10 (check)
if temperature < 10:
    good_weather = False

# if humidity over 80% (check)
if humidity > 80:
    good_weather = False

# if wind_speed over 2.5 (check)
if wind_speed > 2.5:
    good_weather = False

# the most difficult condition: time regarding dark
if hour > sun_down or hour < sun_rises:
    good_weather = False

# ALL CHECKS DONE, we can now use our boolean to decide the outcome
if good_weather:
    print("Good weather outside!")
else:
    print("Bad weather...")