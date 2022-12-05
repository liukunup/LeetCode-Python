#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-05 19:21:08

# 导入所需的依赖库
import collections
import unittest
from typing import List

# 题目编号: 49
# 题目名称: 字母异位词分组
# 题目难度: Medium

# 知识点: 数组, 哈希表, 字符串, 排序

# 题目详情:
"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

&nbsp;

示例 1:


输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

示例 2:


输入: strs = [""]
输出: [[""]]


示例 3:


输入: strs = ["a"]
输出: [["a"]]

&nbsp;

提示：


	1 &lt;= strs.length &lt;= 104
	0 &lt;= strs[i].length &lt;= 100
	strs[i]&nbsp;仅包含小写字母


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for ss in strs:
            key = "".join(sorted(ss))
            mp[key].append(ss)
        return list(mp.values())


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
