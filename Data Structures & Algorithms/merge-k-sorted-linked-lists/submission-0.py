# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

            dummy = ListNode()
            curr = dummy

            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            
            curr.next = list1 if list1 else list2

            return dummy.next
                    
        while len(lists) >= 2:
            merged_lists = []
            
            for idx in range(0, len(lists), 2):
                list1 = lists[idx]
                list2 = lists[idx + 1] if idx + 1 < len(lists) else None

                merged_lists.append(mergeTwoLists(list1, list2))

            lists = merged_lists

        return lists[0]    