from typing import List


class Solution:
    """
    峰值元素是指其值严格大于左右相邻值的元素。
    给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
    你可以假设 nums[-1] = nums[n] = -∞ 。

    示例 1：

    输入：nums = [1,2,3,1]
    输出：2
    解释：3 是峰值元素，你的函数应该返回其索引 2。
    示例 2：

    输入：nums = [1,2,1,3,5,6,4]
    输出：1 或 5
    解释：你的函数可以返回索引 1，其峰值元素为 2；
         或者返回索引 5， 其峰值元素为 6。
    """
    def findPeakElement(self, nums: List[int]) -> int:
        """
        详见宫水三叶的题解
        https://leetcode.cn/problems/find-peak-element/solutions/998441/gong-shui-san-xie-noxiang-xin-ke-xue-xi-qva7v/

        1.nums[-1] = nums[n] = -∞
        2.元素
        :param nums:
        :return:
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    print(Solution().findPeakElement([1, 2, 3, 1]))