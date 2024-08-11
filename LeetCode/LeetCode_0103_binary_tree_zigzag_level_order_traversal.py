#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2024-08-11 21:37:11

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 103
# 题目名称: 二叉树的锯齿形层序遍历
# 题目难度: Medium

# 知识点: 树, 广度优先搜索, 二叉树

# 题目详情:
"""
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

&nbsp;

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]


示例 2：


输入：root = [1]
输出：[[1]]


示例 3：


输入：root = []
输出：[]


&nbsp;

提示：


	树中节点数目在范围 [0, 2000] 内
	-100 &lt;= Node.val &lt;= 100


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        cur = [root]
        while cur:
            nxt = []
            vals = []
            for node in cur:
                vals.append(node.val)
                if node.left:  nxt.append(node.left)
                if node.right: nxt.append(node.right)
            cur = nxt
            ans.append(vals[::-1] if len(ans) % 2 else vals)
        return ans


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
