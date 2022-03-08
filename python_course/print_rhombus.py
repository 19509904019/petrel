'''
Author: yujun
Date: 2022-03-07 22:24:16
LastEditors: yujun
LastEditTime: 2022-03-07 22:24:17
FilePath: \project\test01.py
Description: 

'''
# 打印图案正三角形

for i in range(1, 5):
    for j in range(1, 5 - i):
        print(" ", end="")

    for k in range(1, 2 * i):
        print("*", end="")

    print()

print("------------------------")

# 打印菱形
for i in range(1, 5):
    for j in range(1, 5 - i):
        print(" ", end="")

    for k in range(1, 2 * i):
        print("*", end="")

    print()  # 上半部分

for i in range(1, 4):

    for j in range(1, i + 1):
        print(" ", end="")

    for k in range(1, 8 - 2 * i):
        print("*", end="")

    print()  # 下半部分

print("------------------------")

# 打印菱形更简洁的方法


for i in range(1, 8, 2):
    print(("*" * i).center(7))  # 上半部分

for j in reversed(range(1, 6, 2)):
    print(("*" * j).center(7))  # 下半部分
