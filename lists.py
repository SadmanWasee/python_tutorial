# creating a list

my_list = ['one', 'two', 'three', 'four', 'five', 'six']
others_list = ['seven', 'eight', 'nine']

# adding/concatinating two lists

combined_list = my_list + others_list
print(combined_list)

# slicing a list

print(my_list[1:4])
print(my_list[0::2])

# basic list methods.

# append()/pop()

my_list.append(2)
# my_list.pop()
print(my_list)

# sorting and reversing

first_list = [3, 1, 6, 9, 4, 2, 12]
second_list = ['b', 'j', 'k', 'z', 'l', 't']

first_list.sort()
second_list.sort()
second_list.reverse()
print(second_list)
print(first_list)
