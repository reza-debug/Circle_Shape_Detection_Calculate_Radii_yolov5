import os

# دریافت مسیر عکس از کاربر
image_path = input("Insert Path Of Your Image Here ")

# بررسی وجود فایل
if not os.path.exists(image_path):
  print("There is not Image here!!")
  exit()

# اجرای دستور detect.py
os.system(f" python detect.py --weights yolov5s.pt --source {image_path} --classes 9 11 32 41 45 49 53 54 55 74 --save-txt ")


