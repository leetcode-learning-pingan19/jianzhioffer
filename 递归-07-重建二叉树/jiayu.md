## 思路

根据前序遍历、中序遍历的特点来

* 前序遍历分为三段
  * 第一段是一个根节点
  * 第二段是左子树
  * 第三段是右子树
* 中序遍历也分为三段
  * 第一段是左子树
  * 第二段是一个根节点
  * 第三段是右子树

综上可知，通过前序遍历，我们可以获得根节点，通过根节点便可将中序遍历分为左右子树，然后用该左右子树及前序遍历中左右子树的根节点递归，直到最后。

## code

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        this->preorder = preorder;
        for (int i = 0; i < inorder.size(); ++i) {
            inorder_index_map[inorder[i]] = i;
        }
        return buildRecurse(0, 0, inorder.size() - 1);
    }

private:
    std::vector<int> preorder;
    std::unordered_map<int, int> inorder_index_map;
    TreeNode* buildRecurse(int root_pos_pre, int left_in, int right_in) {
        if (right_in < left_in) {
            return nullptr;
        }
        int root_pos_in = inorder_index_map[preorder[root_pos_pre]];
        TreeNode* node = new TreeNode(preorder[root_pos_pre]);
        node->left = buildRecurse(root_pos_pre + 1, left_in, root_pos_in - 1);
        node->right = buildRecurse(root_pos_pre + root_pos_in - left_in + 1, root_pos_in + 1, right_in);
        return node;
    }
};
```

