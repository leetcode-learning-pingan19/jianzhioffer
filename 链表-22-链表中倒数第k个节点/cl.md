### solution: 双指针

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        fast,slow = head,head
        i = 0
        while i<k and fast:
            fast = fast.next
            i+=1 
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
        
```

### java 
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode getKthFromEnd(ListNode head, int k) {
        ListNode slow=head;
        ListNode fast=head;
        int i=0;
        while(i<k&&fast!=null){
            fast = fast.next;
            i++;
        }
        while(fast!=null&&slow!=null){
            fast = fast.next;
            slow = slow.next;
        }
        return slow;

    }
}
```