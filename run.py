import os

# دریافت مسیر عکس از کاربر
image_path = input("مسیر عکس را وارد کنید: ")

# بررسی وجود فایل
if not os.path.exists(image_path):
  print("فایل عکس وجود ندارد!")
  exit()

# اجرای دستور detect.py
os.system(f" python detect.py --weights yolov5s.pt --source {image_path} --classes 9 11 32 41 45 49 53 54 55 74 --save-txt ")


