# lc BWC 37

7/19

0:07:33

脑子抽了一直在想 T3, 写了一个立方复杂度的记忆化搜索，果不其然 TLE 了，然后一直在想组合数，结果 T4 也没时间做了，比赛结束才发现 T4 特别简单。

大概不仅数学忘光了，脑子也坏了。

------

- 5122 easy
    排序后切片/模拟。

- 5528 medium
    按照题意写函数，然后遍历维护最大值和对应坐标即可。

- 5527 medium
    dp, 最直接的想法就是记忆化搜索，对于每一条线段按照不同右端点分别求次数，但是这样的时间复杂度是 `O(KN^2)` 的。这个时候观察发现求次数数组是有规律的（系数为等差数列），可以通过数列的裂项求和来优化到 `O(NK)`. 
    
    另一种方案是对于每条线段和每个格点定义到达和未到达两种状态，分别列转移方程。还有一种方案是直接转化为组合数 `C(n + k + 1, 2 * k)` 来解决（考虑每条线段的起点和终点，对每条线段右移相应的格数避免重复，就变成最简单的组合问题了）。

- 5530 hard
    维护前缀和和积数组，在每次加入数的时候更新。 query 的时候，只要根据当时的和积和 query 时的和积即可逆推出现在的数字大小。对于取模，除法需要用到数论的求逆，费马小定理+快速幂。


------
