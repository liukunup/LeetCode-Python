#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2024-08-12 00:08:10

# 导入所需的依赖库
import unittest

# 题目编号: 104
# 题目名称: 二叉树的最大深度
# 题目难度: Easy

# 知识点: 树, 深度优先搜索, 广度优先搜索, 二叉树

# 题目详情:
"""
给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

&nbsp;

示例 1：



&nbsp;


输入：root = [3,9,20,null,null,15,7]
输出：3


示例 2：


输入：root = [1,null,2]
输出：2


&nbsp;

提示：


	树中节点的数量在&nbsp;[0, 104]&nbsp;区间内。
	-100 &lt;= Node.val &lt;= 100


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.maxDepth(root.left) 
        right_height = self.maxDepth(root.right) 

        return max(left_height, right_height) + 1


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
