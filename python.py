# python3 基础操作练习

#切片&列表生成式   
#（1）输出：['hello','world','apple']
L1 = ['Hello','World',18,'Apple',None]
L2 = [s.lower() for s in L1[:] if isinstance(s,str) == true]
print(L2)
#（2）os.listdir可列出文件和目录
import os #导入os模块
[d for d in os.listdir('.')]  