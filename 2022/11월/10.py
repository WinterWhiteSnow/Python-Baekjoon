import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/3758
# for _ in range(one()):
#     n_dict = {}
#     n,k,my,r = wow()
#     for i in range(r):
#         a,b,c = wow()
#         if a not in n_dict:
#             n_dict[a]={"cnt":1,"end":i}
#         else:
#             n_dict[a]["cnt"]+=1
#             n_dict[a]["end"]=i
#         if b not in n_dict[a]:
#             n_dict[a][b]=c
#         else:
#             n_dict[a][b]=max(n_dict[a][b],c)
#     list_list = []
#     score_list = []
#     for key in n_dict.keys():
#         cnt = n_dict[key]["cnt"]
#         end = n_dict[key]["end"]
#         score = sum(list(n_dict[key].values())[2:])
#         list_list.append([score,cnt,end,key])
#         if score not in score_list:
#             score_list.append(score)
#     score_list.sort(reverse=True)
#     list_list.sort(key=lambda x: (x[1],x[2]))
#     list_list.sort(key=lambda x: x[0],reverse=True)
#     # print(score_list)
#     # print(list_list)
#     for i in range(len(list_list)):
#         if list_list[i][-1] == my:
#             print(i+1)
#             break

#https://www.acmicpc.net/problem/4779
# for i in sys.stdin.readlines():
#     num = int(i.strip())
#     if num == 0:
#         print("-")
#     else:
#         str_str=["- -"]
#         for _ in range(num-1):
#             str_str=str_str*3
#             str_str[1]=" "*len(str_str[1])
#             str_str=["".join(str_str)]
#         print(*str_str)

#https://www.acmicpc.net/problem/17252
# num = one()
# if num == 0:
#     print("NO")
# else:
#     list_list = []
#     while num != 0:
#         list_list.append(str(num%3))
#         num//=3    
#     print("YES" if "2" not in list_list else "NO")

#https://www.acmicpc.net/problem/6219
# n_dict = {}
# for i in range(2,4000001):
#     if i not in n_dict:
#         for a in range(i,4000001,i):
#             n_dict[a]=0
#         n_dict[i]=1
# n_list = sorted([a for a,b in n_dict.items() if b == 1])
# a,b,c = wow()
# a,b = min(a,b),max(a,b)
# def go(start,end,number):
#     while start<=end:
#         mid = (start+end)//2
#         if n_list[mid] > number:
#             end=mid-1
#         else:
#             start=mid+1
#     return [start,end]
# x = max(go(0,len(n_list),a))
# if x>0:
#     while n_list[x] > a:
#         if n_list[x-1]>=a:
#             x-=1
#         else:
#             break
#         if x == 0:
#             break
# cnt = 0
# for index in range(x,len(n_list)):
#     if a<=n_list[index]<=b:
#         if str(c) in str(n_list[index]):
#             cnt+=1
#     else:
#         break
# print(cnt)

#https://www.acmicpc.net/problem/17212
# num = one()
# if num == 0:
#     print(0)
# else:
#     n_list = [i for i in range(num+2)]
#     # print(n_list)
#     for index in [2,5,7]:
#         if num >= index:
#             n_list[index]=1
#         for number in range(index,num+1):
#             n_list[number]=min(n_list[number-index]+1,n_list[number])
#             # print(n_list)
#     print(n_list[num])

#https://www.acmicpc.net/problem/25487
# for _ in range(one()):
#     a,b,c = wow()
#     print(min(a,b,c))

#https://www.acmicpc.net/problem/6571
# n_list = [1,2]
# while True:
#     a,b = wow()
#     if a==b==0:
#         break
#     while n_list[-1] < b:
#         n_list.append(n_list[-1]+n_list[-2])
#     start = 0
#     end = len(n_list)-1
#     while start<=end:
#         mid = (start+end)//2
#         if n_list[mid] > a:
#             end=mid-1
#         else:
#             start=mid+1
#     # print(n_list)
#     # print(start,end,n_list[start],a)
#     if start-1 >= 0:
#         # print("wow!")
#         while n_list[start-1]>= a:
#             # print("what")
#             if start-1 >= 0:
#                 start-=1
#             # print(start)
#             if start == 0:
#                 break
#     cnt = 0
#     # print(n_list)
#     # print(start,n_list[start])
#     for i in range(start,len(n_list)):
#         if a<=n_list[i]<=b:
#             cnt+=1
#     print(cnt)


        



















