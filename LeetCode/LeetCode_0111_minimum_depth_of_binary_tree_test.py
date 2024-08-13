#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2024-08-14 00:29:45

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 111
# 题目名称: 二叉树的最小深度
# 题目难度: Easy

# 知识点: 树, 深度优先搜索, 广度优先搜索, 二叉树

# 题目详情:
"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。

 

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：2


示例 2：


输入：root = [2,null,3,null,4,null,5,null,6]
输出：5


 

提示：


	树中节点数的范围在 [0, 105] 内
	-1000 


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 or right == 0:
            return max(left, right) + 1

        return min(left, right) + 1


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
