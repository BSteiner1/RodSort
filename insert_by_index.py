# Decide whether to place a number into a list given an input index
# We will insert it into the list if the list will still be in non-decreasing 
# order after insertion

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
