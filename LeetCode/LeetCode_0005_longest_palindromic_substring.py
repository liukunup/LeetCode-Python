#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-21 22:45:18

# 导入所需的依赖库
import unittest

# 题目编号: 5
# 题目名称: 最长回文子串
# 题目难度: Medium

# 知识点: 字符串, 动态规划

# 题目详情:
"""
给你一个字符串 s，找到 s 中最长的回文子串。

&nbsp;

示例 1：


输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。


示例 2：


输入：s = "cbbd"
输出："bb"


&nbsp;

提示：


	1 &lt;= s.length &lt;= 1000
	s 仅由数字和英文字母组成


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def longestPalindrome(self, s: str) -> str:
        # 长度小于2
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0

        # dp[i][j] 表示 s[i..j] 是否为回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for sub_s_len in range(2, n + 1):
            for i in range(n):
                j = sub_s_len + i - 1
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i

        return s[begin:begin + max_len]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome_v2(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            # 长度=1
            left1, right1 = self.expandAroundCenter(s, i, i)
            if right1 - left1 > end - start:
                start, end = left1, right1
            # 长度=2
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

    def expandAroundCenter_v3(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome_v3(self, s: str) -> str:
        start, end = 0, -1
        s = "#" + "#".join(list(s)) + "#"
        # 臂长
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expandAroundCenter_v3(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expandAroundCenter_v3(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start + 1:end + 1:2]


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertIn(self.inst.longestPalindrome_v3("babad"), ["bab", "aba"])

    def test_2(self):
        self.assertEqual(self.inst.longestPalindrome_v3("cbbd"), "bb")


if __name__ == "__main__":
    unittest.main()
