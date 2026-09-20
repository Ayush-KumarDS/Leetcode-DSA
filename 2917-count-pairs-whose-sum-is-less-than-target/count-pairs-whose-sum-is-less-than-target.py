class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort() # Sort the List First
        n = len(nums) - 1
        i = 0
        j = n

        count  =0

        while i < j :
            sum = nums[i] + nums[j]

            if sum < target:
                count += (j-i)

                i+=1
            else:
                j-=1
        return count