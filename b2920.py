# 백준 2920번
# 음계

def check(n):
    result = 0 
 
    for i in range(len(n)):
        if i == len(n)-1:
            break
        elif n[i] > n[i+1]:
            result -= 1
        else:
            result += 1

    if result == 7:
        print('ascending')
    elif result == -7:
        print('descending')
    else:
        print('mixed')


n = list(map(int, input().split()))
check(n)
        

