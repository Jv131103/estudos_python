def max_subarray_divide_conquer(nums):
    if not nums:
        raise ValueError("A lista não pode ser vazia.")

    def solve(lo, hi):
        # intervalo [lo, hi) (hi exclusivo)
        if hi - lo == 1:
            return nums[lo]

        mid = (lo + hi) // 2

        # 1) melhor totalmente à esquerda
        left_best = solve(lo, mid)

        # 2) melhor totalmente à direita
        right_best = solve(mid, hi)

        # 3) melhor atravessando o meio
        # melhor soma que termina em mid-1 (vai pra esquerda)
        s = 0
        best_left_suffix = float("-inf")
        for i in range(mid - 1, lo - 1, -1):
            s += nums[i]
            if s > best_left_suffix:
                best_left_suffix = s

        # melhor soma que começa em mid (vai pra direita)
        s = 0
        best_right_prefix = float("-inf")
        for i in range(mid, hi):
            s += nums[i]
            if s > best_right_prefix:
                best_right_prefix = s

        cross = best_left_suffix + best_right_prefix

        return max(left_best, right_best, cross)

    return solve(0, len(nums))


print(max_subarray_divide_conquer([1, -3, 2, 1, -1]))      # 3  (2 + 1)
print(max_subarray_divide_conquer([-2, -3, -1, -5]))       # -1 (só o -1)
print(max_subarray_divide_conquer([5, -1, 2, -1, 3]))      # 8  (5 -1 +2 -1 +3)
