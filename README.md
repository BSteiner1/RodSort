# RodSort
:warning: **A work in progress**

💡 An idea for a sorting algorithm that sorts one list of numbers into two sorted lists (that are not necessarily sorted when concatenated)
### For example: 
- Input: [**6**,7,**3**,4,**8**,2]
- Output: [2,4,7] and [**3**,**6**,**8**]

❓ **Analysis:**
- It has a best-case run-time of O(n)
- And a worst-case run-time of O(n²)
- It is **not** a [stable sorting algorithm](https://www.geeksforgeeks.org/stability-in-sorting-algorithms/) 

## 🔁 Loop Invariant for `initial_sort()`:
#### "After the *iᵗʰ* iteration, the list `first_half` contains the elements `list[n/2: n/2+i]`sorted in non-decreasing order. Moreover, `second_half` contains at most *i* elements from `list[0:i]` also sorted in non-decreasing order. Furthermore, `recycle_bin` contains at most *i* elements from `list[0:i]`, and these are exactly the elements not already in `first_half`. More formally, `first_half` and `recycle_bin` form a [partition](https://en.wikipedia.org/wiki/Partition_of_a_set) of `list[0:i]`."

## 🔁 Loop Invariant for `empty_bin()`:
#### "After the *iᵗʰ* iteration, `recycle_bin` contains `len(recycle_bin)-i` elements, and `list` contains the initial `len(list) + i` elements sorted in non-decreasing order.

## 🔁 Loop Invariant for `RodSort()`:
#### "After the *iᵗʰ* iteration, `first_half`, `second_half`, and `recycle_bin` contain *i* elements in total. Furthermore, `first_half` and `second_half` always remain sorted in non-decreasing order."
