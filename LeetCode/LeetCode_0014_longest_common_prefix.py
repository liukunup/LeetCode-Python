#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-25 22:22:11

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 14
# 题目名称: 最长公共前缀
# 题目难度: Easy

# 知识点: 字符串

# 题目详情:
"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串&nbsp;""。

&nbsp;

示例 1：


输入：strs = ["flower","flow","flight"]
输出："fl"


示例 2：


输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

&nbsp;

提示：


	1 &lt;= strs.length &lt;= 200
	0 &lt;= strs[i].length &lt;= 200
	strs[i] 仅由小写英文字母组成


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        def lcp(str1, str2):
            length, index = min(len(str1), len(str2)), 0
            while index < length and str1[index] == str2[index]:
                index += 1
            return str1[:index]

        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    def longestCommonPrefix_v2(self, strs: List[str]) -> str:
        if not strs:
            return ""

        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]

        return strs[0]

    def longestCommonPrefix_v3(self, strs: List[str]) -> str:

        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]

            return lcpLeft[:minLength]

        return "" if not strs else lcp(0, len(strs) - 1)

    def longestCommonPrefix_v4(self, strs: List[str]) -> str:

        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))

        if not strs:
            return ""

        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1

        return strs[0][:low]


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        strs = ["flower", "flow", "flight"]
        self.assertEqual(self.inst.longestCommonPrefix(strs), "fl")

    def test_2(self):
        strs = ["dog","racecar","car"]
        self.assertEqual(self.inst.longestCommonPrefix(strs), "")


if __name__ == "__main__":
    unittest.main()
