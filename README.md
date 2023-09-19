# google-chat-space-maker
Allows you to auto generate a google chat space if you often have to create spaces with the same people in them.

all x and y mouse values have to be provided yourself as they are different on all devices but you can use ```get_mouse_pos.py``` to get the ```x,y``` values.

All users/names have to also be provided by repeating the code in lines 24-25 of ```main.py``` and you may want to edit the ```y``` values for ```select_user()``` multiple times e.g

```py
def select_user():
    time.sleep(0.75)
    pyautogui.click(x = 100 , y = 450)
    time.sleep(0.75)
```
to 
```py
def select_user_2():
  time.sleep(0.75)
  pyautogui.click(x = 100, y = 460)
  time.sleep(0.75)
```
Since sometimes the ```y``` values change while typing (if you have a long list of names)
