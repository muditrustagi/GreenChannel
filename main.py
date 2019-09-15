cn=int(input("Enter number of lanes:"))
avg=float(input("Enter average speed of the road in metre per sec:"))
t=[]
t=[0 for i in range(cn)]
for j in range(cn):
      print("For lane number",j+1)
      n=int(input("Number of cars in the lane:"))
      print("Enter acceleration of the cars in metre per sec square:")
      a=[]
      l=[]
      a=[0 for i in range(n)]
      l=[0 for i in range(n)]
      for i in range(n):
            a[i]=float(input())
      print("Enter length of each car in metres:")
      for i in range (n):
            l[i]=float(input())
      k=1
      def ttotal(acc,ln):
           import math
           ts=avg/acc
           sa=0.5*acc*ts*ts
           if(sa>ln):
                tt=math.sqrt(2*ln/acc)
           elif(sa<ln):
                stc=ln-sa
                tt=ts+stc/avg
           else:
                tt=ts
           return (tt)
      lcurrent=0     
      for i in range(n):
               t1=ttotal(a[i],lcurrent)
               if(k==1):
                    t[j]=t1
                    k+=1
               elif(t1>t[j]):
                    t[j]=t1
               lcurrent=lcurrent+l[i]
      print(t[j])
p=1
for j in range(cn):
      if (p==1):
            tlowest=t[j]
            p+=1
            lanenumber=j+1
      elif(tlowest>t[j]):
            tlowest=t[j]
            lanenumber=j+1
print("Free lane number:",lanenumber)
