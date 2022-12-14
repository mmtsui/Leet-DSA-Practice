# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x).strip()
        palin = str(y)[::-1]
        if palin == y:
            return True

        else:
            return False


if __name__ == "__main__":
    tmp = Solution()
    tmp.isPalindrome(121)
