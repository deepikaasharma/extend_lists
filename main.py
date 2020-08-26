"""Write a function called extend_lists. This function takes three lists as arguments. This function should return a new list containing all the elements of the three passed in lists. These elements should be in order of the lists as they were passed in.

Note:

    You can assume that there are no nested lists

For example:

extend_lists([1, 2, 3], [4, 5], [6, 7, 8, 9])

should return:

[1, 2, 3, 4, 5, 6, 7, 8, 9]"""

lst1 = [1,2,3]
lst2 = [4,5]
lst3 = [6,7,8,9]

# new_list = lst1.extend(lst2)
# another_list = lst1.extend(lst3)

def extend_lists(lst1, lst2, lst3):
  lst123 = []
  lst123.extend(lst1)
  lst123.extend(lst2)
  lst123.extend(lst3)
  return lst123

print(extend_lists(lst1, lst2, lst3))


