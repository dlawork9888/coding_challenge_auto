# 종합
def input_process():
    N, K = [int(x) for x in input().split()]
    items = []
    for _ in range(N):
        items.append([int(x) for x in input().split()])
    return N, K, items

N, K, items = input_process()

dp_table = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    now_item_weight = items[i - 1][0]
    now_item_value = items[i - 1 ][1]
    for j in range(1, K + 1):
        if now_item_weight <= j:
            dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i - 1][j - now_item_weight] + now_item_value)
        else:
            dp_table[i][j] = dp_table[i - 1][j]
print(dp_table[-1][-1])