import os

while True:

    print("\n--- Notes Manager ---")
    print("1 - Add Note")
    print("2 - Show Notes")
    print("3 - Delete Note")
    print("4 - Exit")

    choice = input("اختر العملية: ")


    if choice == "1":
        note = input("اكتب الملاحظة: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("تمت الإضافة ")

    elif choice == "2":
        if not os.path.exists("notes.txt"):
            print("لا يوجد ملاحظات بعد ")
        else:
            with open("notes.txt", "r") as file:
                notes = file.readlines()

            print("\nالملاحظات:")
            for note in notes:
                print("-", note.strip())

    elif choice == "3":
        delete_note = input("اكتب الملاحظة لحذفها: ")

        if os.path.exists("notes.txt"):

            with open("notes.txt", "r") as file:
                notes = file.readlines()

            if delete_note + "\n" in notes:
                notes.remove(delete_note + "\n")

                with open("notes.txt", "w") as file:
                    file.writelines(notes)

                print("تم الحذف ")

            else:
                print("الملاحظة غير موجودة ")

        else:
            print("لا يوجد ملف ملاحظات أصلاً")

    elif choice == "4":
        print("تم الخروج ")
        break

    else:
        print("خيار غير صحيح ")