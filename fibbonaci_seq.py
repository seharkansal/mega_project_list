# 1 2 3 5 8 13
total=0
num1=0
num2=1
next_num=num2
while total<=10:
    num1, num2 = num2, next_num
    next_num = num1 + num2
    total+=1
    print(next_num,end=" ")
