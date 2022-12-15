#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-15 15:37:14

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 78
# 题目名称: 子集
# 题目难度: Medium

# 知识点: 位运算, 数组, 回溯

# 题目详情:
"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：


输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


示例 2：


输入：nums = [0]
输出：[[],[0]]


 

提示：


	1 
	-10 
	nums 中的所有元素 互不相同


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(pos, path):
            res.append(path)
            for i in range(pos, len(nums)):
                if nums[i] in path:
                    continue
                dfs(i, path + [nums[i]])

        res = list()
        dfs(0, [])

        return res

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
