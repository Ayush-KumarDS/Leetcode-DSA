# Odd-Even Partition using Two-Pointer Technique

## 📌 Overview
This project demonstrates how to rearrange an array so that **all even numbers appear before odd numbers** using the **two-pointer approach**.  
The algorithm swaps misplaced elements in-place, similar to the partition step in quicksort.

---

## 🛠️ Code Implementation
```python
def odd_even(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        if nums[left] % 2 == 0:   # left is even → move forward
            left += 1
        elif nums[right] % 2 == 1:  # right is odd → move backward
            right -= 1
        else:
            # swap odd on left with even on right
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    return nums

nums = [50, 25, 3, 14, 5, 8, 7, 9, 10]
print(odd_even(nums))
