#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-14 15:45:36

# 导入所需的依赖库
import unittest
from typing import Optional

# 题目编号: 61
# 题目名称: 旋转链表
# 题目难度: Medium

# 知识点: 链表, 双指针

# 题目详情:
"""
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动&nbsp;k&nbsp;个位置。

&nbsp;

示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]


示例 2：


输入：head = [0,1,2], k = 4
输出：[2,0,1]


&nbsp;

提示：


	链表中节点的数目在范围 [0, 500] 内
	-100 &lt;= Node.val &lt;= 100
	0 &lt;= k &lt;= 2 * 109


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if k == 0 or not head or not head.next:
            return head

        size = 1
        cur = head
        while cur.next:
            cur = cur.next
            size += 1

        if (n := size - k % size) == size:
            return head

        # 注意：链变环
        cur.next = head
        while n:
            cur = cur.next
            n -= 1

        # 环断裂点处理
        node = cur.next
        cur.next = None

        return node


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.assertEqual(0, self.inst.rotateRight(head=head, k=2))

    def test_2(self):
        head = ListNode(1, ListNode(2))
        self.assertEqual(0, self.inst.rotateRight(head=head, k=1))

if __name__ == "__main__":
    unittest.main()
