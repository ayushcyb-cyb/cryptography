import random 
import secrets 

N = 10000 

regular_bits = [random.randint(0, 1) for _ in range(N)] 
crypto_bits = [secrets.randbelow(2) for _ in range(N)] 

print("Regular PRNG") 

print("0s:", regular_bits.count(0)) 
print("1s:", regular_bits.count(1)) 

print("\nCryptographic PRNG") 

print("0s:", crypto_bits.count(0)) 
print("1s:", crypto_bits.count(1)) 
