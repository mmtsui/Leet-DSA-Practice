# https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower():
            return True
        elif word[0].isupper():
            if word[1:].islower():
                return True 
            elif word[1:].isupper():
                return True
            elif word[1:-2].isupper or word[-1].isupper(): 
                return False
        else:
            return False

# EC's method. 
# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#         cap = word[0]
#         rest = word[1:]
#         if word.lower() == word:
#             return True
#         elif word.upper() == word:
#             return True
#         elif cap.isupper() and rest.lower() == word[1:]:
#             return True
#         else:
#             return False

if __name__ == "__main__":
    test = Solution()
    print(test.detectCapitalUse("USA"))
    print(test.detectCapitalUse("FFFFFFFFFFFFFFFFFFFFf"))
    print(test.detectCapitalUse("FlaG"))
    print(test.detectCapitalUse("Leetcode"))
    
