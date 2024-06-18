def longest_increasing_subsequence(N, seq):
    # lis <- 해당 인덱스의 원소를 마지막 원소로 가지는 가장 긴 증가하는 부분수열의 길이를 저장
    # 가장 긴 증가부분수열 뒤에 원소가 붙을 수 있다면, 그 원소를 끝으로 하는 가_긴_증_부의 길이는 붙기전 가_긴_증_부 길이 + 1
    lis = [1 for x in range(N)]
    for i in range (1,N):
        for j in range(i):
            if seq[j] < seq[i]:
                lis[i] = lis[j] + 1 if lis[j] + 1 > lis[i] else lis[i]
    return max(lis)
N = int(input())
print(longest_increasing_subsequence(N,[int(x) for x in input().split()]))