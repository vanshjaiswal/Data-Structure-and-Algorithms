def armstrong(n):
    cube=n
    s=0
    while n>0:
        num=n%10
        s=s+(num**3)
        n=n//10

    if cube==s:
        return True
    else:
        return False

#Driver 
print(armstrong(154))


