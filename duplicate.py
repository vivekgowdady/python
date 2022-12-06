lst=[]
n=int(input("enter the number of elements:\n "))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
    
print(lst)
def has_duplicate(lst):
    for i in range(0,n-1):
        s=lst.count(lst[i])
        if(s>1):
            print("true")
            break
has_duplicate(lst)
