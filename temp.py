# class Person:
#     def __init__(self,name,id):
#         self.name = name
#         self.idnumber=id
    
#     def display(self):
#         print(self.name)
#         print(self.idnumber)

# class Employee(Person):
#     def __init__(self,name,idnumber,salary,post):
#         self.salary=salary
#         self.post = post
#         Person.__init__(self,name,idnumber)

# a = Employee('Rahul',1,20000,'Intern')
# a.display()

import random
queries=[]
nums = []
a = int(input('Enter number of insert queries:'))
b = int(input('Enter number of other queries:'))
c = int(input('Enter range insert queries:'))
for i in range(a):
    x = random.randrange(1,c,1)
    nums.append(x)
    my_query = 'INSERT '+ str(x)+'\n'
    queries.append(my_query)
for i in range(b):
    query=random.choice(['RANGE','FIND','COUNT'])
    x=random.choice(nums)
    if query=='RANGE':
        y = random.randrange(x,c,1)
        my_query = query+' '+str(x)+' '+str(y)+'\n'
    else:
        my_query = query+' '+str(x)+'\n'
    queries.append(my_query)

print(queries)
f1 = open('input.txt','w')
f1.writelines(queries)
f1.close()