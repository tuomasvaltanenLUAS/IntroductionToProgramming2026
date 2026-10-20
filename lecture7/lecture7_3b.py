# sometimes you need a range with year values
# e.g. 2018 - 2026

# with ranges, it's often a better idea
# to save the boundaries into helper variables
start = 2018
end = 2026

# you can define start and end of the range
# often used with year ranges, but otherwise
# surprisingly rarely used

# you can also use a third parameter (step size)
# that allows you to skip numbers in the for-loop
# in this case: print every other number only
for year in range(start, end, 2):
    print(year)