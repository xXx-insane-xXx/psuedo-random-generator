import math
import time

# Array to store values between x and y with increment of 0.1
num = []


# User input for x and y
x = float(input("Enter start value : "))
y = float(input("Enter end value : "))


# Iterator
i = x


# Appending values between x and y
# Eg : x=1 and y=10 ==> num -> [1.0, 1.1, 1.2, .... , 5.1, 5.2, .... , 10.0]
while (i < y):
    num.append(round(i, 2))
    i += 0.1

##############################
##### Random index logic #####
##############################

# Get current time in ms
current_time_ms = time.time()

# Get remainder of current_time_ms
fractional_part = current_time_ms % 1

# Random index logic
random_index = fractional_part * len(num)
random_index = int(random_index)

# If random_index exceeds length of the list (not sure why it would)
if random_index >= len(num):
    random_index -= 1

##############################
##############################
##############################


# Select random value fromt the list and display
select_random_value = num[random_index]
print(f"Random value : {select_random_value}");


