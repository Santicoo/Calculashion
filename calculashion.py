    bg_color = "#F0F0F0"
    fg_color = "#333"
    font = ("Arial", 12)
    vent = Tk()
    vent.title("Calculadora Simple")
    vent.geometry("600x400")
    vent.configure(bg=bg_color)
    global txt1, txt2, txt3
def fnsuma():
    n1 = txt1.get()
    n2 = txt2.get()
    r = float(n1) + float(n2)
    txt3.delete(0, 'end')
    txt3.insert(0, r)
