## 思路

* 遍历求解
* 二分法找到target的一个坐标，然后向两边扩散
* 二分法找到target的左右边界值（真好啊）

## 代码

```c++
class Solution {
public:
    int search(vector<int>& nums, int target)
    {
        int len = nums.size();
        if(len == 0)    return 0;
        int left = 0, right = len - 1;
        int boundaryLeft ,boundaryRight;    //target的左右边界
        //第一次二分法求出右边界：boundaryRight
        while(left <= right)    //正是left=right时的这最后这次循环，left又右移了一次使得left成为右边界
        {
            int mid = left + (right - left) / 2;
            if(nums[mid] <= target) //等号在left这里
                left = mid + 1;
            else
                right = mid - 1;    
        }   //退出循环时left为最右target的右边元素，right则应为最右边的target（若target存在）

        if(right >= 0 && nums[right] != target) //血的教训，第一个条件一定放前面
            return 0;
        boundaryRight = left;

        //第二次二分法求出左边界：boundaryLeft
        right = left, left = 0;
        while(left <= right)    //正是left=right时的这最后这次循环，right又左移了一次使得right成为左边界
        {
            int mid = left + (right - left) / 2;
            if(nums[mid] >= target) //等号在right这里
                right = mid - 1;
            else
                left = mid + 1;
        }   //退出循环时right为最左target的左边元素
        boundaryLeft = right;

        return boundaryRight - boundaryLeft - 1;
    }
};
```

