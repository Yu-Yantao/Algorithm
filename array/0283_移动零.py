from typing import List


class Solution:
    """
    283. 移动零
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

    示例 1:
    输入: nums = [0,1,0,3,12]
    输出: [1,3,12,0,0]
    """

    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        l, r = 0, 0
        while r < n:
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1


if __name__ == '__main__':
    s = Solution()
    array = [0, 1, 0, 3, 12]
    s.moveZeroes(array)
    print(array)
