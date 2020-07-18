import numpy as np

n_max=2000000
p_loc = [1,0,0,1,0]
pow_2=1
expo_prev=0
for i in np.arange(0,n_max):	
	p_loc.append(p_loc[-2]+p_loc[-3])
	p_loc.pop(0)
	expo = int(np.floor(i/2))
	pow_2 = pow_2*pow(2, int(expo - expo_prev))
	expo_prev=expo
	q_tmp = pow_2 - p_loc[-1]
	if i>=42:
		if q_tmp % 1000000==0:
			print(i, q_tmp)			
			break

