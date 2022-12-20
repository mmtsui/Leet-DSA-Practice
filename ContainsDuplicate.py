
# https://leetcode.com/problems/contains-duplicate/?envType=study-plan&id=data-structure-i
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        sortedArray = sorted(nums)
        prev = None
        for each in sortedArray:
            if each == prev:
                return True
                # break
            else:
                prev = each
                continue
        return False # Add return false outside of the for loop (when it reaches the end of the list)

if __name__ == "__main__":
    dup = Solution()
    print(dup.containsDuplicate([3, 2, 1,2,3]))

# # the set way
# newSet = set(nums)
# print(nums)
# if len(newSet) != len(nums):
#     print(newSet)
#     print("true")
# else:
#     print("false")
