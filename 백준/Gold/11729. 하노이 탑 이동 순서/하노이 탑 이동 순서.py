n = int(input())

def hanoi(n, from_, via, to):
    if n == 1:
        print(from_, to)
        return
    else:
        hanoi(n-1, from_, to, via)
        print(from_, to)
        hanoi(n-1, via, from_, to)

print(2**n - 1)
hanoi(n, 1, 2, 3)