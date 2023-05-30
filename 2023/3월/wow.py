# from time import time

# N, M, K = 1000, 1000, 10
# a = time()
# visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)] # visited[1000][1000][11]
# # print(asizeof.asizeof(visited)) # 153025040 (≈ 153.0MB)
# b = time()
# print(b-a)
# c = time()
# visited = [[[0] * (M) for _ in range(N)] for _ in range(K+1)] # visited[11][1000][1000]
# # print(asizeof.asizeof(visited)) # 88715384 (≈ 88.7MB)
# d = time()
# print(d-c)


# https://www.acmicpc.net/problem/13164
# https://www.acmicpc.net/problem/2212
#https://www.acmicpc.net/problem/1461