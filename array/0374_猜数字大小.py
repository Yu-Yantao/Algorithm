# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
N = 0
def guess(num: int) -> int:
    if num == N:
        return 0
    elif num > N:
        return -1
    else:
        return 1


class Solution:
    """
    374. 猜数字大小
    我们正在玩猜数字游戏。猜数字游戏的规则如下：
    我会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
    如果你猜错了，我会告诉你，我选出的数字比你猜测的数字大了还是小了。
    你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有三种可能的情况：
    -1：你猜的数字比我选出的数字大 （即 num > pick）。
    1：你猜的数字比我选出的数字小 （即 num < pick）。
    0：你猜的数字与我选出的数字相等。（即 num == pick）。
    返回我选出的数字。

    示例 1：
    输入：n = 10, pick = 6
    输出：6
    """
    def guessNumber(self, n: int) -> int:
        """
        思路：二分查找，逐渐缩小区间
        :param n:
        :return:
        """
        l, r, = 0, n
        while l <= r:
            mid = (l + r) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g == 1:
                l = mid + 1
            else:
                r = mid - 1
        return -1


if __name__ == '__main__':
    N = 7
    print(Solution().guessNumber(10))
