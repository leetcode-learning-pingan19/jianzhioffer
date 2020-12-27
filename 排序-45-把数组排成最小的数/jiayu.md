## 思路

比较字符串拼接后谁更大，所以就是sort里面增加一个自定义比较函数

## code

```c++
class Solution {
public:
    static bool mySortFunction(std::string i, std::string j) {
        return (i + j) < (j + i);
    }

    string minNumber(vector<int>& nums) {
        std::string res;
        std::vector<std::string> nums_string;
        for (auto num : nums) {
            nums_string.push_back(to_string(num));
        }
        std::sort(nums_string.begin(), nums_string.end(), mySortFunction);
        for (auto num_string : nums_string) {
            res += num_string;
        }
        return res;
    }

    
};
```

