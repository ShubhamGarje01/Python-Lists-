num = 12
num_list = [99, 12, 23, 34, 45, 56, 67, 78, 89, 90]
print("Single value Assigning to single variable:-", num)
print("Multiple value assigning to single variable:-", num_list)
print(num_list[0:])


names_list = ['sam', 'rushi', 'vaishu']
print(names_list)
print(names_list[0:2])


list_values = [2.5, 'sam', 25] #multi-data-type list
print(list_values)


list_of_list = [num_list, names_list, list_values]
print("The mix list:\n", list_of_list)

#Sorting syntax --> sort() -> normal
#syntax parameters --> sort(reverse, key)

#Sorting numbers Ascending
x = [3, 5, 1, 4, 2]
print("Given List: ", x)
x.sort()
print("Sorted list: ", x)
#Sorting Descending Order
x.sort(reverse = True)
print("Descending Sort: ", x)

#Vowels Sorting Ascending
vowels = ['e', 'a', 'u', 'i', 'o']
print("Given vowels: ", vowels)
vowels.sort()
print("Sorted Vowels: ", vowels)
#Sorting Descending Order
vowels.sort(reverse = True)
print("Descending Sort: ", vowels)

#sorting using custom key
employee  = [
    {'Name': 'Shubham', 'age': 26, 'salary': 600000},
    {'Name': 'Rushi', 'age': 25, 'salary': 500000},  
    {'Name': 'vaishu', 'age': 20, 'salary': 300000},
]

#custom functions
def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get("salary")

print("\n\n\t#*#*#:- Employee Data -:#*#*#\n\n", employee, end = '\n\n')

#sort by name (Ascending)
employee.sort(key = get_name)
print("#sort by name\n\n", employee, end ='\n\n')

#sort by name (Descending)
employee.sort(reverse = True, key = get_name)
print("#Sort by name (Descending)\n\n", employee, end = '\n\n')

#sort by salary (Ascending)
employee.sort(key = get_salary)
print("sort by salary (Ascending)\n\n", employee, end = '\n\n')

#sort by salary (Descending)
employee.sort(reverse = True, key = get_salary)
print("sort by salary (Descending)\n\n", employee, end='\n\n')

#sort by age (Ascending)
employee.sort(key = get_age)
print("sort by age (Ascending)\n\n", employee, end = '\n\n')

#sort by age (Descending)
employee.sort(reverse=True, key= get_age)
print("sort by age (Descending)\n\n", employee, end='\n\n')
