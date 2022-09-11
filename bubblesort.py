arr = []
n = int(input("enter the number of elements:"))
for i in range(0,n):
    ele = int(input())
    arr.append(ele)

def bubbleSort(arr):
    for i in range (len(arr)):
        for j in range (0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print(arr)

bubbleSort(arr)
