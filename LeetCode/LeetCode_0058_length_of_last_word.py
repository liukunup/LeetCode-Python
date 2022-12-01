#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-01 17:40:07

# 导入所需的依赖库
import unittest

# 题目编号: 58
# 题目名称: 最后一个单词的长度
# 题目难度: Easy

# 知识点: 字符串

# 题目详情:
"""
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

&nbsp;

示例 1：


输入：s = "Hello World"
输出：5
解释：最后一个单词是“World”，长度为5。


示例 2：


输入：s = "   fly me   to   the moon  "
输出：4
解释：最后一个单词是“moon”，长度为4。


示例 3：


输入：s = "luffy is still joyboy"
输出：6
解释：最后一个单词是长度为6的“joyboy”。


&nbsp;

提示：


	1 &lt;= s.length &lt;= 104
	s 仅有英文字母和空格 ' ' 组成
	s 中至少存在一个单词


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1

        while index >= 0 and s[index] == " ":
            index -= 1
        right = index

        while index >= 0 and s[index] != " ":
            index -= 1
        left = index

        return len(s[left + 1:right + 1])


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(self.inst.lengthOfLastWord(s="   fly me   to   the moon  "), 4)
        self.assertEqual(self.inst.lengthOfLastWord(s="a"), 1)
        self.assertEqual(self.inst.lengthOfLastWord(s="day"), 3)


if __name__ == "__main__":
    unittest.main()
