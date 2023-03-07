#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2023-03-07 16:10:02

# 导入所需的依赖库
import unittest
from typing import Optional

# 题目编号: 101
# 题目名称: 对称二叉树
# 题目难度: Easy

# 知识点: 树, 深度优先搜索, 广度优先搜索, 二叉树

# 题目详情:
"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。

&nbsp;

示例 1：


输入：root = [1,2,2,3,4,4,3]
输出：true


示例 2：


输入：root = [1,2,2,null,3,null,3]
输出：false


&nbsp;

提示：


	树中节点数目在范围 [1, 1000] 内
	-100 &lt;= Node.val &lt;= 100


&nbsp;

进阶：你可以运用递归和迭代两种方法解决这个问题吗？

"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, root)

    def check(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)


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
