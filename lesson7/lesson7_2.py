import argparse
import random

parser = argparse.ArgumentParser(description="猜數字遊戲")
parser.add_argument("-n", "--name", type=str, help="姓名")
parser.add_argument("-f", "--frequency", type=int, help="預設玩的次數", default=1)
args = parser.parse_args()

# 取得姓名
if not args.name:
    name = input("請輸入您的姓名: ")
else:
    name = args.name

# 初始設定
frequency = args.frequency
round_number = 0

while round_number < frequency:
    round_number += 1
    print(f"\n======== 猜數字遊戲第 {round_number} 輪 ========\n")
    
    min_num = 1
    max_num = 100
    count = 0
    target = random.randint(min_num, max_num)
    # print(target)  # 除錯用

    while True:
        try:
            keyin = int(input(f"猜數字範圍 {min_num}~{max_num}: "))
        except ValueError:
            print("請輸入有效的整數！\n")
            continue

        if min_num <= keyin <= max_num:
            count += 1
            if keyin == target:
                print(f"賓果！猜對了，答案是：{target}")
                print(f"{name} 共猜了 {count} 次\n")
                break
            elif keyin > target:
                print("猜錯了！再小一點")
                max_num = keyin - 1
            else:
                print("猜錯了！再大一點")
                min_num = keyin + 1
            print(f"{name} 已經猜了 {count} 次\n")
        else:
            print("請輸入提示範圍內的數字！\n")

    # 預設次數到了就問是否繼續
    if round_number >= frequency:
        again = input("是否再玩一輪？(y/n): ").strip().lower()
        if again == 'y':
            frequency += 1  # 多加一輪
        else:
            break

print(f"\n遊戲結束，{name} 共玩了 {round_number} 次")
