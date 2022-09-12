def match(t,p):
    for i in range (len(t)-len(p)+1):
        k=0
        while k<len(p) and t[i+k]==p[k]:
            k+=1
        if k==len(p):
            return i
    return -1

text = input("enter text:")
pattern = input("enter pattern:")
print("found at index:",match(text,pattern))
