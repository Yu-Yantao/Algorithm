from typing import List


class Solution:
    """
    485. 最大连续 1 的个数
    输入一个只包含 0 和 1 的二进制数组，找出只包含 1 的最长连续子数组（包含多个 1）的长度。

    示例 1：
    输入：nums = [1,1,0,1,1,1]
    输出：3
    解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
    """

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # 统计连续1的个数
        cnt = 0
        # 最大连续1的个数
        ans = 0
        for i in range(len(nums)):
            # 遇到1，计数器加1，并更新最大值
            if nums[i] != 0:
                cnt += 1
                ans = max(ans, cnt)
            # 遇到0，计数器清零
            else:
                cnt = 0

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxConsecutiveOnes([1, 1, 0, 1]))
