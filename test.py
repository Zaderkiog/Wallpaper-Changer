import ctypes
import time 

img1 = r"Wallpapers/test1.png"

images = [img1]

n = int(input('Enter n(0-5):'))

if n >= 0 and n <= 20:
   print('You chose: ', n)
   ctypes.windll.user32.SystemParametersInfoW(20, 0, images[n], 0)
   print("Wallpaper ", n, " successfully applied.")
else:
   print("wrong entry, please choose correct input")

for n in range(32):
   print(" wallpaper is img: ", n)
   time.sleep(3.5)
   ctypes.windll.user32.SystemParametersInfoW(20, 0, images[n], 0)