def odd_even(nums):
    left , right = 0, len(nums) - 1
    
    while left < right:
        if nums[left]% 2 ==0:
            left += 1
        elif nums[right]% 2 == 1:
            right-=1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -=1
    return nums

nums = [50, 25, 3, 14, 5,8, 7, 9, 10]
print(odd_even(nums))