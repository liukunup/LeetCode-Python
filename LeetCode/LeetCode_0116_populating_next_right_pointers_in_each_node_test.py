#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2024-08-14 22:25:04

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 116
# 题目名称: 填充每个节点的下一个右侧节点指针
# 题目难度: Medium

# 知识点: 树, 深度优先搜索, 广度优先搜索, 链表, 二叉树

# 题目详情:
"""
给定一个&nbsp;完美二叉树&nbsp;，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：


struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有&nbsp;next 指针都被设置为 NULL。

&nbsp;

示例 1：




输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。




示例 2:


输入：root = []
输出：[]


&nbsp;

提示：


	树中节点的数量在&nbsp;[0, 212&nbsp;- 1]&nbsp;范围内
	-1000 &lt;= node.val &lt;= 1000


&nbsp;

进阶：


	你只能使用常量级额外空间。
	使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        pre = []
        def dfs(node: 'Node', depth: int) -> None:
            if node is None:
                return
            if depth == len(pre):  # node 是这一层最左边的节点
                pre.append(node)
            else:  # pre[depth] 是 node 左边的节点
                pre[depth].next = node  # node 左边的节点指向 node
                pre[depth] = node
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)  # 根节点的深度为 0
        return root
        


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
