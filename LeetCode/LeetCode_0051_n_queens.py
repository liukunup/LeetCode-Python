#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-02 19:38:41

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 51
# 题目名称: N 皇后
# 题目难度: Hard

# 知识点: 数组, 回溯

# 题目详情:
"""
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n&nbsp;皇后问题 研究的是如何将 n&nbsp;个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的&nbsp;n&nbsp;皇后问题 的解决方案。



每一种解法包含一个不同的&nbsp;n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

&nbsp;

示例 1：


输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。


示例 2：


输入：n = 1
输出：[["Q"]]


&nbsp;

提示：


	1 &lt;= n &lt;= 9




"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:

        row_init = ['.'] * n

        queens = [-1] * n

        columns = set()
        diagonal1 = set()
        diagonal2 = set()

        solutions = list()

        def generate():
            board = list()
            for r in range(n):
                row_init[queens[r]] = 'Q'
                board.append(''.join(row_init))
                row_init[queens[r]] = '.'
            return board

        def backtrace(row: int):
            if row == n:
                board = generate()
                solutions.append(board)
            else:
                for col in range(n):
                    if col in columns or row - col in diagonal1 or row + col in diagonal2:
                        continue
                    queens[row] = col
                    columns.add(col)
                    diagonal1.add(row - col)
                    diagonal2.add(row + col)
                    backtrace(row + 1)
                    columns.remove(col)
                    diagonal1.remove(row - col)
                    diagonal2.remove(row + col)

        backtrace(0)
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
        self.assertEqual(0, -1)


if __name__ == "__main__":
    unittest.main()
