import pyautogui as at
import time
print("เริ่มทำงานใน 5 วินาที...")
time.sleep(5)

repeat = 1

for i in range(repeat):
    at.click()
    at.click()
    time.sleep(1)
    at.press('up')
    time.sleep(2)
    at.press('enter')
    time.sleep(2)
    at.press('enter')

print("ทำงานเสร็จแล้ว ✅")
