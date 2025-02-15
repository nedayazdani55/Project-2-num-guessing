import random

# تنظیم محدوده و حداکثر تلاش‌ها
secret_number = random.randint(1, 100)
max_attempts = 7
attempts = 0

print("یک عدد بین 1 تا 100 حدس بزن! (شما فقط 7 بار فرصت دارید)")

while attempts < max_attempts:
    guess = int(input(f"حدس {attempts + 1}/{max_attempts}: "))

    if guess > secret_number:
        print("عدد کوچک‌تر را امتحان کن! ⬇️")
    elif guess < secret_number:
        print("عدد بزرگ‌تر را امتحان کن! ⬆️")
    else:
        print(f"تبریک! عدد {secret_number} را در {attempts + 1} حدس پیدا کردی 🎉")
        break

    attempts += 1

# اگر بازیکن باخت
if attempts == max_attempts:
    print(f"متأسفم! عدد صحیح {secret_number} بود. 😢")
