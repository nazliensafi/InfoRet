__Author__ = 'Naz'
# # 1st
# print('Salam')
# print(8*9-5)
# adad = '89'
# kalame = 'chanta'
# print(kalame + '? ' + adad)
#
# #2nd
# greeting = 'Hi'
# name = input('Please enter your name: ')
# print(greeting + ' ' + name)

splitString = 'This\nsplits\nover\nlines'
print(splitString)

tabbedString = 'a\tb\tc\td'
print(tabbedString)

print("The owner said \"No, no, 'e's uh,... he's resting\"")
print('The owner said "No, no, \'e\'s uh,... he\'s resting"')

anotherSplitString = """This string 
splits over 
several times"""
print(anotherSplitString)

#Variables

a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b) #returns a float
print(a // b) #returns an int
print(a % b)

for i in range (1, a//b):
    print(i)

number = "123456789"
print(number[0::2])

# NICE stuff for searching!!!
word = "beautiful"
print("uti" in word)
print("ful" in word)
print("ugly" in word)

#string formatting

age = 24
print("My age is " + str(age) + " years")
# Usful when there are many numbers to format like the second example
print("My age is {0} years".format(age))
print(f"There are {31} days in {'Jan'}, {'Mar'}, {'May'}, {'Jul'}, {'Aug'}, {'Oct'}, and {'Dec'}")
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))

print("My age is %d %s and %d %s" % (age, "years", 6, "months"))
# 2 holds 2 places for the digits and (Python 2 syntax)
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))
print("*************")
# Python 3 syntax
for i in range(1, 12):
    # notice that <4 makes the digits are started form the left
    print("No. {0:2} squared is {1:4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
print("pi is approx. %12.50f" % (22/7))
print("pi is approx. {0:12.50f}".format (22/7))

### ??? make sure you leearn this before the end of the course
number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

#notice the difference!
letters = "abcdefghijklmnopqrstuvwxyz"
backwards1 = letters[25:0:-1]
backwards2 = letters[25::-1]
backwards3 = letters[::-1]
print(backwards1)
print(backwards2)
print(backwards3)
challenge1 = letters[-10:-13:-1]
# or [16:13:-1]
print(challenge1)
challenge2 = letters[-22::-1]
# or [4::-1]
print(challenge2)
challenge3 = letters[-1:-9:-1]
# or [:-9:-1]
print(challenge3)
