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

def creat_linked_list(arr):
    head = None
    for a in arr:
        head = ListNode(a, next=head)
    return head


if __name__ == "__main__":
    list1 = [9, 9, 9, 9, 9, 9, 9]
    list2 = [9, 9, 9, 9]
    llist1 = creat_linked_list(list1)
    llist2 = creat_linked_list(list2)
    obj = AddTwoNumbers()
    # print(obj.addTwoNumbers(llist1, llist2))
    x = obj.addTwoNumbers(llist1, llist2)
    arr = []
    while x != None:
        arr.append(x.val)
        x = x.next
    print(arr)
