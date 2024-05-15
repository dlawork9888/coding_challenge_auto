from collections import deque
from collections import defaultdict

def solution(game_board, table):
    
    def piece_scaling(piece):
        front_smallest = min([front for front, _ in piece])
        back_smallest = min([back for _, back in piece])
        for idx, loc in enumerate(piece):
            piece[idx] = [loc[0] - front_smallest, loc[1] - back_smallest]
        return piece

    def search_pieces(arr, n):  # n은 0또는 1 => n인 부분을 찾음
        # search directions
        d_row = [0, 1, 0, -1]
        d_col = [1, 0, -1, 0]
        # 조각을 저장할 배열
        pieces = defaultdict(list)
        # n과 반대 => 1 or 0
        reverse_n = 1 if n == 0 else 0
        while True:
            start_node = [-1, -1]
            start_node_flag = False
            for row_idx, row in enumerate(arr):
                for col_idx, value in enumerate(row):
                    if value == n:
                        start_node = [row_idx, col_idx]
                        start_node_flag = True
                        break
                if start_node_flag == True:
                    break
            # 시작 노드를 못찾았을 경우에는 while True를 종료
            if start_node_flag == False:
                break

            # bfs
            piece = []
            q = deque()
            q.append(start_node)
            arr[start_node[0]][start_node[1]] = reverse_n  # 방문 표시
            piece.append(start_node)
            while q:
                now_node = q.popleft()
                # 주변 노드 조사
                for i in range(4):
                    next_row = now_node[0] + d_row[i]
                    next_col = now_node[1] + d_col[i]
                    # arr 안쪽 ?
                    if 0 <= next_row < len(arr) and 0 <= next_col < len(arr):
                        # n인가?
                        if arr[next_row][next_col] == n:
                            q.append([next_row, next_col])
                            piece.append([next_row, next_col])
                            arr[next_row][next_col] = reverse_n  # 방문 표시
            piece = piece_scaling(piece)
            piece.sort(key=lambda x: (x[0], x[1]))
            pieces[len(pieces)] = piece
        # print(f'pieces(not scaled): {pieces}')
        return pieces

    def rotate_90(piece):
        len_arr = max([x for x, _ in piece])
        return [[y, len_arr - x] for x, y in piece]

    game_table_pieces = search_pieces(game_board, 0)
    table_pieces = search_pieces(table, 1)

    count = 0
    for game_key in game_table_pieces.keys():
        hole = game_table_pieces[game_key]
        for key in table_pieces.keys():
            break_flag = False
            target = table_pieces[key]
            for i in range(4):
                target = rotate_90(target)
                target.sort(key=lambda x: (x[0], x[1]))
                if hole == target:
                    count += len(target)
                    del table_pieces[key]
                    break_flag = True
                    break
            if break_flag == True:
                break
    return count
    