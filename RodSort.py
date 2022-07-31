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
      
    return list, index              # 0th index is the list, 1st is index


#--------------------------------------------------------------------------

def insert_by_index(list, num, index):
    
    recycle_bin = []
    
    if list == []:
        list.append(num)
        return list, recycle_bin
        
        
    if index > len(list):
        index = len(list)
        if num >= list[index-1]:
            list.append(num)
        else:
            recycle_bin.append(num)
        
    else:
        if num >= list[index] and num <= list[index+1]:
            list = list[:index] + [num] + list[index:]
        else:
            recycle_bin.append(num)

    return list, recycle_bin

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
        else:
            rod = [rod[1], rod[0]]
        
        insert_number(second_half, rod[1])
        second_half = insert_number(second_half, rod[1])[0] 
        
        first_half = insert_by_index(first_half, 2, 5)
        
        #first_half = insert_number(first_half, rod[0])[0]
        
                
    return first_half, second_half, recycle_bin

numbs = [6,1,7,2,8,4]                
            
print(RodSort(numbs))
        

