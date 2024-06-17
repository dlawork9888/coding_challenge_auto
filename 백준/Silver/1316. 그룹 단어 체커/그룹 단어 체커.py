def check(word):
    # 길이가 100밖에 안되니 해시는 안써도 될듯\
    atoms = []
    now_c = ''
    for c in word:
        if c == now_c:
            continue
        if not c in atoms:
            atoms.append(c)
            now_c = c
        else: # atoms에 있는 경우는 그룹단어가 아님
            return False
    return True


count = 0
for _ in range(int(input())):
    word = input()
    if check(word) == True:
        count += 1
print(count)