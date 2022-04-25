from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class AddTwoNumbers:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, c=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10)

        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, c)
        return ret

if __name__ == "__main__":
    obj = AddTwoNumbers()
    l1 = ListNode(0)
    l2 = ListNode(0)
    print(l1, type(l1))
    list1 = [2, 4, 3]
    list2 = [5, 6, 4]
    for l in list1:
        l1.val = l
        l1.next = ListNode(0)
    print(l1.val, l1.next)
    # print(obj.addTwoNumbers(l1, l2))