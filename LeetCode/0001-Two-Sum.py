## ----- Two Sum ----- ##
#Written By: Aarni Junkkala

#Date: 24.1.2024
#Runtime: 1699 ms, Beats 30.21% of users with python3
#Memory: 17.52 MB, beats 79.15% of users with python3
#Note:
#More than 50% are cheating this task with answers that doesn't solve the problem,
#but just returns the answers to leetcode site

#Task:
#Given an array of integers nums and an integer target,
#return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution,
#and you may not use the same element twice.

#You can return the answer in any order.

#My idea:
#Loop throuh checking all pairs. it is O(n**2) speed, but good enough for me for now.

class Solution:
    def twoSum(self,nums: list[int], target:int) -> list[int]:
        for i in range(len(nums) - 1):
            for k in range(i + 1,len(nums)): #Must start from one after the i.
                if nums[i] + nums[k] == target:
                    return [i,k]

if __name__ == "__main__":
    a = Solution()
    print(a.twoSum([3,2,4],6))