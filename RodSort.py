def insert_number(list, x):
  
    index = len(list)
    # Searching for the position
    for i in range(len(list)):
      if list[i] > x:
        index = i
        break
  
    # Inserting n in the list
    if index == len(list):
      list = list[:index] + [x]
    else:
      list = list[:index] + [x] + list[index:]
      
    return list, index              

#--------------------------------------------------------------------------

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

#--------------------------------------------------------------------

def RodSort(lst):
    
    first_half = []
    second_half = []
    recycle_bin = []
    rod_length = int(len(lst)/2)
    
    for i in range(rod_length):
        rod = [lst[i], lst[i + rod_length]]
        
        if rod[0] < rod[1]:
            None
            
        if lst[i] <= lst[i + rod_length]:
            rod = [lst[i], lst[i + rod_length]]
        else:
            rod = [lst[i + rod_length], lst[i]]
        
        index = insert_number(second_half, rod[1])[1]
        second_half = insert_number(second_half, rod[1])[0] 
        
        insert_by_index(first_half, rod[0], index, recycle_bin)
        
                
    return first_half, second_half, recycle_bin


import random
numbs = [randint(0,20) for i in range(16)]                
            
print(RodSort(numbs))
        

