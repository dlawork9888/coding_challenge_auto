def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 4, reverse=True) #문자열비교
    #print(numbers)
    if all(x == '0' for x in numbers):
        return '0'
    return ''.join(numbers)
