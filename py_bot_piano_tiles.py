import pyautogui
import win32api,win32con
import keyboard
import time

def playClick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(587,500)[0] == 0:
        playClick(587,510)
    if pyautogui.pixel(684,500)[0] == 0:
        playClick(684,510)
    if pyautogui.pixel(775,500)[0] == 0:
        playClick(775,510)
    if pyautogui.pixel(869,500)[0] == 0:
        playClick(869,510)



#X:  587 Y:  500 RGB: (0,  0,   0)
#X:  684 Y:  500 RGB: (255, 255, 255)
#X:  775 Y:  500 RGB: (255, 255, 255)
#X:  869 Y:  500 RGB: (208, 108, 118)
