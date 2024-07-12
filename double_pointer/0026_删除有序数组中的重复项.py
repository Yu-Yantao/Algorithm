from typing import List


class Solution:
    """
    26. 删除有序数组中的重复项
    给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
    元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

    示例 1：
    输入：nums = [1,1,2]
    输出：2, nums = [1,2,_]
    解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        思路：双指针，利用快慢指针slow，fast，保证[0, slow]区间内无重复项
        当nums[slow] == nums[fast]时，slow不动，fast右移（过滤掉所有nums[slow]）
        当nums[slow] != nums[fast]时，slow + 1，将nums[fast]赋值给nums[slow+1]。
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return 1
        s, f = 0, 1
        while f < len(nums):
            if nums[s] != nums[f]:
                s += 1
                nums[s] = nums[f]
            f += 1
        print(nums[:s + 1])
        return s + 1


if __name__ == '__main__':
    print(Solution().removeDuplicates([1, 1, 2]))
