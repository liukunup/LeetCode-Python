#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-05 19:45:42

# 导入所需的依赖库
import copy
import unittest
from typing import List

# 题目编号: 46
# 题目名称: 全排列
# 题目难度: Medium

# 知识点: 数组, 回溯

# 题目详情:
"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

&nbsp;

示例 1：


输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


示例 2：


输入：nums = [0,1]
输出：[[0,1],[1,0]]


示例 3：


输入：nums = [1]
输出：[[1]]


&nbsp;

提示：


	1 &lt;= nums.length &lt;= 6
	-10 &lt;= nums[i] &lt;= 10
	nums 中的所有整数 互不相同


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        # 1. 描述解的形式，定一个解空间，包含问题的所有解；
        solutions = list()

        # 2. 构造解的状态空间树，进行试探性的深度优先搜索；
        # 描述数字是否已经被使用
        num_used = [False] * len(nums)
        def backtrace(cur, used):
            # 4. 搜索结束
            if len(cur) == len(nums):
                solutions.append(copy.deepcopy(cur))
                return

            for i, val in enumerate(nums):
                # 3. 构造解的约束条件，用于扩展或剪枝。
                # 约束条件: 数字已经被使用过
                if used[i] is True:
                    continue

                # 搜索和回溯的过程
                used[i] = True
                backtrace(cur + [val], used)
                used[i] = False

        # 起始情况
        backtrace([], num_used)

        return solutions


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
                         self.inst.permute(nums=[1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
