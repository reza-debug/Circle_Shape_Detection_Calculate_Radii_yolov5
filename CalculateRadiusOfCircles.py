import os
import math



# مسیر پوشه labels
print("-" * 20)
print("For Show Radius of circles Objects Go To 'runs/detect/exp/labels' And Copy path Of labels's Folder ")
labels_dir = input("Insert Here Copy Path Of Labels's Folder: ")

# تابع برای خواندن اطلاعات از فایل txt
def read_file(file_path):
  """
  خواندن اطلاعات مربوط به اشیاء شناسایی شده از یک فایل txt

  Args:
    file_path: مسیر فایل txt

  Returns:
    لیست شامل اطلاعات مربوط به اشیاء
  """

  with open(file_path, "r") as f:
    lines = f.readlines()

  # لیست برای ذخیره اطلاعات اشیاء
  objects = []

  for line in lines:
    # تفکیک اطلاعات هر شیء
    data = line.split()

    # استخراج شناسه کلاس، مختصات و اطمینان
    class_id = int(data[0])
    x1, y1, x2, y2 = float(data[1]), float(data[2]), float(data[3]), float(data[4])
    

    # محاسبه عرض و ارتفاع
    width = x2 - x1
    height = y2 - y1

    # محاسبه قطر
    diameter = math.sqrt(width**2 + height**2)

    # محاسبه شعاع
    radius = diameter / 2

    # اضافه کردن اطلاعات شیء به لیست
    objects.append({
        "class_id": class_id,
        "x1": x1,
        "y1": y1,
        "x2": x2,
        "y2": y2,        
        "width": width,
        "height": height,
        "diameter": diameter,
        "radius": radius,
    })

  return objects

# اسکن پوشه labels و پردازش هر فایل txt
for filename in os.listdir(labels_dir):
  # بررسی فقط فایل‌های txt
  if not filename.endswith(".txt"):
    continue

  # مسیر کامل فایل
  file_path = os.path.join(labels_dir, filename)

  # خواندن اطلاعات اشیاء از فایل
  objects = read_file(file_path)

  # شمارش اشیاء
  num_objects = len(objects)

  # چاپ اطلاعات
  print(f"Image {filename}:")
  print(f"Number Of Circles: {num_objects}")

  # چاپ شعاع هر شیء
  for obj in objects:
    print(f"Radius : {obj['radius']}")


  print("-" * 20)  
  # دریافت مقیاس واقعی از کاربر
  print("Insert Real Scale For Calculate(Pixel To CentiMeter): ")
  scale_factor = float(input())

  # چاپ شعاع هر شیء در مقیاس واقعی
  for obj in objects:
    # محاسبه شعاع در مقیاس واقعی
    radius_real = obj["radius"] * scale_factor

    print(f"Radius of circle  (Real scale): {radius_real:.2f} CentiMeter")

  print("-" * 20)
