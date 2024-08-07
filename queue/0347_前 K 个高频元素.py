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


if __name__ == '__main__':
    print(Solution().topKFrequent([-1, -1, -1, -2, -2, -3], 2))
    print(Solution().topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
