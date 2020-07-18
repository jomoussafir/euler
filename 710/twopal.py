import numpy as np

p = [1,2,1]


def pad(p):
	p_tmp = p.copy()
	p_tmp.append(0)
	return([0]+p_tmp)
	

def add_one(p):
	k=len(p)
	res=[]	
	for i in np.arange(k):
		p_tmp=p.copy()
		p_tmp[i]+=1
		p_tmp[k-1-i]+=1
		if not p_tmp in res:
			res.append(p_tmp)
	return(res)
	

def crop(p):
	p_tmp = p.copy()
	if p[0]==0:
		res=p_tmp[1:-1]
	else:
		res=p_tmp
	return(res)

def padovan(n):
	if n>=3:
		res = padovan(n-2) + padovan(n-3)
	elif (n==1 or n==2):
		res = 0
	else:
		res=1
	return(res)
	
def padovan2(n):
	if n==0:
		return 1
	elif (n==1 or n==2):
		return 0
	else:
		res=[1,0,0]
		for i in np.arange(3,n+1):
			res.append(res[i-2]+res[i-3])
	return res[-1]

def P(n):
	if n>=3:
		res=[]
		for p in P(n-2):
			#print("[",n,"]", end ="")
			res_tmp = [crop(x) for x in add_one(pad(p))]
			for q in res_tmp:
				if not q in res:			
					res.append(q)
	elif n==2:
		res = [[2],[1,1]]
	else:
		res = [[1]]
	
	return(res)


def TP(n):
	res = [x for x in P(n) if (2 in x)]
	return(res)


n_max=10000000
p_loc = [1,0,0]
for i in np.arange(3,n_max):
	if i%10000==0:
		print("["+str(i)+"]", end="", flush=True)
	#p.append(p[i-2]+p[i-3])
	p_loc.append(p_loc[1]+p_loc[0])
	p_loc.pop(0)
	q_tmp = 2**(int(np.floor((i-5)/2))) - p_loc[-1]
	if i>=5:
		if q_tmp % 1000000 ==0:
			print([i-5, 2**(int(np.floor((i-5)/2))) - p_loc[-1]])






# q = [None]*n_max
# for i in np.arange(6,n_max):
# 	q[i-5] = 2**(int(np.floor((i-5)/2))) - p[i]
# 	if q[i]%1000000==0:
# 		print([i, q[i], 2**(int(np.floor(i/2))) - padovan2(i+5)])

#print([i, q[i], 2**(int(np.floor(i/2))) - padovan2(i+5)])

## The 	sequence we are looking for is defined as
# for i in np.arange(1,1000):
# 	#print([i, len(TP(i)), 2**(int(np.floor(i/2))) -  padovan(i+5)])
# 	z = 2**(int(np.floor(i/2))) -  padovan(i+5)
# 	if z%100==0:
# 		print([i,  2**(int(np.floor(i/2))) -  padovan2(i+5)])







