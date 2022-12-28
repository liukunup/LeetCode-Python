#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-28 15:49:43

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 84
# 题目名称: 柱状图中最大的矩形
# 题目难度: Hard

# 知识点: 栈, 数组, 单调栈

# 题目详情:
"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 

示例 1:




输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10


示例 2：




输入： heights = [2,4]
输出： 4

 

提示：


	1 5
	0 4


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n

        stack = list()

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                right[stack[-1]] = i
                stack.pop()

            left[i] = stack[-1] if stack else -1
            stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0

        return ans



# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(10, self.inst.largestRectangleArea(heights = [2,1,5,6,2,3]))


if __name__ == "__main__":
    unittest.main()
