t = int(input())
res_lst = []
for _ in range(t):
    n, k = map(int, input().split())
    row = input()
    lst = []
    for i in range(0, n, k):
        term = row[i:i + k]
        lst.append((term, term.count('W')))
    res_lst.append(min(lst, key=lambda x: x[1])[1])
print(*res_lst, sep='\n')
