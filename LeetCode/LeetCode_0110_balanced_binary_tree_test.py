#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2024-08-14 00:17:20

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 110
# 题目名称: 平衡二叉树
# 题目难度: Easy

# 知识点: 树, 深度优先搜索, 二叉树

# 题目详情:
"""
给定一个二叉树，判断它是否是 平衡二叉树 &nbsp;

&nbsp;

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：true


示例 2：


输入：root = [1,2,2,3,3,null,null,4,4]
输出：false


示例 3：


输入：root = []
输出：true


&nbsp;

提示：


	树中的节点数在范围 [0, 5000] 内
	-104 &lt;= Node.val &lt;= 104


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True

        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced_1(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0


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
