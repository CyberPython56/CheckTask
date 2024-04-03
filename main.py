def func():
    n, k = map(int, input().split())
    row = input()
    res = 10 ** 6
    # for i in range(0, n, k):
    #     d = {'B': 0, 'W': 0}
    #     for j in range(k):
    #         d[row[j]] += 1
    #     res = min(res, d['W'])
    for i in range(0, n, k): # for проходит по n // k количеству элементов
        term = row[i:i + k].count('W') # count() проходится по строке длиной k
        if term < res:
            res = term
    return res


t = int(input())
res_lst = [func() for i in range(t)]
print(*res_lst, sep='\n')
