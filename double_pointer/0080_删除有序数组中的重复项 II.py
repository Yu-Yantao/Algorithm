from typing import List


class Solution:
    """
    80. 删除有序数组中的重复项 II
    给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
    不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

    示例 1：
    输入：nums = [1,1,1,2,2,3]
    输出：5, nums = [1,1,2,2,3]
    解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3。 不需要考虑数组中超出新长度后面的元素。
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        思路：快慢指针，[0,slow]是合规元素，fast是当前遍历到的元素。
        在26题中，要求我们删除重复元素，我们可以固定slow，fast指向slow的下一个元素，向后遍历。
        当nums[slow] = nums[fast]时，就意味着出现了重复元素。

        在本题中，题目要求删除出现次数大于2的元素，使得出现次数超过两次的元素只出现两次。
        一种思路是记录一个起始位置，记录这个元素出现了几次，然后将slow移动到合适的位置。

        另一种思路是，我们可以将slow，fast的起始位置，设置为2，如果nums[slow - 2] = nums[fast]
        说明nums[slow - 2] = nums[slow - 1] = nums[slow]，意味着这个元素出现了至少三次，此时移动fast，过滤掉不合法的重复元素
        :param nums:
        :return:
        """
        if len(nums) <= 2:
            return len(nums)
        slow, fast = 2, 2
        while fast < len(nums):
            if nums[slow - 2] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow


if __name__ == '__main__':
    print(Solution().removeDuplicates([1, 1, 1, 1, 1, 2, 2, 3]))
