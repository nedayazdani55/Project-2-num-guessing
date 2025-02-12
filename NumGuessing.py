import random

# تولید یک عدد تصادفی بین 1 تا 100
secret_number = random.randint(1, 100)

print("یک عدد بین 1 تا 100 حدس بزن!")

while True:
    guess = int(input("حدس شما: "))

    if guess > secret_number:
        print("عدد کوچک‌تر را امتحان کن!")
    elif guess < secret_number:
        print("عدد بزرگ‌تر را امتحان کن!")
    else:
        print("تبریک! عدد درست را حدس زدی 🎉")
        break
