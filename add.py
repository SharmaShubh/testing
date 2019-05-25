def add(a,*b):
    c=a
    print(b)
    for i in b:
        c=c+i
    return c

result=add(4,5,6,7,8)
print(result)