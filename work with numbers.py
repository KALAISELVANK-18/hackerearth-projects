from math import ceil

mod = 1000000007
n = int(input())
a = [1]+list(map(int,input().split()))
b = a.copy()
#work with numbers
for i in range(1, n+1):
    a[i] *= a[i-1]
    a[i] %= mod

inv = [1] * (n+1)

inv[n] = pow(a[n], mod-2, mod)

for i in range(n-1, -1, -1):
    inv[i] = inv[i + 1] * b[i + 1] % mod


ans = 0
for i in range(1, ceil(n/2)+2):
    ans += (a[i+n//2-1] * inv[i-1]) % mod

ans %= mod
print(ans)
