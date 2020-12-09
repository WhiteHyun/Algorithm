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
        if key.get()==0:
            self.key=bitskey(0)
            self.external=False
        else:
            self.key=key
            self.external=True
        self.left=0
        self.right=0

class Dict:
    itemMin=bitskey(0)
    head=0
    head_check=False

    def search(self,v):
        v=bitskey(v)
        return self.searchR(self.head,v,maxb-1)
    def insert(self,v):
        v=bitskey(v)
        self.insertR(self.head,v,maxb-1)
    def insertR(self,h,v,d):
        if h==0:
            h=node(v)
            if self.head_check==False:
                self.head=h
            return h
        if h.external:
            leaf=node(v)
            h=self.split(leaf,h,d)
            if self.head_check==False:
                self.head=h
                self.head_check=True
            return h
        if v.bits(d,1)==0:
            h.left=self.insertR(h.left,v,d-1)
        else:
            h.right=self.insertR(h.right,v,d-1)
        return h
    def split(self,p,q,d):
        t=node(self.itemMin)
        if ((p.key.bits(d,1))*2+(q.key.bits(d,1)))==0:
            t.left=self.split(p,q,d-1)
        elif ((p.key.bits(d,1))*2+(q.key.bits(d,1)))==1:
            t.left=p
            t.right=q
        elif ((p.key.bits(d,1))*2+(q.key.bits(d,1)))==2:
            t.right=p
            t.left=q
        elif ((p.key.bits(d,1))*2+(q.key.bits(d,1)))==3:
            t.right=self.split(p,q,d-1)
        return t
    def searchR(self,h,v,d):
        if h==0:
            return self.itemMin
        if v.get()==h.key.get():
            #self.check(h.key.get())
            return v
        if v.bits(d,1)==0:
            #print('left',end=' ')
            return self.searchR(h.left,v,d-1)
        else:
            #print('right',end=' ')
            return self.searchR(h.right,v,d-1)
    '''def check(self,v):
        print(v)'''
for N in range(10000,40000,10000):
    for maxb in range(15,21):
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
        d.head.external=True
        start_time=time.time()
        for i in range(N):
            result=d.search(s_key[i])
            if result.get()==-1 or result.get()!=s_key[i]:
                print('탐색 오류')
        end_time=time.time()-start_time
        print('기수 탐색 트라이 실행 시간(N=%d,maxb=%d) : %0.3f'%(N,maxb,end_time))
        print('탐색 완료')