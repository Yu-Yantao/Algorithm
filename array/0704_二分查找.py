from typing import List


class Solution:
    """
    704. 二分查找
    给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

    示例 1:
    输入: nums = [-1,0,3,5,9,12], target = 9
    输出: 4
    """
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


if __name__ == '__main__':
    print(Solution().search([-1, 0, 3, 5, 9, 12], 13))
    print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
    print(Solution().search([-1, 0, 3, 5, 9, 12], -1))
