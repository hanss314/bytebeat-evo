import time, random
from math import sin, log
from operations import sing_ops, doub_ops

sing_range = list(range(len(sing_ops)))
doub_range = list(range(len(doub_ops)))

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
				
def create_random_alg(its=0):
	choice = random.choice(range(int(its)+2))
	alg = []
	if choice == 0:
		alg.append(random.choice(sing_range))
		alg.append(create_random_alg(its+0.5))
	elif choice == 1:
		alg.append(create_random_alg(its+0.5))
		alg.append(random.choice(doub_range))
		alg.append(create_random_alg(its+0.5))
	else:
		return random.choice(range(-10,42))
		
	return alg

if __name__ =='__main__':
	alg = create_random_alg()
	print(alg)
	print(parse_func(alg))
