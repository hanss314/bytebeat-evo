from operations import sing_ops, doub_ops
from math import sin, log
import time

def parse_func(function):
    if type(function) is int:
        if function < 0:
            return 't'
        else:
            return str(function)
    else:
        if len(function) == 2:
            op = sing_ops[function[0]]
            value = parse_func(function[1])
            return '{}({})'.format(op,value)
        else:
            op = doub_ops[function[1]]
            left = parse_func(function[0])
            right = parse_func(function[2])
            if function[1] <= 6:
                return 'int({}){}int({})'.format(left,op,right)
            else:
                return '({}){}({})'.format(left,op,right)

if __name__ =='__main__':
    start = time.time()
    func = parse_func([[[-1,4,[4,7,[1,3,[7,2,[-1,4,19]]]]],0,-1],4,7])
    print(str(time.time()-start))
    parse_time = time.time()
    for t in range(800000):
        q = eval(func)
    print(str(time.time()-parse_time))
