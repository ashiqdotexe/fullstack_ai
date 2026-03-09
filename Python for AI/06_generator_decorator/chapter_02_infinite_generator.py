def infinite_tea(user):
    count = 0
    while True:
        yield print(f"Serving cup {count+1} for {user}")
        count+=1
user_1 = infinite_tea(user="user-1")
user_2 = infinite_tea(user="user-2")

for _ in range(5):
    next(user_1)
for _ in range(3):
    next(user_2)