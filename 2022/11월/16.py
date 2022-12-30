import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2149
# key = list(input())
# nlist =input()
# sortkey=sorted(key)
# ndict={}
# r = len(nlist)//len(key)
# index = 0
# for k in sortkey:
#     gap = r*index
#     if k not in ndict:
#         ndict[k]=[nlist[gap:gap+r]]
#     else:
#         ndict[k]+=[nlist[gap:gap+r]]
#     index+=1
# # print(ndict)
# listlist=[]
# for i in key:
#     listlist+=[ndict[i][0]]
#     ndict[i]=ndict[i][1:]
#     # print(i,listlist)
# adict={}
# for p in listlist:
#     for i in range(len(p)):
#          if i not in adict:
#             adict[i]=p[i]
#          else:
#             adict[i]+=p[i]
# for kk in adict.keys():
#     print(adict[kk],end="")



























