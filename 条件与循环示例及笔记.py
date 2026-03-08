#循环结构#
#while循环#
love='yes'
while love=='yes'
    love=input('今天你还爱我吗？')




i=1
sum=0
while sum<=100000
    sum=sum+1
    i=i+1

print(sum)

#中间部分还有另外一种写法#
i=1
sum=0
while sum<=100000:
    sum+=i
    i+=1

print(sum)

#死循环示例#
while True:
    print('人是一切社会关系的总和')

#跳出死循环之break语句#
while True:
    answer=input('宝宝，我可以退出循环了吗')
    if answer="可以":
        break
    print("呜呜呜，人家累啦")

#coninue语句 只是跳出本轮循环，若条件成立还会进入下一个循环#
i=0
while i<10:
    i+=1
    if i%2==0:
        continue
    print(i)

    #将打印出13579 因为在2468十的时候会继续while循环（条件为真就跳入下一个循环）#


#else语句在循环里 contrast to continue 当else里语句不为真的时候就会执行else语句里面的内容#
while i<6666666666:
    i+=1
    print('循环内，i的值是',i)
else:
    print('循环外，i的值是',i)



#若没有else还是会得到一样的结果#
#else是在条件不真之后才执行“寿终正寝”#
#而break是可以让循环中途跳出“死于非命”#
i=1
while i<66666666:
    print('循环内，i的值为',i)
    if i==1000
        break
    i += 1
else:
    print('循环外，i的值为',i)
#到1000就结束了，不会执行之后的代码#


#每周打卡小程序#
day=1
while day<=7:
    answer=input('今天你有爱我吗：')
    if !='有'
        break
    day += 1
    
else:
    print('好耶——你已经连续7天爱我啦')

#循环结构的嵌套#
    #打印九九乘法表#
i=1
while i<=9:
    j = 1
    while j<=9:
        print(j,"*",i,"=",j * i,end="")#end防止自动换行 否则打出来的可能是一列#
        j += 1
    print()
    i+=1

#注意！无论是break语句还是continue语句都只能作用于一层循环体#

day=1
hour=1
while day<=7:
    while hour<=8:
        print('今天我一定要学满8个小时')
        hour+=1
        if hour>1:
            break
    day+=1#这里因为时间大于1跳出了hour<=8的循环体 因为它是在这个代码块里 它影响不到day+=1 (停止的是hour+=1)#




#for循环#
#语法结构：for 变量 in 可迭代对象：statement(s)#

for each in "Khalil":
    print(each)

#结果为K h a l i l(竖着写的)#

#现在我用下标索引和while循环做一遍#
i=0
while i<len("Khalil"):
    print("Khalil"[i])
    i+=1
#结果同上#

#for的孪生兄弟#
for i range(10):
    print(i)

for i in range(5,10):
    print(i)

for i in range(5,10,2):
    print(i)

#显示10 8 6#

sum=0
for i in range(1000001)
    sum+=1
print(sum)

#找到1到10内所有素数#
for n in range(2,10)：
    for x in range(2,n)：
        if n%x==0：
            print(n,"=",x,"*",n//x)
            break
    else:
            print(n,"是一个素数")
        
