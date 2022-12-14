# https://practice.geeksforgeeks.org/problems/get-minimum-element-from-stack/1?page=1&category[]=Stack&curated[]=1&sortBy=submissions

class MinStack:
    def __init__(self):
        self.s=[]
        self.minEle=None
        

    def push(self,val:int):
        self.s.append(val)
        return self.s

    def pop(self):
        last = self.s[-1]
        del self.s[-1]
        return last
        
    def getMin(self):
        toSort = self.s[:]
        toSort.sort()
        return toSort[0]
    
    def top(self):
        return self.s[-1]

if __name__ == "__main__":
    minStack = MinStack() # Create class object in order to access the functions inside of it. 
    # print(minStack)
    print(minStack.push(2))
    print(minStack.push(0))
    print(minStack.push(3))
    print(minStack.push(0))
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.getMin())
    print(minStack.pop()) # should be popping 0, then 3 from [2, 0 , 3, 0] but not popping that, should return


    