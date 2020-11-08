# solution1: 集合遍历第二次出现的数字， 空间复杂度和时间复杂度均为O(N)
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for i in nums:
            if i in s:
                return i
            s.add(i)
        return -1
# solution2: 原地交换，将k放到num[k],如果出现相同的数字，则返回，如果不相同则交换位置,无额外空间，空间复杂度为O(1)，时间复杂度为O(N),因为针对一个数字最多进行一次“安置”
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        i =0 
        while i<l:
            if nums[i]==i:
                i+=1
                continue
            if nums[nums[i]]==nums[i]:
                return nums[i]
            tmp = nums[nums[i]]
            nums[nums[i]] = nums[i]
            nums[i] = tmp
        return -1

# solution3: java版本的solution2
class Solution {
    public int findRepeatNumber(int[] nums) {
        int i = 0;
        int l = nums.length;
        while(i<l){
            if(nums[i]==i){
                i++;
                continue;
            }
            if(nums[nums[i]]==nums[i]){
                return nums[i];
            }
            int tmp;
            tmp = nums[nums[i]];
            nums[nums[i]] = nums[i];
            nums[i]=tmp;
        }
        return -1;
    }
}