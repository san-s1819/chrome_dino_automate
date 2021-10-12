import msvcrt
while True:
    if msvcrt.kbhit():
        key_stroke = msvcrt.getch()
       # print(typeof(key_stroke))
        if(ord(key_stroke)==120):
            print("1")
        else:
            print(ord(key_stroke))
