# lc BWC 47

1:01:35 + 1 error - 1:06:35

T3 被卡常了，换了个做法过了；T4 想了半天，然后 debug 半天，最后发现写成拿排序后的数组取下标。。。

------

- 5680 easy

    按要求枚举并维护。

- 5681 medium

    从大到小减去 3 的幂次，最终看结果是否为 0. 或者转换为 3 进制看是否全部为 0 或 1.

- 5682 medium

    枚举左端点，不断增加右端点，维护字符频率并计算结果。使用 `dict` 会比数组快一些。或者预处理频率前缀和。

- 5683 hard

    首先预处理每个点的度数和每个点对的边数（用 `dict` 维护，二维数组空间显然会炸）。首先不考虑重复计算的问题，对于每个询问预处理符合要求的点对数目（排序后二分或者双指针）。然后枚举点对去重显然会超时，因此枚举边去重。计算每条边对应点对去重前后的边数，并更新询问结果即可。

------