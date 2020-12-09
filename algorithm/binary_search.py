import time,random

class node:
    def __init__(self,key=None):
        self.key=key
class Dict:
    def __init__(self):
        Dict.a=[]
    def search(self,search_key):
        k=0
        left=0
        right=len(Dict.a)-1
        while right>=left:
            mid=int((left+right)/2)
            k+=1
            if Dict.a[mid].key==search_key:
                return mid,k
            if Dict.a[mid].key>search_key:
                right=mid-1
            else:
                left=mid+1
        return -1,k
    def insert(self,v):
        Dict.a.append(node(v))

N=10000
key=list(range(1,N+1))
s_key=list(range(1,N+1))
random.shuffle(s_key)
d=Dict()
for i in range(N):
    d.insert(key[i])
start_time=time.time()
for i in range(N):
    result,k=d.search(s_key[i])
    if result==-1 or key[result]!=s_key[i]:
        print('탐색 오류')
end_time=time.time()-start_time
print('이진 탐색 실행 시간(N=%d) : %0.3f' %(N,end_time))
print('탐색 횟수 : %d'%k)
print('탐색 완료')