lst=[]
n=int(input("enter the number of elements:\n "))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
    
print(lst)
sum=[]
sum.append(lst[0])
for i in range(1,n):
    s=lst[i-1]+lst[i]
    sum.append(s)
print(sum)
