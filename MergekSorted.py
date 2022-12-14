# https://leetcode.com/problems/merge-k-sorted-lists/
## This solution below is based on given lists assuming that these are not LINKED lists.##


# Assume each item in each list is node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self,head=None):
        self.head = head # First list value . Not sure if it matters. Everything will be sorted. 

class Solution:
    def mergeKLists(self, lists): #[[1,4,5],[1,3,4],[2,6]]
        listOfLinkedLists = []
        for eachList in lists: # This converts the lists of lists into lists of linked list (nodes with pointers). # [[1->4->5],[1->3->4],[2->6]]
            linkedList = LinkedList() 
            prev = None #  We need to set a reference to the previous node. While we convert the NEXT ELEMENT into a node. 
            for item in eachList:
                node = ListNode(item,None) # This is the process of converting elements into nodes. Nodes consist of data and pointers. 
                if linkedList.head == None:
                    linkedList.head = node
                if prev:
                    prev.next = node
                prev = node # This holds a reference to the node we just created while we work on transforming the next element into a node.
            
            listOfLinkedLists.append(linkedList)
            # print(listOfLinkedLists)
    
    ## Testing Below (how to print our linked lists) ##
        # for eachList in listOfLinkedLists:
        #     node = eachList.head
        #     while node:
        #         print(node.val)
        #         node = node.next
        #
        # [[1->4->5],[1->3->4],[2->6]]
        
        finalLinkedList = LinkedList()  # -> final = head = [](Node)
        #input -> listOfLinkedLists = [[1->4->5],[1->3->4],[2->6]]
        for eachList in listOfLinkedLists:
            # first time through is first linkedlist -> [1->4->5]
            # can't do a "for loop" like this: for eachItem in eachList:   # Now we are iterating on each node -> Node(1), Node(4), Node(5)
            eachItem = eachList.head
            while eachItem:
                if finalLinkedList.head == None:
                    finalLinkedList.head = ListNode(eachItem.val)       # DON'T FORGET TO MAKE AN ENTIRELY NEW NODE OBJECT SO YOU DON'T KEEP PREVIOUS LINKS!!
                    eachItem = eachItem.next
                    continue
                eachFinalNode = finalLinkedList.head
                # We want to perform something like this -> for eachFinalNode in finalLinkedList:  -> But it's not that simple anymore
                prev = None
                while eachFinalNode:
                    if eachItem.val >= eachFinalNode.val:        # 1st time through -> finalLinkedList = [Node(1)] | we are on eachItem = Node(4) | will create [Node(1) -> Node(4)]
                        prev = eachFinalNode
                        eachFinalNode = eachFinalNode.next
                        continue
                    else:
                        tempNode = ListNode(eachItem.val)
                        prev.next = tempNode
                        tempNode.next = eachFinalNode
                        # while node:
                        #     print(node.val)
                        #     node = node.next
                        # print("next iteration2")
                        break
                if eachFinalNode == None:
                    # print("each:",eachItem.val)
                    # print("prev:",prev.val)
                    prev.next = ListNode(eachItem.val)
                    node = finalLinkedList.head
                    # while node:
                    #     print(node.val)
                    #     node = node.next
                    # print("next iteration1")
                eachItem = eachItem.next

        node = finalLinkedList.head
        finalSortedList = []
        while node:
            # print(node.val)
            finalSortedList.append(node.val)
            node = node.next
        return finalSortedList

# 1. create final linked list object (finalLinkedList = LinkedList())
# 2. iterate through each linkedlist in listOfLinkedLists:
#       3. for each "currentNode" in each linkedlist:
#           4. iterate through each "finalNode" in finalLinkedList until finalNode.val is greater than current currentNode.val,
#              then set previousFinalNode.next to currentNode, and set currentNode.next to finalNode.next
#               - remember to keep track of previous node! (hint: you will likely need to use a temporary variable)
#               - also remember, if you hit the end of the list, just append the currentNode to the previousFinalNode.next


# finalLinkedList = LinkedList()   -> final = head = [](Node)
# input -> listOfLinkedLists = [[1->4->5],[1->3->4],[2->6]]
#   for eachList in listOfLinkedLists:
#       # first time through is first linkedlist -> [1->4->5]
#       for eachItem in eachList:   # Now we are iterating on each node -> Node(1), Node(4), Node(5)
#           if finalLinkedList.head == None:
#               finalLinkedList.head = ListNode(eachItem.val)       # DON'T FORGET TO MAKE AN ENTIRELY NEW NODE OBJECT SO YOU DON'T KEEP PREVIOUS LINKS!!
#               continue
#           eachFinalNode = finalLinkedList.head
#           # We want to perform something like this -> for eachFinalNode in finalLinkedList:  -> But it's not that simple anymore
#           prev = None
#           while eachFinalNode:
#               if eachItem.val >= eachFinalNode.val:        # 1st time through -> finalLinkedList = [Node(1)] | we are on eachItem = Node(4) | will create [Node(1) -> Node(4)]
#                   prev = eachFinalNode
#                   eachFinalNode = eachFinalNode.next
#                   continue
#               else:
#                   tempNode = ListNode(eachItem.val)
#                   prev.next = tempNode
#                   tempNode.next = eachFinalNode
#                   break
#           prev.next = ListNode(eachItem.val)

# we are now at finalLinkedList = [Node(1) -> Node(4) -> Node(5)] | we will be getting a Node(1) from the next list | will create [Node(1) -> Node(1) -> Node(4) -> Node(5)] via else case
# next iteration is [Node(1) -> Node(1) -> Node(4) -> Node(5)], and we are on Node(3) | will create [Node(1) -> Node(1) -> Node(3) -> Node(4) -> Node(5)]



if __name__ == "__main__":
    tmp = Solution()
    tmp.mergeKLists([[1,4,5],[1,3,4],[2,6]])
    # print(tmp)


### This solution below is based on Leetcode already giving as a linked list (if you print linkedlist and list node you can see the structure) ###
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class LinkedList:
    def __init__(self,head=None):
        self.head = head # First list value . Not sure if it matters. Everything will be sorted. 

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        print(lists)
        finalLinkedList = LinkedList()
        for eachHead in lists:
            if eachHead:
                # print(eachHead.val)
                eachItem = eachHead
                while eachItem:
                    if finalLinkedList.head == None:
                        finalLinkedList.head = ListNode(eachItem.val)
                        eachItem = eachItem.next
                        continue
                    eachFinalNode = finalLinkedList.head
                # We want to perform something like this -> for eachFinalNode in finalLinkedList:  -> But it's not that simple anymore
                    prev = None
                    while eachFinalNode:
                        if eachItem.val >= eachFinalNode.val:        # 1st time through -> finalLinkedList = [Node(1)] | we are on eachItem = Node(4) | will create [Node(1) -> Node(4)]
                            prev = eachFinalNode
                            eachFinalNode = eachFinalNode.next
                            continue
                        else:
                            tempNode = ListNode(eachItem.val)
                            if prev == None:
                                prev = eachFinalNode
                                if prev.val > tempNode.val:
                                    tempNode.next = prev
                                    # prev.next = None
                                    finalLinkedList.head = tempNode
                                else:
                                    prev.next = tempNode
                                    tempNode.next = None
                            else:
                                prev.next = tempNode
                                tempNode.next = eachFinalNode
                            # while node:
                            #     print(node.val)
                            #     node = node.next
                            # print("next iteration2")
                            break
                    if eachFinalNode == None:
                        # print("each:",eachItem.val)
                        # print("prev:",prev.val)
                        prev.next = ListNode(eachItem.val)
                        node = finalLinkedList.head
                        # while node:
                        #     print(node.val)
                        #     node = node.next
                        # print("next iteration1")
                    eachItem = eachItem.next
        # print(finalLinkedList)
        node = finalLinkedList.head
        return node
        # print(node)
        # while node:
        #     print(node)
        #     node = node.next