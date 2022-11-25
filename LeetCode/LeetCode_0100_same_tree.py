#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-22 00:58:27
import collections
# 导入所需的依赖库
import unittest
from typing import Optional
# 题目编号: 100
# 题目名称: 相同的树
# 题目难度: Easy

# 知识点: 树, 深度优先搜索, 广度优先搜索, 二叉树

# 题目详情:
"""
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

 

示例 1：


输入：p = [1,2,3], q = [1,2,3]
输出：true


示例 2：


输入：p = [1,2], q = [1,null,2]
输出：false


示例 3：


输入：p = [1,2,1], q = [1,1,2]
输出：false


 

提示：


	两棵树上的节点数目都在范围 [0, 100] 内
	-104 4


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """ 深度优先 """
        if not p and not q:  # 均None
            return True
        elif not p or not q:  # 其中一个为None
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree_v2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """ 广度优先 """
        if not p and not q:  # 均None
            return True
        if not p or not q:  # 其中一个为None
            return False
        #
        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val != node2.val:
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if (not left1) ^ (not left2):
                return False
            if (not right1) ^ (not right2):
                return False
            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)

        return not queue1 and not queue2


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        p = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
        self.assertTrue(self.inst.isSameTree_v2(p=p, q=p))

    def test_2(self):
        p = TreeNode(val=1, left=TreeNode(val=2))
        q = TreeNode(val=1, right=TreeNode(val=2))
        self.assertFalse(self.inst.isSameTree_v2(p=p, q=q))

    def test_3(self):
        p = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=1))
        q = TreeNode(val=1, left=TreeNode(val=1), right=TreeNode(val=2))
        self.assertFalse(self.inst.isSameTree_v2(p=p, q=q))


if __name__ == "__main__":
    unittest.main()
