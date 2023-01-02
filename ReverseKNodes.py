# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list. 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
class Solution:
    class Stack:
        def __init__(self):
            self.data = []

        def __len__(self):
            return len(self.data)
        
        def pop(self):
            tmp = self.data[-1]
            del self.data[-1]
            return tmp
        
        def push(self, x):
            self.data.append(x)

        def top(self):
            return self.data[-1]
        
        def is_empty(self):
            return len(self.data) == 0

    def reverseKGroup(self, head, k):
        head_swap = True
        stack = self.Stack()
        i = 1
        current_node = head
        k_last_node = head
        while current_node:
            # print(current_node)
            if i == k:
                # print("printing stack:")
                # for each in stack.data:
                #     print(each.val)
                i = 1 # Reset i for each iteration
                # temp = stack.pop()
                temp = current_node
                tempNext = current_node.next
                k_last_node.next = temp
                if head_swap: # This means if head_swap = True
                    head = temp
                    head_swap = False
                while len(stack) != 0:
                    temp.next = stack.pop()
                    temp = temp.next
                k_last_node = temp
                temp.next = tempNext
                current_node = tempNext
                continue
                # print(head)

            # print("pushing current node:",current_node.val)
            stack.push(current_node)
            i += 1

            if current_node.val != None:
                current_node = current_node.next
        # print("head:",head)
        return head


if __name__ == "__main__":
    myInput = ListNode(1, ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
    # myInput = ListNode(1, ListNode(2,None))
    # for each in myInput
    k = 2
    s = Solution()
    temp = s.reverseKGroup(myInput,k)
    while temp:
        print(temp.val)
        temp = temp.next






# PROGRAMMATIC WAY # 
# Reversing array every K elements. 

# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# head = [1,2,3,4,5]
# k = 2
# head = [1,2,3,4,5,6, 7]
# k = 3
# Output: [3,2,1,4,5] 

# for i in range(0,len(head)//k):# This chunks the data 
#     head[i*k:(i+1)*k] = head[i*k:(i+1)*k][::-1]
# print(head)


