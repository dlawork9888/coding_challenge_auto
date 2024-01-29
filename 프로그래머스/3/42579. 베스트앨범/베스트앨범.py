# genre_play_dict 
# genre_song_dict 
from collections import defaultdict

def solution(genres, plays):
    genre_play_dict = defaultdict(int)
    genre_song_dict = defaultdict(list)

    # 순회
    for idx, genre in enumerate(genres):
        genre_play_dict[genre] += plays[idx]
        genre_song_dict[genre].append((idx, plays[idx])) # 고유번호, 재생수

    # dict => list => 정렬
    genre_play_list = list(genre_play_dict.items())
    genre_play_list.sort(key = lambda x: x[1], reverse = True) ## 문법
    """
    lambda x: x[1]
    =
    def func(x):
        return x[1]
    """
    answer = []
    for genre, play in genre_play_list: # 원소는 튜플, play는 안씀
        # 고유번호, 재생수
        genre_song_dict[genre].sort(key = lambda x: (x[1], -x[0]), reverse = True) # 마이너스!
        # 1차 기준 x[1] => 재생수는 내림차
        # 2차 기준 x[0] => 고유번호는 오름차, 
        # 1차 기준 위상 동일 => 2차 기준 비교
        for x in genre_song_dict[genre][:2]:
            answer.append(x[0])
    return answer