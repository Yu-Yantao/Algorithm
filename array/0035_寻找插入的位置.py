from typing import List


class Solution:
    """
    35. 搜索插入位置
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

    示例 1:
    输入: nums = [1,3,5,6], target = 5
    输出: 2

    示例 2:
    输入: nums = [1,3,5,6], target = 2
    输出: 1
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        思路：找到第一个大于等于target的数，返回其索引
        :param nums:
        :param target:
        :return:
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # num[mid]大于等于target时，缩小右边界
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    print(Solution().searchInsert([1, 3, 5, 6], 5))
    print(Solution().searchInsert([1, 3, 5, 6], 2))
