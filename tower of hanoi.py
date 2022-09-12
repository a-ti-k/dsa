def hanoi(disk,tower1,tower2,tower3):
    if disk==1:
        print("move disk 1 from",tower1,"to",tower2)
        return
    hanoi(disk-1,tower1,tower3,tower2)
    print("move disk",n,"from",tower1,"to",tower2)
    hanoi(disk-1,tower3,tower2,tower1)
n=3
hanoi(n,'a','b','c')
