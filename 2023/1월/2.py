import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2015
# l,k = wow()
# n_list = list(wow())
# n_dict = {} #순서적으로 index-1까지만 반영하기 때문에, 여러구간의 누적합을 고려할 수 있음
# prefix = 0
# cnt = 0 
# for i in n_list:
#     prefix+=i
#     # print(prefix,cnt)
#     if prefix ==  k:
#         cnt+=1
#     if prefix-k in n_dict:
#         cnt+=n_dict[prefix-k]    
#     if prefix not in n_dict:
#         n_dict[prefix]=1
#     else:
#         n_dict[prefix]+=1
# print(cnt)

def go(a,aa,aaa):
    index = f"{a}{aa}{aaa}"
    # print(a,aa,aaa)
    # print(n_dict)
    n_dict[index]=1
    if a>=2:
        b,bb,bbb=a-2,aa+1,aaa
        index_index = f"{b}{bb}{bbb}"
        if index_index not in n_dict:
            go(b,bb,bbb)
    if a>=1 and aa>=1:
        b,bb,bbb=a-1,aa-1,aaa+1
        index_index = f"{b}{bb}{bbb}"
        if index_index not in n_dict:
            go(b,bb,bbb)
    if a>=3:
        b,bb,bbb=a-3,aa,aaa+1
        index_index = f"{b}{bb}{bbb}"
        if index_index not in n_dict:
            go(b,bb,bbb)
    
    
for _ in range(one()):
    num = one()
    n_dict = {}
    go(num,0,0)
    print(len(n_dict))



























