# creating a dictionary

dictionary1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
dictionary2 = {'string': 'abcd', 'integer': '12', 'float': '1.5', 'list': ['a', 'b', 'c']}
dictionary3 = {}

# Accessing objects from dictionary

print(dictionary1['key1'])
print(dictionary2['string'].upper())
print(dictionary2['list'][1])

# Adding new keys through assignment

dictionary3['one'] = 1
dictionary3['two'] = 2
dictionary3['three'] = 3

print(dictionary3)

# arithmatic in dictionary

result = dictionary3['one']+dictionary3['two']
print(result)
result2 = dictionary3['three']-7
print(result2)

# using dictionary methods

print(dictionary2.values())
print(dictionary2.keys())

# mutability of dictionary

# dictionary3['three'] = '4'

print(dictionary3)
