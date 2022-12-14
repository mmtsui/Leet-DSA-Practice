# https://practice.geeksforgeeks.org/problems/get-minimum-element-from-stack/1?page=1&category[]=Stack&curated[]=1&sortBy=submissions

class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        self.s.append(x)
        return self.s

    def pop(self):
        last = self.s[-1]
        self.s.remove(last)
        return last
        
    def getMin(self):
        self.s.sort()
        return self.s[0]

if __name__ == "__main__":
    tmp = stack() # Create class object in order to access the functions inside of it. 
    print(tmp.push(2))
    print(tmp.push(3))
    print(tmp.pop())
    print(tmp.getMin())
    print(tmp.push(1))
    print(tmp.getMin())
    

    