import os

print("="*20)
print("in poroje mitavanad ashia e dAyere shekl mesle kasse,top,pizza,... ra dar ax peyda konad va tedad va shoA begoyad")
print("="*20)
# دریافت مسیر عکس از کاربر
image_path = input("Insert Path Of Your Image Here ")

# بررسی وجود فایل
if not os.path.exists(image_path):
  print("There is not Image here!!")
  exit()

# اجرای دستور detect.py
os.system(f" python detect.py --weights yolov5s.pt --source {image_path} --classes 9 11 32 41 45 49 53 54 55 74 --save-txt ")

print("="*20)
print("For see the result open image in runs\detect\exp")
print("="*20)
print("Now run CalculateRadiusOfCircles.py for more!")
print("="*20)


