#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-08 09:48:42

# 导入所需的依赖库
import unittest
from typing import Optional

# 题目编号: 25
# 题目名称: K 个一组翻转链表
# 题目难度: Hard

# 知识点: 递归, 链表

# 题目详情:
"""
给你链表的头节点 head ，每&nbsp;k&nbsp;个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是&nbsp;k&nbsp;的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

&nbsp;

示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]


示例 2：




输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]


&nbsp;
提示：


	链表中的节点数目为 n
	1 &lt;= k &lt;= n &lt;= 5000
	0 &lt;= Node.val &lt;= 1000


&nbsp;

进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？




"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverse(self, head: ListNode, tail: ListNode):
        # 参考第 206 题 反转链表
        # 反转子链表并返回新的头尾
        prev = tail.next
        curr = head
        while prev != tail:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        return tail, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 递归
        dummy = ListNode()
        dummy.next = head
        cursor = dummy

        while head:
            tail = cursor

            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            temp = tail.next
            head, tail = self.reverse(head, tail)

            cursor.next = head
            tail.next = temp
            cursor = tail
            head = tail.next

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
