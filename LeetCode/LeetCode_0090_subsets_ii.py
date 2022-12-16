#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-16 11:35:52

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 90
# 题目名称: 子集 II
# 题目难度: Medium

# 知识点: 位运算, 数组, 回溯

# 题目详情:
"""
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。



 

示例 1：


输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]


示例 2：


输入：nums = [0]
输出：[[],[0]]


 

提示：


	1 
	-10 




"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def dfs(pos, path):

            if pos == len(nums):
                if path not in results:
                    results.append(path)
                return

            dfs(pos + 1, path)
            if pos > 0 and nums[pos - 1] not in path and nums[pos - 1] == nums[pos]:
                return

            dfs(pos + 1, path + [nums[pos]])

        results = list()
        nums.sort()
        dfs(0, [])

        return results


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual([[],[1],[1,2],[1,2,2],[2],[2,2]], self.inst.subsetsWithDup(nums = [1,2,2]))


if __name__ == "__main__":
    unittest.main()
