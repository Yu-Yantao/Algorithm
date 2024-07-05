from typing import List


class Solution:
    """
    33. 搜索旋转排序数组
    整数数组 nums 按升序排列，数组中的值 互不相同 。
    数组是经过旋转的，旋转点未知。
    示例 1：

    输入：nums = [4,5,6,7,0,1,2], target = 0
    输出：4
    """

    def search(self, nums: List[int], target: int) -> int:
        """
        思路:二分查找
        原始问题，是对一个分段有序数组进行二分
        但当对被旋转后的数组二分时，至少有一边是有序的，可以判断target是否在有序部分中
        如果在有序部分中，则进行继续二分，否则，对无序部分进行二分（与原始问题相同）
        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 如果左半部分有序
            if nums[0] <= nums[mid]:
                # target在nums[0]和nums[mid]之间
                if nums[0] <= target < nums[mid]:
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
        return left if nums[left] == target else -1


if __name__ == '__main__':
    print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    print(Solution().search(nums=[3, 1], target=1))
