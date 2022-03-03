#syntax ---> new_list = old_list.copy()

a = [81, 81, 81, 63, 80]
print("value of a:", a)
a_dublicate = a.copy()
print("value of a_duplicate:", a_dublicate)

#copy using slicing

b = ['cat', 99, 33.55]
print('elelments of b', b)
b_duplicate = b[:]
print("copied by slicing:", b_duplicate)
b_duplicate.append('dog')
print("copied and append:", b_duplicate)

#copy using =

old_list = [5, 4, 3, 2, 1, 0]
new_list = old_list
print("old: ", old_list)
print("new: ", new_list)