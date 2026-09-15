# String Reversal using Two-Pointer Technique

## 📌 Overview
This project demonstrates how to reverse a string in Python using the **two-pointer approach**.  
The algorithm uses two indices (`left` and `right`) to swap characters until the string is reversed.

---

## 🛠️ Code Implementation
```python
def text_reverse(text):
    l1 = list(text)          # convert string to list (mutable)
    n = len(l1)
    left, right = 0, n-1     # two pointers at start and end
    
    while left < right:
        l1[left], l1[right] = l1[right], l1[left]  # swap
        left += 1
        right -= 1
    
    return ''.join(l1)       # convert list back to string

text = "lovable"
print(text_reverse(text))
