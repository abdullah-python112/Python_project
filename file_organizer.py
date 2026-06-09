import os
import shutil

if not os.path.exists("Photos"):
    os.mkdir("Photos")

if not os.path.exists("PDFs"):
    os.mkdir("PDFs")

if not os.path.exists("Texts"):
    os.mkdir("Texts")

files = os.listdir()

for file in files:

    if file.endswith(".jpg") or file.endswith(".png"):
        shutil.move(file, "Photos/" + file)

    elif file.endswith(".pdf"):
        shutil.move(file, "PDFs/" + file)

    elif file.endswith(".txt"):
        shutil.move(file, "Texts/" + file)

print("تم ترتيب الملفات بنجاح ")