class Solution:
    """
    76. 最小覆盖子串
    给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

    示例 1：
    输入：s = "ADOBECODEBANC", t = "ABC"
    输出："BANC"
    解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。

    示例 2：
    输入：s = "a", t = "a"
    输出："a"
    解释：整个字符串 s 是最小覆盖子串。

    示例 3:
    输入: s = "a", t = "aa"
    输出: ""
    解释: t 中两个字符 'a' 均应包含在 s 的子串中，
    因此没有符合条件的子字符串，返回空字符串。
    """

    def minWindow(self, s: str, t: str) -> str:
        window = dict()
        need = dict()
        for c in t:
            need[c] = need.get(c, 0) + 1
        left, right = 0, 0
        start, length = 0, len(s) + 1
        valid = 0
        while right < len(s):
            # 新的字符
            c = s[right]
            # 扩大窗口
            right += 1
            # 如果是需要的字符
            if c in need:
                # 更新窗口统计有效字符的map
                window[c] = window.get(c, 0) + 1
                # 某个字符是否已经"够了"，但多出来的不会被统计
                if window[c] == need[c]:
                    valid += 1
            """
            当窗口符合要求(所有字符都够了)，尝试缩小窗口
            此处的循环结束条件是valid < len(need)，此时窗口内的数据都不满足要求，在下一轮循环中，就会增大窗口，然后继续判断是否满足条件
            """
            while valid == len(need):
                # 和上一次的长度比较，更新结果
                if right - left < length:
                    start = left
                    length = right - left
                # 要删除的字符
                d = s[left]
                # 左指针右移
                left += 1
                # 更新窗口统计有效字符的map
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if length == len(s) + 1 else s[start:start + length]


if __name__ == '__main__':
    print(Solution().minWindow("ABBBECODEBANC", "ABC"))
