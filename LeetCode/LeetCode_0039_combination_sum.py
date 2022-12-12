#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-12 11:56:25

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 39
# 题目名称: 组合总和
# 题目难度: Medium

# 知识点: 数组, 回溯

# 题目详情:
"""
给你一个 无重复元素 的整数数组&nbsp;candidates 和一个目标整数&nbsp;target&nbsp;，找出&nbsp;candidates&nbsp;中可以使数字和为目标数&nbsp;target 的 所有&nbsp;不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。&nbsp;

对于给定的输入，保证和为&nbsp;target 的不同组合数少于 150 个。

&nbsp;

示例&nbsp;1：


输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。

示例&nbsp;2：


输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]

示例 3：


输入: candidates = [2], target = 1
输出: []


&nbsp;

提示：


	1 &lt;= candidates.length &lt;= 30
	2 &lt;= candidates[i] &lt;= 40
	candidates 的所有元素 互不相同
	1 &lt;= target &lt;= 40


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(begin, size):
                dfs(candidates, i, size, path + [candidates[i]], res, target - candidates[i])
            pass

        n = len(candidates)
        if n == 0:
            return []

        candidates.sort()

        path = []
        res = []
        dfs(candidates, 0, n, path, res, target)

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
