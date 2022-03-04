start = 2
end = 20
step = 2
#range in list
#list(range(start, end, step)) --> syntax for range in list
print("Range of numbers:- ", list(range(start, end, step)))
print("5th table:- ", list(range(5, 51, 5)))
print("10th table:- ", list(range(10, 101, 10)))
print(list(range(start, 51, 3)))

#SUM --> syntax--> sum([iterable],start)
print(sum([1, 2, 3, 4, 5])) # to add all elements in list
n_list = list(range(2, 21, 2)) #creating new list
print("n_list:- ", n_list)
print("Addition of n_list: ", sum(n_list))

m_list = [2, 4, 6, 8, 10, -5]
print("m_liast:- ", m_list)
print("sum of m_list: ", sum(m_list))

p_list = [9, 8, 7, 6, 5]
print("p_list:- ", p_list)
print("sum of p_list starting with 5: ", sum(p_list, 5)) #does not changes the output


# min and max from list

print("min in n_list:- ", min(p_list))
print("max of p_list:- ", max(p_list))
print("min of m_list:- ", min(m_list))
print("max of m_list:- ", max(m_list))


# zip() --> used to mix list 1 with list 2 --> list(zip(list_1, list_2))

list_a = ['a', 'b', 'c', 'd']
list_z = [1, 2, 3, 4]
print("list_a:- ", list_a)
print("list_z:- ", list_z)

print("zip of list a and z:- ", list(zip(list_a, list_z)))

list_b = [-1, -2, -3, -4]
print(list(zip(list_a, list_b, list_z))) #zip of 3 lists

list_c = ['sam', 'vaishu', 'rushi', 'omee']
print("zip of 4 lists:- \n:--> ", list(zip(list_a, list_b, list_c, list_z)))