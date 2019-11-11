import keyboard

__author__      = "Anwesha Sen"

KEY_PRESSED = ''

def eng2beng(event):
    key = event.name
    #while key != 'esc' :
    '''
    if key != 'esc':
        print("Please press esc key to get contol over Bangla keyboard.....")
    if key == 'esc':
        print("Welcome to bangla keyboard...")
        print("Now write anything in Inscript Layout....")
    '''
    if False:
        pass
    else:
        if key not in keyboard.all_modifiers:
            keyboard.write('\b')
        if key == '1':
            keyboard.write("১")
        if key == '2':
            keyboard.write("২")
        if key == '3':
            keyboard.write("৩")         
        if key == '4':
            keyboard.write("৪")
        if key == '5':
            keyboard.write("৫")
        if key == '6':
            keyboard.write("৬")
        if key == '7':
            keyboard.write("৭")
        if key == '8':
            keyboard.write("৮")
        if key == '9':
            keyboard.write("৯")
        if key == '0':
            keyboard.write("o")
        if key == '_':
            keyboard.write("ঃ")
        if key == '+':
            keyboard.write("ঋ")
        if key == '=':
            keyboard.write("ৃ")    
        if key == 'Q':
            keyboard.write("ঔ")
        if key == 'W':
            keyboard.write("ঐ")
        if key == 'E':
            keyboard.write("আ")
        if key == 'R':
            keyboard.write("ঈ")
        if key == 'T':
            keyboard.write("ঊ")
        if key == 'Y':
            keyboard.write("ভ")
        if key == 'U':
            keyboard.write("ঙ")
        if key == 'I':
            keyboard.write("ঘ")
        if key == 'O':
            keyboard.write("ধ")
        if key == 'P':
            keyboard.write("ঝ")
        if key == '{':
            keyboard.write("ঢ")
        if key == '}':
            keyboard.write("ঞ")
        if key == 'A':
            keyboard.write("ও")
        if key == 'S':
            keyboard.write("এ")
        if key == 'D':
            keyboard.write("অ")
        if key == 'F':
            keyboard.write("ই")
        if key == 'G':
            keyboard.write("উ")
        if key == 'H':
            keyboard.write("ফ")
        if key == 'J':
            keyboard.write("J")
        if key == 'K':
            keyboard.write("খ")
        if key == 'L':
            keyboard.write("থ")    
        if key == ':':
            keyboard.write("ছ")
        if key == '"':
            keyboard.write("ঠ")      
        if key == 'Z':
            keyboard.write("Z")
        if key == 'X':
            keyboard.write("ঁ")
        if key == 'C':
            keyboard.write("ণ")
        if key == 'V':
            keyboard.write("V")
        if key == 'B':
            keyboard.write("B")
        if key == 'N':
            keyboard.write("N")
        if key == 'M':
            keyboard.write("শ")
        if key == '<':
            keyboard.write("ষ")
        if key == '>':
            keyboard.write("|")
        if key == '?':
            keyboard.write("য")
        if key == 'q':
            keyboard.write("ৌ")
        if key == 'w':
            keyboard.write("ৈ")
        if key == 'e':
            keyboard.write("া")
        if key == 'r':
            keyboard.write("ী")
        if key == 't':
            keyboard.write("ূ")
        if key == 'y':
            keyboard.write("ব")
        if key == 'u':
            keyboard.write("হ")
        if key == 'i':
            keyboard.write("গ")
        if key == 'o':
            keyboard.write("দ")
        if key == 'p':
            keyboard.write("জ")
        if key == '[':
            keyboard.write("ড")
        if key == ']':
            keyboard.write("্")
        if key == 'a':
            keyboard.write("ো")
        if key == 's':
            keyboard.write("ে")
        if key == 'd':
            keyboard.write("্")
        if key == 'f':
            keyboard.write("ি")
        if key == 'g':
            keyboard.write("ু")
        if key == 'h':
            keyboard.write("প")
        if key == 'j':
            keyboard.write("র")
        if key == 'k':
            keyboard.write("ক")
        if key == 'l':
            keyboard.write("ত")    
        if key == ';':
            keyboard.write("চ")
        if key == '\'':
           keyboard.write("ট")      
        if key == 'z':
            keyboard.write("z")
        if key == 'x':
            keyboard.write("ং")
        if key == 'c':
            keyboard.write("ম")
        if key == 'v':
            keyboard.write("ন")
        if key == 'b':
            keyboard.write("ব")
        if key == 'n':
            keyboard.write("ল")
        if key == 'm':
            keyboard.write("স")
        if key == '/':
            keyboard.write("য়")       
            
    
def print_pressed_keys(event):
    global KEY_PRESSED
    prev_key = KEY_PRESSED
    key = event.name
    # event_type = event.event_type
    if prev_key != key:
        KEY_PRESSED = key
        eng2beng(event)
    
keyboard.hook(print_pressed_keys)
keyboard.wait()
