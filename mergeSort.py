arr = []
n = int(input("enter the number of elements:"))
for i in range(0,n):
    ele = int(input())
    arr.append(ele)

def merge(s1,s2,s):
	i=j=0
	while i+j <len(s):
		if j==len(s2) or (i<len(s1) and s1[i]<s2[j]):
			s[i+j]=s1[i]
			i+=1
		else:
			s[i+j]=s2[j]
			j+=1

def mergeSort(s):
    n=len(s)
    if n<2:
        return
    
    mid = n//2
    s1 = s[0:mid]
    s2 = s[mid:n]
    mergeSort(s1)
    mergeSort(s2)
    merge(s1,s2,s)
    

print("array before sorting:",arr)
mergeSort(arr)
print("array after sorting:",arr)
