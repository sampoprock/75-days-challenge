# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for i in nums:
            if count == 0:
                res = i
            count += (1 if i == res else -1)
        return res

        # has={}
        # result, maxCount=0,0
        # for i in nums:
        #     has[i]=1 + has.get(i,0)
        #     result=i if has[i]> maxCount else result
        #     maxCount=max(has[i],maxCount)
        # return result
#         count = 1


#         result = nums[0]

#         for num in nums[1:]:

#             if num != result:

#                 count -= 1

#                 if count == 0:
#                     result = num
#                     count = 1
#             else:

#                 count += 1

#         return result

