
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
  
# Driver function
#list = []
#list = insert_number(list,3)
#list = insert_number(list[0],4)

#print(list)

from random import randint


def insert_by_index(list, num, index, bin):
    
    bin = []
    
    if list == []:
        list.append(num)
        
        return list, bin
        
    if index >= len(list):
        index = len(list)
        if num >= list[index-1]:
            list.append(num)
        else:
            bin.append(num)
        
    else:
        if num >= list[index-1] and num <= list[index]:
            list = list[:index] + [num] + list[index:]          #stable sort
        else:
            print('to bin: ', num)
            bin.append(num)
  
    return list, bin

# =============================================================================
# list = []
# list2 = [2,3,1,5,2,7,3,7,9]
# 
# recycle_bin = []
# 
# for x in list2:
#     z = randint(0,10)
#     print(x, 'at', z)
#     insert_by_index(list, x, z, recycle_bin)[0]
#     #recycle_bin = recycle_bin + insert_by_index(list, x, 3, recycle_bin)[1]
#     print(list, ' +', bin)
#     
# print(list)
#     
# =============================================================================

binn = []
list = [-3,-2,-1]
list2 = [1,6,2,6,9]

for x in list2:
    insert_by_index(list, x, 3, binn)
    list = insert_by_index(list, x, 5, binn)[0]
    print(list, binn)
        
    
insert_by_index(list, x, 5, binn)[0]
