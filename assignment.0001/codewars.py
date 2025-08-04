# Even or Odd
# Create a function that takes an integer as an argument and returns "Even" or "Odd"

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Number to String
# Create a function that can transform a number(integer) into a string

def number_to_string(num):
    return str(num)

# Remove String Spaces
# Create a function that removes the spaces from the string and returns the resultant string

def no_space(x):
    return x.replace(" ","")
