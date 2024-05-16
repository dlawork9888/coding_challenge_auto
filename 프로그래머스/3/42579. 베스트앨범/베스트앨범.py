from collections import defaultdict
def solution(genres, plays):
    genres_play = defaultdict(int)  # 장르: 총 재생수
    genres_idx = defaultdict(list)  # 장르:[(재생수, 고유번호),(재생수, 고유번호), ...]
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        # 장르별 총 재생 수 계산
        genres_play[genre] += play
        # 장르별 (재생수, 고유번호) 분류
        genres_idx[genre].append((play, idx))
    result = []
    # 총재생수의 내림차순으로 정리된 genres_play.items()
    for genre, _ in sorted(genres_play.items(), key=lambda genre_play: -genre_play[1]):  # (장르, 재생수)에서 재생수의 내림차순으로 정렬
        # (재생수, 고유번호)에서 재생수는 내림차순, 재생수 같다면 고유번호 오름차순 => [:2] => 고유번호만
        result.extend(
            [ele[1] for ele in sorted(genres_idx[genre], key=lambda play_idx: (-play_idx[0], play_idx[1]))[:2]])
    return result