# Setting and Swapping

myNumber = 42
myName = "Sue"
x = myNumber
myNumber = myName
myName = x
print(myName)
print(myNumber)
# *************************************************
# Print -52 to 1066

x = range(-52, 1066)
for i in x:
    print(i)
# *************************************************
# Multiples of Three – but Not All

x = range(-300, 0, 3)
skipNum = [-3, -6]
for i in x:
    if i == skipNum[0] or i == skipNum[1]:
        continue
    else:
        print(i)
# *************************************************
# Printing Integers with While

x = 2000
while x < 5281:
    print(x)
    x += 1
# *************************************************
# You Say It’s Your Birthday

birthMn = 8
birthDay = 4

date = [3, 9]

if date[0] == birthMn and date[1] == birthDay:
    print("How did you know?")
else:
    print("Just another day....")
# *************************************************
# Leap Year

year = 2022

if year % 4 == 0:
    print("It is a leap year!")
elif year % 400 == 0:
    print("It is a leap year!")
elif year % 100 == 0:
    print("It's not a leap year.")
else:
    print("It's not a leap year.")
# *************************************************
# Print and Count

nums = []
for x in range(512, 4096, 5):
    nums.append(x)
    print(x)
count = len(nums)
print(count)
# *************************************************

# Multiples of Six
x = 0
while x <= 60000:
    print(x)
    x += 6
# *************************************************
# Counting, the Dojo Way

for x in range(0, 100):
    if x % 10 == 0:
        print("Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

# What Do You Know?
name = input("Enter name: ")

print("My name is {}".format(name))
# *************************************************
# Whoa, That Sucker’s Huge…


def add():
    sum = 0
    for x in range(-290000, 300000):
        sum += x
    return sum


print(add())
# *************************************************
# Countdown by Fours

x = 2016
while x > 0:
    print(x)
    x = x - 4
    if x < 0:
        break
# ************************************************
# Flexible Countdown

count = (2, 9, 3)

lowNum = count[0]
highNum = count[1]
mult = count[2] * -1

for x in range(highNum, lowNum, mult):
    print(x)
# ************************************************
# The Final Countdown

count = (3, 5, 17, 9)

param1 = count[0]
param2 = count[1]
param3 = count[2]
param4 = count[3]

for x in range(param2, param3):
    if x % param4 == 0:
        continue
    if x % param1 == 0:
        print(x)
