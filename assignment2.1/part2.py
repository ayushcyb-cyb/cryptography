import random 

random.seed(12345) 
print("First run:") 

for i in range(10): 
    print(random.randint(0, 255), end=" ") 
print("\n") 

random.seed(54321) 
print("Second run:") 

for i in range(10): 
    print(random.randint(0, 255), end=" ")
