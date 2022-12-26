#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-26 15:57:23

# 导入所需的依赖库
import unittest

# 题目编号: 60
# 题目名称: 排列序列
# 题目难度: Hard

# 知识点: 递归, 数学

# 题目详情:
"""
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：


	"123"
	"132"
	"213"
	"231"
	"312"
	"321"


给定 n 和 k，返回第 k 个排列。

 

示例 1：


输入：n = 3, k = 3
输出："213"


示例 2：


输入：n = 4, k = 9
输出："2314"


示例 3：


输入：n = 3, k = 1
输出："123"


 

提示：


	1 
	1 


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)

        k -= 1
        ans = list()
        valid = [1] * (n + 1)
        for i in range(1, n + 1):
            order = k // factorial[n - i] + 1
            for j in range(1, n + 1):
                order -= valid[j]
                if order == 0:
                    ans.append(str(j))
                    valid[j] = 0
                    break
            k %= factorial[n - i]

        return "".join(ans)


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
