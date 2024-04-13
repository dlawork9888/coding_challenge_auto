def solution(N, number):
    if N == number: 
        return 1
    cal_results = [[],[N]]
    count = 2
    while count < 9:
        cal_results.append([N*int('1'*count)])
        for i in range(count):
            fronts = cal_results[i]
            backs = cal_results[count - i]
            for front in fronts:
                for back in backs:
                    cal_results[count].append(front + back)
                    cal_results[count].append(front - back)
                    cal_results[count].append(front * back)
                if back != 0:
                    cal_results[count].append(front // back)
        cal_results[count] = list(set(cal_results[count]))
        if number in cal_results[count]:
            return count
        count += 1
    return -1
    
        
                