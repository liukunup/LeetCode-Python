#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-08 10:28:30

# 导入所需的依赖库
import unittest
from typing import Optional

# 题目编号: 206
# 题目名称: 反转链表
# 题目难度: Easy

# 知识点: 递归, 链表

# 题目详情:
"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。


 

示例 1：


输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]


示例 2：


输入：head = [1,2]
输出：[2,1]


示例 3：


输入：head = []
输出：[]


 

提示：


	链表中节点的数目范围是 [0, 5000]
	-5000 


 

进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？



"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        return prev


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
