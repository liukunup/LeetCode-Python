#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2024-08-11 16:29:50

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 102
# 题目名称: 二叉树的层序遍历
# 题目难度: Medium

# 知识点: 树, 广度优先搜索, 二叉树

# 题目详情:
"""
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

&nbsp;

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]


示例 2：


输入：root = [1]
输出：[[1]]


示例 3：


输入：root = []
输出：[]


&nbsp;

提示：


	树中节点数目在范围 [0, 2000] 内
	-1000 &lt;= Node.val &lt;= 1000


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        def dfs(index, r):
            if len(res)<index:
                res.append([])
            res[index-1].append(r.val)
            if r.left:
                dfs(index+1,r.left)
            if r.right:
                dfs(index+1,r.right)
        dfs(1, root)
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
