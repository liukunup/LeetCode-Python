#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-02 16:47:04

# 导入所需的依赖库
import unittest
from typing import Optional

# 题目编号: 19
# 题目名称: 删除链表的倒数第 N 个结点
# 题目难度: Medium

# 知识点: 链表, 双指针

# 题目详情:
"""
给你一个链表，删除链表的倒数第&nbsp;n&nbsp;个结点，并且返回链表的头结点。

&nbsp;

示例 1：


输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]


示例 2：


输入：head = [1], n = 1
输出：[]


示例 3：


输入：head = [1,2], n = 1
输出：[1]


&nbsp;

提示：


	链表中结点的数目为 sz
	1 &lt;= sz &lt;= 30
	0 &lt;= Node.val &lt;= 100
	1 &lt;= n &lt;= sz


&nbsp;

进阶：你能尝试使用一趟扫描实现吗？

"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def getLength(head: ListNode):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
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
