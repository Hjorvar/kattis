v, a, t = map(int, input().split())

vt = v * t
t2 = t ** 2
at = a * t2
ans = vt + 0.5 * at

print(ans)