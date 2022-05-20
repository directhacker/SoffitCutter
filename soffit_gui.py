from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
import tkinter.font
import math
#import RPi.GPIO as GPIO
import time
#GPIO.setmode(GPIO.BCM)
home = 0
readyToCut = 0
defaultSoffitLength = 144
stepsPerIn = 400
jogSpeed = 10
#num_pressed = 0
#on = GPIO.HIGH
#off = GPIO.LOW
font = "Quicksand"
require_home = True

pul = 17
dir = 27
ena = 22
switch = 21
cutRelay = 23
"""GPIO.setup(switch,GPIO.IN)
GPIO.setup(pul,GPIO.OUT)
GPIO.setup(cutRelay,GPIO.OUT)
GPIO.setup(dir,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.output(dir,off)
GPIO.output(pul,off)
GPIO.output(ena,on)
time.sleep(.0001)
GPIO.output(ena,off)
time.sleep(.0001)
def moveright(rotate):
    
    GPIO.output(dir,off)
    GPIO.output(pul,off)
    GPIO.output(ena,on)
    time.sleep(.0001)
    GPIO.output(ena,off)
    time.sleep(.0001)
    for i in range(rotate):
      GPIO.output(pul,on)
      time.sleep(.01/int(jogSpeed))
      GPIO.output(pul,off)
      time.sleep(.01/int(jogSpeed))
def moveleft(rotate):
    
    GPIO.output(dir,off)
    GPIO.output(pul,off)
    GPIO.output(ena,on)
    time.sleep(.0001)
    GPIO.output(ena,off)
    time.sleep(.0001)
    GPIO.output(dir,on)
    time.sleep(.0001)
    for i in range(rotate):
      GPIO.output(pul,on)
      time.sleep(.01/int(jogSpeed))
      GPIO.output(pul,off)
      time.sleep(.01/int(jogSpeed))
      """

def convert_to_inch(val):
        num = int(''.join(filter(str.isdigit, val)))
        if "FT" in val.upper() or "FEET" in val.upper() or "\'" in val.upper():
            result = num*12
        elif "MM" in val.upper():
            result = num/25.4
        elif "CM" in val.upper():
            result = num/2.54
        elif "IN" in val.upper() or "INCHES" in val.upper() or "\"" in val.upper():
            result = num
        else:
            result = val
            
        return int(result)
"""def cut(cutLength, numCuts):
    steps = stepsPerIn*convert_to_inch(cutLength)
    print(str(steps) + " steps")
    for i in range(int(numCuts)):
        GPIO.output(dir,off)
        GPIO.output(pul,off)
        GPIO.output(ena,on)
        time.sleep(.0001)
        GPIO.output(ena,off)
        time.sleep(.0001)
        GPIO.output(dir,on)
        time.sleep(.0001)
        for i in range(steps):
            GPIO.output(pul,on)
            time.sleep(.01/int(jogSpeed))
            GPIO.output(pul,off)
            time.sleep(.01/int(jogSpeed))
        time.sleep(1)
        GPIO.output(cutRelay, on)
        time.sleep(2)
        GPIO.output(cutRelay, off)
        time.sleep(2)
    
def goHome():
    
    GPIO.output(ena,off)
    while not(GPIO.input(switch)):
        GPIO.output(pul,on)
        time.sleep(0.005)
        GPIO.output(pul,off)
    home = 1
"""

class Widget1():
    
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        
        if parent == 0:
            self.w1 = Tk()
            self.w1.title("Soffit Cutter")
            self.value = BooleanVar()
            
            self.w1.configure(bg = '#212121')
            self.w1.geometry('1150x740')
            self.w1.resizable(0,0)
        else:
            self.w1 = Frame(parent)
            self.w1.configure(bg = '#212121')
            self.w1.place(x = 0, y = 0, width = info_screenwidth(), height = winfo_screenheight())
        self.tab1 = Notebook(self.w1)
        
        self.tab1.place(x = -1, y = 0, width = 1160, height = 750)
        self.ta1 = Frame(self.tab1)
        self.ta1.configure(bg = "#212121")
        
        self.ta1.place(x = 0, y = 0, width = 1160, height = 740)
        self.tab1.add(self.ta1, text = "Control")
        self.ta2 = Frame(self.tab1)
        self.ta2.place(x = 0, y = 0, width = 1150, height = 740)
        self.ta2.configure(bg = "#212121")
        self.tab1.add(self.ta2, text = "Settings")
        self.backward_jog = Button(self.ta1, border = 0,anchor = "n", highlightthickness = 0, text = "<", bg = "#333333", fg = "#FFFFFF", activebackground = "#111111", activeforeground= "#FFFFFF",font = tkinter.font.Font(family = font, size = 70), cursor = "arrow", state = "normal")
        self.backward_jog.place(x = 40, y = 220, width = 250, height = 150)
        self.backward_jog['command'] = self.jog_backward
        self.forward_jog = Button(self.ta1, border = 0, anchor="n",highlightthickness = 0, text = ">", bg = "#333333", fg = "#FFFFFF", activebackground = "#111111", activeforeground= "#FFFFFF",font = tkinter.font.Font(family = font, size = 70), cursor = "arrow", state = "normal")
        self.forward_jog.place(x = 300, y = 220, width = 250, height = 150)
        self.forward_jog['command'] = self.jog_forward
        self.radio_one = Radiobutton(self.ta1, highlightthickness = 0, selectcolor = "#212121", bg = "#212121", fg = "#ffffff", activebackground = "#212121", activeforeground= "#FFFFFF",text = "1in", value = 1, font = tkinter.font.Font(family = font, size = 10), cursor = "arrow", state = "normal")
        self.radio_one.place(x = 180, y = 390, width = 90, height = 32)
        self.radio_one['command'] = self.one_selected
        self.radio_six = Radiobutton(self.ta1, highlightthickness = 0, selectcolor = "#212121", bg = "#212121", fg = "#ffffff",activebackground = "#212121", activeforeground= "#FFFFFF", text = "6in", value = 2, font = tkinter.font.Font(family = font, size = 10), cursor = "arrow", state = "normal")
        self.radio_six.place(x = 280, y = 390, width = 90, height = 32)
        self.radio_six['command'] = self.six_selected
        self.radio_twelve = Radiobutton(self.ta1, highlightthickness = 0, selectcolor = "#212121", bg = "#212121", fg = "#ffffff", activebackground = "#212121", activeforeground= "#FFFFFF", text = "12in", value = 3, font = tkinter.font.Font(family = font, size = 10), cursor = "arrow", state = "normal")
        self.radio_twelve.place(x = 380, y = 390, width = 110, height = 32)
        self.radio_twelve['command'] = self.twelve_selected
        self.home = Button(self.ta1, border = 0, highlightthickness = 0,text = "Home", bg = "#333333", fg = "#FFFFFF", activebackground = "#111111", activeforeground= "#FFFFFF",font = tkinter.font.Font(family = font, size = 15, weight = 'bold'), cursor = "arrow", state = "normal")
        self.home.place(x = 40, y = 40, width = 510, height = 82)
        self.home['command'] = self.home_pressed
        self.lock = Button(self.ta1, border = 0, highlightthickness = 0, text = "Lock", bg = "#333333", fg = "#FFFFFF",activebackground = "#111111", activeforeground= "#FFFFFF", font = tkinter.font.Font(family = font, size = 15, weight = 'bold'), cursor = "arrow", state = "normal")
        self.lock.place(x = 40, y = 130, width = 250, height = 82)
        self.lock['command'] = self.lock_pressed
        self.unlock = Button(self.ta1, border = 0, highlightthickness = 0,text = "Unlock", bg = "#333333", fg = "#FFFFFF", activebackground = "#111111", activeforeground= "#FFFFFF",font = tkinter.font.Font(family = font, size = 15, weight = 'bold'), cursor = "arrow", state = "normal")
        self.unlock.place(x = 300, y = 130, width = 250, height = 82)
        self.unlock['command'] = self.unlock_pressed
        self.label2 = Label(self.ta1, anchor='w',text = "Jog Distance:", bg = "#212121", fg = "#ffffff", font = tkinter.font.Font(family = font, size = 12, weight = 'bold'), cursor = "arrow", state = "normal")
        self.label2.place(x = 40, y = 390, width = 130, height = 32)
        self.button6 = Button(self.ta1, text = "Next", border = 0, highlightthickness = 0,bg = "#333333", fg = "#FFFFFF", activebackground = "#111111", activeforeground= "#FFFFFF",font = tkinter.font.Font(family = font, size = 20, weight = 'bold'), cursor = "arrow", state = "normal")
        self.button7 = Button(self.ta1, text = "Cut", border = 0, highlightthickness = 0,bg = "#333333", fg = "#FFFFFF", activebackground = "#111111", activeforeground= "#FFFFFF",font = tkinter.font.Font(family = font, size = 20, weight = 'bold'), cursor = "arrow", state = "normal")
        self.button8 = Button(self.ta1, text = "Back", border = 0, highlightthickness = 0,bg = "#333333", fg = "#FFFFFF", activebackground = "#111111", activeforeground= "#FFFFFF",font = tkinter.font.Font(family = font, size = 20, weight = 'bold'), cursor = "arrow", state = "normal")
        self.button7.place(x = 830, y = 488, width = 250, height = 152)
        self.button7.place_forget()
        self.button8.place(x = 310, y = 488, width = 250, height = 152)
        self.button8.place_forget()
        self.button6.place(x = 570, y = 488, width = 510, height = 152)
        self.button6['command'] = self.next_pressed
        self.button7['command'] = self.cut_pressed
        self.button8['command'] = self.back_pressed
        self.label3 = Label(self.ta1, anchor='w', text = "Soffit Length", bg = "#212121", fg = "#ffffff", font = tkinter.font.Font(family = font, size = 12, weight = 'bold'), cursor = "arrow", state = "normal")
        self.label3.place(x = 570, y = 40, width = 120, height = 32)
        self.soffit_filler = Label(self.ta1, anchor='e', highlightthickness = 0, text = "", bg = "#333333", fg = "#FFFFFF", font = tkinter.font.Font(family = font, size = 12, weight = 'bold'), cursor = "arrow", state = "normal")
        self.soffit_filler.place(x = 570, y = 80, width = 150, height = 50)
        self.soffit_length = Entry(self.ta1, border = 0, highlightthickness = 0,bg = "#333333", fg = "#FFFFFF", font = tkinter.font.Font(family = font, size = 12, weight = 'bold'), cursor = "arrow", state = "normal")
        
        self.soffit_length.place(x = 580, y = 80, width = 500, height = 50)
        self.soffit_length.focus_set()
        self.soffitIndicator = Label(self.ta1, anchor='e', highlightthickness = 0, text = "", bg = "#333333", fg = "#FFFFFF", font = tkinter.font.Font(family = font, size = 12, weight = 'bold'), cursor = "arrow", state = "normal")
        self.soffitIndicator.place(x = 920, y = 80, width = 150, height = 50)
        self.cut_filler = Label(self.ta1, anchor='e', highlightthickness = 0, text = "", bg = "#333333", fg = "#FFFFFF", font = tkinter.font.Font(family = font, size = 12, weight = 'bold'), cursor = "arrow", state = "normal")
        self.cut_filler.place(x = 570, y = 180, width = 150, height = 50)
        self.cut_length = Entry(self.ta1, border = 0, highlightthickness = 0,bg = "#333333", fg = "#FFFFFF", font = tkinter.font.Font(family = font, size = 12, weight = 'bold'), cursor = "arrow", state = "normal")
        self.cut_length.place(x = 580, y = 180, width = 500, height = 50)
        self.cutIndicator = Label(self.ta1, text = "", highlightthickness = 0, bg = "#333333", fg = "#FFFFFF", anchor='e', font = tkinter.font.Font(family = font, size = 12, weight = 'bold'), cursor = "arrow", state = "normal")
        self.cutIndicator.place(x = 920, y = 180, width = 150, height = 50)
        self.label4 = Label(self.ta1, anchor='w', text = "Cut Length", bg = "#212121", fg = "#ffffff", font = tkinter.font.Font(family = font, size = 12, weight = 'bold'), cursor = "arrow", state = "normal")
        self.label4.place(x = 570, y = 140, width = 110, height = 32)
        self.num_cuts = Entry(self.ta1, border = 0, highlightthickness = 0,bg = "#333333", fg = "#FFFFFF", font = tkinter.font.Font(family = font, size = 12, weight = 'bold'), cursor = "arrow", state = "normal")
        self.num_cuts.place(x = 570, y = 280, width = 510, height = 50)
        self.label5 = Label(self.ta1,anchor='w', text = "Number of cuts", bg = "#212121", fg = "#ffffff", font = tkinter.font.Font(family = font, size = 12, weight = 'bold'), cursor = "arrow", state = "normal")
        self.label5.place(x = 570, y = 250, width = 150, height = 22)
        self.remainder = Label(self.ta1, bg = "#333333", fg = "#FFFFFF", anchor='w', font = tkinter.font.Font(family = font, size = 12, weight = 'bold'), cursor = "arrow", state = "normal")
        self.remainder.place(x = 570, y = 380, width = 510, height = 50)
        self.label6 = Label(self.ta1,anchor='w', text = "Remainder", bg = "#212121", fg = "#ffffff", font = tkinter.font.Font(family = font, size = 12, weight = 'bold'), cursor = "arrow", state = "normal")
        self.label6.place(x = 570, y = 350, width = 100, height = 22)
        self.label7 = Label(self.ta1, anchor='w', text = "Message:", bg = "#212121", fg = "#ffffff", font = tkinter.font.Font(family = font, size = 12, weight = 'bold'), cursor = "arrow", state = "normal")
        self.label7.place(x = 40, y = 450, width = 100, height = 32)
        self.label8 = Label(self.ta1, text = "", bg = "#333333", fg = "#ffffff", font = tkinter.font.Font(family = font, size = 10, weight = 'bold'), cursor = "arrow", state = "normal")
        self.label8.place(x = 40, y = 488, width = 510, height = 152)
        self.jog_speed = Entry(self.ta2, border = 0, highlightthickness = 0,bg = "#333333", fg = "#FFFFFF", font = tkinter.font.Font(family = font, size = 8), cursor = "arrow", state = "normal")
        self.jog_speed.place(x = 40, y = 84, width = 80, height = 30)
        self.jog_speed.insert(INSERT, "10")
        self.jog_speed_label = Label(self.ta2, anchor='w', bg = "#212121", fg = "#ffffff",text = "Jog Speed", font = tkinter.font.Font(family = font, size = 10), cursor = "arrow", state = "normal")
        self.jog_speed_label.place(x = 38, y = 50, width = 127, height = 32)
        self.require_homing = Checkbutton(self.ta2,anchor='w', variable=self.value, highlightthickness = 0, selectcolor="#212121", bg = "#212121", fg = "#ffffff", text = "Require Homing(recommended)", activebackground = "#212121", activeforeground= "#ffffff", font = tkinter.font.Font(family = font, size = 10), cursor = "arrow", state = "normal")
        self.require_homing.place(x = 38, y = 270, width = 480, height = 30)
        self.require_homing.select()
        self.default_soffit_length = Entry(self.ta2, border = 0, highlightthickness = 0,bg = "#333333", fg = "#FFFFFF", font = tkinter.font.Font(family = "Bahnschrift", size = 8), cursor = "arrow", state = "normal")
        self.default_soffit_length.place(x = 40, y = 220, width = 80, height = 30)
        self.default_soffit_length.insert(INSERT, "144in")
        self.soffit_length_label = Label(self.ta2, anchor='w',bg = "#212121", fg = "#ffffff", text = "Maximum Soffit Length", font = tkinter.font.Font(family = "Bahnschrift", size = 10), cursor = "arrow", state = "normal")
        self.soffit_length_label.place(x = 38, y = 190, width = 350, height = 30)
        self.button2 = Button(self.ta2, border = 0, highlightthickness = 0,bg = "#333333", fg = "#FFFFFF", activebackground = "#111111", activeforeground= "#FFFFFF", text = "Apply", font = tkinter.font.Font(family = "Bahnschrift", size = 10), cursor = "arrow", state = "normal")
        self.button2.place(x = 898, y = 615, width = 210, height = 62)
        self.button2['command'] = self.settings_applied
        self.author = Label(self.ta2, anchor='w', bg = "#212121", fg = "#ffffff",text = "lukerichardson.co", font = tkinter.font.Font(family = "Bahnschrift", size = 7), cursor = "arrow", state = "normal")
        self.author.place(x = 30, y = 670, width = 200, height = 32)
        self.step_per_in = Entry(self.ta2, border = 0, highlightthickness = 0,bg = "#333333", fg = "#FFFFFF", font = tkinter.font.Font(family = "Bahnschrift", size = 8), cursor = "arrow", state = "normal")
        self.step_per_in.place(x = 40, y = 150, width = 80, height = 30)
        self.step_per_in.insert(INSERT, "400")
        self.step_per_in_label = Label(self.ta2, anchor='w', bg = "#212121", fg = "#ffffff",text = "Steps/Inch", font = tkinter.font.Font(family = "Bahnschrift", size = 10), cursor = "arrow", state = "normal")
        self.step_per_in_label.place(x = 38, y = 120, width = 127, height = 32)
        def callback(event):
            # After 1 ms call `_callback`
            # That is to make sure that tkinter has handled the keyboard press
            self.w1.after(1, _callback)

        def _callback():
            print(1)
            val = self.soffit_length.get()
            if "FT" in val.upper() or "FEET" in val.upper() or "\'" in val.upper():
                self.soffitIndicator.configure(text = "feet")
            elif "MM" in val.upper():
                self.soffitIndicator.configure(text = "millimeters")
            elif "CM" in val.upper():
                self.soffitIndicator.configure(text = "centimeters")
            elif "IN" in val.upper() or "INCHES" in val.upper() or "\"" in val.upper():
                self.soffitIndicator.configure(text = "inches")
            else:
                self.soffitIndicator.configure(text = "")
        def callback1(event):
            # After 1 ms call `_callback`
            # That is to make sure that tkinter has handled the keyboard press
            self.w1.after(1, _callback1)

        def _callback1():
            print(2)
            val = self.cut_length.get()
            if "FT" in val.upper() or "FEET" in val.upper() or "\'" in val.upper():
                self.cutIndicator.configure(text = "feet")
            elif "MM" in val.upper():
                self.cutIndicator.configure(text = "millimeters")
            elif "CM" in val.upper():
                self.cutIndicator.configure(text = "centimeters")
            elif "IN" in val.upper() or "INCHES" in val.upper() or "\"" in val.upper():
                self.cutIndicator.configure(text = "inches")
            else:
                self.cutIndicator.configure(text = "")

        
        self.soffit_length.bind("<Key>",callback)
        self.cut_length.bind("<Key>",callback1)
        
    def settings_applied(self):
        print('settings_applied')
        global defaultSoffitLength
        global jogSpeed
        global stepsPerIn
        global require_home
        require_home = self.value.get()
        jogSpeed = self.jog_speed.get()
        defaultSoffitLength = convert_to_inch(self.default_soffit_length.get())
        stepsPerIn = int(self.step_per_in.get())
        print(require_home)
        
    
    
    def home_pressed(self):
        self.label8.configure(text = "Homing...")      
        print("homing")
        #goHome()
        global home
        home = 1
        #self.home.configure(bg = "#333333")
        
        self.label8.configure(text = "Homed!")
        self.home.configure(bg = "#278a41", activebackground = "#056820")
    
    def next_pressed(self):
        print('next_pressed')
        if home == 0 and require_home:
            self.label8.configure(text = "Please Home Machine Before Cutting")
            self.home.configure(bg = "#632e2a")
        elif self.soffit_length.index("end") == 0:
            self.soffit_length.focus_set()
            self.label8.configure(text = "Please Enter a Value in the Soffit Length Box")
            
            self.soffit_length.configure(bg="#632e2a")
            self.soffitIndicator.configure(bg="#632e2a")
            self.soffit_filler.configure(bg="#632e2a")
        elif convert_to_inch(self.soffit_length.get()) > defaultSoffitLength:
            print(defaultSoffitLength)
            self.soffit_length.focus_set()
            self.label8.configure(text = "The Maximum Soffit Size is " + str(convert_to_inch(defaultSoffitLength/12)) +"ft (" + str(defaultSoffitLength) + "in)", fg = "#bd251a")
        elif self.cut_length.index("end") == 0:
            self.label8.configure(text = "Please Enter a Value in the Cut Length Box")
            self.cut_length.focus_set()
            self.cut_length.configure(bg="#632e2a")
            self.cutIndicator.configure(bg="#632e2a")
            self.cut_filler.configure(bg="#632e2a")
            self.soffit_length.configure(bg="#333333")
            self.soffitIndicator.configure(bg="#333333")
            self.soffit_filler.configure(bg="#333333")
        elif self.num_cuts.index("end") == 0:
            self.num_cuts.insert(END, str(math.floor((convert_to_inch(self.soffit_length.get()))/convert_to_inch(self.cut_length.get()))))
            self.label8.configure(text = "Auto Populated Number of cuts", fg = "#278a41")
            self.num_cuts.configure(bg = "#278a41")
            self.soffit_length.configure(bg="#333333")
            self.cut_length.configure(bg="#333333")
            self.cutIndicator.configure(bg="#333333")
            self.cut_filler.configure(bg="#333333")
        elif self.num_cuts.index("end") > 0 and convert_to_inch(self.cut_length.get())*int(self.num_cuts.get())>convert_to_inch(self.soffit_length.get()):
            self.label8.configure(text = "Not Enough Material for This Cut", fg = "#bd251a")
        
            
        else:
            if str(self.soffit_length.get().isdecimal()):
                self.soffitIndicator.configure(text = "inches")
                
            if self.cut_length.get().isdecimal():
                self.cutIndicator.configure(text = "inches")
            
                
            self.num_cuts.configure(bg="#333333")
            self.remainder.configure(text = str(convert_to_inch(self.soffit_length.get())-(convert_to_inch(self.cut_length.get())*int(self.num_cuts.get()))) + "in")
            self.button6.place_forget()
            self.button7.place(x = 835, y = 488, width = 245, height = 152)
            self.button8.place(x = 570, y = 488, width = 245, height = 152)
            if int(self.num_cuts.get()) > 1:
                message = "You are about to cut a " + str(convert_to_inch(self.soffit_length.get())) + " inch piece of soffit \n into " + str(self.num_cuts.get()) + ", " + str(convert_to_inch(self.cut_length.get())) + " inch pieces. You will have " + str(''.join(filter(str.isdigit, self.remainder['text']))) + " inches \n left over. Press cut to continue or back to go back"
            else: 
                message = "You are about to cut a " + str(convert_to_inch(self.soffit_length.get())) + " inch piece of soffit \n into " + str(self.num_cuts.get()) + ", " + str(convert_to_inch(self.cut_length.get())) + " inch piece. You will have " + str(''.join(filter(str.isdigit, self.remainder['text']))) + " inches \n left over. Press cut to continue or back to go back"
            
            
            self.label8.configure(text = message, fg = "#ffffff")
            
    def back_pressed(self):
        print('back_pressed')
        self.button7.place_forget()
        self.button8.place_forget()
        self.button6.place(x = 570, y = 488, width = 510, height = 152)
        self.label8.configure(text = "")
    def cut_pressed(self):
        print('cut_pressed')
        self.home.configure(bg = "#333333")
        self.label8.configure(text = "Cutting...")
        #cut(self.cut_length.get(),int(self.num_cuts.get()))
        self.label8.configure(text = "Cut is complete, homing...")
        #goHome()
        self.label8.configure(text = "Done!", fg = "#278a41")
        self.button7.place_forget()
        self.button8.place_forget()
        self.button6.place(x = 570, y = 488, width = 510, height = 152)
    def one_selected(self):
        print('one_selected')
        
        global jog_distance
        jog_distance = 1

    def six_selected(self):
        print('six_selected')
        global jog_distance
        jog_distance = 6

    def twelve_selected(self):
        print('twelve_selected')
        global jog_distance
        jog_distance = 12

    def jog_forward(self):
        print('jog_forward')
        self.home.configure(bg = "#333333")
        #moveright(int(stepsPerIn*jog_distance))
    def jog_backward(self):
        print('jog_backward')
        self.home.configure(bg = "#333333")
        #moveleft(int(stepsPerIn*jog_distance))
    def lock_pressed(self):
        print('lock_pressed')
        #GPIO.output(ena,off)
    def unlock_pressed(self):
        print('unlock_pressed')
        #GPIO.output(ena,on)
    
    
if __name__ == '__main__':
    a = Widget1(0)
    a.w1.mainloop()

