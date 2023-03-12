# paragraph
print('''hello world
welcome 
isn't the weather lovely''')

# Checking the length of a string.
print(len('My name is sadman. '))

# string indexing and slicing
my_string = 'abcdefghijklmnopqrstuvwxyz'
print(my_string[4:9])
print(my_string[::-1])
print(my_string[1:12:2])

# string concatinating
name = "Sam"
last_name = name[1:]
new_name = "P" + last_name
print(new_name)

# .format method
print('The {q} {b} {f}.'.format(q='quick', b='brown', f='fox'))

# float formatting
result = 2373/23
print('The result is {r:1.3f}'.format(r=result))

# f-string, formatting string literals

print(f'Your weight is {result} lbs.')
