# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#O(n) time || O(n) space
def reverseLinkedList(head):
    length = -1
    vals = []
    
    while head:
        length += 1
        vals.append(head.value)
        head = head.next

    reverseLinkedList = LinkedList(0)
    dummy = reverseLinkedList
    while length >= 0:
        print(vals[length])
        dummy.next =  LinkedList(vals[length])
        dummy = dummy.next
        length -= 1

    return reverseLinkedList.next

#0(n) time and 0(1) space
def reverseLinkedList2(head):
    if not head:
        return head

    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

class LinkedList(LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


def test_case_1():
    test = LinkedList(0).addMany([1, 2, 3, 4, 5])
    result = reverseLinkedList(test).getNodesInArray()
    expected = LinkedList(5).addMany([4, 3, 2, 1, 0]).getNodesInArray()
    assert (result == expected)