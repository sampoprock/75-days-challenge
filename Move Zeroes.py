# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution-1 1024ms
        # for i in nums:
        #     if i == 0:
        #         nums.remove(i)
        #         nums.append(0)
        # print(nums)
        # Solution 2 124ms
        ind=0

        for i in range(len(nums)):
            if nums[i]!=0:
                nums[ind]=nums[i]
                ind+=1

        for i in range(ind,len(nums)):
            nums[i]=0

        print(nums)