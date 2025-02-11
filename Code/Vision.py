import pyautogui
from pynput import mouse
from pynput import keyboard
from PIL import ImageGrab
import time

color = []
searchedColor = []

# Function to find the pixel with the target color
def find_color(color):
    screen = ImageGrab.grab()  # Capture the full screen
    screen_width, screen_height = screen.size

    # Loop through all pixels to find the target color
    for x in range(0, screen_width, 10):
        for y in range(0, screen_height, 10):
            pixel_color = screen.getpixel((x, y))
            if pixel_color == color:
                return (x, y)
    return None

def on_click(x, y, button, pressed):
    if pressed:
        screen = ImageGrab.grab()  # Capture the full screen
        color.append(screen.getpixel((x, y)))
        print(color)

def on_press(key):
    try:
        if key.char == 'p':
            color_position = find_color(searchedColor[-1])
            if color_position:
                pyautogui.click(color_position)  # Click the position of the found color
                print(f"Clicked on color at position: {color_position}")
            else:
                print("Color not found on the screen.")
        if key.char == 'l':
            searchedColor.append(color[-1])
    except: 
        pass

with mouse.Listener(on_click=on_click), keyboard.Listener(on_press=on_press) as listener:
    listener.join()