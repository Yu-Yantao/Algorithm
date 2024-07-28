from typing import List


class Solution:
    """
    1658. 将 x 减到 0 的最小操作数
    给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。
    如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。

    示例 1：
    输入：nums = [1,1,4,2,3], x = 5
    输出：2

    示例 2：
    输入：nums = [5,6,7,8,9], x = 4
    输出：-1
    """

    def minOperations(self, nums: List[int], x: int) -> int:
        """
        思路: 可以转化一下思路，当我们求出一个和为 sum(nums) - target 的 最长 子数组，那么剩余的部分，和一定是一个和为 target 的 最短 子数组
        :param nums:
        :param x:
        :return:
        """
        count = sum(nums) - x
        if count < 0:
            return -1
        if count == 0:
            return len(nums)
        left, right = 0, 0
        window = 0
        ans = float('-inf')
        while right < len(nums):
            # 不断扩大窗口
            window += nums[right]
            # 循环缩小窗口，直到小于等于count
            while window > count:
                window -= nums[left]
                left += 1
            # 如果等于count，则说明找到了一个和为count的子数组，则更新最大长度
            if window == count:
                ans = max(ans, right - left + 1)
            right += 1
        return len(nums) - ans if ans != float('-inf') else -1


if __name__ == '__main__':
    print(Solution().minOperations([1, 1, 4, 2, 3], 5))
    print(Solution().minOperations([5, 6, 7, 8, 9], 4))
    print(Solution().minOperations([3, 2, 20, 1, 1, 3], 10))
