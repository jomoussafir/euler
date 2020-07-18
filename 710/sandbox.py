import numpy as np
import itertools

def unique(a):
    indices = sorted(range(len(a)), key=a.__getitem__)
    indices = set(next(it) for k, it in 
                  itertools.groupby(indices, key=a.__getitem__))
    return [x for i, x in enumerate(a) if i in indices]

def partition(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]


def pal(p):
	p_rev = p.copy()
	p_rev.reverse()
	return(p == p_rev)

 

for n in np.arange(12,13):
	twopal_list=[]
	part_tmp = [p for p in partition(n) if (2 in p)]
	#part_tmp = [p for p in partition(n)]

	for p in part_tmp:
		p_perm = unique([list(t) for t in itertools.permutations(p)])
	
		twopal_list_tmp = [x for x in p_perm if pal(x)]
	
		if len(twopal_list_tmp)>0:
			twopal_list+=twopal_list_tmp
		
	for p in twopal_list:
		print(p)
	print(n,len(twopal_list))

