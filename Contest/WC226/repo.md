lc weekly contest 226

18/18

0:37:20 + 2 errors = 0:47:20

日常不认真读题 结果 T2 T3 全都看复杂了

------

- 5654 easy

    数据范围小，可以依次统计，如果数据范围大需要使用数位 dp 来求解。

- 5665 medium

    简化的欧拉回路问题。由于数组元素不同，因此统计度后首尾元素必定为 1. 拓扑排序即可。如果数组元素有重复可以使用 Hierholzer 算法来解决。

- 5667 medium

    阅读理解题。由于每天可以吃不同种类的糖，因此可以对不同种类糖的数量取前缀和。对于每个 query 只需要判断当天可以吃到糖果的上下界和喜欢的糖果的上下界是否重合即可。

- 5666 hard

    首先预处理每个区间是否为回文串，其次枚举边界即可。如果分割的数量更多则可以再次使用 dp.

------

还是要认真读题再做（