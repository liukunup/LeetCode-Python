#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2024-08-12 00:12:52

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 105
# 题目名称: 从前序与中序遍历序列构造二叉树
# 题目难度: Medium

# 知识点: 树, 数组, 哈希表, 分治, 二叉树

# 题目详情:
"""
给定两个整数数组&nbsp;preorder 和 inorder&nbsp;，其中&nbsp;preorder 是二叉树的先序遍历， inorder&nbsp;是同一棵树的中序遍历，请构造二叉树并返回其根节点。

&nbsp;

示例 1:


输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]


示例 2:


输入: preorder = [-1], inorder = [-1]
输出: [-1]


&nbsp;

提示:


	1 &lt;= preorder.length &lt;= 3000
	inorder.length == preorder.length
	-3000 &lt;= preorder[i], inorder[i] &lt;= 3000
	preorder&nbsp;和&nbsp;inorder&nbsp;均 无重复 元素
	inorder&nbsp;均出现在&nbsp;preorder
	preorder&nbsp;保证 为二叉树的前序遍历序列
	inorder&nbsp;保证 为二叉树的中序遍历序列


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def myBuildTree(preorder_left, preorder_right, inorder_left, inorder_right):

            if preorder_left > preorder_right:
                return None
            
            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]
            
            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root
        
        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)


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
