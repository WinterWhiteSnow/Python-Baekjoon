import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1524
# import heapq
# for _ in range(one()): #세준세비
#     inputing()
#     a,b = wow()
#     a_list = sorted(list(wow()))
#     b_list = sorted(list(wow()))
#     while len(a_list) != 0 and len(b_list) != 0:
#         x,y = heapq.heappop(a_list),heapq.heappop(b_list)
#         if x==y:
#             heapq.heappush(a_list,x)
#         else:
#             if x>y:
#                 heapq.heappush(a_list,x)
#             else:
#                 heapq.heappush(b_list,y)
#     # print(a_list,b_list)
#     x,y = len(a_list),len(b_list)
#     if x==y:
#         print("C")
#     else:
#         if x>y:
#             print("S")
#         else:
#             print("B")

#https://www.acmicpc.net/problem/2607
# state = "none"
# cnt = 0
# for _ in range(one()):
#     a = list(inputing())
#     if state == "none":
#         state = a
#     else:
#         ss,aa = set(state),set(a)
#         total = ss | aa
#         count = 0
#         a_cnt = 0
#         s_cnt = 0
#         check = "yes"
#         for t in total:
#             # print("Start",t)
#             if t in a and t in state:
#                 xx,yy = a.count(t),state.count(t)
#                 if xx==yy:
#                     pass
#                 else:
#                     index = abs(xx-yy)
#                     if index == 1:
#                         if xx > yy:
#                             if s_cnt == 0:
#                                 s_cnt = index
#                             else:
#                                 check = "no"
#                         else:
#                             if a_cnt == 0:
#                                 a_cnt=index
#                             else:
#                                 check = "no"
#                     else:
#                         check = "no"
#             else:
#                 if t in a:
#                     if s_cnt == 0:
#                         s_cnt = a.count(t)
#                     else:
#                         check = "no"
#                 else:
#                     if a_cnt == 0:
#                         a_cnt = state.count(t)
#                     else:
#                         check = "no"
#             if a_cnt != 0 and s_cnt != 0:
#                 if a_cnt == s_cnt == 1:
#                     pass
#                 else:
#                     check = "no"
#             # print(t,s_cnt,a_cnt,check)
#         # print(check,a)
#         if check == "yes":
#             cnt+=1
# print(cnt)

#https://www.acmicpc.net/problem/2138
# l = one()
# a_list = list(inputing())
# b_list = list(inputing())
# press_b = [i for i in b_list]
# wait_b = [i for i in b_list]
# p_cnt = 1
# w_cnt = 0
# for i in range(0,2):
#     press_b[i]="0" if press_b[i]=="1" else "1"
# # print(a_list)
# # print(press_b,wait_b)
# for i in range(1,l):
#     p,w = press_b[i-1],wait_b[i-1]
#     check = a_list[i-1]
#     if p!=check:
#         p_cnt+=1
#         for index in range(i-1,min(i+2,l)):
#             press_b[index]="0" if press_b[index]=="1" else "1"
#     if w != check:
#         w_cnt+=1
#         for index in range(i-1,min(i+2,l)):
#             wait_b[index]="0" if wait_b[index]=="1" else "1"
# # print("end",press_b,wait_b)
# if press_b==wait_b==a_list:
#     print(min(p_cnt,w_cnt))
# else:
#     if press_b == a_list:
#         print(p_cnt)
#     elif wait_b==a_list:
#         print(w_cnt)
#     else:
#         print(-1)                                  
# # print(p_cnt,w_cnt)

x,y,line,cross=wow()
y_index,x_index=0,0
time = 0
while True:
    x_gap = x-x_index
    y_gap=y-y_index
    if x_gap>0 and y_gap>0:
        plus = min(x_gap,y_gap)
        y_index+=plus
        x_index+=plus
        if line*2 >= cross:
            time+=cross*plus
        else:
            time+=(line*2)*plus
    else:
        if x_gap > 0:
            x_index=x
            time+=line*x_gap
        else:
            y_index=y
            time+=line*y_gap
    if x_index==x and y_index==y:
        break
    
print(time)
        
            
                        
                    
                












