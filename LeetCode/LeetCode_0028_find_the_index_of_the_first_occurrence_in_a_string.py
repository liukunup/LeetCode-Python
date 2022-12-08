#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-08 11:42:34

# 导入所需的依赖库
import unittest

# 题目编号: 28
# 题目名称: 找出字符串中第一个匹配项的下标
# 题目难度: Medium

# 知识点: 双指针, 字符串, 字符串匹配

# 题目详情:
"""
给你两个字符串&nbsp;haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果&nbsp;needle 不是 haystack 的一部分，则返回&nbsp; -1 。

&nbsp;

示例 1：


输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。


示例 2：


输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。


&nbsp;

提示：


	1 &lt;= haystack.length, needle.length &lt;= 104
	haystack 和 needle 仅由小写英文字符组成


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        # 判空
        if not haystack:
            return 0

        # 计算next数组
        n, m = len(haystack), len(needle)
        arr_next = [-1] * m
        i, j = 1, 0
        while i < m:
            while j > 0 and needle[i] != needle[j]:
                j = arr_next[j - 1]
            if needle[i] == needle[j]:
                j += 1
            arr_next[i] = j
            i += 1

        # 搜索
        i, j = 0, 0
        while i < n:
            while j > 0 and haystack[i] != needle[j]:
                j = arr_next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == m:
                return i - m + 1
            i += 1

        # 找不到返回 -1
        return -1




# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(0, self.inst.strStr("abeababeabf", "abeabf"))


if __name__ == "__main__":
    unittest.main()
