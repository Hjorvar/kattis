n = int(input())
numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)

for num in reversed(numbers):
    print(num)
