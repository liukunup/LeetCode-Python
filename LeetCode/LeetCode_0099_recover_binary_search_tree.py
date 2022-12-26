#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-26 11:38:19

# 导入所需的依赖库
import unittest
from typing import Optional

# 题目编号: 99
# 题目名称: 恢复二叉搜索树
# 题目难度: Medium

# 知识点: 树, 深度优先搜索, 二叉搜索树, 二叉树

# 题目详情:
"""
给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树&nbsp;。

&nbsp;

示例 1：


输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 的左孩子，因为 3 &gt; 1 。交换 1 和 3 使二叉搜索树有效。


示例 2：


输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 &lt; 3 。交换 2 和 3 使二叉搜索树有效。

&nbsp;

提示：


	树上节点的数目在范围 [2, 1000] 内
	-231 &lt;= Node.val &lt;= 231 - 1


&nbsp;

进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用&nbsp;O(1) 空间的解决方案吗？

"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = list()
        pred = None
        x, y = None, None

        while len(stack) > 0 or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if pred is not None and root.val < pred.val:
                y = root
                if not x:
                    x = pred
                else:
                    break

            pred = root
            root = root.right

        x.val, y.val = y.val, x.val




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
