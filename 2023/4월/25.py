import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n = one()
# cnt = 1
# index = 2
# while index**2 <n:
#     cnt+=1
#     index+=1
# print(cnt)

# l = one()
# n_list = list(wow())
# list_list = []
# for i in range(1,l+1):
#     num = i
#     list_list.insert(n_list[i-1],num)
#     # print(list_list)
# print(*list_list[::-1])

n_list = [one() for i in range(9)]
n_list.sort()
# print(sum(n_list))
minus = sum(n_list)-100
for x in range(8):
    c = False
    for y in range(x+1,9):
        if n_list[x]+n_list[y] == minus:
            n_list[x],n_list[y]=0,0
            c = True
            break
    if c:
        break
n_list.sort()
n_list = n_list[2:]
print(*n_list,sep="\n")














