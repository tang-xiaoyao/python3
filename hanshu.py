import math

#求和
def mysum(a, b):
    sum1=a+b
    print(a,'和',b,'的和为：',sum1)
   

#解一元二次方程
def jie(a, b, c):
    s = b**2 - 4*a*c
    if s<0:
        print('方程：%sx**2 + %sx + %s = 0 无实数根！' % (a,b,c) )
    else:
        x1 = (-b + math.sqrt(s))/(2*a)
        x2 = (-b - math.sqrt(s))/(2*a)
        print('方程：%sx**2 + %sx + %s = 0 的两个根为：' % (a,b,c) ,x1,',',x2)


 #阶乘
def jiecheng(n):
    if n == 1:
        return 1
    return  n * jiecheng(n - 1)  


 # 用函数打印：斐波拉契数列（1,1,2,3,5,8,13,21,34,...）,除第一个和第二个数外，任意一个数都可由前两个数相加得到。
 # 调用 fib（6），直接输出结果
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b    #赋值语句，与上面 "n,a,b = 0,0,1" 同，等号左右两边意为两个list/tuple
        n = n + 1
    return 'done'
    #上面例子改成 生成器（generator）,
        # 如下：返回generator对象.
def fibg(m):
    n,a,b = 0,0,1
    while n < m:
        yield b
        a,b = b,a+b
        n = n + 1
    return 'done'
        #命令行调用函数：
        #把函数体赋值并传给"f"：f = fib(10)
        #打印结果：print('fib(10):',f)
        #由于结果是一个generator对象，故用for打印结果：for x in f:
        #                                            print(x)
        #如要手动控制输入格式，则如下：
        # g = fib(10)
        # while 1:
        #     try:
        #         x = next(g)
        #         print('g:',x)
        #     except StopIteration as e:
        #         print('Generator return value:', e.value)
        #         break
    #用生成器（generator）,定义一个杨辉三角，如下：  ！！！！ 实验失败 ！！！！！
def tri():
    L = [1]
    while True:
        yield L
        L = L + [L[x-1]+L[x] for x in range(1,len(L) )] + L
        #命令行调用函数，输入结果。
    # n = 0
    # for t in tri():
    #     print(t)
    #     n = n + 1
    #     if n == 10:
    #         break


         
    
     

