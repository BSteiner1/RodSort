# initial_sort() will create a list with the second half of the elements of 
# the list. It then either places the first element of the rod into the
# first_half list or the recycle bin.

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

# =========================================================================
 
def insert_by_index(list, num, index, bin):
    
    if list == []:
        list.append(num)
        
        return list, bin
        
    if index >= len(list):
        index = len(list)
        if num >= list[-1]:
            list.append(num)
        else:
            bin.append(num)
            
        return list, bin
        
    else:
        if num >= list[index-1] and num <= list[index]:
            list.insert(index, num)
        else:
            bin.append(num)
  
    return list, bin

# =====================================================================

def initial_sort(lst):
    
    # Initialise the lists we will need
    first_half = []
    second_half = []
    recycle_bin = []
    rod_length = int(len(lst)/2)
    
    # Set the rod length as half of the length of the list
    for i in range(rod_length):
        rod = [lst[i], lst[i + rod_length]]
        
        if rod[0] < rod[1]:
            None
          
        # Rotate the rod so the larger number of the two is at index 1
        if lst[i] <= lst[i + rod_length]:
            rod = [lst[i], lst[i + rod_length]]
        else:
            rod = [lst[i + rod_length], lst[i]]
        
        # Insert the larger number into second_half
        index = insert_number(second_half, rod[1])[1]
        second_half = insert_number(second_half, rod[1])[0] 
        
        # Check if we can insert the lesser number into the first_half list
        insert_by_index(first_half, rod[0], index, recycle_bin)
        
    return first_half, second_half, recycle_bin