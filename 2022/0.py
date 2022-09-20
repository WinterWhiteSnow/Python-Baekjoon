import sys
import os

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# 파일 생성
# for i in range(1,31):
#     wow = open(f"C:\\Users\\선옥\\Desktop\\코딩\\JS\\파이썬 백준\\2022\\11월\\{i}.py","a",encoding="utf8")
#     wow.write("import sys")
#     wow.write("\n")
#     wow.write("\ninputing = lambda : sys.stdin.readline().rstrip()")
#     wow.write("\nwow = lambda : map(int,inputing().split())")
#     wow.write("\none = lambda : int(inputing())")

#폴더 생성
for i in range(4,70):
   os.mkdir(f"C:/Users/선옥/Desktop/블리치 스캔본/{i}권")

    






