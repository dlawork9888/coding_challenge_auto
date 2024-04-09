# 장르 별 Top2
# 장르 > 재생 수 (재생 수 같다면 고유번호 낮은 기준)

from collections import defaultdict as dd

#def for_sort(x):
    

def solution(genres, plays):
    
    # 1.
    # 장르 재생수 defaultdict
    # 장르별 재생 수와 고유번호
    # 이 둘의 한 번의 순회로
    
    play_of_genre = dd(int)
    play_and_idx = dd(list)
    
    for idx, genre in enumerate(genres):
        play_of_genre[genre] += plays[idx]
        play_and_idx[genre].append((plays[idx], idx)) #(재생 수, 고유번호)
    
    answer = []
    for item in sorted(play_of_genre.items(), key = lambda x: -x[1]):
        genre = item[0]
        answer += [x[1] for x in sorted( play_and_idx[genre], key = lambda x: (-x[0],x[1]) )[:2]]

    return answer
    
    