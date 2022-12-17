#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-17 23:45:05

# 导入所需的依赖库
import unittest
from typing import Optional

# 题目编号: 92
# 题目名称: 反转链表 II
# 题目难度: Medium

# 知识点: 链表

# 题目详情:
"""
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left  。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
 

示例 1：


输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]


示例 2：


输入：head = [5], left = 1, right = 1
输出：[5]


 

提示：


	链表中节点数目为 n
	1 
	-500 
	1 


 

进阶： 你可以使用一趟扫描完成反转吗？

"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prev_node = dummy
        for _ in range(left - 1):
            prev_node = prev_node.next

        curr_node = prev_node.next
        for _ in range(right - left):
            next_node = curr_node.next
            curr_node.next = next_node.next
            next_node.next = prev_node.next
            prev_node.next = next_node

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
