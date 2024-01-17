#1
# rangeST = int(input("начало диапазона:"))
# rangeEND = int(input("конец диапазона:"))
# for i in range(rangeST, rangeEND + 1):
#     if i > 1:
#         for f in range(2, int(i**0.5) + 1):
#             if (i % f) == 0:
#                 break
#         else:
#             print("Простое число:",i)
#2
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i}*{j} = {i*j}\t", end='')
#     print()
#3
rangeST = int(input("начало диапазона:"))
rangeEND = int(input("конец диапазона:"))
for i in range(1, 11):
    for j in range(rangeST, rangeEND + 1):
        print(f"{j}*{i} = {j*i}\t", end='')
    print()