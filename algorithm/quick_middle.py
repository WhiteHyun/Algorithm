import time,random,sys
sys.setrecursionlimit(3001)

def quickSort(a,l,r):
    if r>l:
        v,i,j=a[r],l-1,r
        while True:
            i+=1
            while a[i]<v:
                i+=1
            j-=1
            while a[j]>v:
                j-=1
            if i>=j:
                break
            a[i],a[j]=a[j],a[i]
        a[i],a[r]=a[r],a[i]
        quickSort(a,l,i-1)
        quickSort(a,i+1,r)

def quickSort_motp(a,l,r):          #중간 값 분할을 이용한 퀵 정렬
    if r-l>1:
        mid=int((l+r)/2)
        if a[l]>a[mid]:
            a[l],a[mid]=a[mid],a[l]
        if a[mid]>a[r]:
            a[mid],a[r]=a[r],a[mid]
        if a[l]>a[mid]:
            a[l],a[mid]=a[mid],a[l]
        a[mid],a[r-1]=a[r-1],a[mid]
        v,i,j=a[r-1],l,r-1
        while True:
            i+=1
            while a[i]<v:
                i+=1
            j-=1
            while a[j]>v:
                j-=1
            if i>=j:
                break
            a[i],a[j]=a[j],a[i]
        a[i],a[r-1]=a[r-1],a[i]
        quickSort_motp(a,l,i-1)
        quickSort_motp(a,i+1,r)
    elif a[l]>a[r]:
        a[l],a[r]=a[r],a[l]

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

N=300000
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1, N))
b=a.copy()
start_time=time.time()
quickSort(a,1,N-1)
end_time=time.time()-start_time
checkSort(a,N)
print('퀵 정렬 실행 시간 (N=%d): %0.3f'%(N,end_time))
start_time=time.time()
quickSort_motp(b,1,N)
end_time=time.time()-start_time
print('중간 값 분할을 쓴 퀵 정렬 실행 시간 (N=%d): %0.3f'%(N,end_time))
checkSort(b,N)