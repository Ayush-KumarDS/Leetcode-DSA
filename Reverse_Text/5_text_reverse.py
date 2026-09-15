def text_reverse(text):
    l1 = list(text)
    n = len(l1)
    left, right = 0, n-1
    while left < right:
        l1[left], l1[right] = l1[right], l1[left]
        left += 1
        right -= 1
    return ''.join(l1)

text = "lovable"
print(text_reverse(text))