# -*- coding: utf-8 -*-
print 'Hello, world'
print '你好'

# 多行字符串
print '''静夜思

床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。
'''

# 测试 range() 函数
i = 0
while i < 5:
    print i
    i += 2
    print i
    print '一轮结束'

print '---------------------'

for i in range(5):
    print i
    i += 2  # 不会影响下次循环时 i 的值，i 会在 for 指定的范围(range(5))重新赋值
    print i
    print '一轮结束'

# 测试 if...elif...else
age = 8
# age = 20
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'

# 以上代码若不改变代码写法，就应该修改各条件的顺序，使得范围小条件判断的在前面

# 计算100以内的奇数之和
sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum += x
print sum

sum=0
x=0
while x<100:
    x += 1
    if not x % 2:
        continue
    sum += x
print sum

# 对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。
count = 0
for x in [ 1,2,3,4,5,6,7,8 ]:
    for y in range(x + 1, 10):
        count += 1
        print x * 10 + y
print '一共 :', count, '个'

# 针对下面的set，给定一个list，对list中的每一个元素，如果在set中，就将其删除，如果不在set中，就添加进去。
# s = set(['Adam', 'Paul'])
# L = ['Adam', 'Lisa', 'Bart', 'Paul']

s = set(['Adam', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for x in L:
    if x in s:
        s.remove(x)
    else:
        s.add(x)
print s

s = set(['Adam', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
t = set(L)
for a in s:
    t.remove(a)
print t

# 定义函数
