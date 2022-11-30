#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-30 19:41:33

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 11
# 题目名称: 盛最多水的容器
# 题目难度: Medium

# 知识点: 贪心, 数组, 双指针

# 题目详情:
"""
给定一个长度为 n 的整数数组&nbsp;height&nbsp;。有&nbsp;n&nbsp;条垂线，第 i 条线的两个端点是&nbsp;(i, 0)&nbsp;和&nbsp;(i, height[i])&nbsp;。

找出其中的两条线，使得它们与&nbsp;x&nbsp;轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

&nbsp;

示例 1：




输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为&nbsp;49。

示例 2：


输入：height = [1,1]
输出：1


&nbsp;

提示：


	n == height.length
	2 &lt;= n &lt;= 105
	0 &lt;= height[i] &lt;= 104


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        p_left, p_right = 0, n - 1
        max_area = 0
        while p_left < p_right:
            h = min(height[p_left], height[p_right])
            w = p_right - p_left
            area = h * w
            max_area = max(max_area, area)
            if height[p_left] < height[p_right]:
                p_left += 1
            else:
                p_right -= 1
        return max_area


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual(self.inst.maxArea([1,8,6,2,5,4,8,3,7]), 49)

    def test_2(self):
        self.assertEqual(self.inst.maxArea([1,1]), 1)

if __name__ == "__main__":
    unittest.main()
