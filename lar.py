n,m,p=[int(c) for c in input().split()]
if n>m and n>p:
    print(n)
elif m>p and m>n:
    print(m)
else:
    print(p)
