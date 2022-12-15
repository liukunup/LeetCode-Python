#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-15 16:29:58

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 80
# 题目名称: 删除有序数组中的重复项 II
# 题目难度: Medium

# 知识点: 数组, 双指针

# 题目详情:
"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

&nbsp;

说明：

为什么返回数值是整数，但输出的答案是数组呢？

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:


// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i &lt; len; i++) {
&nbsp; &nbsp; print(nums[i]);
}


&nbsp;

示例 1：


输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素。


示例 2：


输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为&nbsp;0, 0, 1, 1, 2, 3, 3 。 不需要考虑数组中超出新长度后面的元素。


&nbsp;

提示：


	1 &lt;= nums.length &lt;= 3 * 104
	-104 &lt;= nums[i] &lt;= 104
	nums 已按升序排列


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        def remove(nums: List[int], k: int) -> int:
            n = len(nums)
            if n <= k:
                return n

            slow, fast = k, k
            while fast < n:
                if nums[slow - k] != nums[fast]:
                    nums[slow] = nums[fast]
                    slow += 1
                fast += 1

            return slow

        return remove(nums, k=2)


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(5, self.inst.removeDuplicates(nums=[1, 1, 1, 2, 2, 3]))
        self.assertEqual(7, self.inst.removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]))
        self.assertEqual(2, self.inst.removeDuplicates(nums=[1, 1, 1]))
        self.assertEqual(6, self.inst.removeDuplicates(nums=[1, 1, 1, 2, 2, 2, 3, 3]))


if __name__ == "__main__":
    unittest.main()
