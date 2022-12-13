#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-13 16:18:05

# 导入所需的依赖库
import unittest

# 题目编号: 32
# 题目名称: 最长有效括号
# 题目难度: Hard

# 知识点: 栈, 字符串, 动态规划

# 题目详情:
"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

 



示例 1：


输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"


示例 2：


输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"


示例 3：


输入：s = ""
输出：0


 

提示：


	0 4
	s[i] 为 '(' 或 ')'




"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        return max(dp)

    def longestValidParentheses_v2(self, s: str) -> int:
        stack = list()
        stack.append(-1)
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    cur_len = i - stack[-1]
                    max_len = max(max_len, cur_len)
        return max_len


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(4, self.inst.longestValidParentheses_v2(s="()(()()"))


if __name__ == "__main__":
    unittest.main()
