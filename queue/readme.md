# 优先队列

## 1.介绍

优先队列是一种特殊的队列，入队与普通队列相同，但出队与普通队列不同。

优先队列中的元素在出队时，要按照**优先级**顺序出队，也就是说，优先队列中的元素，都有一个**优先级**。

以[1, 5, 3, 7, 2]为例(元素值即代表优先级)，出队顺序，[7, 5, 3, 2, 1]。

优先队列可以通过数组或链表实现，使用数组，在出队时，需要遍历找出优先级最高的元素，时间复杂度O(n)
；使用链表，可以在入队时保证有序，时间复杂度O(n)，出队时取出队首元素。

另一种高效实现优先队列的方式是使用**二叉堆**，二叉堆入队和出队的时间复杂度均为O(log n)。

优先队列适用场景:

- 任务调度
- 排序问题，第k个元素

## 2 有意思的题目

- 347.前 K 个高频元素

## 3.总结

### 3.1 TopK问题

以[347.前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/description/)为例，介绍两种解决思路。

1. 小顶堆

```python
import collections
import heapq
from typing import List


class Solution:
    """
    347. 前 K 个高频元素
    给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

    示例 1:
    输入: nums = [1,1,1,2,2,3], k = 2
    输出: [1,2]

    示例 2:
    输入: nums = [1], k = 1
    输出: [1]
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 计数器
        counter = collections.Counter(nums)
        # 优先队列
        queue = []
        # 堆化
        heapq.heapify(queue)
        # 遍历计数器
        for i, e in enumerate(counter):
            # i小于k时，直接入堆
            if i < k:
                heapq.heappush(queue, (counter[e], e))
            # i大于k时，意味着堆中已经有了K个元素，如果要加入新元素，先要移除旧元素
            else:
                # 如果堆定元素出现的次数(queue[0]代表堆顶元素，queue[0][0]，代表堆顶元素出现的次数)小于新元素出现的次数，则堆顶元素一定不满足要求
                if queue[0][0] < counter[e]:
                    heapq.heappop(queue)
                    heapq.heappush(queue, (counter[e], e))

        return [e[1] for e in queue]
```

2. 大顶堆

```python
import collections
import heapq
from typing import List


class Solution:
    """
    347. 前 K 个高频元素
    给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

    示例 1:
    输入: nums = [1,1,1,2,2,3], k = 2
    输出: [1,2]

    示例 2:
    输入: nums = [1], k = 1
    输出: [1]
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 计数器
        counter = collections.Counter(nums)
        # 构建一个数组，[(num, count(num)), ...]，Python的优先队列默认是从小到大的，这里使用取反的方式，构建一个最大堆
        queue = [(-counter[e], e) for e in counter]
        # 堆化
        heapq.heapify(queue)
        ans = []
        # 循环取K次堆顶元素
        for num in range(k):
            ans.append(heapq.heappop(queue)[1])
        return ans
```
> 小顶堆是在建堆过程中求解，堆中元素即是结果；大顶堆是先进行建堆，然后取出元素。相比之下，本题中，使用小顶堆更优。