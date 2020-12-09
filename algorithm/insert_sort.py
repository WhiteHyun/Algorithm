import random,time
def insertionSort(a,n):
    for i in range(2,n+1):
        v,j=a[i],i
        while a[j-1]>v:
            a[j]=a[j-1]
            j-=1
        a[j]=v

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
insertionSort(a,N)
end_time=time.time()-start_time
print('삽입 정렬의 실행 시간 (N=%d) : %0.3f'%(N,end_time))
checkSort(a,N)