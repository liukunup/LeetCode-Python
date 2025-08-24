#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2025-08-24 22:09:38

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 124
# 题目名称: 二叉树中的最大路径和
# 题目难度: Hard

# 知识点: 树, 深度优先搜索, 动态规划, 二叉树

# 题目详情:
"""
二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

&nbsp;

示例 1：


输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -&gt; 1 -&gt; 3 ，路径和为 2 + 1 + 3 = 6

示例 2：


输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -&gt; 20 -&gt; 7 ，路径和为 15 + 20 + 7 = 42


&nbsp;

提示：


	树中节点数目范围是 [1, 3 * 104]
	-1000 &lt;= Node.val &lt;= 1000


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.__maxVal = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def subMaxPathSum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            leftVal = max(subMaxPathSum(node.left), 0)
            rightVal = max(subMaxPathSum(node.right), 0)

            val = node.val + leftVal + rightVal
            self.__maxVal = max(self.__maxVal, val)

            return node.val + max(leftVal, rightVal)
        
        subMaxPathSum(root)
        return self.__maxVal


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(0, 0)


if __name__ == "__main__":
    unittest.main()
