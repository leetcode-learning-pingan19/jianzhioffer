### solution

先序遍历第一个元素为根节点，找到在中序遍历中的位置，将中序遍历分成左右两个子树的中序遍历，根据其数量，再将对应的剩下的先序遍历分成左右两个子树的中序遍历，可见使用递归可以解决，终止条件为，中序遍历的left>right,返回空

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        dt ={item:i for i,item in enumerate(inorder)}
        def _func(root,left,right):
            if left>right:
                return None
            root_val = preorder[root]
            node = TreeNode(root_val)
            new_root = dt[root_val]
            node.left = _func(root+1,left,new_root-1)
            node.right = _func(root+new_root-left+1,new_root+1,right)
            return node
        return _func(0,0,len(preorder)-1)

            


        
```