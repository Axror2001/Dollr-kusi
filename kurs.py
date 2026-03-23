import turtle
import json
import urllib.request

# Kursni olish funksiyasi
def get_live_rate(frm, to):
    url = f"https://open.er-api.com/v6/latest/{frm.upper()}"
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            data = json.load(resp)
            return float(data["rates"][to.upper()])
    except:
        return 12950.0 if frm.upper() == "USD" else 1/12950.0

def main():
    # Foydalanuvchidan ma'lumot so'rash (Grafik oynada)
    screen = turtle.Screen()
    screen.title("Valyuta Konverter v1.0")
    screen.setup(width=600, height=400)
    
    amount_str = screen.textinput("Miqdor", "Qancha pulni hisoblamoqchisiz?")
    if not amount_str: return
    
    currency = screen.textinput("Valyuta", "Valyutani kiriting (usd yoki som):").lower()
    if not currency: return

    amount = float(amount_str)
    
    # Mantiqni aniqlash
    if currency in ['usd', 'dollar', '$']:
        frm, to = "USD", "UZS"
        color = "green"
        title = "USD dan UZB ga o'tish"
    else:
        frm, to = "UZS", "USD"
        color = "blue"
        title = "UZB dan USD ga o'tish"

    rate = get_live_rate(frm, to)
    result = amount * rate

    # Turtle orqali chizish
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()

    # Fon rangi
    screen.bgcolor("#f0f0f0")

    # Sarlavha chizish
    t.goto(0, 100)
    t.color(color)
    t.write(title, align="center", font=("Arial", 20, "bold"))

    # Ramka chizish
    t.goto(-200, 80)
    t.pendown()
    t.pensize(3)
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(150)
        t.right(90)
    t.penup()

    # Natijalarni yozish
    t.color("black")
    t.goto(-180, 40)
    t.write(f"Kiritildi: {amount:,.2f} {frm}", font=("Verdana", 14, "normal"))
    
    t.goto(-180, 10)
    t.write(f"Natija: {result:,.2f} {to}", font=("Verdana", 16, "bold"))
    
    t.goto(-180, -30)
    t.write(f"Kurs: 1 {frm} = {rate:,.2f} {to}", font=("Verdana", 10, "italic"))

    t.goto(0, -180)
    t.write("Yopish uchun ekranga bosing", align="center", font=("Arial", 10, "normal"))

    screen.exitonclick()

if __name__ == "__main__":
    main()