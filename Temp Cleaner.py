
import os

files = os.listdir()

for file in files:
    if file.endswith(".tmp") or file.endswith(".log"):
        os.remove(file)
        print("تم حذف:", file)

print("تم تنظيف الملفات المؤقتة ")