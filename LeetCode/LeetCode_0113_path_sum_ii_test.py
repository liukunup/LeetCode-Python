#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2024-08-14 00:41:46

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 113
# 题目名称: 路径总和 II
# 题目难度: Medium

# 知识点: 树, 深度优先搜索, 回溯, 二叉树

# 题目详情:
"""
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。



 

示例 1：


输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]


示例 2：


输入：root = [1,2,3], targetSum = 5
输出：[]


示例 3：


输入：root = [1,2], targetSum = 0
输出：[]


 

提示：


	树中节点总数在范围 [0, 5000] 内
	-1000 
	-1000 




"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res, path = [], []

        def helper(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            helper(root.left, tar)
            helper(root.right, tar)
            path.pop()

        helper(root, targetSum)

        return res


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
