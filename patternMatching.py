def match(t,p):
    i=0
    while i<=(len(t)-len(p)):
        for j in range (len(p)):
            if t[i+j] is not p[j]:
                break
            if j==len(p)-1:
                return i
        i +=1
        

str =input("enter the string:")
str1 =input("need to find:")

print("found at position:",match(str,str1))

