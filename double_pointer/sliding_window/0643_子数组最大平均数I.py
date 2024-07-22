from typing import List


class Solution:
    """
    643. 子数组最大平均数 I
    给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
    请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。

    示例 1：
    输入：nums = [1,12,-5,-6,50,3], k = 4
    输出：12.75
    解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
    """
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_total = total = sum(nums[:k])
        n = len(nums)

        for i in range(k, n):
            # 移除窗口最左边的元素，添加窗口最右边的元素
            total = total - nums[i - k] + nums[i]
            max_total = max(max_total, total)

        return max_total / k


if __name__ == '__main__':
    print(Solution().findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
    print(Solution().findMaxAverage(nums=[5], k=1))
    print(Solution().findMaxAverage(nums=[0, 1, 1, 3, 3], k=4))
