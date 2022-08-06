# Search and place a number into a list that is already in increasing order
# We also return the index that the number is placed into so we can then decide 
# whether the first element of the rod will be placed into the first_half list 

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