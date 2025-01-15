import random

arr = {"User ID":[], "Game ID":[], "Review Score": []}

num_users = 523
num_games = 342

for i in range(1, 524):
    arr.get("User ID").append(i)

for i in range(1, 524):
    arr.get("Game ID").append(random.randint(1, num_games))

for i in range(1, 524):
    arr.get("Review Score").append(random.randint(0, 10))

#look for a way to increase the percentage of 0's as most users do not rate games

for i in range(1, 523):
    if arr.get("Review Score")[i] == 0:
        arr.get("Review Score")[i] = float("NaN")

print(arr.get("User ID"))
print(arr.get("Game ID"))
print(arr.get("Review Score"))
print(len(arr.get("Game ID")))