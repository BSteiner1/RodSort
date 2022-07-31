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

from random import randint


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

    
binn = []
list = []
list2 = [randint(0,10) for i in range(10)]

print(list2)

for x in list2:
    z = randint(0,10)
    insert_by_index(list, x, z, binn)
    print(list, binn)
    
print('SUM: ', len(list) + len(binn))


    
