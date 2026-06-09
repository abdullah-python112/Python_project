import os

files = os.listdir()

count = 1

for file in files:

    if file.endswith(".jpg"):

        new_name = "image_" + str(count) + ".jpg"

        os.rename(file, new_name)

        count += 1

print("تمت إعادة تسمية", count - 1, "صورة بنجاح ")