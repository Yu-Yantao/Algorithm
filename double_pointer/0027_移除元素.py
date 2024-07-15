from typing import List


class Solution:
    """
    27. 移除元素
    给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。

    示例 1：
    输入：nums = [3,2,2,3], val = 3
    输出：2, nums = [2,2,_,_]
    解释：你的函数函数应该返回 k = 2, 并且 nums 中的前两个元素均为 2。
    你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        """
        思路：使用双指针，slow，fast，保证[0,slow]内的元素是合规的
        初始时，slow，fast指向第一个元素，当nums[fast] == val时，fast后移，否则进行覆盖
        :param nums:
        :param val:
        :return:
        """
        if not nums:
            return 0
        if len(nums) <= 1 and nums[0] == val:
            return 0
        if len(nums) <= 1:
            return 1
        slow, fast = 0, 0
        while fast < len(nums) - 1:
            if nums[fast] == val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        print(nums[:slow])
        return slow


if __name__ == '__main__':
    print(Solution().removeElement([3, 2, 2, 3], 3))
