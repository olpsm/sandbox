#!/usr/bin/python3.2

Unsort=['CD','DE','AB','BC']
all_a=[]
all_z=[]
a=[]
z=[]
sort=[]
for e in Unsort:
  all_a.append(e[0])
  all_z.append(e[1])
for e in all_a:
  if all_a.count(e)==1 and (e not in all_z): a.append(e)
for e in all_z:
  if all_z.count(e)==1 and (e not in all_a): z.append(e)
  #print('e[0]-', e[0], 'e[1]-', e[1])
  #if Unsort.count(e[1])==1: a.append(e[0])
  #if Unsort.count(e[1])==1: z.append(e[1])

print ('all_a=',all_a)
print ('all_z=',all_z) 
print ('a=',a)
print ('z=',z)

if len(a)==1 then:
  while len(sort)!=len(Unsort):
    for e in unsort:
    
  #for e in unsort:
    
if len(z)==1 then:
  
