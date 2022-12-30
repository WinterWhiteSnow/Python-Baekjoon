import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1614
# n_list = "".join([str(i) for i in range(1,6)]+[str(i) for i in range(4,0,-1)])
# number = inputing()
# for i in range(2,6):
#     n_list+=str(i)
#     if n_list[-1]==number:
#         break
# r = one()+1
# l_find = n_list.find(number)
# cnt = l_find+1
# # print(n_list)
# n_list = n_list[l_find+1:]
# r-=1
# if number == "1":
#     n_list+="4321"  
# # print(n_list)  
# if number != "5":
#     r_find = n_list.find(number)
#     l_find = n_list.rfind(number)-r_find
#     r_find+=1
#     cnt += (r//2)*(r_find+l_find)
#     # print(l_find,r_find,r,cnt)
#     if r%2:
#         cnt+=r_find
# else:
#     r_find = n_list.find(number)+1
#     cnt+=r*r_find
# cnt-=1
# print(cnt)
#123454321














