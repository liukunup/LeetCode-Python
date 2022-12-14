#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-14 15:23:47

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 59
# 题目名称: 螺旋矩阵 II
# 题目难度: Medium

# 知识点: 数组, 矩阵, 模拟

# 题目详情:
"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

 

示例 1：


输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]


示例 2：


输入：n = 1
输出：[[1]]


 

提示：


	1 


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, bottom, left, right = 0, n - 1, 0, n - 1
        num = 1
        matrix = [[0] * n for _ in range(n)]

        while True:
            # 左到右
            for index in range(left, right + 1, 1):
                matrix[top][index] = num
                num += 1
            top += 1
            if top > bottom:
                break

            # 上到下
            for index in range(top, bottom + 1, 1):
                matrix[index][right] = num
                num += 1
            right -= 1
            if right < left:
                break

            # 右到左
            for index in range(right, left - 1, -1):
                matrix[bottom][index] = num
                num += 1
            bottom -= 1
            if bottom < top:
                break

            # 下到上
            for index in range(bottom, top - 1, -1):
                matrix[index][left] = num
                num += 1
            left += 1
            if left > right:
                break

        return matrix


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual([[1,2,3],[8,9,4],[7,6,5]], self.inst.generateMatrix(3))


if __name__ == "__main__":
    unittest.main()
