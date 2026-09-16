# Move Zeroes to End (Two-Pointer Approach)

## 📌 Overview
This project demonstrates how to move all zeroes in a list to the end while maintaining the relative order of non-zero elements.  
The algorithm uses the **two-pointer technique** for an optimal in-place solution.

---

## 🛠️ Code Implementation
```python
def Sorting_Zeroes(nums):
    n = len(nums)
    left = 0
    
    for right in range(n):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums

nums = [0, 1, 0, 3, 12]
print(Sorting_Zeroes(nums))
