#How to copy a list using list slicing without modifying the initial list

initial_list = ['black', 'red', 'yellow', 'white']
new_list = initial_list
new_list[0] = 'brown' #here, the first object in the new_list was changed to brown
print(new_list)
print(initial_list)

#Did you observe that initial_list has entirely changed to the new_list when printed?
#This is because by using the '=' operator in line 4, we replaced what was in memory of initial_list to new_list and vice versa.
#To avoid this if we do not plan to modify the initial_list we copy the enitire data to new_list using list slicing during assignment.

#here is how

initial_list_new = ['black', 'red', 'yellow', 'white']
new_list_new = initial_list [:]
new_list_new[0] = 'brown'
print(new_list_new)
print(initial_list_new)

#here we see that initial_list_new did not change beacause we used the [:] when assigning new_list_new to initial_list_new.
