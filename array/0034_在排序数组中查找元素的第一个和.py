from typing import List


class Solution:
    """
    34. 在排序数组中查找元素的第一个和最后一个位置
    给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
    如果数组中不存在目标值 target，返回 [-1, -1]。

    示例 1：
    输入：nums = [5,7,7,8,8,10], target = 8
    输出：[3,4]
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        # 找到左边界
        while l <= r:
            mid = (l + r) // 2
            # num[mid]大于等于target时，缩小右边界
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        # 未找到target，返回[-1,-1]
        if l >= len(nums) or nums[l] != target:
            return [-1, -1]
        # 从左边界开始向右找
        r = l
        while r < len(nums):
            if nums[r] == target:
                r += 1
            else:
                break
        return [l, r - 1]


if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 9))
