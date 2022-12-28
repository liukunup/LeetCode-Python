#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-28 15:03:02

# 导入所需的依赖库
import unittest
from collections import Counter

# 题目编号: 76
# 题目名称: 最小覆盖子串
# 题目难度: Hard

# 知识点: 哈希表, 字符串, 滑动窗口

# 题目详情:
"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

&nbsp;

注意：


	对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
	如果 s 中存在这样的子串，我们保证它是唯一的答案。


&nbsp;

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

&nbsp;

提示：


	m == s.length
	n == t.length
	1 &lt;= m, n &lt;= 105
	s 和 t 由英文字母组成


&nbsp;
进阶：你能设计一个在 o(m+n) 时间内解决此问题的算法吗？
"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_counter = Counter(t)
        s_counter = Counter()

        def check():
            for k, v in t_counter.items():
                if s_counter[k] < v:
                    return False
            return True

        left, right = 0, -1
        ans_len, ans_l, ans_r = 2**31 - 1, -1, -1

        while right < len(s):

            right += 1

            if right < len(s) and s[right] in t_counter:
                s_counter[s[right]] += 1

            while check() and left <= right:
                if right - left + 1 < ans_len:
                    ans_len = right - left + 1
                    ans_l = left
                if left < len(s) and s[left] in t_counter:
                    s_counter[s[left]] -= 1
                left += 1

        ans_r = ans_l + ans_len

        return "" if ans_l == -1 else s[ans_l: ans_r]


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual("BANC", self.inst.minWindow(s = "ADOBECODEBANC", t = "ABC"))


if __name__ == "__main__":
    unittest.main()
