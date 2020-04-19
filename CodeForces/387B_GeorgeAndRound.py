# https://codeforces.com/problemset/problem/387/B

from collections import Counter

n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0
i = 0
j = 0

while i<n:
    while j<m and i<n:
        if A[i]<=B[j]:
            i += 1
            ans += 1
        j += 1
    i += 1
print(max(n-ans,0))