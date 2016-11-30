# Python: 2.7
#
# Author: Me
#
# Purpose: The Tech Academy - Python Course, Drill item 36
#          To demonstrate the following consepts.        
#   
#

counter = 100          # An integer assignment
miles   = 5000.0       # A floating point
name    = "George"       # A string



print ('The value is {:0,.2f}'.format(counter)) # Using print with .format()

#######################
# Examples of operator usage
add = counter + miles
print add

subtract = counter - miles
print subtract

multiply = counter * miles
print multiply

divide = counter / miles
print divide

counter += 1
print counter

counter = 100
print counter

modulus = miles % counter
print modulus

####################
#Examples of Logical operators
x = True
y = False

# Output: x and y is False
print('x and y is',x and y)

# Output: x or y is True
print('x or y is',x or y)

# Output: not x is False
print('not x is',not x)

###################
# Examples of conditional statements


number = 53
if number == 0:
    print(number, "is equal to zero.")
elif number > 0:
    print(number, "is a positive number.")    
else:
    print(number, "is a negative number.")

# Example of while loop
countto = 100
counter = 0

while counter <> countto:
      counter += 1

print counter

####################
# Example of For loop

shoppingListPrices = [16,7,8,8,1,2,9,3,171]

# variable to store the total
total = 0

# iterate over the list
for val in shoppingListPrices:
	total = total+val

# print the total
print("The shopping total is",total)

#####################
# Example of creating a list and iterate to print each item on a line

shoppingListPrices = [16,7,8,8,1,2,9,3,171]

# iterate over the list
for val in shoppingListPrices:
    print val
    
#####################
# Create a tuple and iterate through it using a for loop to print each item out on a new line

shoppingListPricesTuple = (16,7,8,8,1,2,9,3,171)

# iterate over the tuple
for val in shoppingListPricesTuple:
    print val

#####################
#Define a function that returns a string variable

def shave(person):
    """This function shaves the person"""
    print ("Hello, " + person + ". zzzzssss. You have now been shaved!")


#####################
#Call the function you defined above and print the result to the shell

shave(name)

