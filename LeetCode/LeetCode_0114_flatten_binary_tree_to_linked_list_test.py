#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2024-08-14 00:43:21

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 114
# 题目名称: 二叉树展开为链表
# 题目难度: Medium

# 知识点: 栈, 树, 深度优先搜索, 链表, 二叉树

# 题目详情:
"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：


	展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
	展开后的单链表应该与二叉树 先序遍历 顺序相同。


 

示例 1：


输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]


示例 2：


输入：root = []
输出：[]


示例 3：


输入：root = [0]
输出：[0]


 

提示：


	树中结点数在范围 [0, 2000] 内
	-100 


 

进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？

"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        right = root.right
        self.flatten(root.left)
        self.flatten(root.right)
        root.left, root.right = None, root.left
        node = root
        while node.right:
            node = node.right
        node.right = right


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
