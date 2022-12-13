#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-13 17:30:41

# 导入所需的依赖库
import unittest
from collections import Counter

# 题目编号: 1960
# 题目名称: 判断句子是否为全字母句
# 题目难度: Easy

# 知识点: 哈希表, 字符串

# 题目详情:
"""
全字母句 指包含英语字母表中每个字母至少一次的句子。

给你一个仅由小写英文字母组成的字符串 sentence ，请你判断 sentence 是否为 全字母句 。

如果是，返回 true ；否则，返回 false 。

 

示例 1：


输入：sentence = "thequickbrownfoxjumpsoverthelazydog"
输出：true
解释：sentence 包含英语字母表中每个字母至少一次。


示例 2：


输入：sentence = "leetcode"
输出：false


 

提示：


	1 
	sentence 由小写英语字母组成


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(Counter([ch for ch in sentence]).keys()) >= 26


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
