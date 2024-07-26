from typing import List


class Solution:
    """
    1004. 最大连续1的个数 III
    给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。

    示例 1：
    输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
    输出：6
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        思路: 控制窗口内只能有 k 个 0 。
        统计窗口内的 0 的个数，当个数大于 k 时，缩小窗口。
        :param nums:
        :param k:
        :return:
        """
        zero_count = 0
        left, right = 0, 0
        ans = 0
        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            right += 1
            # 每次只需要处理一个数字，所以不需要使用while循环
            if zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            # 更新结果，但是不能加判断 if zero_count == k ，因为 k 是可以反转的最大次数，但不一定要反转 k 次，并且在上述缩小窗口后，窗口内的 zero_count 不会大于 k 。
            ans = max(ans, right - left)
        return ans


if __name__ == '__main__':
    print(Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
    print(Solution().longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
    print(Solution().longestOnes([0, 0, 0, 1], 4))
