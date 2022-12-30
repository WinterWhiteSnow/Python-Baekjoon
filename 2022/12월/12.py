import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/10986
# l,k = wow()
# n_list = list(wow())
# tem_list = [n_list[0]%k]
# for i in range(1,l):
#     tem_list.append((tem_list[-1]+n_list[i])%k)
# n_dict = {}
# for i in tem_list:
#     if i not in n_dict:
#         n_dict[i]=1
#     else:
#         n_dict[i]+=1
# cnt = 0 if 0 not in n_dict else n_dict[0]
# for key in n_dict.keys():
#     index = n_dict[key]-1
#     cnt+=(index*(index+1))//2
# print(cnt)

zero_list = [[0]*(4) for _ in range(10001)]
zero_list[1][1]=1
zero_list[2][1]=1
zero_list[2][2]=1
zero_list[3][1]=1
zero_list[3][2]=1
zero_list[3][3]=1
for num in range(4,10001):
    zero_list[num][1]=1
    zero_list[num][2]=zero_list[num-2][1]+zero_list[num-1][2]
    zero_list[num][3]=zero_list[num-3][1]+zero_list[num-3][2]+zero_list[num-3][3]
for _ in range(one()):
    r = one()
    print(zero_list[r][1]+zero_list[r][2]+zero_list[r][3])














