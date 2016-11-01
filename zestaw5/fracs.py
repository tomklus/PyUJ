import fractions
import sys

def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

def simplify(frac): 
	while fractions.gcd(frac[0],frac[1]) > 1:
		Gcd = fractions.gcd(frac[0],frac[1])
		frac[0] = int(float(frac[0]) / Gcd)
		frac[1] = int(float(frac[1]) / Gcd)
	return frac



def add_frac(frac1, frac2):         # frac1 + frac2
	
	res = [0,lcm(frac1[1],frac2[1])]

	if frac1[1] != res[1]:
		res[0] += res[1]/frac1[1]*frac1[0]
	else:
		res[0] += frac1[0]
		
	if frac2[1] != res[1]:
		res[0] += res[1]/frac2[1]*frac2[0]
	else:
		res[0] += frac2[0]
		
	return res


def sub_frac(frac1, frac2): 	        # frac1 - frac2
	res = [0,lcm(frac1[1],frac2[1])]

	if frac1[1] != res[1]:
		res[0] += res[1]/frac1[1]*frac1[0]
	else:
		res[0] += frac1[0]
		
	if frac2[1] != res[1]:
		res[0] -= res[1]/frac2[1]*frac2[0]
	else:
		res[0] -= frac2[0]
		
	return res


def mul_frac(frac1, frac2): 	        # frac1 * frac2
	return [frac1[0]*frac2[0],frac1[1]*frac2[1]]
	
	
def div_frac(frac1, frac2): 	        # frac1 / frac2
	if frac1[1] != 0:
		if frac2[1] != 0:
			return mul_frac(frac1,[frac2[1],frac2[0]])

	
def is_positive(frac): 		             # bool, czy dodatni
	if frac[0] >= 0:
		if frac[1] >= 0:
			return True
	return False
	
	 
def is_zero(frac): 		                 # bool, typu [0, x]
	return frac[0] == 0
	
	
def cmp_frac(frac1, frac2): 	        # -1 | 0 | +1
	if simplify(frac1) == simplify(frac2):
		return 0
	
	elif frac2float(frac1) > frac2float(frac2):
		return 1 
	else:
		return -1
		

def frac2float(frac): 	              # konwersja do float
	return (float(frac[0])/float(frac[1]))
	
f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznacznosc)
f5 = [0, 2]                   # zero (niejednoznacznosc)


