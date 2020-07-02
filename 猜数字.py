import random# 载入import 模组random
# drandom相当一个箱子 randint就是randowm里面的一个箱子里面的工具
# randint就是产生随机数的代码是random模组其中一个套件
start = input('请决定随机数字范围的开始值')
end = input('请决定随机数字范围结束值得')

start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
    count += 1 # count = count + 1
    num=input('请猜数字： ')
    num = int(num)
    if num == r:
        print('你猜中了')
        break
    elif num > r:
        print('比答案大')
    elif num > r:
        print('你答案小')
    print('这是你猜的第', count, '次')


