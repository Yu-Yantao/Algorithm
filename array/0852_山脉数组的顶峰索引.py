from typing import List


class Solution:
    """
    852.山脉数组的顶峰索引
    给定一个长度为 n 的整数 山脉 数组 arr ，其中的值递增到一个 峰值元素 然后递减。
    返回峰值元素的下标。

    示例 1：
    输入：arr = [0,1,0]
    输出：1
    """
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            # 如果mid小于mid+1，山峰在右边，并且一定不是mid
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            # mid大于等于mid+1，山峰在左边，山峰可能是mid
            else:
                right = mid
        return left


if __name__ == '__main__':
    print(Solution().peakIndexInMountainArray([1, 2, 3, 4, 5, 1, 1]))
    print(Solution().peakIndexInMountainArray([0, 10, 5, 2]))
    print(Solution().peakIndexInMountainArray([0, 2, 1, 0]))
