# 통합 => 아.. 클래스 쓰지말걸... 난잡해...

# 입력 처리
class Node:
    def __init__(self):
        self.name = -1 
        self.left_child = None
        self.right_child = None
    def set_name(self, name):
        self.name = name
    def set_children(self, left_child, right_child):
        self.left_child = left_child
        self.right_child = right_child

N = int(input())
tree = []
for i in range(N):
    node = Node()
    node.set_name(i)
    left_child, right_child = [int(x)-1 if x!= "-1" else None for x in input().split()]
    node.set_children(left_child, right_child)
    tree.append(node)
    
def check_direction(now_node, K):
    if now_node.left_child == None and now_node.right_child == None:
        return 'stop', K
    if now_node.left_child != None and now_node.right_child == None:
        return 'left', K
    if now_node.left_child == None and now_node.right_child != None:
        return 'right', K
    if K % 2 != 0:
        return 'left', K // 2 + 1 if K % 2 == 1 else K // 2
    if K % 2 == 0:
        return 'right', K // 2

K = int(input())
now_node_name = 0

while True:
    now_node = tree[now_node_name]
    direction, now_K = check_direction(now_node, K)
    if direction == 'stop':
        print(now_node.name + 1)
        break
    elif direction == 'left':
        #print('왼')
        now_node_name = now_node.left_child
        K = now_K
    else:
        #print('오')
        now_node_name = now_node.right_child
        K = now_K
    