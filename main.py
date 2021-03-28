################################
# Learn Python with no stress! #
#       #1 - Variables         #
################################



### # This is a commentary (Which you can comment wherever you want)

### Print Syntax

print("Hello, World!")

## Str Variables

print("Best cars of all time!")
car_1 = "Lamborghini"
car_2 = "Wolkswagen"
car_3 = "Russian Lada"
car_4 = "Ferrari"

# Variables (Which are right are Strings [Variables with texts]) can be printed

print(car_1)
print(car_2)
print(car_3)
print(car_4)

# Variables can change (Optional, because you can choose between this and naming variables)

status = "Incomplete"
status = "Complete"
print(status)

status = "New data required"
print(status)

# Variables can change their values too

default_option = "upload"
new_status = "download"

new_status = default_option
print(new_status)

# We can add string values together with a + sign

"Followers:" + "55"
print("Followers:" + " 55")

# If it's values they can do the same thing!

likes = "69"
print("Likes: " + likes)

# Or inverse!

label = "Posts: " + "13"
print(label)

# Or by using two (or more) variables!

temperature = "14"
temperature_defined = " degrees"
print(temperature + temperature_defined)

## Int Variables

# Variables can be numbers too

active_users = 5

# We can create expressions with numbers too. You can add +1 to our int.

apps = 5 + 1
print(apps)

# Can multiply/divide or subtract

math_1 = 0.5 * 100
print(math_1)

math_2 = 10 - 5
print(math_2)

math_3 = 25 / 5
print(math_3)

# We can add/subtract/divide or multiply from the print syntax!

steps = 5
print(steps + 1)

# Or in variables!

private = 3
public = 10
total = private + public
print(total)

## Bool Variables

# There's a special value that's neither a string nor a number and that is bool!
# There are no quotes around it, and it's not a numeric value

# True - Checks that if that variable it's true

powered_on = True

# We can store it too as a string or a number. Displaying it also works the same
# like when we display powered_on here.

print(powered_on)

# False - Is another special value and it's the opposite of True

# Same as True will display the same value

print("Turn on the computer")
powered_off = False
print(powered_off)

# Both of them can show in the print syntax

print(True)
print(False)

# Both can have not format in front of them. If it's not True then it turns into False
# and if it's not False then it turns into True. not is the negation operator.
# It turns values into their opposite

print(not True)
print(not False)

# We can use the not operator with variables to negate their values too! By
# displaying here, we'll see its negated value in print syntax

available = True
print(not available)

# Or by variables

morning = True
evening = not morning
print(evening)

## Equality Variables

# We learned hot to create and store variables, but how do we compare them?
# Like checking if a user's entered PIN matches their saved PIN.

entered_pin = 5448
expected_pin = 5440

# To compare if two numbers are the same, we use the equality operator ==.

5 == 5

# When comparing, there are only two results: True or False.
# NOTE: When we compare the same numbers with the equality operator, the result
# is True.

print(10 == 10)

# NOTE: When we compare the different numbers with ==, the result is False.

print(9 == 10)

# This is working with int(not str). That means we could use with variables too

votes = 10
print(votes == 11)

# Or two (or more) variables!

dog_1 = 1
dog_2 = 2
dog_3 = 3
print(dog_1 == dog_2 == dog_3)

## Inequality Variables

# To check if a number isn't equal to another number, we use the inequality
# operator, !=

print(1 != 10)

# We can store the result of a comparison with != in a variable

result = 1 != 2
print(result)

## Comparing Variables

# We can use comparisons to check if number is less than or greater than another
# number
# To check if a number is less than another number, we use the less-than operator
# <.

1 < 90

# If the number on the left is less than the number on the right,
# then the result will be True

print(1 < 2)

# If the number on the left isn't less than the number on the right,
# then the result will be False

print(2 < 1)

# To check if a number is greater than another number, we use the greater-than
# operator >.

print(3 > 2)

# To check if a number is less than or equal to another number, we use the
# less-than-or-equal-to-operator <=.

print(1 <= 3)

# If the number on the left is less than or equal to the number on the right,
# the result is True.

print(11 <= 11)

# To check if a number is greater than or equal to another number, we use the
# greater-than-or-equal-to operator, >=

print(3099 >= 3099)

# To store the result of a comparison in a variable it's possible (both)

result_1 = 1 <= 15
print(result)

result_2 = 2 >= 14
print(result)

# Or with variables too!

min_1 = 5
max_2 = 10
result_3 = min_1 <= max_2
print(result)

# We can use comparison operators for str too!

print("online" == "offline")
print("online" != "offline")

# Same with variables

fruit_1 = "apple"
fruit_2 = "orange"
print(fruit_1 == fruit_2)

## Float Variables

# Float is another number type we use to describe number with one or more digits
# the decimal point, like 3.14169

pie = 3.14169
print(pie)

# Results with variables too!

pie = 3.345
pie_2 = 4.555

print(pie + pie_2)

## Formating Strings

#We've learned that we can use + to add two strings and display them togheter

print("new" + "message")

# But adding with a integer will cause errors.
# That's why we will learn how to display different kinds of values to make it
# work!

# F-Strings, short for formatted strings, allow us to display int, bool and float
# without any errors!

print(f"{2} new messages")

# The f shows that the string is a f-string. And {} (curly braces)
#allow us to input bools, ints, floats.

# Works with other variables too!

new_messages = 2
print(f"{new_messages} new messages")

# Same with mathematical symbols!

new = 5
read = 2
print(f"{new - read} unread message")

# The curly braces can be two or more in a print syntax!

print(f"{2} new messages and {5} friend requests")

# Can be variables too!

new = 5
status = f"{new} new messages"
print(status)



