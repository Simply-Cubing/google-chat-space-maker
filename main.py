import pyautogui
import time
space_name = input("space name -> ")
space_description = input("space description -> ")
def select_user():
    time.sleep(0.75)
    pyautogui.click(x = , y =)
    time.sleep(0.75)

time.sleep(3)
pyautogui.click(x = , y =)
#clicks the "new space" button
time.sleep(0.5)
pyautogui.click(x = , y =)
#clicks the "create space" button
time.sleep(1)
pyautogui.write(space_name)
#writes the name of the space
time.sleep(0.5)
pyautogui.click(x = , y =)
#clicks the space description field
time.sleep(0.5)
pyautogui.write(space_description)
#writes the description
time.sleep(0.5)
#clicks the add user(s) field 
pyautogui.click(x = , y =)
time.sleep(0.5)

#writes the user's name
pyautogui.write("name")
#selects it
select_user()
#repeat for all users OR use a list + for loop

#clicks off the user adding thing
pyautogui.click(x =,y =)
#clicks the "create" button
pyautogui.click(x =,y =)

