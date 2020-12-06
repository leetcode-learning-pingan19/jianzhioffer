##  思路

天秀

## 代码

```c++
class Solution {
public:
    string reverseLeftWords(string s, int n) {
        return (s+s).substr(n,s.size());
    }
};
```

