# Two-Pointer Sorting in Python

## 📌 Overview
This project demonstrates how to sort a tuple of strings using the **two-pointer technique**.  
The algorithm compares elements pairwise and swaps them if they are out of order, similar to a selection sort.

---

## 🛠️ Code Implementation
```python
def sorting(techs):
    n = len(techs)
    l1 = list(techs)   # convert tuple to list
    
    for i in range(n):
        j = i + 1
        while j < n:
            if l1[i] > l1[j]:   # swap if out of order
                l1[i], l1[j] = l1[j], l1[i]
            j += 1
    
    return tuple(l1)   # convert back to tuple


techs = ('python','aws', 'java', 'sql', 'nodejs', 'pandas')

print("Before sorting:", techs)
print("After sorting:", sorting(techs))
