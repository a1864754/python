"""
已知列表['0','1','2','','a',['1','2','3']]，采用异常处理结构编写程序，
将每个列表元素转换为整型，类型转换过程中若未发生异常，打印“第i个位置元素是数值型”；
若发生ValueError和TypeError异常，打印“第i个位置元素转换为整型时发生异常”，
并打印异常信息；无论是否存在异常，均打印“第i个位置元素为X”，其中X为该元素的值。
"""
a = ['0', '1', '2', '', 'a', ['1', '2', '3']]
for index, i in enumerate(a):
    try:
        i = int(i)
        print("第%d个位置元素是数值型" % index)
    except (ValueError, TypeError):
        print("第%d个位置元素转换为整型时发生异常" % index)
    finally:
        print("第%d个位置元素为%s" % (index, i))
