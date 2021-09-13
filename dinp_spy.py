import msvcrt
while True:
    if msvcrt.kbhit():
        key_stroke = msvcrt.getch()
        if(key_stroke=="x"):
            print(key_stroke)
        else:
            print("1")
