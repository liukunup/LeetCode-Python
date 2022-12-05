#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-05 11:42:44

# 导入所需的依赖库
import unittest

# 题目编号: 50
# 题目名称: Pow(x, n)
# 题目难度: Medium

# 知识点: 递归, 数学

# 题目详情:
"""
实现&nbsp;pow(x, n)&nbsp;，即计算 x 的整数&nbsp;n 次幂函数（即，xn ）。

&nbsp;

示例 1：


输入：x = 2.00000, n = 10
输出：1024.00000


示例 2：


输入：x = 2.10000, n = 3
输出：9.26100


示例 3：


输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25


&nbsp;

提示：


	-100.0 &lt; x &lt; 100.0
	-231 &lt;= n &lt;= 231-1
	-104 &lt;= xn &lt;= 104


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def myPow(self, x: float, n: int) -> float:

        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

    def myPow_v2(self, x: float, n: int) -> float:

        def quickMul(N):
            ans = 1
            x_c = x
            while N > 0:
                if N % 2 == 1:
                    ans *= x_c
                x_c *= x_c
                N //= 2
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


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
