class Solution:
    """
    1358. 包含所有三种字符的子字符串数目
    给你一个字符串 s ，它只包含三种字符 a, b 和 c 。
    请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。

    示例 1：
    输入：s = "abcabc"
    输出：10

    示例 2：
    输入：s = "aaacb"
    输出：3
    """

    def numberOfSubstrings(self, s: str) -> int:
        """
        思路: 使用滑动窗口，不断扩大窗口，当窗口内abc都出现了至少一次时，缩小窗口。
        这里的难点是，怎么计算子串的数量。
        对于一个子串，假设在[i:j]区间内，abc至少出现了一次，并且[k:j](k >= i)是满足条件的最小窗口，那么意味着i会向k靠拢，在此过程中，每一个子串都是满足条件的。
        但是，对于任意位置窗口[i:j]，除了它自身是一个满足条件的子串，它和j后边的所有字符也可以构成满足条件的子串。
        例如: "aaacbXXXX"，X代指abc任意字符，此处只关注第一个b。
        "acb" + "X"
        "acb" + "XX"
        "acb" + "XXX"
        ....
        它们都是一个满足条件的子串，所以在更新结果时
        ans += len(s) - right
        :param s:
        :return:
        """
        ans = 0
        cnt = [0] * 3
        l = 0
        for r in range(len(s)):
            cnt[ord(s[r]) - ord('a')] += 1
            while all(cnt):
                ans += len(s) - r
                cnt[ord(s[l]) - ord('a')] -= 1
                l += 1
        return ans


if __name__ == '__main__':
    print(Solution().numberOfSubstrings("abcabc"))
    print(Solution().numberOfSubstrings("aaacb"))
