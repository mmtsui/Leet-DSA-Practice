# Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.
# https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1?utm_source=gfg&utm_medium=article_practice_tab&utm_campaign=article_practice_tab 
class Solution:
    def maximumSumSubarray (self,K,numbers):
        Arr = numbers
        # Arr = [200,100,400,300]
        # numbers = int(input("Enter number of elements : "))
        # for i in range(0, numbers):
        #     ele = int(input("enter a list of numbers, seperated by commas")) # "20,30,40,50,60"
        #     Arr.append(ele)
        # K = int(input("Enter K : "))
        N = len(Arr)
        Arr.sort()
        maxNum = Arr[-K:]
        return sum(maxNum)
        

if __name__ == "__main__":
    tmp = Solution() # Create class object in order to access the functions inside of it. 
    print(tmp.maximumSumSubarray(2,[200,100,400,300]))