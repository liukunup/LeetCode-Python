#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-26 15:21:38

# 导入所需的依赖库
import unittest

# 题目编号: 52
# 题目名称: N皇后 II
# 题目难度: Hard

# 知识点: 回溯

# 题目详情:
"""
n&nbsp;皇后问题 研究的是如何将 n&nbsp;个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。

&nbsp;



示例 1：


输入：n = 4
输出：2
解释：如上图所示，4 皇后问题存在两个不同的解法。


示例 2：


输入：n = 1
输出：1


&nbsp;

提示：


	1 &lt;= n &lt;= 9




"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def totalNQueens(self, n: int) -> int:

        def solve(row: int, columns: int, diagonals1: int, diagonals2: int) -> int:
            if row == n:
                return 1
            else:
                count = 0
                availablePositions = ((1 << n) - 1) & (~(columns | diagonals1 | diagonals2))
                while availablePositions:
                    position = availablePositions & (-availablePositions)
                    availablePositions = availablePositions & (availablePositions - 1)
                    count += solve(row + 1, columns | position, (diagonals1 | position) << 1,
                                   (diagonals2 | position) >> 1)
                return count

        return solve(0, 0, 0, 0)


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(0, self.inst.totalNQueens(n=4))


if __name__ == "__main__":
    unittest.main()
