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

        solutions = list()
        ch_used = [False] * len(nums)

        def backtrace(outputs, data, used, index):
            if index == len(data):
                solutions.append(copy.deepcopy(outputs))
                return
            else:
                for i in range(len(data)):
                    if not used[i]:
                        used[i] = True
                        outputs.append(data[i])
                        backtrace(outputs, data, used, index + 1)
                        outputs.remove(data[i])
                        used[i] = False

        backtrace([], nums, ch_used, 0)

        return solutions


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(self.inst.permute(nums=[1, 2, 3]), [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])


if __name__ == "__main__":
    unittest.main()
