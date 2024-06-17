# 올바른 괄호 쌍 => STACK !
def VPS(PS):
    stack = []
    for p in PS:
        if p == '(':
            stack.append(p)
        else: # ')'
            if not stack or stack[-1] == ')':
                stack.append(p)
            else: # 스택이 차있고 stack top이 여는 괄호일때
                stack.pop()
    if stack:
        return 'NO'
    return 'YES'

for _ in range(int(input())):
    print(VPS(input()))