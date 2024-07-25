from typing import List


class Solution:
    """
    209. 长度最小的子数组
    给定一个含有 n 个正整数的数组和一个正整数 target 。
    找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

    示例 1：
    输入：target = 7, nums = [2,3,1,2,4,3]
    输出：2

    示例 2：
    输入：target = 4, nums = [1,4,4]
    输出：1
    """

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        ans = float('inf')
        window = 0
        while right < len(nums):
            window += nums[right]
            right += 1
            while window >= target:
                ans = min(ans, right - left)
                window -= nums[left]
                left += 1
        return ans if ans != float('inf') else 0


if __name__ == '__main__':
    print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(Solution().minSubArrayLen(4, [1, 4, 4]))
    print(Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
