arr = []
n = int(input("enter the number of elements:"))
for i in range(0,n):
    ele = int(input())
    arr.append(ele)

def linearSearch(arr,find):
    for i in range (len(arr)):
        if find == arr[i]:
            return i+1

find =int(input("need to find:"))

print("found in the index:",linearSearch(arr,find))
