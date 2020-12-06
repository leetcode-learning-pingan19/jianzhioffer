## 思路

利用栈

## code

```c++
class Solution {
public:
    string reverseWords(string s) {
        stack<string> stk;
        string res,str;
        istringstream ss(s);
        while (ss >> str) stk.push(str), stk.push(" ");
        if (!stk.empty()) stk.pop();
        while (!stk.empty()) res += stk.top(), stk.pop();
        return res;
    }
};
```

