# a=1
# b=2.5
# c='dgsa'
# d="let's go"
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(a,b,c,"dsds")

# a = input('请输入一个值：')
# print('a的值为:' ,a)
#
# # a,b = input('please input:').split(',')
# a=1
# b=2
# print('a和b的值为：' ,a,b)
# print('a的值为：{}，b的值为{}'.format(a,b))
# print('a的值为%03d,b的值为%.2f'%(a,b))
# print(f'a的值为：{a},b的值为：{b}')


# s = (1,2,3,4,5,6,7,8,9)
# print(s[3:8:2])
# print(s[-3])


# s=[1,2,7,4,8,6,9]
# s1=['c','d','k']
# s.extend(s1)
# print(s)

# s=[11,13,5,7,0,56,23,34,72]
# s1=[66,67,68]
# print(max(s))
# print(min(s))
# print(len(s))
# print(s.index(56))
# s.append(7)
# del s[4]
# s.reverse()
# s.extend(s1)
# print(s)
# s = {5,6,9,77}
# d = {'a':10,'b':5,'c':66}

# s.add(55)  第一题
# print(s)
# d['e']=88
# print(d)
# s.remove(6)  第二题
# s.discard(6)
# del d['a']    字典删除是一个元素
# print(d)
# b=list(d.values())  第三题
# b.extend(s)
# print(b)
# 集合是单个元素，字典的元素成对出现
# d.clear()
# print(d)

# s=[1,5,6,9]
# a = int(input("请输入数字："))
# if a in s:
#     print("haapy")
#     n=s.index(a)
#     s[n]+=1
#     print(s)
# else:
#     print("sad")
# print(s)

# a = int(input("请输入成绩："))
# if a<60:
#     print("D")
# elif a>=60 and a<80:
#     print("C")
# elif a>=80 and a < 90:
#     print("B")
# else:
#      print("A")

# n = 0
# sum=0
# while n<=100:
#     n += 1
#     sum=sum + n
# print(sum)

for i in [1,2,1,4]:
    print(i,'ok')