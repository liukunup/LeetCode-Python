#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-05 15:00:00
# 抖音一面 4x4 矩阵顺时针旋转90度

# 视频图像测试开发工程师-抖音
# 职位描述
# 1、负责图像/视频主客观评测，产出全面的评测报告；
# 2、分析图像/视频增强和编解码算法的不足，提出改进意见；
# 3、负责图像/视频画质效果评测流程的建立和优化;
# 4、负责图像/视频画质评测能力增强和效率提升。
# 职位要求
# 1、软件工程、电子工程、CV、人工智能、多媒体等相关专业，本科及以上学历；
# 2、了解图像和视频主客观相关评测标准以及评测方法，熟练运用图像质量评测设备和软件(streameye,imatest等）；
# 3、了解视频超分，插帧，HDR，降噪等增强算法基本原理，有过相关测试调优经验优先；
# 4、有视频编解码的相关经验，熟悉视频编码标准H.264/H.265/VVC/VP9;
# 5、对视频编码标准技术有很好的理解，熟练使用ffmpeg；
# 6、熟练掌握C/C++，java，python等语言编写脚本和工具优化测试效率。

import unittest
from typing import List


class Solution:

    @staticmethod
    def rotate(matrix: List[List]) -> List[List]:

        # 交换矩阵行
        row_begin, row_end = 0, len(matrix) - 1
        while row_begin < row_end:
            tmp = matrix[row_begin]
            matrix[row_begin] = matrix[row_end]
            matrix[row_end] = tmp
            row_begin += 1
            row_end -= 1

        # 矩阵镜像
        n = len(matrix)
        for i in range(n):
            for j in range(0, i, 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        return matrix

    @staticmethod
    def rotate_v2(matrix: List[List]) -> List[List]:

        n = len(matrix)

        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = \
                    matrix[n - 1 - j][i], matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j]

        return matrix


    @staticmethod
    def rotate_v3(matrix: List[List]) -> List[List]:

        n = len(matrix)

        matrix_new = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                matrix_new[j][n-1-i] = matrix[i][j]

        return matrix_new


class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_base(self):
        matrix = [[0, 1, 2, 3],
                  [4, 5, 6, 7],
                  [8, 9, 10, 11],
                  [12, 13, 14, 15]]
        target = [[12, 8, 4, 0],
                  [13, 9, 5, 1],
                  [14, 10, 6, 2],
                  [15, 11, 7, 3]]
        res = self.inst.rotate_v3(matrix=matrix)
        print(res)
        self.assertEqual(res, target)


if __name__ == "__main__":
    unittest.main()
