import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2688
# n_dict = {}
# for i in range(10):
#     n_dict[i]=1
# n_list = [0]*(1001)
# n_list[1]=10

# for k in range(2,1001):
#     m_dict = {}
#     for i in range(10):
#         m_dict[i]=n_dict[i]
#         for key in range(i-1,-1,-1):
#             m_dict[i]+=n_dict[key]
#     value = sum(m_dict.values())
#     n_list[k]=value
#     n_dict=m_dict
# for _ in range(one()):
#     print(n_list[one()])    

n_dict = {}
for _ in range(one()):
    num = one()
    if num not in n_dict:
        cnt = 1
        n_list = [0]*(num+1)
        n_list[num]=1
        
        cnt+=num//2
        cnt+=num//3
        n_dict[num]=cnt
    print(n_dict[num])
            
        
        
    
    
        
    





















