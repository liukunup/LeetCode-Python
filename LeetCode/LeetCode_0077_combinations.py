#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-15 15:27:58

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 77
# 题目名称: 组合
# 题目难度: Medium

# 知识点: 回溯

# 题目详情:
"""
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。

 

示例 1：


输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

示例 2：


输入：n = 1, k = 1
输出：[[1]]

 

提示：


	1 
	1 


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def dfs(pos, path):
            if len(path) == k:
                res.append(path)
                return
            for i in range(pos, n + 1):
                if i in path:
                    continue
                dfs(i + 1, path + [i])

        res = list()
        dfs(1, [])

        return res


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
