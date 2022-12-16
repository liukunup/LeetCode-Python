#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-16 11:19:02

# 导入所需的依赖库
import unittest
from typing import Optional

# 题目编号: 86
# 题目名称: 分隔链表
# 题目难度: Medium

# 知识点: 链表, 双指针

# 题目详情:
"""
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

 

示例 1：


输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]


示例 2：


输入：head = [2,1], x = 2
输出：[1,2]


 

提示：


	链表中节点的数目在范围 [0, 200] 内
	-100 
	-200 


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy_small = ListNode()
        small = dummy_small
        dummy_large = ListNode()
        large = dummy_large

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next

        large.next = None
        small.next = dummy_large.next

        return dummy_small.next






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
