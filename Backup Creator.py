import os
import shutil

count = 0

if not os.path.exists("Backup"):
    os.mkdir("Backup")

files = os.listdir()

for file in files:
    if file != "Backup":
        shutil.copy(file, "Backup/" + file)
        count += 1

print("تم إنشاء النسخة الاحتياطية بنجاح ")
print("تم نسخ", count, "ملف")