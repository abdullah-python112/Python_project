
import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$&+*/?_-"

all_characters = letters + numbers + symbols

length = int(input("كم طول كلمة السر الخاصة بك؟ اكتب رقمًا: "))

password = ""

for x in range(length):
password += random.choice(all_characters)

print("\n كلمة السر الخاصة بك هي:")
print(password)

save = input("\nهل تريد حفظ كلمة السر؟ نعم / لا : ")

if save == "نعم":
with open("passwords.txt", "a") as file:
file.write(password + "\n")
print(" تم حفظ كلمة السر بنجاح")

if save == "لا":
print(" لم يتم الحفظ")