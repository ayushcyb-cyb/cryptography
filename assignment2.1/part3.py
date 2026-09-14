import secrets 
# print("Cryptographically secure random numbers:") 
# for i in range(10): 
#     print(secrets.randbelow(256), end=" ") 


key = secrets.token_hex(16) 
print("Random key:") 
print(key)