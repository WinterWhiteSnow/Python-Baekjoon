import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n_list = [str(i) for i in range(10)]
# m_list = "ABCDEFGHIJKL"
# mm = m_list.index("F")
# nn = n_list.index("9")
# n = one()
# if n >= 2013:
#     gap = n-2013
#     m_index = (mm+(gap%len(m_list)))%len(m_list)
#     n_index = (nn+(gap%len(n_list)))%len(n_list)
# else:
#     gap = 2013-n
#     # print(mm,nn,gap%len(m_list),gap%len(n_list))
#     m_index = (mm-(gap%len(m_list)))%len(m_list)
#     n_index = (nn-(gap%len(n_list)))%len(n_list)
# print(m_list[m_index]+n_list[n_index])
# from decimal import Decimal
# a,b = wow()
# x = a//b
# print(f"{x}.",end="")
# a%=b
# a,b=str(a),str(b)
# # print("start:",a,b)
# for _ in range(2000):
#     a = str(a)
#     a+="0"
#     # print(a)
#     print(Decimal(a)//Decimal(b),end="")
#     a =Decimal(a)%Decimal(b)




