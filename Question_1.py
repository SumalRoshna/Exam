num_list=input("Enter comma seperated the elements of list: ")
new_list=num_list.split(",")
duplicate=[]
print("Duplicates are: ")
for i in new_list:
    if i not in duplicate:
        duplicate.append(i)
    else:
        print(i,end=" ")
