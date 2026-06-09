import requests

city = input("اكتب اسم المدينة: ")

API_KEY = "ضع مفتاح API هنا"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

data = response.json()

if "main" in data:

    temp = data["main"]["temp"]

    weather = data["weather"][0]["description"]

    print("\n معلومات الطقس")
    print("المدينة:", city)
    print("درجة الحرارة:", temp, "°C")
    print("الحالة:", weather)

else:
    print("حدث خطأ أو المدينة غير موجودة ")