# lc weekly contest 208

18/18

0:41:17 + 1 error 0:46:17

全程暴力，感觉自己没睡醒

------

- 5523 easy
    模拟，一个 dot 不变，两个 dot 深度减一，其余深度加一，到零减不下去。

- 5524 medium
    首先排除永远无法盈利的情况，其次维护最大值和对应时间，在有游客抵达范围内模拟。如果最后还有人等待，求余计算最大值。注意细节，没了。

- 5525 medium
    N 叉树遍历，用一个 hash table 维护姓名到对应节点的映射。

- 5526 hard
    数据范围很小，筛掉自环，然后暴力 dfs （甚至不需要剪枝）

------

困，读题时间太长，没考虑 edge case