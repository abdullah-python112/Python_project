
import os
a=[]
if os.path.exists("data.txt"):
    file=open("data.txt","r")
    for line in file :
        itm,praic = line.strip().split(",")
        a.append([itm,float(praic)])
    file.close()
while True: 
    action=input("اختر نوع العمليه : add / show / total  / delet  / edit  /  search /sort/ unsort / max /exit : ")
    if action=="exit":
        print ("يومًا سعيدًا")
        break
    elif action =="add":
        itm=input("ماذا اشتريت؟ ")
        praic=float(input("كم سعره"))
        a.append([itm,praic])
        
        file=open("data.txt" , "a")
        file.write(itm+","+str(praic)+"\n")
        file.close()
    elif action=="show":
        for i,x in enumerate(a):
            print (i+1,"_",x[0],":", x[1])
    elif action=="total":
        total=0
        for x in a :
            total += x[1]
        print(total)
    elif action=="delet":
        for i , x in enumerate(a):
            print(i+1,"_",x[0],":",x[1])
        num=int(input("اختر الرقم الذي تريد حذفه"))
        a.pop(num-1)
        print("تم الحذف بنجاح")
        file=open("data.txt","w")
        for x in a:
            file.write(x[0] + "," + str(x[1])+ "\n")
        file.close()
    elif action=="edit":
        for i,x in enumerate(a):
            print(i+1,"_",x[0] ,":",x[1])
        num=int(input("اختر الرقم الذي تريد استبداله"))
        new_num=input("ماذا اشتريت بدلًا منه؟  :")
        new_praic=float(input("كم سعره؟ : "))
        a[ num-1]=[new_num,new_praic]
        print("تم التعديل بنجاح !")
        file=open("data.txt", "w")
        for x in a :
            file.write(x[0] + "," + str(x[1]) + "\n")
        file.close()
    elif action=="search":
        world=input("عن ماذا تبحث :  ")
        for x in a:
            if world in x[0]:
                print(x[0] , ":", x[1])
    elif action =="sort":
     a.sort(key=lambda x :x[1])
     print("تم ترتيب العناصر من الاغلى للارخص")
     for x in a :
         print(x[0],":",(x[1]),"\n")
    elif action =="unsort":
       a.sort(key=lambda x :x[1] , reverse=True)
       print("تم ترتيب العناصر من الارخص للاغلى")
       for x in a :
           print(x[0],":",(x[1]),"\n")
    elif action =="max":
        if len(a)==0:
            print("لا يوجد مصاريف")
        else:
            max_item=max(a, key=lambda x :x[1])
            print("اغلى سعر هوا")
            print(max_item[0],":",max_item[1]) 