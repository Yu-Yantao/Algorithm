from typing import List


class Solution:
    """
    503. 下一个更大元素 II
    给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。
    数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。

    示例 1:
    输入: nums = [1,2,1]
    输出: [2,-1,2]

    示例 2:
    输入: nums = [1,2,3,4,3]
    输出: [2,3,4,-1,4]
    """
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1] * n * 2
        nums = nums + nums
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        return ans[:n]


if __name__ == '__main__':
    print(Solution().nextGreaterElements([1, 2, 1]))
    print(Solution().nextGreaterElements([1, 2, 3, 4, 3]))
