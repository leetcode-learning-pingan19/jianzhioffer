# 
### solution

从右上角开始

#### if 
当前位置的数字小于target,则比当前位置大的数字一定在下一行【row++】
#### elif
 当前位置的数字大于target,则比当前位置大的数字一定在左边的列【col--】


```python
class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 从右上角开始
        if not matrix or not(matrix[0]):
            return False
        m,n = len(matrix),len(matrix[0])
        row,col = 0,n-1
        while row<m and col>=0:
            if matrix[row][col]==target:
                return True
            if matrix[row][col]<target:
                row+=1
            elif matrix[row][col]>target:
                col-=1
        return False
```

### java版本
```java
class Solution {
    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        if(matrix==null||matrix.length==0||matrix[0]==null||matrix[0].length==0){
            return false;
        }
        int m = matrix.length;
        int n = matrix[0].length;
        int row = 0;
        int col = n-1;
        while(row<m&&col>=0){
            if(matrix[row][col]==target){
                return true;
            }
            else if(matrix[row][col]>target){
                col--;
            }
            else{
                row++;
            }
        }
        return false;
    }
}
```