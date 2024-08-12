#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2024-08-12 00:21:40

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 106
# 题目名称: 从中序与后序遍历序列构造二叉树
# 题目难度: Medium

# 知识点: 树, 数组, 哈希表, 分治, 二叉树

# 题目详情:
"""
给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗&nbsp;二叉树&nbsp;。

&nbsp;

示例 1:


输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]


示例 2:


输入：inorder = [-1], postorder = [-1]
输出：[-1]


&nbsp;

提示:


	1 &lt;= inorder.length &lt;= 3000
	postorder.length == inorder.length
	-3000 &lt;= inorder[i], postorder[i] &lt;= 3000
	inorder&nbsp;和&nbsp;postorder&nbsp;都由 不同 的值组成
	postorder&nbsp;中每一个值都在&nbsp;inorder&nbsp;中
	inorder&nbsp;保证是树的中序遍历
	postorder&nbsp;保证是树的后序遍历


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def myBuildTree(in_left, in_right):
            # 如果这里没有节点构造二叉树了，就结束
            if in_left > in_right:
                return None
            
            # 选择 post_idx 位置的元素作为当前子树根节点
            val = postorder.pop()
            root = TreeNode(val)

            # 根据 root 所在位置分成左右两棵子树
            index = idx_map[val]
 
            # 构造右子树
            root.right = myBuildTree(index + 1, in_right)
            # 构造左子树
            root.left = myBuildTree(in_left, index - 1)
            return root
        
        # 建立（元素，下标）键值对的哈希表
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return myBuildTree(0, len(inorder) - 1)


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
