## ----- Median of Two Sorted Arrays ----- ##
#Written By: Aarni Junkkala

#Date: 24.1.2024
#Runtime: 73 ms, Beats 96.18% of users with python3
#Memory: 16.92 MB, beats 53.57% of users with python3

#Given two sorted arrays nums1 and nums2 of size m and n respectively,
#return the median of the two sorted arrays.

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = (nums1 + nums2) #Combines the lists
        nums.sort() #Sorting
        if len(nums) % 2 == 1: #Odd lengths takes the middle
            return nums[int(len(nums)/2)]
        else: #Even avarages two closest to the middle
            return (nums[int(len(nums)/2) - 1] + nums[int(len(nums)/2)]) / 2

if __name__ == "__main__":
    a = Solution()
    print(a.findMedianSortedArrays([1,3],[2])) # 2
    print(a.findMedianSortedArrays([1,2],[3,4])) #2.5