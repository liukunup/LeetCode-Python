#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-06 19:33:31

# 导入所需的依赖库
import unittest
from typing import List, Optional

# 题目编号: 23
# 题目名称: 合并K个升序链表
# 题目难度: Hard

# 知识点: 链表, 分治, 堆（优先队列）, 归并排序

# 题目详情:
"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

&nbsp;

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1-&gt;4-&gt;5,
  1-&gt;3-&gt;4,
  2-&gt;6
]
将它们合并到一个有序链表中得到。
1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4-&gt;5-&gt;6


示例 2：

输入：lists = []
输出：[]


示例 3：

输入：lists = [[]]
输出：[]


&nbsp;

提示：


	k == lists.length
	0 &lt;= k &lt;= 10^4
	0 &lt;= lists[i].length &lt;= 500
	-10^4 &lt;= lists[i][j] &lt;= 10^4
	lists[i] 按 升序 排列
	lists[i].length 的总和不超过 10^4


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 正确 但是会超时
        # 判空 (示例2/3)
        dummy = ListNode()
        if not lists or (len(lists) == 1 and not lists[0]):
            return dummy.next

        # 每个链表的队头维护
        heads = list()
        for i in range(len(lists)):
            heads.append(ListNode())
            heads[i] = lists[i]

        # 初始化指向
        cur = dummy
        # 遍历结束计数
        end_count = 0

        while end_count < len(heads):

            # 选取序号
            index = -1
            # 重置计数
            end_count = 0

            # 遍历头节点
            for i in range(len(heads)):
                # 当前在遍历的头
                head = heads[i]
                if not head:
                    end_count += 1
                    continue

                # 初始虚拟节点
                if not cur.next:
                    cur.next = head
                    index = i
                    continue

                # 更新节点
                if head.val <= cur.next.val:
                    cur.next = head
                    index = i

            # 游标前移
            if index >= 0:
                heads[index] = heads[index].next
                cur = cur.next

        # 打印检查
        p = dummy.next
        while p:
            print(p.val)
            p = p.next

        return dummy.next

    def mergeKLists_v2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 优先队列
        import heapq
        # 初始化虚拟节点
        dummy = ListNode()
        cur = dummy

        # 头节点入优先队列
        heads = list()
        for i in range(len(lists)):
            if lists[i]:
                # 入队
                heapq.heappush(heads, (lists[i].val, i))
                # 未入队的调整为下一次的头节点
                lists[i] = lists[i].next

        while heads:
            # 最小的出队
            val, idx = heapq.heappop(heads)
            # 组装 & 移动游标
            cur.next = ListNode(val)
            cur = cur.next
            # 最小的链表这条，头节点继续入队
            if lists[idx]:
                heapq.heappush(heads, (lists[idx].val, idx))
                lists[idx] = lists[idx].next

        # 打印检查
        p = dummy.next
        while p:
            print(p.val)
            p = p.next

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
        l1 = ListNode(3, ListNode(6, ListNode(9)))
        l2 = ListNode(2, ListNode(5, ListNode(8)))
        l3 = ListNode(1, ListNode(4, ListNode(7)))
        self.assertEqual(None, self.inst.mergeKLists_v2(lists=[l1, l2, l3]))


if __name__ == "__main__":
    unittest.main()
