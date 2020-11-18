### solution

- 使用hashmap维护已经访问过的node，
- 使用深度遍历复制各个节点
  
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        def dfs(head):
            if not head:
                return head
            if head in visited:
                return visited[head]
            copy = Node(head.val,None,None)
            visited[head] = copy
            copy.next = dfs(head.next)
            copy.random = dfs(head.random)
            return copy
        visited = {}
        return dfs(head)
            
```

### java version

```python
/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/
class Solution {
    public Node dfs(Node head, HashMap<Node,Node> visited){
        if(head==null){
            return head;
        }
        if(visited.containsKey(head)){
            return visited.get(head);
        }
        Node copy = new Node(head.val,null,null);
        visited.put(head,copy);
        copy.next = this.dfs(head.next,visited);
        copy.random = this.dfs(head.random,visited);
        return copy;
    }
    public Node copyRandomList(Node head) {
        HashMap<Node,Node> visited= new HashMap<Node,Node>();
        return this.dfs(head,visited);

    }
}
```