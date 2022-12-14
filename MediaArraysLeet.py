# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        c = nums1 + nums2
        c.sort()
        if len(c) % 2 == 0: 
            middle = len(c)/2 
            middleOne = c[int(middle)-1]
            middleTwo = c[int(middle)]
            medianEven = (int(middleOne) + int(middleTwo))/2
            print(medianEven)

        else: 

            middleOdd = (len(c)+1)/2
            medianOdd = c[int(middleOdd)-1]
            print(medianOdd)


if __name__ == "__main__":
    numbers = Solution()
    median = numbers.findMedianSortedArrays([1,2], [3,4])
    