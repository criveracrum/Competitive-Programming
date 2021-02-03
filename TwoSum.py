##Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

##You may assume that each input would have exactly one solution, and you may not use the same element twice.

##You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff =[]
        for i in range(len(nums)):
            res1=  target - nums[i] 
            if res1 in nums:
                if (i==nums.index(res1)):
                    continue
                else: 
                    diff.append(nums.index(res1))
                    diff.append(i)
                    break
            
        
        ##res=[]
       ## for j in range(len(diff)):
            ##print(diff[j], " from dif")
        ####    if diff[j] in nums:
        ##        if (j==nums.index(diff[j])):
        ##            continue
        ##            break
        return diff
