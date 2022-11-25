#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-26 00:16:37

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 94
# 题目名称: 二叉树的中序遍历
# 题目难度: Easy

# 知识点: 栈, 树, 深度优先搜索, 二叉树

# 题目详情:
"""
给定一个二叉树的根节点 root ，返回 它的 中序&nbsp;遍历 。

&nbsp;

示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]


示例 2：


输入：root = []
输出：[]


示例 3：


输入：root = [1]
输出：[1]


&nbsp;

提示：


	树中节点数目在范围 [0, 100] 内
	-100 &lt;= Node.val &lt;= 100


&nbsp;

进阶:&nbsp;递归算法很简单，你可以通过迭代算法完成吗？

"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, rst = [root], []
        while stack:
            i = stack.pop()
            if isinstance(i, TreeNode):
                stack.extend([i.right, i.val, i.left])
            elif isinstance(i, int):
                rst.append(i)
        return rst


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        root = TreeNode(val=1, right=TreeNode(val=2, left=TreeNode(val=3)))
        res = [1, 3, 2]
        self.assertTrue(all(i == j for i,j in zip(res, self.inst.inorderTraversal(root=root))))

    def test_2(self):
        self.assertEqual(len(self.inst.inorderTraversal(root=None)), 0)

    def test_3(self):
        root = TreeNode(val=1)
        res = [1]
        self.assertTrue(all(i == j for i, j in zip(res, self.inst.inorderTraversal(root=root))))


if __name__ == "__main__":
    unittest.main()
