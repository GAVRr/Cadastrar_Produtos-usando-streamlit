from keyboard import is_pressed

while True:
    if is_pressed("w"):
        print("Andando")

    if not is_pressed('w'):
        print('parado')
