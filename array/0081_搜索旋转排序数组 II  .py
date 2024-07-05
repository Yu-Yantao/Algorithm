from typing import List


class Solution:
    """
    81. 搜索旋转排序数组 II
    已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。
    给你 旋转后 的数组 nums 和一个整数 target ，
    请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。

    示例 1：
    输入：nums = [2,5,6,0,0,1,2], target = 0
    输出：true
    """

    def search(self, nums: List[int], target: int) -> bool:
        """
        思路：二分查找
        整体思路与33题相似，但此处有相同元素，如[1, 0, 1, 1, 1]这种情况
        left,mid,right相等，此时，可以直接缩小left，right
        只要left，right，mid，三者不完全相同，至少有一边是有序的，回归到对分段有序数组的二分
        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return False
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            # left，right，mid相等，缩小left，right
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            # 如果左半部分有序
            elif nums[left] <= nums[mid]:
                # target在nums[0]和nums[mid]之间
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # target不在nums[0]和nums[mid]之间，去右边找
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
        # 退出while循环，left和right重合，判断target是否在nums[left]和nums[right]之间
        return True if nums[left] == target else False


if __name__ == '__main__':
    print(Solution().search([2, 5, 6, 0, 0, 1, 2], 0))
    print(Solution().search([1, 0, 1, 1, 1], 0))
