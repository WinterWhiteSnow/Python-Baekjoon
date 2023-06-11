import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://school.programmers.co.kr/learn/courses/30/lessons/42587
# from collections import deque
# def solution(priorities, location):
#     global cnt
#     n_list = priorities
#     cnt = 0
#     m_list = deque()
#     for i in range(len(n_list)):
#         m_list.append([i,n_list[i]])
#     n_list.sort()
#     # print("start!")
#     # print(n_list)
#     # print(m_list)
#     while len(m_list)>0:
#         if m_list[0][1]==n_list[-1]:
#             cnt+=1
#             n_list.pop()
#             index,num = m_list.popleft()
#             if index == location:
#                 return cnt
#         else:
#             m_list.rotate(-1)

#https://school.programmers.co.kr/learn/courses/30/lessons/42584
# def solution(prices):
#     n_list = prices
#     l = len(n_list)
#     answer = [0]*l
#     for start in range(l):
#         num = n_list[start]
#         cnt = 0
#         for end in range(start+1,l):
#             if num<=n_list[end]:
#                 cnt+=1
#             else:
#                 cnt+=1
#                 break
#         answer[start]=cnt
#     return answer

#https://school.programmers.co.kr/questions/39655
#https://school.programmers.co.kr/learn/courses/30/lessons/42577#qna
# def solution(phone_book):
#     n_list= phone_book
#     n_list.sort()
#     answer = True
#     l = len(n_list)
#     for i in range(l-1):
#         a,b = n_list[i],n_list[i+1]
#         if a == b[:len(a)]:
#             return False
#     return True

#https://school.programmers.co.kr/learn/courses/30/lessons/42578
# def solution(clothes):
#     n_list = clothes
#     n_dict = {}
#     answer=1
#     for value,key in n_list:
#         if key not in n_dict:
#             n_dict[key]=[value]
#         else:
#             n_dict[key]+=[value]
#     new_list = list(n_dict.values())
#     new_list = [len(i) for i in new_list]
#     for num in new_list:
#         answer*=num+1
#     return answer-1

#https://www.acmicpc.net/problem/1713
# n = one()
# l = one()
# n_list = list(wow())
# key = {}
# for i in range(l):
#     num = n_list[i]
#     if len(key)<n:
#         if num not in key:
#             key[num]=[1,i]
#         else:
#             key[num][0]+=1
#     else:
#         if num in key:
#             key[num][0]+=1
#         else:
#             time = 0
#             min_min = 10000000001
#             key_key = "none"
#             for k in key.keys():
#                 cnt,location = key[k]
#                 if min_min > cnt:
#                     key_key=k
#                     min_min=cnt
#                     time = location
#                 else:
#                     if min_min == cnt:
#                         if time > location:
#                             key_key=k
#                             min_min=cnt
#                             time = location
#             del key[key_key]
#             key[num]=[1,i]
# print(*sorted(key.keys()))

#https://school.programmers.co.kr/learn/courses/30/lessons/42579#
# def solution(genres, plays):
#     n_dict = {}
#     index = 0
#     for key,value in zip(genres,plays):
#         if key not in n_dict:
#             n_dict[key]=[[index,value]]
#             n_dict[key]+=[value]
#         else:
#             n_dict[key].insert(0,[index,value])
#             n_dict[key][-1]+=value
#         index+=1
#     new_list = list(n_dict.items())
#     new_list.sort(key=lambda x: x[1][-1],reverse=True)
#     answer = []
#     for key,list_list in new_list:
#         list_list = list_list[:-1]
#         list_list.sort(key=lambda x: x[0])
#         list_list.sort(key=lambda x: x[1],reverse=True)
#         for i in range(min(2,len(list_list))):
#             answer.append(list_list[i][0])
#     return answer
    

        













             












