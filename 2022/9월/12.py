import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# import string
# str_str = list(string.ascii_uppercase)
# for index in range(1,1+one()):
#     a,b = inputing().split()
#     a=a*(len(b)//len(a))+a
#     print("Ciphertext:",end=" ")
#     for aa,bb in zip(a,b):
#         print(str_str[(str_str.index(aa)+str_str.index(bb))%26],end="")
#     print()
# import string
# strstr = list(string.ascii_lowercase)
# for _ in range(one()):
#     n,k = wow()
#     a = n
#     n_list = []
#     nnn_list = []
#     if n != 0:
#         while n != 0:
#             n_list.append(n%k)
#             nnn_list.append(n%k if n%k<10 else strstr[n%k-10])
#             n//=k
#         nn_list = sorted(list(set([i for i in range(k)])))
#         m_list = sorted(list(set(n_list)))
#         if m_list == nn_list:
#             answer = " contains all digits."
#         else:
#             answer = " does not contain all digits."
#         str_str = "".join(list(map(str,nnn_list[::-1])))
#     else:
#         str_str=0
#         answer = " does not contain all digits."
#     print(f"Base-{k} representation of {a} is {str_str};{answer}")

