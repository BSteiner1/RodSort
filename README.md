# RodSort

💡 An idea for a sorting algorithm that sorts a list of numbers into non-decreasing order
### For example: 
- Input: [2,7,4,1,5,3]
- Output: [1,2,3,4,5,7]

### 🔧 How it works:
- ➗ It employs a [Divide and Conquer](https://www.geeksforgeeks.org/divide-and-conquer-algorithm-introduction/) approach during `initial_sort()` and `empty_bin()`:
- 🔀 And then uses `Merge()` from [MergeSort()](https://www.geeksforgeeks.org/merge-sort/) which has run-time θ(n)

### ❓ **Analysis:**
- It has a best-case run-time of O(n)
- And a worst-case run-time of O(n²)
- It has a Space Complexity of θ(n)
- It is **not** a [stable sorting algorithm](https://www.geeksforgeeks.org/stability-in-sorting-algorithms/) 

### ⏳ Expected Run-Time Proof:

<img src="https://user-images.githubusercontent.com/96544001/187798548-c8e277a5-02fe-4dbf-b6dd-475b0483440c.jpg" width="800" height="800" />
<img src="https://user-images.githubusercontent.com/96544001/187798562-6567dd91-e268-4ea9-acae-ab437d8ca1f3.jpg" width="800" height="800" />
<img src="https://user-images.githubusercontent.com/96544001/187798572-91b96e9a-1ac0-4aa8-8691-dfd888d13be9.jpg" width="800" height="800" />


### 🤔 How does it compare to other sorting algorithms?
<img src="https://user-images.githubusercontent.com/96544001/184625085-fe4c0529-ae2b-47be-a9ca-a530e46f8141.png" width="700" height="400" />

## 🔁 Loop Invariant for `initial_sort()`:
#### "After the *iᵗʰ* iteration, the list `first_half` contains the elements `list[n/2: n/2+i]`sorted in non-decreasing order. Moreover, `second_half` contains at most *i* elements from `list[0:i]` also sorted in non-decreasing order. Furthermore, `recycle_bin` contains at most *i* elements from `list[0:i]`, and these are exactly the elements not already in `first_half`. More formally, `first_half` and `recycle_bin` form a [partition](https://en.wikipedia.org/wiki/Partition_of_a_set) of `list[0:i]`."

## 🔁 Loop Invariant for `empty_bin()`:
#### "After the *iᵗʰ* iteration, `recycle_bin` contains the initial length of `recycle_bin` - i elements, and `first_half` contains the initial length of `first_half` + i elements sorted in non-decreasing order."

## 🔁 Loop Invariant for `RodSort()`:
#### "After the *iᵗʰ* iteration, `first_half`, `second_half`, and `recycle_bin` contain *i* elements in total. Furthermore, `first_half` and `second_half` always remain sorted in non-decreasing order."

