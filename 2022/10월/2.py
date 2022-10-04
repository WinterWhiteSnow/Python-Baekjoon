import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#배스킨라빈스 31
# n_dict = {}
# for index in range(1,one()+1):
#     a,b = wow()
#     c = (a-1)%(b+1)
#     cnt = 1
#     ind = 1
#     while True:
#         if c+(b+1)*ind < a:
#             cnt+=1
#         else:
#             break
#         ind+=1
#     n_dict[index]=cnt*2
# n_list = list(n_dict.items())
# n_list.sort(key=lambda x : (x[1],x[0]))
# print(*n_list[0])








