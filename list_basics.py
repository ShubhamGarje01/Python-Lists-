num = 12
num_list = [99, 12, 23, 34, 45, 56, 67, 78, 89, 90]
print("Single value Assigning to single variable:-", num)
print("\n\nMultiple value assigning to single variable:-", num_list)
print(num_list[0:]) #list slicing (int)


names_list = ['sam', 'rushi', 'vaishu']
print(names_list)
print(names_list[2])
print(names_list[0:2]) #list slicing (char)

print('\n\n')

list_values = [2.5, 'sam', 25] #multi-data-type list
print(list_values)
print(list_values[-1])

print('\n\n')

list_of_list = [num_list, names_list, list_values] #printing list of multiple lists
print("The mix list:\n", list_of_list)

print('\n\n')

#Nested - Slicing of List

n_list = ["Happy", [2, 0, 1, 5]]
print(n_list[0][1]) # from 0th list 1st element
print(n_list[1][2]) # from 1st list 2nd element
print(n_list[0][-1]) #from 0th list last element
print(n_list[0][1:]) # 0th list from 1nd element to all
print(n_list[0][1:5])
print(n_list[1][1:4])

#Reverse the list using slicing
print(n_list[::-1])
x_list = ['shubham']
print(x_list)
print(x_list[::-1])
new_list = [9, 7, 5, 3, 1, 0]
print("Original List:- ", new_list)
print("reverse string:- ", new_list[::-1])