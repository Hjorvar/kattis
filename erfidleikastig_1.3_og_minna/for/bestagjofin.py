ammount = int(input())

bestGift = 0
bestGiver = ''

for i in range(ammount):
    name, gift = input().split()
    if int(gift) > int(bestGift):
        bestGiver = name
        bestGift = gift

print(bestGiver)