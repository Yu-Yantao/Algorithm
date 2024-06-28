from typing import List


class Solution:
    """
    66. 加一
    给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
    最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
    你可以假设除了整数 0 之外，这个整数不会以零开头。

    示例 1：
    输入：digits = [1,2,3]
    输出：[1,2,4]
    解释：输入数组表示数字 123。
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        digits[len(digits) - 1] += 1
        for i in range(len(digits) - 1, 0, -1):
            # 如果当前位不是10，则跳出循环
            if digits[i] != 10:
                break
            else:
                # 当前位是10，则当前位变为0，前一位加1
                digits[i] = 0
                digits[i - 1] += 1
        return digits[1:] if digits[0] == 0 else digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([9, 9, 9, 9]))
