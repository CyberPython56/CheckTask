t = int(input())
res_lst = []
for _ in range(t):
    n, k = map(int, input().split())
    row = input()
    lst = []
    cur_row = ''
    rows_of_black = [x for x in row.split('W') if x]
    if any([True for x in rows_of_black if len(x) == k]):
        res_lst.append(0)
    elif n == k:
        res_lst.append(row.count('W'))
    else:
        for i in range(n - 1):
            cur_row += row[i]
            if row[i + 1] != row[i]:
                lst.append(cur_row)
                cur_row = ''
            if i == n - 2:
                if row[i + 1] == row[i]:
                    lst[-1] += row[-1]
                else:
                    lst.append(row[-1])
        res_ = []
        for i in range(len(lst) - 2):
            if len(lst[i]) + len(lst[i + 1]) + len(lst[i + 2]) >= k:
                res_.append(len(lst[i + 1]))
            elif len(lst[-i - 1]) + len(lst[- i - 2]) + len(lst[-i - 3]) >= k:
                res_.append(len(lst[-i - 2]))
        res_lst.append(min(res_))
print(*res_lst, sep='\n')
