class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        # ll = head
        # count = 0
        # while ll:
        #     count += 1
        #     ll = ll.next

        # ll = head
        # middle = 0
        # count = count // 2
        # print(ll)
        # while middle != count:
        #     middle += 1
        #     ll = ll.next
        # return ll
