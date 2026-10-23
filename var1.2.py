nums = [3, 2, 1, 5, 6, 4]
k = 2

for i in range(k):
    m = nums.index(max(nums))
    x = nums.pop(m)

print(x)
