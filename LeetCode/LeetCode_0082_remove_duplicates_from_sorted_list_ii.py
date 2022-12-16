#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-16 11:02:39

# 导入所需的依赖库
import unittest
from typing import Optional

# 题目编号: 82
# 题目名称: 删除排序链表中的重复元素 II
# 题目难度: Medium

# 知识点: 链表, 双指针

# 题目详情:
"""
给定一个已排序的链表的头&nbsp;head ，&nbsp;删除原始链表中所有重复数字的节点，只留下不同的数字&nbsp;。返回 已排序的链表&nbsp;。

&nbsp;

示例 1：


输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]


示例 2：


输入：head = [1,1,1,2,3]
输出：[2,3]


&nbsp;

提示：


	链表中节点数目在范围 [0, 300] 内
	-100 &lt;= Node.val &lt;= 100
	题目数据保证链表已经按升序 排列


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(next=head)

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                duplicated_value = cur.next.val
                while cur.next and cur.next.val == duplicated_value:
                    cur.next = cur.next.next
            else:
                cur = cur.next

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
