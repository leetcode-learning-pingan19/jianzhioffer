### solution 1 :
前后指针
注意判断第一个head为val的特殊情况
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        if head.val == val:
            return head.next
        prev = head
        cur = head.next
        while cur:
            if cur.val==val:
                prev.next = cur.next
                break
            else:
                cur = cur.next
                prev = prev.next
        return head

```

### java version
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
    public ListNode deleteNode(ListNode head, int val) {
        if(head==null){
            return head;
        }
        if(head.val==val){
            return head.next;
        }
        ListNode prev=head;
        ListNode cur=head.next;
        while(cur!=null){
            if(cur.val==val){
                prev.next = cur.next;
                break;
            }
            else{
                prev = prev.next;
                cur = cur.next;
            }
        }
        return head;
    }
}
```