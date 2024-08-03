from typing import List


class Solution:
    """
    496. 下一个更大元素 I
    nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。

    示例 1：
    输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
    输出：[-1,3,-1]
    """

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = []
        num_dict = dict()
        for i in range(len(nums2)):
            n = nums2[i]
            while stack and n > stack[-1]:
                num_dict[stack[-1]] = n
                stack.pop()
            stack.append(n)

        for num in nums1:
            ans.append(num_dict.get(num, -1))
        return ans


if __name__ == '__main__':
    print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
    print(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]))
