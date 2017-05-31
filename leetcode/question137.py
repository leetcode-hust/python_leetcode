#!/usr/bin/python
# -*- coding: utf-8 -*
"""
:author:
    Lou yuting
:create_date:
    2017
:descrition:
    Q137. Single Number II  【medium】 一个整型数组，每个元素出现三次，有一个出现一次，找出这个单独的数字：
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int] 是一个列表
        :rtype: int  返回值是一个整形
        1）解决思路：用hash表啊， 统计每个数字出现的次数，最后遍历hash表，找出出现一次的数字

        2）解决思路：数据压缩，依次将每一个数字转换成二进制，然后统计每一位上出现的次数。最后依次统计结果，
           当某一位不是3的倍数，那么该位就是1.最后获取到结果。
        """
        hash = {}
        for key in nums:
            value = hash.get(key)
            if (value is None):
                hash[key] = 1
            else:
                hash[key] = value + 1

        for key, value in hash.items():
            if (value % 3 == 0):
                continue
            else:
                return key

solution = Solution()
print solution.singleNumber([1,2,3,4,4,3,1,1,2,2,3,4,5])


