#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-13 11:39:39

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 438
# 题目名称: 找到字符串中所有字母异位词
# 题目难度: Medium

# 知识点: 哈希表, 字符串, 滑动窗口

# 题目详情:
"""
给定两个字符串&nbsp;s&nbsp;和 p，找到&nbsp;s&nbsp;中所有&nbsp;p&nbsp;的&nbsp;异位词&nbsp;的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

&nbsp;

示例&nbsp;1:


输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。


&nbsp;示例 2:


输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。


&nbsp;

提示:


	1 &lt;= s.length, p.length &lt;= 3 * 104
	s&nbsp;和&nbsp;p&nbsp;仅包含小写字母


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        ans = []
        if s_count == p_count:
            ans.append(0)

        for i in range(s_len - p_len):
            # 滑动
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1
            # 判断
            if s_count == p_count:
                ans.append(i + 1)

        return ans














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
