from typing import List


class Solution:
    """
    485. 最大连续 1 的个数
    给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。

    示例 1：
    输入：nums = [1,1,0,1,1,1]
    输出：3
    解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
    """

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0, 0
        res = 0
        while right < len(nums):
            if nums[right] == 1:
                res = max(res, right - left + 1)
            else:
                left = right + 1
            right += 1
        return res


if __name__ == '__main__':
    print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
