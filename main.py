t = int(input())
res_lst = []
for _ in range(t):
    n, k = map(int, input().split())
    row = input()
    lst = []
    for i in range(0, n, k):
        lst.append((row[i:i + k].count('W')))
    res_lst.append(min(lst))
print(*res_lst, sep='\n')
