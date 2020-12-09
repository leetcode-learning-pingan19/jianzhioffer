## 思路

本体其实也不算难，就是读取数据流到数组，然后排序，取中位数即可。

优化点在于每次取中位数时，不是堆数组排序然后取值，而是插入数据时就维护一个有序数组：使用一个大堆一个小堆实现，各维护近一半的数据。

## code

```cpp
class MedianFinder {
public:
    std::priority_queue<int> big;
    std::priority_queue<int, vector<int>, greater<int>> small;
    /** initialize your data structure here. */
    MedianFinder() {

    }
    
    void addNum(int num) {
        big.push(num);
        small.push(big.top());
        big.pop();
        if ((small.size() - big.size()) > 1) {
            big.push(small.top());
            small.pop();
        }
    }
    
    double findMedian() {
        if (small.size() > big.size()) {
            return small.top();
        } else {
            return (small.top() + big.top()) / double(2);
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
```

