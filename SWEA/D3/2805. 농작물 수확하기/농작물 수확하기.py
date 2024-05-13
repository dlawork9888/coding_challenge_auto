def sol(arr):
    val_sum = 0
    for idx, row in enumerate(arr):
        temp = abs(len(arr)//2 - idx)
        val_sum += sum(row[temp:len(arr)-temp])
    return val_sum

for testcase in range(1, int(input())+1):
    arr_len = int(input())
    arr = []
    for _ in range(arr_len):
        arr.append([int(x) for x in input()])
    print(f"#{testcase} {sol(arr)}")