from typing import List


class Solution:
    """
    11. 盛水最多的容器
    给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
    找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
    返回容器可以储存的最大水量。

    示例 1：
    输入：[1,8,6,2,5,4,8,3,7]
    输出：49
    """

    def maxArea(self, height: List[int]) -> int:
        """
        思路：
        任意两点的最大容积是min(height[l], height[r]) * (r - l)
        此时移动高度较小的指针，因为移动高度较小的指针，可以得到更大的容积。
        :param height:
        :return:
        """
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            area = max(area, min(height[l], height[r]) * (r - l))
            if height[l] >= height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
        return area


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(Solution().maxArea([4, 4, 2, 11, 0, 11, 5, 11, 13, 8]))
