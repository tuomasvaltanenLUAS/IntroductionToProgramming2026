# open our text file (create connection) in READ mode
file_handle = open("weekdays.txt", "r")

# read the contents into a variable
content = file_handle.read()

# let's close the file connection (good practice)
file_handle.close()

# just a normal variable now, print it out
print(content)