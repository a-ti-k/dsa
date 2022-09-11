arr = []
n = int(input("enter the elements:"))
for i in range (0,n) :
	ele = int (input())
	arr.append(ele)
print(arr)

def insert():
	print("for inserting:")
	index = int(input("index:"))
	element = int(input("element:"))
	arr.insert(index,element)
	print("array after inserting:",arr)

def delete():
	print("for deleting:")
	index= int(input("index:"))
	arr.remove(arr[index])
	print("array after deleting:",arr)


insert()
delete()
