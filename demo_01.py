#1.	给定一个非空正整数的列表，按照列表内数字重复出现次数，从高到低排序
list01 = [6,2,3,4,3,3,2,6]
c = dict()
for i in list01:
    c[i] = list01.count(i)  #c[key] = value 为字典添加元素，且key重复时不报错，只覆盖。
print(c)                    #将元素出现次数及元素本身存入字典
print(c.items())            #字典不可迭代，items() 是将key，value 组合放到一个元组，然后将所有元组组成列表
cc = sorted(c.items(), key=lambda x: x[1], reverse=True)    #参数一：放入需要迭代的对象，参数二：放入需要比较的参数位置、参数三：升降序，默认为False升序
print(cc)                   #对列表内元素（元组）第二个元素进行降序排序。
list02 = []
for j in cc:
    list02.append(j[0])     #将排序后的元组列表取出下标为0的元素
print(list02)

#2.	月份缩写：如果有 months = "Jan.Feb.Mar.Apr.May.Jun.Jul.Aug.Sep.Oct.Nov.Dec."，编写一个程序，用户输入一个月份的数字，输出月份的缩写。
# months = "Jan.Feb.Mar.Apr.May.Jun.Jul.Aug.Sep.Oct.Nov.Dec."
# x = tuple(months.split("."))
# ppp = [1,2,3,4,5,6,7,8,9,10,11,12]
# while True:
#     a = input("请输入月份：\n")
#     for i in ppp:
#         if a == str(i):
#             print(x[i-1])
#             break

# 3、定义列表：
L = [['Apple', 'Google', 'Microsoft'],['Java', 'Python', 'Ruby', 'PHP'],   ['Adam', 'Bart', 'Lisa']]
# 请分别取出['Apple', 'Google', 'Microsoft’]、’Ruby’,[‘Adam’,’Bart’]
print(L[0])
print(L[1][2])
print(L[2][0:2])
# a.计算列表长度并输出
print(len(L))
# b.列表中追加元素"seven"，并输出添加后的列表
L.append('seven')
print(L)
# c.请在列表的第1个位置插入元素 "Tony"，并输出添加后的列表
L.insert(0,"Tony")
print(L)
# d.请修改列表第2个位置的元素为 "Kelly"，并输出修改后的列表
L[1] = "Kelly"
print(L)
# 4.	写代码，有如下列表，按照要求实现每一个功能：
li = ['alex','eric','rain']
# a.计算列表长度并输出 
print(len(li))
# b.列表中追加元素"seven"，并输出添加后的列表
li.append("seven")
print(li)
# c.请在列表的第1个位置插入元素 "Tony"，并输出添加后的列表
li.insert(0,"Tony")
print(li)
# d.请修改列表第2个位置的元素为 "Kelly"，并输出修改后的列表
li[1] = "Kelly"
print(li)
# e.请删除列表中的元素"eric"，并输出修改后的列表
li.remove("eric")
print(li)
# f.请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
print(li.pop(1))
print(li)
# g.请删除列表中的第3个元素，并输出删除元素后的列表
li.pop(2)
print(li)
# h.请删除列表中的第2至4个元素，并输出删除元素后的列表
l2 = ['Tony', 'Kelly', 'eric', 'rain', 'seven']
del l2[1:4]
print(l2)
# i.请将列表所有的元素反转，并输出反转后的列表
x = sorted(l2,reverse=True)
print(x)
# j.请使用for、len、range 输出列表的索引
l3 = ['Tony', 'Kelly', 'eric', 'rain', 'seven']
for i in l3:
    print(l3.index(i))
# k.请使用enumrate输出列表元素和序号（序号从 100 开始）
for i in list(enumerate(l3,start=100)):
    print(i)                            #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# l.请使用for循环输出列表的所有元素
for i in l3:
    print(i)
#5、购物车功能要求：要求用户输入总资产，例如： 2000显示商品列表，让用户根据序号选择商品，加入购物车购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
goods=[{"name":"电脑","price":1999},
       {"name":"鼠标","price":10},
       {"name":"游艇","price":20},
       {"name":"美女","price":998}
]
all_price = []
all_name = []
while True:
    for i in range(0,len(goods)):
        print("序号{0}： 商品名称：{1}，价格为{2}".format(i+1,list(goods[i].items())[0][1],list(goods[i].items())[1][1]))   #输出商品列表
        all_price.append(list(goods[i].items())[1][1])      #商品价格列表
    money = int(input("请输入钱包余额："))
    while money >= sorted(all_price)[0]:                    #判断剩余金额
        shopping_id = int(input("请输入想购买的商品序号："))
        if shopping_id > len(goods):                        #判断序号
            print("输入有误！请重新输入序号")
            continue
        if money >= list(goods[shopping_id-1].items())[1][1]:       #购买模块，余额判断
            money = money - list(goods[shopping_id-1].items())[1][1]
            print("购买{0}成功！".format(list(goods[shopping_id-1].items())[0][1]))
            all_name.append(list(goods[shopping_id-1].items())[0][1])
        else:
            print("购买{0}失败！钱不够".format(list(goods[shopping_id-1].items())[0][1]))
        print("当前余额：{0}".format(money))
        print("已购买商品：{0}".format(all_name))          #购买清单
    else:
        print("余额不足以购买单价最低商品，结束购买！")        #结束购买



