import keyboard
import time

def putDir(x,y):
    with open('keystroke','w') as file:
        file.write(str(x)+"\n")
        file.write(str(y))
        print(f' "Going [{x}][{y}]"' )

while True:
    try:
        if keyboard.is_pressed('i'):
            putDir(-1,0)
        if keyboard.is_pressed('k'):
            putDir(+1,0)
        if keyboard.is_pressed('j'):
            putDir(0,-1)
        if keyboard.is_pressed('l'):
            putDir(0,+1)
        if keyboard.is_pressed('z'):
            break

        time.sleep(0.05)
        
            
    except:
        continue