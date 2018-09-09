from functools import reduce

def str2num(s):
    try:
        return int(s)
    except:
        return float(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()



# 断言
# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10/n


# foo('0')




import logging
logging.basicConfig(level=logging.INFO)

import pdb

s = '0'
n = int(s)
# 运行到这里会自动暂停
# pdb.set_trace()

logging.info('n = %d' % n)
print(10 / n)

