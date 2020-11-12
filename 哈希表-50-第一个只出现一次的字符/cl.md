### solution 1: ordereddict
代码中没有用ordereddict

```python 

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return " "
        dt = dict()
        min_idx = len(s)
        for i,item in enumerate(s):
            if item not in dt:
                dt[item]=i
            else:
                dt[item]=-1
        for k,v in dt.items():
            if v==-1:
                continue
            min_idx = min(min_idx,v)
        if min_idx==len(s):
            return " "
        return s[min_idx]
```

### java版本
```java
class Solution {
    public char firstUniqChar(String s) {
        if(s==null||s.length()==0){
            return ' ';
        }
        HashMap <Character,Integer> map = new HashMap<>();
        int min_pos = s.length();
        for(int i=0;i<s.length();i++){
            if(map.containsKey(s.charAt(i))){
                map.put(s.charAt(i),-1);
            }
            else{
                map.put(s.charAt(i),i);
            }
        }
        for(Map.Entry<Character,Integer> entry:map.entrySet()){
            int val = entry.getValue();
            if(val!=-1){
                min_pos = Math.min(min_pos,val);
            }
        }
        return min_pos>=s.length() ? ' ':s.charAt(min_pos);
    }
}
```
