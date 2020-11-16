teeth = [95,103,71,99,114,64,95,53,97,114,109,11,2,21,45,2,26,81,54,14,118,108,117,27,115,43,70,58,107]
coins = [20, 10, 5, 1]

a = []
for i in range(len(teeth)):
    a.append([])
    for j in range(len(coins)):
        a[i].append(int(teeth[i] / coins[j]))
        teeth[i] -= (coins[j] * a[i][j])

print(a)
