#--------------------------------------------------------------------------------------------------
#  Function			Description
#--------------------------------------------------------------------------------------------------
#  all()            Returns True if all the Boolean values in the list are True, else returns False
#  any()			Returns True if any of the Boolean values in the list is True
#  append()         Adds an item to the end of the list
#  len()			Returns the numbers of items in a list
#  insert()         Inserts an item at a given position
#  pop([])          Removes the item at the given position in the list
#  clear()          Removes all items from the list.           
#  reverse()        Reverses the elements of the list
#  sort()			Sorts the elements of the list.
#  min()            Returns the smallest item in the list.
#  max()            Returns the largest item in the list.
#--------------------------------------------------------------------------------------------------

mylist = [True, True, True, 2==2]
print(all(mylist))
#---------------------------------------

mylist_2 = [True, 2==3, False]
print(any(mylist_2))

#---------------------------------------

mylist_3 = ['first', 'last']
mylist_3.append("name")
print(mylist_3)

#---------------------------------------

mylist_4 = [1, 2, 3, 4]
print(len(mylist_4))

#---------------------------------------

mylist_5 = [1, 2, 3, 5]
mylist_5.insert(1, 4)
print(mylist_5)

#------------------------------

mylist_6 = [1, 2, 3, 4]
remove_item = mylist_6.pop(2)

print(mylist_6)
print(remove_item)

#------------------------------

mylist_7 = [1, 2, 3, 4]
mylist_7.clear()
print(mylist_7)

#------------------------------

mylist_8 = [1, 2, 3, 4]
mylist_8.reverse()
print(mylist_8)
#------------------------------

mylist_9 = [4, 3, 2, 1]
mylist_9.sort()
print(mylist_9)
#------------------------------

mylist_10 = [4, 3, 2, 1]
print(max(mylist_10))
print(min(mylist_10))