# 백준 1920번
# 수 찾기
# 0
# 시간초과 : list -> set 으로 해결

import sys

def check(n, a, m, b):

    for i in b:
        if i in a:
            res = 1
        else:
            res = 0

        print(res)
    

n = int(sys.stdin.readline())
a = set(map(int, sys.stdin.readline().split()))    
m = int(sys.stdin.readline())
b = set(map(int, sys.stdin.readline().split()))

check(n, a, m, b)