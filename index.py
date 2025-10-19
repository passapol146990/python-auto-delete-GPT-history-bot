import pyautogui as at
import time
print("เริ่มทำงานใน 5 วินาที...")
time.sleep(3)

repeat = 20

for i in range(repeat):
    at.press('tab')
    at.press('tab')
    at.press('enter')
    at.press('down')
    at.press('down')
    at.press('down')
    at.press('enter')
    at.press('enter')
    at.click()
    at.click()
    time.sleep(1)

print("ทำงานเสร็จแล้ว ✅")
