def get_max(nums, trade):
    t = 0
    while trade > t:
        max_idx = []
        for i in range(len(nums)):
            if nums[i] == max(nums):
                max_idx.append(i)
        chance = len(max_idx)
        for _ in range(chance):
            c = nums.index(min(nums[:chance]))
            d = max_idx.pop()
            nums[c], nums[d] = nums[d], nums[c]
            t += 1
            if t == trade:
                break

T = int(input())
for tc in range(1, T+1):
    n, trade = map(str, input().split())
    nums = list(map(int, n))
    trade = int(trade)
    get_max(nums, trade)
    print(f'#{tc} {"".join(map(str, nums))}')
