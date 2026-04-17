# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # merge list1 and list2
        i, j = 0, 1
        h1, h2 = list1, list2
        dummy = ListNode()
        cur = dummy

        while h1 is not None and h2 is not None:
            if h1.val <= h2.val:
                cur.next = h1
                h1 = h1.next
            else:
                # h1.val > h2.val
                cur.next = h2
                h2 = h2.next
            cur = cur.next
        
        if h1 is None:
            cur.next = h2
        else:
            cur.next = h1

        # dummy.next is the merged head
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2

        merged_left = self.mergeKLists(lists[0:mid])
        merged_right = self.mergeKLists(lists[mid:])

        merged = self.merge_two_lists(merged_left, merged_right)
        return merged