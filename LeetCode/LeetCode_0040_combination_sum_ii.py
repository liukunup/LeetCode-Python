#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-12 15:03:30

# 导入所需的依赖库
import collections
import unittest
from typing import List

# 题目编号: 40
# 题目名称: 组合总和 II
# 题目难度: Medium

# 知识点: 数组, 回溯

# 题目详情:
"""
给定一个候选人编号的集合&nbsp;candidates&nbsp;和一个目标数&nbsp;target&nbsp;，找出&nbsp;candidates&nbsp;中所有可以使数字和为&nbsp;target&nbsp;的组合。

candidates&nbsp;中的每个数字在每个组合中只能使用&nbsp;一次&nbsp;。

注意：解集不能包含重复的组合。&nbsp;

&nbsp;

示例&nbsp;1:


输入: candidates =&nbsp;[10,1,2,7,6,1,5], target =&nbsp;8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

示例&nbsp;2:


输入: candidates =&nbsp;[2,5,2,1,2], target =&nbsp;5,
输出:
[
[1,2,2],
[5]
]

&nbsp;

提示:


	1 &lt;=&nbsp;candidates.length &lt;= 100
	1 &lt;=&nbsp;candidates[i] &lt;= 50
	1 &lt;= target &lt;= 30


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(pos: int, rest: int):
            nonlocal sequence

            # 恰好减完为 0
            if rest == 0:
                ans.append(sequence)
                return
            # 数字用完 or 不够减
            if pos == len(freq) or rest < freq[pos][0]:
                return

            # 不选用
            dfs(pos + 1, rest)

            # 选用
            most = min(rest // freq[pos][0], freq[pos][1])
            for i in range(1, most + 1):
                sequence.append(freq[pos][0])
                dfs(pos + 1, rest - i * freq[pos][0])
            sequence = sequence[:-most]  # 还原

        # [(值, 频数)]
        freq = sorted(collections.Counter(candidates).items())

        ans = list()
        sequence = list()
        dfs(0, target)

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
        self.assertEqual([[2, 6], [1, 7], [1, 2, 5], [1, 1, 6]],
                         self.inst.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))


if __name__ == "__main__":
    unittest.main()
