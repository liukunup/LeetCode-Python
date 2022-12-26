#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-26 11:09:52

# 导入所需的依赖库
import unittest
from typing import Optional

# 题目编号: 98
# 题目名称: 验证二叉搜索树
# 题目难度: Medium

# 知识点: 树, 深度优先搜索, 二叉搜索树, 二叉树

# 题目详情:
"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：


	节点的左子树只包含 小于 当前节点的数。
	节点的右子树只包含 大于 当前节点的数。
	所有左子树和右子树自身必须也是二叉搜索树。


&nbsp;

示例 1：


输入：root = [2,1,3]
输出：true


示例 2：


输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。


&nbsp;

提示：


	树中节点数目范围在[1, 104] 内
	-231 &lt;= Node.val &lt;= 231 - 1


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def func(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= low or val >= high:
                return False

            if not func(node.right, val, high):
                return False
            if not func(node.left, low, val):
                return False

            return True

        return func(root)



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
