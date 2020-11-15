# 思路
1. 递归


# 代码
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        ret = []
        def dfs(node):
            if not node:
                return
            else:
                dfs(node.next)
            ret.append(node.val)

        dfs(head)

        return ret

```