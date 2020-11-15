# 思路
1. 先找到第k个节点
2. 第1个节点和第k个节点同时向后移动，当第k个节点到尾部后，第一个节点正好在倒数第k个节点

# 代码

```python
### 解题思路
此处撰写解题思路

### 代码

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None       
        k_node = head
        for _ in range(k):
            k_node = k_node.next
        while k_node:
            k_node = k_node.next
            head = head.next

        return head
```