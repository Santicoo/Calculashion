from tkinter import Tk, Label, Button, Entry

def crear_ventana():
    global vent  

    bg_color = "#F0F0F0"
    fg_color = "#333"
    font = ("Arial", 12)
    vent = Tk()
    vent.title("Calculadora Simple")
    vent.geometry("600x400")
    vent.configure(bg=bg_color)
    global txt1, txt2, txt3
    lbl1 = Label(vent, text="Número 1", fg=fg_color, bg=bg_color, font=font)
    lbl1.place(relx=0.5, rely=0.1, anchor='center', relwidth=0.6, relheight=0.1)
    txt1 = Entry(vent)
    txt1.place(relx=0.5, rely=0.2, anchor='center', relwidth=0.6, relheight=0.1)
    lbl2 = Label(vent, text="Número 2", fg=fg_color, bg=bg_color, font=font)
    lbl2.place(relx=0.5, rely=0.3, anchor='center', relwidth=0.6, relheight=0.1)
    txt2 = Entry(vent)
    txt2.place(relx=0.5, rely=0.4, anchor='center', relwidth=0.6, relheight=0.1)
def fnsuma():
    n1 = txt1.get()
    n2 = txt2.get()
    r = float(n1) + float(n2)
    txt3.delete(0, 'end')
    txt3.insert(0, r)

def fnresta():
    n1 = txt1.get()
    n2 = txt2.get()
    r = float(n1) - float(n2)
    txt3.delete(0, 'end')
    txt3.insert(0, r)

def fnmulti():
    n1 = txt1.get()
    n2 = txt2.get()
    r = float(n1) * float(n2)
    txt3.delete(0, 'end')
    txt3.insert(0, r)

def fndivi():
    n1 = txt1.get()
    n2 = txt2.get()
    r = float(n1) / float(n2)
    txt3.delete(0, 'end')
    txt3.insert(0, r)

def fnminimomultiplo():
    n1 = int(txt1.get())
    n2 = int(txt2.get())
    r = n1
    while r % n2 != 0:
        r += 1
    txt3.delete(0, 'end')
    txt3.insert(0, r)

def fnmaximodivisor():
    n1 = int(txt1.get())
    n2 = int(txt2.get())
    r = min(n1, n2)
    while r > 1:
        if n1 % r == 0 and n2 % r == 0:
            break
        r -= 1
    txt3.delete(0, 'end')
    txt3.insert(0, r)

def fnsalir():
    vent.destroy()

vent = crear_ventana()
vent.mainloop()