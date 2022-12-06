#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-05 20:19:33

# 导入所需的依赖库
import copy
import unittest
from typing import List

# 题目编号: 47
# 题目名称: 全排列 II
# 题目难度: Medium

# 知识点: 数组, 回溯

# 题目详情:
"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

&nbsp;

示例 1：


输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]


示例 2：


输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


&nbsp;

提示：


	1 &lt;= nums.length &lt;= 8
	-10 &lt;= nums[i] &lt;= 10


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
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
                # 约束条件: 跳过未被使用但是相同的数字，刚刚被撤销的那个数字
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] is False:
                    continue

                # 搜索和回溯的过程
                used[i] = True
                backtrace(cur + [val], used)
                used[i] = False

        # 为什么要排序？希望判相邻的数字是否相同
        nums.sort()
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
        self.assertEqual([[1, 1, 2], [1, 2, 1], [2, 1, 1]],
                         self.inst.permuteUnique(nums=[1, 1, 2]))

    def test_2(self):
        self.assertEqual([[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]],
                         self.inst.permuteUnique(nums=[2, 2, 1, 1]))


if __name__ == "__main__":
    unittest.main()
