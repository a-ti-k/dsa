def knapSack(c,wt,p,n):
    if n==0 or c==0:
        return 0
    if (wt[n-1]>c):
        return knapSack(c,wt,p,n-1)
    else:
        return max(
            p[n-1],knapSack(c-wt[n-1],wt,p,n-1),
            knapSack(c,wt,p,n-1)
        )

profit = [15,25,13,23]
weight = [2,6,12,9]
capacity = 20
n = 4
print (knapSack(capacity,weight,profit,n))
