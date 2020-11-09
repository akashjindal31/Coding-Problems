"""
LINKEDLIST MERGE SORT

"""

# Class to create an Linked list with an Null head pointer
class LinkedList:
    def __init__(self):
        self.head = None

    # append new_node in the linkedlist with the given data
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
    
    # sorting of linked list using merge sort in O(nlogn) time complexity
    def mergeSort(self, head):
        if head == None or head.next == None:
            return head

        middle = self.printMiddle(head)
        nextToMiddle = middle.next

        middle.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(nextToMiddle)

        sortedList = self.sortedMerge(left, right)
        return sortedList

    # helper function for merge sort to compare two elements of partitioned linkedlist.
    def sortedMerge(self, left, right):
        sortedList = None
        if left == None:
            return right
        if right == None:
            return left

        if left.data <= right.data:
            sortedList = left
            sortedList.next = self.sortedMerge(left.next, right)
        else:
            sortedList = right
            sortedList.next = self.sortedMerge(left, right.next)
        return sortedList

    # add two linkedlist nodes to create a new linkedlist with the sum of their values.
    def addLists(self, first, second):
        temp = None
        prev = None
        carry = 0
        while first is not None or second is not None:
            fData = 0 if first == None else first.data
            sData = 0 if second == None else second.data
            Sum = carry + fData + sData
            carry = 1 if Sum >= 10 else 0
            Sum = Sum if Sum < 10 else Sum % 10

            temp = Node(Sum)
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            prev = temp
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
        if carry > 0:
            temp.next = Node(carry)

    # print linkedlist data
    def printList(self, head):
        if head is None:
            print(" ")
        curr_node = head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print(" ")

    # get middle of an linkedlist, middle in case of odd else second element in middle.
    def printMiddle(self, head):  
        slow = head 
        fast = head 
        while (fast != None and fast.next != None): 
            slow = slow.next
            fast = fast.next.next     
        return slow
   
    # recursively reverse the given list by changing the links of given list.
    def reverseList(self, node):
        if node == None:
            return node
        if node.next == None:
            return node

        node1 = self.reverseList(node.next)
        node.next.next = node
        node.next = None
        return node1

    # insert new node at the beginning of given linked list
    def insertNode(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


# class to create a new node of an linkedlist
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    nodes = int(input("Enter number of nodes for linkedlist: "))
    llist = LinkedList()
    while nodes > 0:
        data = int(input("Enter data for node: "))
        llist.append(data)
        nodes -= 1
    llist.printList(llist.head)

    data = int(input("Enter data for new Node: "))
    llist.insertNode(data)
    llist.printList(llist.head)
    # llist.reverseList(llist.head)

    # nodes = int(input("Enter number of nodes for second linkedlist: "))
    # llist1 = LinkedList()
    # while nodes > 0:
        # data = int(input("Enter data for node: "))
        # llist1.append(data)
        # nodes -= 1

    # newList = LinkedList()
    # newList.addLists(llist.head, llist1.head)
 
    # newList.head = newList.mergeSort(newList.head)

    

