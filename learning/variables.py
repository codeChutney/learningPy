# Lesson 1
# Learning to use variables
print('Lesson starts here')

print('This is an example of ' + 'concatenation')
print('This is an example of \\ escape character')
print('\'This is another example of \n \t an escape character\'')

# Usage of type(), pay close attention to the type of 10. and type of type
print('note that python will throw an error if you try and concatenate 2 different types(in this case -> type + '
      'string will give you an error)')
print('type of string is ' + str(type('someString')))
print('type of a number without any decimals is ' + str(type(10)))
print('type of a number with decimals is ' + str(type(11.)))
print('type of boolean is ' + str(type(True)))
print('does type have its own type' + str(type(type('anythingCanGoHere'))))

# Some string functions
dummy_string = "note the variable name, snake case is the pythonic way of naming variables"
print(dummy_string)
print('type of dummy_string is ' + str(type(dummy_string)))
print('printing the string in upper case ' + dummy_string.upper())
