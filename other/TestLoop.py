n = 100

sum = 0
counter = 1
while counter <= n:
    print("add number: %d" % counter)
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))



#-----------for loop example next----------
# !/usr/bin/python3

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")