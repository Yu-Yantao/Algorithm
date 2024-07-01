from typing import List


class Solution:
    """
    LCR 164. 破解闯关密码
    闯关游戏需要破解一组密码，闯关组给出的有关密码的线索是：
    一个拥有密码所有元素的非负整数数组 password
    密码是 password 中所有元素拼接后得到的最小的一个数
    请编写一个程序返回这个密码。

    示例 1:
    输入: password = [15, 8, 7]
    输出: "1578"
    """

    def crackPassword(self, password: List[int]) -> str:
        """
        思路：对数组进行字典序排序
        如果x+y < y+x，则x应该在y的左边，否则应该在y的右边，如[4,51] 451 < 514
        :param password:
        :return:
        """

        def quick_sort(l, r):
            if l >= r:
                return
            left, base, right = l, l, r
            while left < right:
                while (left < right and int(str(password[right]) + str(password[base])) >=
                       int(str(password[base]) + str(password[right]))):
                    right -= 1
                while (left < right and int(str(password[left]) + str(password[base])) <=
                       int(str(password[base]) + str(password[left]))):
                    left += 1
                password[right], password[left] = password[left], password[right]
            password[right], password[base] = password[base], password[right]
            quick_sort(l, right)
            quick_sort(right + 1, r)

        quick_sort(0, len(password) - 1)
        return ''.join(map(str, password))


if __name__ == '__main__':
    print(Solution().crackPassword(password=[15, 8, 7]))
