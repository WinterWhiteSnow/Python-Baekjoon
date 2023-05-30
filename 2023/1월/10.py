import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# a,b,r = wow()
# r = str(r)
# cnt = 0
# for i in range(a,b+1):
#     i = str(i)
#     cnt+=i.count(r)
# print(cnt)

# l = one()
# str_str = inputing()
# print(min(str_str.count("H"),str_str.count("I"),str_str.count("A"),str_str.count("R"),str_str.count("C")))

# for _ in range(one()):
#     n_list = [list(wow()) for _ in range(one())]
#     k,d,ass =wow()
#     total =0
#     for i in n_list:
#         a,b,c = i
#         cnt = a*k-b*d+c*ass
#         total+=cnt if cnt >0 else 0
#     print(max(total,0)) 

# n,start = wow()
# n_list = list(wow())
# index = 0
# while True:
#     if n_list[index]>=start:
#         start+=1
#         index+=1
#         index%=n
#     else:
#         break
# print(index+1)

# import string
# str_str = list(string.ascii_uppercase)
# goal = "ILOVEYONSEI"
# start = inputing()
# cnt = 0
# for i in range(len(goal)):
#     index = str_str.index(start)
#     state = str_str.index(goal[i])
#     # print(index,state)
#     if index >= state:
#         cnt+=index-state
#     else:
#         cnt+=state-index
#     start = goal[i]
#     # print(cnt)
# print(cnt)

# while True:
#     a = one()
#     cnt = 0
#     if a == 0:
#         break
#     n_list = list(wow())
#     for i in range(1,a-1):
#         a,b,c = n_list[i-1],n_list[i],n_list[i+1]
#         if a<b and b>c:
#             cnt+=1
#     print(cnt)

# n_list = [[i+1]+list(wow()) for i in range(one())]
# n_list.sort(key=lambda x: x[2],reverse=True)
# answer = n_list[0]
# index,time,score = answer
# print(time+(index-1)*20 if score != 0 else 0)

for _ in range(one()):
    b,p = map(float,inputing().split())
    index = 15/p
    time = p*index
    beat = b*index
    print(time,beat)









