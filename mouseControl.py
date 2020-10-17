import pyautogui

resolution = pyautogui.size()
print(resolution)

width, height = pyautogui.size()
position = pyautogui.position()
pyautogui.moveTo(10,10, duration=2.5)
pyautogui.moveRel(200,0, duration=2)
print(position)
pyautogui.click(435,75)
pyautogui.doubleClick(435,75)

Draw a squarre spirowshape
pyautogui.click()    # Click to make the window active.
distance = 300
change = 20
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2)   # Move right.
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.2)   # Move down.
    pyautogui.drag(-distance, 0, duration=0.2)  # Move left.
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.2)  # Move up.
