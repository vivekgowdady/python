lst=[]
n=int(input("enter the number of elements:\n "))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
    
print(lst)

def remove(lst):
    lst.pop(0)
    lst.pop(n-2)
    print(lst)
remove(lst)
