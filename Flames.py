a = input("Enter the First Name:\t")
b = input("Enter the Second Name:\t")
a1 = list(a.strip().replace(" ", ""))
a2 = list(b.strip().replace(" ", ""))
common = []

for i in a1[:]: # create a copy of a1
    for j in a2[:]: # create a copy of a2
        if i == j:
            common.append(i)
            a1.remove(i) # remove from the copy of a1
            a2.remove(j) # remove from the copy of a2
            break
#print(a1)
#print(a2)
for i in a2:
    a1.append(i)

#print(a1)
n=len(a1)
res=['f','l','a','m','e','s']
n1=len(res)

if(n>n1):
    i=n-n1
else:
    i=n

while(n1>2):
    while(i>n1):
        i=i-n1    
    a=len(res[i:])
    r=res.pop(i-1)
    #print(r)
    n1=len(res)
    #print(a)
    i=n-n1-a
    #print(i)
    
if(n1==2):
    if(n%2==0):
        res.pop(1)
    else:
        res.pop(0)
#print(res)
# print the result
if(res==['f']):
    print("\nFriends")
if(res==['l']):
    print('\nLovers')
if(res==['a']):
    print('\nAffection')
if(res==['m']):
    print('\nMarriage')
if(res==['e']):
    print('\nEnemy')
if(res==['s']):
    print('\nSister')

print('\n')