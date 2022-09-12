arr = []
n = int(input("enter the number of elements:"))
for i in range(0,n):
    ele = int(input())
    arr.append(ele)

def binarySearch(arr,find,low,high):
    if low > high:
        return False
    else:
        mid = (low+high)//2
        if find == arr[mid]:
            return mid+1
        elif find < arr[mid]:
            return binarySearch(arr,find,low,mid-1)
        else:
            return binarySearch(arr,find,mid+1,high)

low=0
high=n-1

find =int(input("need to find:"))

print("array after sorting:",binarySearch(arr,find,low,high))
