print("hello python")
import random
print("========猜數字遊戲=========\n")
min=1
max=100
count=0
ans=random.randint(min,max)
#print(ans)
while(True):
  keyin = int(input(f"猜數字範圍{min}~{max}:"))
  count+=1
  if(keyin>=min and keyin<=max):
    if ans==keyin:
      print(f"猜對了, 答案是:{ans}")
      print(f"你共猜了{count}次\n")
      break

    elif(keyin>ans):
      print("猜錯了!再小一點")
      max=keyin-1

    else:
      print("猜錯了!再大一點")
      min=keyin+1
    print(f"你已經猜了{count}次\n")
  else:
    print("請輸入提示範圍內的數字")

print("遊戲結束")