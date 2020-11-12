### solution 1: 动态规划的方法

时间复杂度O(N),空间复杂度O(1)

此方法等同于双指针；维护一个26个字母的dict，记作dt，记录最新出现的位置
$f(0)=1$

if $s[i]$ not in $dt$:

$f(i) = f(i-1)+1$



else:

计算距离$d=i-dt[s[i]]$

if 上次出现的字符在前一个位置的最长字符串中间$(d<=f(i-1))$ :

$f(i)=d$

else:(上次出现的字符在前一个位置的最长字符之外)

$f(i)=f(i-1)+1$

最大的f(x)则为最长不重复子串的长度

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 1 # 全局
        last_max_pos = 1 # 记录以当前位置字符结束的最长不重复子串的长度
        last_pos={s[0]:0}
        for i in range(1,len(s)):
            if s[i] not in last_pos:
                last_max_pos += 1
            else:
                d = i-last_pos[s[i]]
                last_max_pos = d if d<=last_max_pos else last_max_pos+1
            last_pos[s[i]]=i
            res = max(last_max_pos,res)
        return res
```

### java 版本
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s==null||s.length()==0){
            return 0;
        }
        int last_max_value = 1;
        int res = 1;
        HashMap<Character,Integer> map = new HashMap<>();
        map.put(s.charAt(0),0);
        for(int i=1;i<s.length();i++){
            if(map.containsKey(s.charAt(i))!=true){
                last_max_value+=1;
            }
            else{
                int dist = i-map.get(s.charAt(i));
                last_max_value = dist<=last_max_value ? dist:last_max_value+1;
            }
            map.put(s.charAt(i),i);
            res = Math.max(res,last_max_value);
        }
        return res;

    }
}
```

