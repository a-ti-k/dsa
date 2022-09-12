arr = []
n = int(input("enter the number of elements:"))
for i in range(0,n):
    ele = int(input())
    arr.append(ele)

def select(arr,start):
    minIndex = start
    for j in range (start+1,len(arr)):
        if arr[minIndex]>arr[j]:
            minIndex = j

        return minIndex

def selectionSort(arr):
    for i in range (len(arr)-1):
        minIndex = select(arr,i)
        arr[i],arr[minIndex]=arr[minIndex],arr[i]


print("array before sorting:",arr)
selectionSort(arr)
print("array after sorting:",arr)
