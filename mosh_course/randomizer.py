import random
num = random.random()
print(num)

for i in range(3):
    print(random.random())


for i in range(5):
    print(random.randint(100, 200))
    

members = ["Justin","Michael","Alex","Trace","Jackson"]
leader = random.choice(members)
print(leader)