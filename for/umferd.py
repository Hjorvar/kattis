m = int(input())
n = int(input())
total = 0
dots = 0
for i in range(n):
    line = input()
    total += len(line)
    dots += line.count('.')
print(dots / total)
