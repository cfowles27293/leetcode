# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoListsBetter(self, l1, l2):
        """
             :type l1: ListNode
             :type l2: ListNode
             :rtype: ListNode
             """
        head1 = l1
        head2 = l2

        if head1 == None and head2 == None:
            return None
        elif head2 == None:
            return head1
        elif head1 == None:
            return head2
        else:
            if head1.val < head2.val:
                head1.next = self.mergeTwoListsBetter(head1.next, head2)
            else:
                temp = head2
                head2 = head2.next
                temp.next = head1
                head1 = temp
                head1.next = self.mergeTwoListsBetter(head1.next, head2)
        return head1


    def printSorted(self, head):
        while (head != None):
            print(head.val)
            head = head.next
        return

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


if __name__ == "__main__":
    l1 = ListNode(-3)
    l11 = ListNode(-2)
    l12 = ListNode(-1)
    l1.next = l11
    l11.next = l12

    l2 = ListNode(-1)
    l21 = ListNode(0)
    l22 = ListNode(1)
    l2.next = l21
    l21.next = l22

    s = Solution()
    head = s.mergeTwoListsBetter(l1, l2)
    s.printSorted(head)