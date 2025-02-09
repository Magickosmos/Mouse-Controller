import pyautogui
from pynput import mouse
from pynput import keyboard

#Initial testing indidcates about a limit of 10 cps for pyautogui
#Additionally movement slow even with 0 delay so better to specify pose

Mouse_Pose = []

#Records the mouse position every time the user clicks and stoes in Mouse_Pose
def on_click(x, y, button, pressed):
    if pressed:
        x, y = pyautogui.position()
        row = [x , y] 
        Mouse_Pose.append(row)

#Pressing the button p will play back all the mouse clicks recroded by the program
def on_press(key):
    try:
        if key.char == 'p':
            for element in Mouse_Pose:
                x, y = element
                pyautogui.moveTo(x, y)
                pyautogui.click()
                Mouse_Pose.pop()
    except: 
        pass
        

with mouse.Listener(on_click=on_click), keyboard.Listener(on_press=on_press) as listener:
    listener.join()