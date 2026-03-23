import turtle
import json
import urllib.request
import sys
from tkinter import messagebox

def get_live_rate(frm, to):
    url = f"https://open.er-api.com/v6/latest/{frm.upper()}"
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            data = json.load(resp)
            if data.get("result") == "success":
                return float(data["rates"][to.upper()])
            raise Exception
    except:
        return 12950.0 if frm.upper() == "USD" else 1/12950.0

def exit_program(x, y):
    if -50 < x < 50 and -160 < y < -120:
        confirm = messagebox.askyesno("Tasdiqlash", "Siz haqiqatdan ham dasturdan chiqmoqchimisiz?")
        if confirm:
            turtle.bye()
            sys.exit()

def main():
    screen = turtle.Screen()
    screen.title("Valyuta Konverter v2.0")
    screen.setup(width=600, height=500)
    screen.bgcolor("#f8f9fa")

    amount_str = screen.textinput("Miqdor", "Summani kiriting (masalan: 100):")
    if not amount_str: return
    
    try:
        amount = float(amount_str)
    except ValueError:
        messagebox.showerror("Xato", "Iltimos, faqat raqam kiriting!")
        return

    currency = screen.textinput("Valyuta", "Nima deb hisoblaymiz? (usd yoki som):").lower()
    if not currency: return

    if currency in ['usd', 'dollar', '$']:
        frm, to, color, title = "USD", "UZS", "#27ae60", "USD dan UZB ga o'tish"
    elif currency in ['som', 'uzs', 'so\'m', 'somda']:
        frm, to, color, title = "UZS", "USD", "#2980b9", "UZB dan USD ga o'tish"
    else:
        messagebox.showwarning("Ogohlantirish", "Faqat 'usd' yoki 'som' deb yozing!")
        return

    rate = get_live_rate(frm, to)
    result = amount * rate

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()

    t.goto(0, 160)
    t.color(color)
    t.write(title, align="center", font=("Segoe UI", 24, "bold"))

    t.goto(-220, 140)
    t.pensize(2)
    t.color("#bdc3c7")
    t.pendown()
    for _ in range(2):
        t.forward(440)
        t.right(90)
        t.forward(130)
        t.right(90)
    t.penup()

    t.color("#2c3e50")
    t.goto(-190, 90)
    t.write(f"Kiritildi: {amount:,.2f} {frm}", font=("Verdana", 14, "normal"))
    
    t.goto(-190, 50)
    t.write(f"Natija: {result:,.2f} {to}", font=("Verdana", 18, "bold"))
    
    t.goto(-190, 20)
    display_rate = rate if frm == "USD" else 1/rate
    t.write(f"Kurs: 1 USD = {display_rate:,.2f} UZS", font=("Verdana", 10, "italic"))

    t.goto(-50, -120)
    t.fillcolor("#e74c3c") 
    t.begin_fill()
    for _ in range(2):
        t.forward(100)
        t.right(90)
        t.forward(40)
        t.right(90)
    t.end_fill()

    t.color("white")
    t.goto(0, -152)
    t.write("CHIQISH", align="center", font=("Arial", 12, "bold"))

    screen.onclick(exit_program)
    
    turtle.done()

if __name__ == "__main__":
    main()