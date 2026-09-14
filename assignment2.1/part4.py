import random 
import secrets 

from collections import Counter 
N = 10000 

normal = [random.randint(0, 3) for _ in range(N)] 
crypto = [secrets.randbelow(4) for _ in range(N)] 

normal_count = Counter(normal) 
crypto_count = Counter(crypto) 
print("Regular PRNG:") 

for number in range(4): 
    print(number, normal_count[number]) 
print("\nCryptographic PRNG:") 
for number in range(4): 
    print(number, crypto_count[number])
