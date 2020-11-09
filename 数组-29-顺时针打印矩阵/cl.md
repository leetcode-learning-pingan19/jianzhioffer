## solution 1:思路，将每一圈视作一层,时间复杂度为O(MN)
### 1）从(top,left)到（top,right)
### 2) 从(top+1,right)到(bottom,right)
### 3) 【需要判断是不是有多行,即top<bottom，否则会与1有重复】从(bottom,right-1)到(bottom,left)
### 4) 【需要判断是不是有多列,即left<right，否则会与3有重复】从(bottom-1,left)到(top+1,left)
### 每圈结束后，更新四个坐标
### 循环的条件为top<=bottom and left<=right 
```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m,n = len(matrix),len(matrix[0])
        top,bottom=0,m-1
        left,right = 0,n-1
        res = []
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            for i in range(top+1,bottom+1):
                res.append(matrix[i][right])
            if top<bottom:
                for i in range(right-1,left-1,-1):
                    res.append(matrix[bottom][i])
            if left<right:
                for i in range(bottom-1,top,-1):
                    res.append(matrix[i][left])
            top+=1
            bottom-=1
            left+=1
            right-=1
        return res
```

## solution1 的java版本

```java
class Solution {
    public int[] spiralOrder(int[][] matrix) {
        if(matrix==null||matrix.length==0||matrix[0].length==0){
            return new int[0];
        }
        int m = matrix.length;
        int n = matrix[0].length;
        int[] res= new int[m*n];
        int top=0, bottom = m-1, left = 0, right=n-1;
        int idx = 0;
        while(top<=bottom&&left<=right){
            for(int i=left;i<right+1;i++){
                res[idx]=matrix[top][i];
                idx++;
            }
            for(int i=top+1;i<bottom+1;i++){
                res[idx]=matrix[i][right];
                idx++;
            }
            if(top<bottom){
                for(int i=right-1;i>left-1;i--){
                res[idx]=matrix[bottom][i];
                idx++;
            }
            }
            if(left<right){
                for(int i=bottom-1;i>top;i--){
                res[idx]=matrix[i][left];
                idx++;
            }
            }
            top++;
            left++;
            bottom--;
            right--;
        }
        return res;
    }
}
```