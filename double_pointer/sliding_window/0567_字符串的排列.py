from collections import defaultdict


class Solution:
    """
    567. 字符串的排列
    给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
    换句话说，s1 的排列之一是 s2 的 子串 。

    示例 1：
    输入：s1 = "ab" s2 = "eidbaooo"
    输出：true
    解释：s2 包含 s1 的排列之一 ("ba").

    示例 2：
    输入：s1= "ab" s2 = "eidboaoo"
    输出：false
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = dict()
        need = dict()
        left, right = 0, 0
        valid = 0
        for c in s1:
            need[c] = need.get(c, 0) + 1
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while right - left >= len(s1):
                if valid == len(need):
                    return True
                d = s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False


if __name__ == '__main__':
    print(Solution().checkInclusion("ab", "eidbaooo"))
    print(Solution().checkInclusion("ab", "eidboaoo"))
