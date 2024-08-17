#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2024-08-17 11:26:33

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 119
# 题目名称: 杨辉三角 II
# 题目难度: Easy

# 知识点: 数组, 动态规划

# 题目详情:
"""
给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。



 

示例 1:


输入: rowIndex = 3
输出: [1,3,3,1]


示例 2:


输入: rowIndex = 0
输出: [1]


示例 3:


输入: rowIndex = 1
输出: [1,1]


 

提示:


	0 


 

进阶：

你可以优化你的算法到 O(rowIndex) 空间复杂度吗？

"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [comb(rowIndex, i) for i in range(rowIndex + 1)]


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
