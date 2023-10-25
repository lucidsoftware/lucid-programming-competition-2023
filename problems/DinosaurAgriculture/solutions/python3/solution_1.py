from functools import lru_cache

H, W, n = map(int, input().split())
def rhw():
    h, w = map(int, input().split())
    onerow = (1<<w)-1
    m = 0
    for i in range(h):
        m |= onerow << (i*W)
    return h, w, m, h*w

hws = [rhw() for _ in range(n)]

@lru_cache(maxsize=None)
def f(ni, map):
    if ni == n:
        return 0, 0
    h, w, m, a = hws[ni]
    best = f(ni+1, map)
    for i in range(0, H-h+1):
        for j in range(0, W-w+1):
            hm = m<<(i*W+j)
            if not (map&hm):
                hn, ha = f(ni+1, map|hm)
                best = max(best, (hn+1, ha+a))
    return best

k, a = f(0, 0)
print(k, H*W-a)
