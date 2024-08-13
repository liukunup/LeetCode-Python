#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2024-08-13 00:28:27

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 109
# 题目名称: 有序链表转换二叉搜索树
# 题目难度: Medium

# 知识点: 树, 二叉搜索树, 链表, 分治, 二叉树

# 题目详情:
"""
给定一个单链表的头节点 &nbsp;head&nbsp;，其中的元素 按升序排序 ，将其转换为 平衡 二叉搜索树。

&nbsp;

示例 1:




输入: head = [-10,-3,0,5,9]
输出: [0,-3,9,-10,null,5]
解释: 一个可能的答案是[0，-3,9，-10,null,5]，它表示所示的高度平衡的二叉搜索树。


示例 2:


输入: head = []
输出: []


&nbsp;

提示:


	head&nbsp;中的节点数在[0, 2 * 104]&nbsp;范围内
	-105&nbsp;&lt;= Node.val &lt;= 105


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def getLength(head: ListNode) -> int:
            ret = 0
            while head:
                ret += 1
                head = head.next
            return ret
        
        def buildTree(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            mid = (left + right + 1) // 2
            root = TreeNode()
            root.left = buildTree(left, mid - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = buildTree(mid + 1, right)
            return root
        
        length = getLength(head)
        return buildTree(0, length - 1)


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        nums = [-10,-3,0,5,9]
        head = curr = ListNode()
        for n in nums:
            node = ListNode(n)
            curr.next = node
            curr = curr.next
        res = self.inst.sortedListToBST(head=head.next)
        self.assertEqual(0, -1)


if __name__ == "__main__":
    unittest.main()
