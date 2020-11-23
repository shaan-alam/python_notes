import time
# Type conversions in Python

# float value
value = 5.6

# Type Conversions are done here
print (int(value))


# Rounding number
print (round(value))


# Displaying current time

currentTime = time.time()

# obtain the total seconds 
totalSeconds = int (currentTime)

# Get the current second
currentSecond = totalSeconds % 60

# Obtain the total minutes
totalMinutes = totalSeconds // 60

# Compute the current minute in hour
currentMinute = totalMinutes % 60

# obtain the total hours
totalHours = totalMinutes // 60

# compute the current hour
currentHour = totalHours % 24


# Display the result
print ("Current time = " , currentHour , ":", currentMinute, ":", currentSecond, "GMT")


