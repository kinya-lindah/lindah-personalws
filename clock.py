import time
import tkinter as tk
from tkinter import *
from beepy import *
from threading import *
from tkmacosx import Button as button
#digital clock with alarm and timer with tkinter gui

x = 'MidnightBlue'
y = "DarkSlateGray"
timeron = False
alarmon = False
timereached = False
snoozedalarm = False


def pressed():
    if alarmbutton['fg'] == 'black':
        alarmbutton.config(fg='pink')
        alarmlabel.pack(side='left')
        firstpart.pack(side='left')
        secondpart.pack(side='left')
        setbutton2.pack(side='left')
    else:
        variable1.set(timer['text'][:2])
        variable2.set('00')
        global alarmon
        alarmbutton.config(fg="black")
        alarmbutton.config(fg='black')
        setbutton2['fg'] = 'black'
        alarmlabel.pack_forget()
        firstpart.pack_forget()
        secondpart.pack_forget()
        setbutton2.pack_forget()
        if alarmon:
            snoozebutton.pack_forget()
            cancelbutton.pack_forget()
            timer.config(fg=y)
            alarmon = False


def Threaded():
    t = Thread(target=setalarm)
    t.start()


def setalarm():
    global timereached
    global snoozedalarm
    global alarmon
    if setbutton2['fg'] == 'black':
        setbutton2['fg'] = 'pink'
        alarmon = True
        while alarmon:
            set_alarm_time = f"{variable1.get()}:{variable2.get()}"
            time.sleep(2)
            current_time = timer['text'][:5]
            if timer['text'][:5] == set_alarm_time:
                timereached = True
                beep(sound='ping')
                snoozebutton.pack(side=LEFT)
                cancelbutton.pack(side=LEFT)
            if timer['text'][:2] == f'{variable1.get()}' and int(timer['text'][3:5]) == int(variable2.get())+1:
                if not snoozedalarm:
                    snoozebutton.pack_forget()
                    cancelbutton.pack_forget()
                    if int(variable2.get()) + 3 > 60:
                        if (int(variable1.get()) + 1) % 24 < 10:
                            variable1.set("0" + str(int(variable1.get() + 1)))
                        elif (int(variable1.get()) + 1) % 24 >= 10:
                            variable1.set(str(int(variable1.get()) + 1))
                        if int(variable2.get()) + 3 - 60 < 10:
                            variable2.set("0" + str(int(variable2.get() + 3 - 60)))
                        elif int(variable2.get()) + 3 -60 >= 10:
                            variable2.set(str(int(variable2.get() + 3 - 60)))
                    else:
                        variable2.set(str(int(variable2.get()) + 3))
            if set_alarm_time != f"{variable1.get()}:{variable2.get()}":
                alarmon = False
                setbutton2['fg'] = 'black'

    else:
        setbutton2['fg'] = 'black'
        alarmon = False
        snoozedalarm = False
        if timereached:
            snoozebutton.pack_forget()
            cancelbutton.pack_forget()


def snooze():
    global snoozedalarm
    snoozedalarm = True
    if int(variable2.get())+10 > 60:
        print('snoozed')
        if int(variable1.get()) + 1 < 10:
            variable1.set("0"+str(int(variable1.get()) + 1))
        elif int(variable1.get()) + 1 >= 10:
            variable1.set(str(int(variable1.get()) + 1))
        if int(variable2.get()) + 10 -60 < 10:
            variable2.set("0"+str(int(variable2.get()) + 10 - 60))
        elif int(variable2.get()) + 10 -60 >= 10:
            variable2.set(str(int(variable2.get()) + 10 - 60))
    else:
        variable2.set(str(int(variable2.get()) + 10))


def cancelalarm():
    global alarmon
    global snoozedalarm
    snoozedalarm = False
    alarmon = False
    snoozebutton.pack_forget()
    cancelbutton.pack_forget()
    setbutton2['fg'] = 'black'
    alarmlabel.pack_forget()
    firstpart.pack_forget()
    secondpart.pack_forget()
    setbutton2.pack_forget()
    alarmbutton.config(fg="black")


def pressedt():
    global timeron
    if timerbutton['fg'] == 'black':
        timerbutton.config(fg="pink")
        timerlabel.pack(side='left')
        thirdpart.pack(side='left')
        forthpart.pack(side='left')
        fifthpart.pack(side='left')
        setbutton.pack(side='left')
        timeron = True
    else:
        timerbutton.config(fg="black")
        setbutton.config(fg="black")
        timerlabel.pack_forget()
        thirdpart.pack_forget()
        forthpart.pack_forget()
        fifthpart.pack_forget()
        setbutton.pack_forget()
        variable5.set('00')
        variable4.set('00')
        variable3.set('00')
        setbutton['text'] = 'START'
        if timeron:
            snoozebuttontimer.pack_forget()
            cancelbuttontimer.pack_forget()
        timeron = False


def settimer():
    global timeron
    if setbutton['fg'] == 'black':
        active()
    elif setbutton['fg'] == 'pink':
        print("THERE")
        variable5.set('00')
        variable4.set('00')
        variable3.set('00')
        setbutton['text'] = 'START'
        timerbutton.config(fg="black")
        setbutton.config(fg="black")
        timerlabel.pack_forget()
        thirdpart.pack_forget()
        forthpart.pack_forget()
        fifthpart.pack_forget()
        setbutton.pack_forget()
        snoozebuttontimer.pack_forget()
        cancelbuttontimer.pack_forget()
        timeron = False


def active():
    global timeron
    snoozebuttontimer.pack(side='right')
    cancelbuttontimer.pack(side='left')
    tt = int(variable3.get()) * 3600 + int(variable4.get()) * 60 + int(variable5.get())
    while tt >= 0 and timeron:
        setbutton['text'] = 'STOP'
        setbutton.config(fg="pink")
        minute, second = (tt // 60, tt % 60)
        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)
        variable5.set(second)
        variable4.set(minute)
        variable3.set(hour)
        # Update the time frame
        setframes.update()
        time.sleep(1)
        if (tt == 0):
            variable5.set('00')
            variable4.set('00')
            variable3.set('00')
            beep(sound='ready')
        tt -= 1


def add30():
    tt = int(variable3.get()) * 3600 + int(variable4.get()) * 60 + int(variable5.get())
    tt += 30
    minute, second = (tt // 60, tt % 60)
    hour = 0
    if minute > 60:
        hour, minute = (minute // 60, minute % 60)
    variable5.set(second)
    variable4.set(minute)
    variable3.set(hour)
    active()


def sub30():
    tt = int(variable3.get()) * 3600 + int(variable4.get()) * 60 + int(variable5.get())
    tt -= 30
    minute, second = (tt // 60, tt % 60)
    hour = 0
    if minute > 60:
        hour, minute = (minute // 60, minute % 60)
    variable5.set(second)
    variable4.set(minute)
    variable3.set(hour)
    active()


root = tk.Tk()
root.minsize(500, 350)
root.title("Alarm Clock")
empty = Label(root, text="", bg=x)
empty1 = Label(root, text="", bg=x)


timer = Label(root, text=time.strftime('%H:%M:%S '), font=('calibri', 25, 'bold'), borderwidth=2, relief="raised", foreground=y, bg="AliceBlue")
buttonframes = Frame(root, bg=x)
buttonframes.config(background=x)
alarmbutton = button(buttonframes, text="Alarm", command=pressed, background='GhostWhite',borderwidth=2, relief=RAISED, padx=10, pady=10)
empty2 = Label(buttonframes, text="", bg=x)
timerbutton = button(buttonframes, text="Timer", command=pressedt, background='GhostWhite',borderwidth=2, relief=RAISED, padx=10, pady=10)

setframes = Frame(root, bg=x)
empty3 = Label(setframes, text="", bg=x)

variable1 = StringVar(setframes)
variable1.set(timer['text'][:2])
firstpart = OptionMenu(setframes, variable1, '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24')
variable2 = StringVar(setframes)
variable2.set("00")
secondpart = OptionMenu(setframes, variable2, '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60')
setbutton2 = button(setframes, text="SET", command=Threaded, fg='black', background='GhostWhite',borderwidth=2, relief=RAISED)
firstpart.config(bg=x)
secondpart.config(bg=x)

variable3 = StringVar(setframes)
variable3.set("00")
thirdpart = OptionMenu(setframes, variable3, '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24')
variable4 = StringVar(setframes)
variable4.set("00")
forthpart = OptionMenu(setframes, variable4, '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60')
variable5 = StringVar(setframes)
variable5.set("00")
fifthpart = OptionMenu(setframes, variable5, '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60')
thirdpart.config(bg=x)
forthpart.config(bg=x)
fifthpart.config(bg=x)
setbutton = button(setframes, text="START", command=settimer, background='GhostWhite',borderwidth=2, relief=RAISED)
alarmlabel = Label(setframes, text="Alarm", bg=x, fg='White')
timerlabel = Label(setframes, text="Timer", bg=x, fg='White')


empty4 = Frame(root, bg=x)
e1 = Label(empty4, bg=x )

snoozeframes = Frame(root, bg=x, bd=6)
snoozebutton = button(snoozeframes, text="+10 min",borderwidth=2,  command=snooze, background='GhostWhite',  relief=RAISED)
cancelbutton = button(snoozeframes, text="Done", command=cancelalarm, background='GhostWhite',borderwidth=2, relief=RAISED)

timersnoozeframes = Frame(root, bg=x)
snoozebuttontimer = button(timersnoozeframes, text="+30 Seconds", command=add30, background='GhostWhite',borderwidth=2, relief=RAISED)
cancelbuttontimer = button(timersnoozeframes, text="-30 Seconds", command=sub30, background='GhostWhite',borderwidth=2, relief=RAISED)
timeleftlabel = Label(timersnoozeframes, text="1", bg=x, relief="raised", fg='white')


def ticker():
    timer.config(text=time.strftime('%H:%M:%S '))
    timer.after(1000, ticker)


empty1.pack()
buttonframes.pack()
alarmbutton.pack(side='left')
empty2.pack(side='left')
timerbutton .pack(side='left')
empty.pack()

timer.pack()
empty3.pack()
setframes.pack()
empty4.pack()
e1.pack()

snoozeframes.pack()
timersnoozeframes.pack()

ticker()
root.config(background=x)
root.mainloop()
