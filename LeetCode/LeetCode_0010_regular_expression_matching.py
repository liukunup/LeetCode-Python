#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-29 19:18:06

# 导入所需的依赖库
import unittest

# 题目编号: 10
# 题目名称: 正则表达式匹配
# 题目难度: Hard

# 知识点: 递归, 字符串, 动态规划

# 题目详情:
"""
给你一个字符串&nbsp;s&nbsp;和一个字符规律&nbsp;p，请你来实现一个支持 '.'&nbsp;和&nbsp;'*'&nbsp;的正则表达式匹配。


	'.' 匹配任意单个字符
	'*' 匹配零个或多个前面的那一个元素


所谓匹配，是要涵盖&nbsp;整个&nbsp;字符串&nbsp;s的，而不是部分字符串。
&nbsp;

示例 1：


输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。


示例 2:


输入：s = "aa", p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。


示例&nbsp;3：


输入：s = "ab", p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。


&nbsp;

提示：


	1 &lt;= s.length&nbsp;&lt;= 20
	1 &lt;= p.length&nbsp;&lt;= 30
	s&nbsp;只包含从&nbsp;a-z&nbsp;的小写字母。
	p&nbsp;只包含从&nbsp;a-z&nbsp;的小写字母，以及字符&nbsp;.&nbsp;和&nbsp;*。
	保证每次出现字符&nbsp;* 时，前面都匹配到有效的字符


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]

        return f[m][n]


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(0, -1)


if __name__ == "__main__":
    unittest.main()
