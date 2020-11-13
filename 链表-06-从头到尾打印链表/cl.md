### solution 1 栈

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = list()
        if not head:
            return []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        res = list()
        while stack:
            res.append(stack.pop())
        return res
```

### java 版本

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
    public int[] reversePrint(ListNode head) {
        if(head==null){
            return new int[0];
        }
        ListNode cur = head;
        Stack<ListNode> stack = new Stack<>();
        while(cur!=null){
            stack.push(cur);
            cur = cur.next;
        }
        int[] res = new int[stack.size()];
        int i=0;
        while(!stack.isEmpty()){
            res[i] = stack.pop().val;
            i++;
        }
        return res;
    }
}
```

### solution 2 : 递归
```python 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if not head:
            return []
        res = []
        def func(cur):
            if cur.next:
                func(cur.next)
            res.append(cur.val)
        cur = head
        func(cur)
        return res
        
```

### java 版本

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
    private void recu(ListNode cur, int[] res,int i){
        if(cur.next!=null){
            this.recu(cur.next,res,i-1);
        }
        res[i] = cur.val;
    }
    public int[] reversePrint(ListNode head) {
        if(head==null){
            return new int[0]; 
        }
        int cnt=0;
        ListNode cur =head;
        while(cur!=null){
            cnt++;
            cur = cur.next;
        }
        int[] res = new int[cnt];
        this.recu(head,res,cnt-1);
        return res;
    }
}
```