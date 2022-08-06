#  This will empty all elements of the recycle bin into the first_half list, 
# leaving the recycle bin empty, and all the first half of the original list
# will be sorted in non-decreasing order.

def insert_number(list, num):
  
    index = len(list)
    # Searching for the position
    for i in range(len(list)):
      if list[i] > num:
        index = i
        break
  
    # Inserting num in the list
    if index == len(list):
      list = list[:index] + [num]
    else:
      list = list[:index] + [num] + list[index:]
      
    return list, index

# ========================================================================

def empty_bin(recycle_bin, list):

    # Place number into list and remove from recycle bin
    for i in range(len(recycle_bin)):
        list = insert_number(list, recycle_bin[-1])[0]
        recycle_bin.pop()
        
    return list, recycle_bin