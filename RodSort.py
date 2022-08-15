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

#--------------------------------------------------------------------------

def insert_by_index(list, num, index, bin):
    
    # Check if list is empty
    if list == []:
        list.append(num)
        
        return list, bin
        
    # If the index is out of range, we will make it the last index of the 
    # list and try and place it at the end
    if index >= len(list):
        index = len(list)
        if num >= list[-1]:
            list.append(num)
        else:
            bin.append(num)
            
        return list, bin
     
    # Otherwise, check if we can keep the list in non-decreasing order by
    # inserting it
    else:
        if num >= list[index-1] and num <= list[index]:
            list.insert(index, num)
        else:
            bin.append(num)
  
    return list, bin

#--------------------------------------------------------------------

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

# -----------------------------------------------------------------------

def empty_bin(recycle_bin, list):

    # Place number into list and remove from recycle bin
    for i in range(len(recycle_bin)):
        list = insert_number(list, recycle_bin[-1])[0]
        recycle_bin.pop()
        
    return list, recycle_bin

# ------------------------------------------------------------------------

def Merge(left , right ):
    
    l, r = 0, 0
    result = []
    
    while l < len(left) and r < len(right ):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
            
    result += left[l:]
    result += right[r:]
    
    return result

# -------------------------------------------------------------------------
        
def RodSort(lst):
    
    first_half = initial_sort(lst)[0]
    second_half = initial_sort(lst)[1]
    recycle_bin = initial_sort(lst)[2]
    
    # Empty the bin into the first list
    full_first_half = empty_bin(recycle_bin, first_half)[0]
    
    # Merge the two lists together
    sorted_list = Merge(full_first_half, second_half)
    
    return sorted_list


import random
numbs = [random.randint(0,20) for i in range(20)]                
            
print(RodSort(numbs))
        


