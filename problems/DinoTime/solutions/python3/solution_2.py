from itertools import product
n,m=map(int, input().split(','))
g = [list(input()) for _ in range(n)]
def init():
    ri, rj = -1,-1
    for i in range(n):
        for j in range(m):
            if g[i][j]=='@':
                g[i][j]='.'
                ri,rj= i,j
            if 'A'<=g[i][j]<='Z':
                g[i][j]=ord(g[i][j])-ord('A')+1
    return ri, rj

type = {
    '#': float('inf'),
    '^': float('inf'),
    '&': float('inf'),
    '~': 2,
    '"': 2,
    '*': 3,
    '.': 1,
}
si,sj = init()

def f(l):
    sz=1
    en=1
    st=0
    ch=[]
    i,j=si,sj

    def die(ret):
        for i,j,v in reversed(ch):
            g[i][j]=v
        return ret

    for di, dj in l:
        if en <=0:
            return die(-1)
        i+=di
        j+=dj
        if not(0<=i<n and 0<=j<m):
            return die(-1)

        if isinstance(g[i][j], int):
            v = g[i][j]
            if v> sz:
                return die(-1)
            st+=v
            ch.append((i,j,v))
            g[i][j]='.'
            if st>=sz:
                st-=sz
                sz+=1
            en=sz
        else:
            en-=type[g[i][j]]
            if en <=0:
                return die(-1)


            

    return die(sz)





dirs = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0),
]

b = 1
for l in product(dirs, repeat=10):
    b = max(b, f(l))

print(b)
