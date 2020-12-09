import time,random
def shellSort(a,n):
    h=1
    while h<n:
        h=3*h+1
    while h>0:
        for i in range(h+1,n+1):
            v,j=a[i],i
            while j>h and a[j-h]>v:
                a[j]=a[j-h]
                j-=h
            a[j]=v
        h=int(h/3)

def checkSort(list,n):
    isSorted=True
    for i in range(1,n-1):
        if(list[i]>list[i+1]):
           isSorted=False
        if(not isSorted):
           break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")

N=5000
a=[]
a.append(-1)
for i in range(N):
    a.append(random.randint(1,N))
start_time=time.time()
shellSort(a,N)
end_time=time.time()-start_time
print('쉘 정렬의 실행 시간 (N=%d) : %0.3f'%(N,end_time))
checkSort(a,N)