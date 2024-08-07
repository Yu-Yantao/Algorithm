import queue
import heapq
from typing import List


class Solution:
    """
    239. 滑动窗口最大值
    给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
    返回 滑动窗口中的最大值 。

    示例 1：
    输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
    输出：[3,3,5,5,6,7]
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """

        :param nums:
        :param k:
        :return:
        """
        size = len(nums)
        # 构造优先队列，优先队列默认顺序是从小到大，此处取反，即可得到一个顺序是从大到小的优先队列，下标在后续移除元素时会用到
        """
        这里的队列的大小是不固定的，不可以定为k，以[1,3,-1,-3,5,3,6,7]为例，窗口由[1,3,-1]A变为[3,-1,-3]B的过程中，队列无法与窗口保持一致。
        A窗口最大值为3，同时也是作为B窗口的最大值，如果将3出队，那B窗口中的最大值就无法计算了。
        
        所以，这里的处理方式时，不断扩大队列，通过对比队首元素和窗口左边界，如果在窗口内，队首元素就是当前窗口的最大值；如果队首元素不在窗口内，
        则要将队首元素出队，直到队首元素在窗口内时，更新结果
        """
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        # 取出队首元素
        res = [-q[0][0]]

        for i in range(k, size):
            # 新元素入队
            heapq.heappush(q, (-nums[i], i))
            # 使用下标判断队首元素是否在窗口内，如果不在窗口内(i-k, i]，则要将队首元素出队，直到队首元素在窗口内
            while q[0][1] <= i - k:
                heapq.heappop(q)
            res.append(-q[0][0])
        return res


if __name__ == '__main__':
    print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
