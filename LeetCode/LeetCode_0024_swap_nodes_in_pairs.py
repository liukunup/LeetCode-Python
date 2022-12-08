#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-07 20:24:57

# 导入所需的依赖库
import unittest
from typing import Optional

# 题目编号: 24
# 题目名称: 两两交换链表中的节点
# 题目难度: Medium

# 知识点: 递归, 链表

# 题目详情:
"""
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

&nbsp;

示例 1：


输入：head = [1,2,3,4]
输出：[2,1,4,3]


示例 2：


输入：head = []
输出：[]


示例 3：


输入：head = [1]
输出：[1]


&nbsp;

提示：


	链表中节点的数目在范围 [0, 100] 内
	0 &lt;= Node.val &lt;= 100


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归
        if not head or not head.next:
            return head

        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head

        return new_head

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 迭代
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            node1 = cur.next
            node2 = cur.next.next
            cur.next = node2
            node1.next = node2.next
            node2.next = node1
            cur = node1
        return dummy.next


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
