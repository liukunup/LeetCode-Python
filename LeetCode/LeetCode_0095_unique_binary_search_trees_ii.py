#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-26 09:45:43

# 导入所需的依赖库
import unittest
from typing import List, Optional

# 题目编号: 95
# 题目名称: 不同的二叉搜索树 II
# 题目难度: Medium

# 知识点: 树, 二叉搜索树, 动态规划, 回溯, 二叉树

# 题目详情:
"""
给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。

 



示例 1：


输入：n = 3
输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]


示例 2：


输入：n = 1
输出：[[1]]


 

提示：


	1 




"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def generate(start, end):
            if start > end:
                return [None, ]

            allTrees = []
            for i in range(start, end + 1):
                leftTree = generate(start, i - 1)
                rightTree = generate(i + 1, end)

                for lt in leftTree:
                    for rt in rightTree:
                        curTree = TreeNode(i)
                        curTree.left = lt
                        curTree.right = rt
                        allTrees.append(curTree)

            return allTrees

        return generate(1, n) if n else []



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
