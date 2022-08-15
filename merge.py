# This is taken straight from MergeSort() so that we can turn our two sorted 
# lists into one sorted list

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

print(Merge([1,3,5,7,9], [2,4,6,10]))