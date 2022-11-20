#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-20 23:42:23

# 导入所需的依赖库
import unittest

# 题目编号: 3
# 题目名称: 无重复字符的最长子串
# 题目难度: Medium

# 知识点: 哈希表, 字符串, 滑动窗口

# 题目详情:
"""
给定一个字符串 s ，请你找出其中不含有重复字符的&nbsp;最长子串&nbsp;的长度。

&nbsp;

示例&nbsp;1:


输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。


示例 2:


输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。


示例 3:


输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是&nbsp;"wke"，所以其长度为 3。
&nbsp;    请注意，你的答案必须是 子串 的长度，"pwke"&nbsp;是一个子序列，不是子串。


&nbsp;

提示：


	0 &lt;= s.length &lt;= 5 * 104
	s&nbsp;由英文字母、数字、符号和空格组成


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        n = self.inst.lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(3, n)

    def test_2(self):
        n = self.inst.lengthOfLongestSubstring("bbbbb")
        self.assertEqual(1, n)

    def test_3(self):
        n = self.inst.lengthOfLongestSubstring("pwwkew")
        self.assertEqual(3, n)


if __name__ == "__main__":
    unittest.main()
