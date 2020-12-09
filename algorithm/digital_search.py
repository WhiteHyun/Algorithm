import random,time

class bitskey:
    def __init__(self,x):
        self.x=x

    def get(self):
        return self.x
    
    def bits(self,k,j):
        return (self.x>>k)&~(~0<<j)

class node:
    def __init__(self,key):
        self.key=bitskey(key)
        self.left=None
        self.right=None

class Dict:
    itemMin=bitskey(0)
    z=node(itemMin)
    head=node(itemMin)
    head.left=z
    head.right=z

    def search(self,v):
        v=bitskey(v)
        x=self.head.left
        #k=x.key.get()
        b=maxb
        self.z.key=v
        while v.get()!=x.key.get():
            b=b-1
            if v.bits(b,1):
                #k=x.key.get()
                x=x.right
            else:
                #k=x.key.get()
                x=x.left
        if x==self.z:
            return -1
        else:
            #self.check(x.key.get(),k)
            return x.key.get()
    
    def insert(self,v):
        v=bitskey(v)
        b=maxb-1
        x=self.head.left
        p=self.head
        while x.key.get()!=self.z.key.get():
            p=x
            if v.bits(b,1):
                x=x.right
            else:
                x=x.left
            b-=1
        x=node(self.itemMin)
        x.key=v
        x.left=self.z
        x.right=self.z
        if v.bits(b+1,1):
            p.right=x
        else:
            p.left=x

    '''def check(self,v,p):
        print('key : %d, parents: %d' %(v,p))'''


for maxb in range(15,21):       #maxb는 키 안에 있는 것은 2^maxb만큼의 숫자까지만 커버 가능하다는 뜻
    N=10000
    key=list(range(1,N+1))
    s_key=list(range(1,N+1))
    random.shuffle(key)
    '''N=7
    maxb=5
    key=[1,19,5,18,3,26,9]
    s_key=[1,3,5,9,18,19,26]'''
    d=Dict()
    for i in range(N):
        d.insert(key[i])
    start_time=time.time()
    for i in range(N):
        result=d.search(s_key[i])
        if result==-1 or result!=s_key[i]:
            print('탐색 오류')
    end_time=time.time()-start_time
    print('디지털 탐색 트리 실행시간(N=%d, maxb=%d) : %0.3f'%(N,maxb,end_time))
    print('탐색 완료')