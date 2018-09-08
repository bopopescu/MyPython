#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'HelloWorld'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('HL1')
    elif len(args) == 2:
        print("HL2 %s" % args[1])
    else:
        print("Too many")

if __name__=='__main__':
    test()



# 作用域
# 我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用
# 在Python中，是通过_前缀来实现的
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
