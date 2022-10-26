# import string
# str_str = [str(i) for i in range(10)]+list(string.ascii_uppercase)
# print(str_str.index("Z"),len(str_str))

index = 1
str_str = ""
for i in range(1,100):
    str_str+=str(i)
for i in str_str:
    print(index,i)
    index+=1



