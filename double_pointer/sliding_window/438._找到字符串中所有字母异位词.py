from typing import List


class Solution:
    """
    438. 找到字符串中所有字母异位词
    给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
    异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

    示例 1:
    输入: s = "cbaebabacd", p = "abc"
    输出: [0,6]

    示例 2:
    输入: s = "abab", p = "ab"
    输出: [0,1,2]
    """

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        window = dict()
        need = dict()
        for c in p:
            need[c] = need.get(c, 0) + 1
        left, right = 0, 0
        valid = 0
        ans = []
        while right < len(s):
            # 扩大窗口
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            """
            缩小窗口
            当窗口内的元素，已经满足要求时，尝试缩小
            """
            while valid == len(need):
                # 题目要求输出子串的起始索引，所以需要记录left
                if valid == len(need) and right - left == len(p):
                    ans.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return ans


if __name__ == '__main__':
    print(Solution().findAnagrams("cbaebabacd", "abc"))
    print(Solution().findAnagrams("abab", "ab"))
    print(Solution().findAnagrams("baa", "aa"))
