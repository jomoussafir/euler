mod = 1000000

# T represents [odd-length,even-length,all]
T = [2,2,4]
s = 1
inc = 4
while True:
    # Update odd-length twopals
    # Modular_pow calculates A^B mod C for large values
    T[0] = s + pow(2,inc-2,mod)
    T[0] = T[0] % mod
    
    # Update sum
    s += T[1]
    s = s % mod
    
    # Update even-length twopals
    T[1] = T[2]
    T[1] = T[1] % mod
    
    # Update overall twopals
    T[2] = T[0] + T[1]
    if T[2] % mod == 0:
        print("The solution is:",inc * 2)
        break
    else:
        inc += 1
        
