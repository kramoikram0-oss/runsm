import tkinter as tk
import random
import time
import arabic_reshaper
from bidi.algorithm import get_display

# ==============================
#        SETTINGS
# ==============================

PASSWORD = "1234"

MESSAGE = """
تم اختراق النظام بنجاح

جميع البيانات أصبحت تحت السيطرة

L3ABOUCH
"""

# ==============================
#       ARABIC FIX
# ==============================

def ar(text):
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

# ==============================
#       WINDOW
# ==============================

root = tk.Tk()

root.title("SYSTEM BREACH")

root.attributes("-fullscreen", True)

root.configure(bg="black")

WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

canvas = tk.Canvas(
    root,
    bg="black",
    highlightthickness=0
)

canvas.pack(fill="both", expand=True)

# ==============================
#      CYBER BACKGROUND
# ==============================

particles = []

for i in range(120):

    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)

    size = random.randint(1, 3)

    particle = canvas.create_oval(
        x,
        y,
        x + size,
        y + size,
        fill="#00ff66",
        outline=""
    )

    particles.append((particle, random.randint(1, 4)))

def animate_particles():

    for particle, speed in particles:

        canvas.move(particle, 0, speed)

        pos = canvas.coords(particle)

        if pos[1] > HEIGHT:

            x = random.randint(0, WIDTH)

            canvas.coords(
                particle,
                x,
                0,
                x + 2,
                2
            )

    root.after(30, animate_particles)

# ==============================
#        MATRIX EFFECT
# ==============================

chars = "01アイウエオカサタナハマヤラワ"

drops = [random.randint(0, HEIGHT) for _ in range(WIDTH // 20)]

def matrix():

    canvas.delete("matrix")

    for i in range(len(drops)):

        char = random.choice(chars)

        x = i * 20
        y = drops[i]

        canvas.create_text(
            x,
            y,
            text=char,
            fill="#00ff66",
            font=("Courier", 14, "bold"),
            tags="matrix"
        )

        drops[i] += 18

        if drops[i] > HEIGHT:
            drops[i] = 0

    root.after(50, matrix)

# ==============================
#      MAIN TITLE
# ==============================

shadow = canvas.create_text(
    WIDTH // 2 + 3,
    HEIGHT // 3 + 3,
    text=ar(MESSAGE),
    fill="#220000",
    font=("Arial", 30, "bold"),
    justify="center"
)

main_text = canvas.create_text(
    WIDTH // 2,
    HEIGHT // 3,
    text=ar(MESSAGE),
    fill="#ff0033",
    font=("Arial", 30, "bold"),
    justify="center"
)

# ==============================
#      GLOW EFFECT
# ==============================

glow = True

def glow_effect():

    global glow

    if glow:

        canvas.itemconfig(main_text, fill="#ff3355")

    else:

        canvas.itemconfig(main_text, fill="#ff0033")

    glow = not glow

    root.after(500, glow_effect)

# ==============================
#      TIMER
# ==============================

seconds = 300

timer = canvas.create_text(
    WIDTH // 2,
    HEIGHT // 2 + 70,
    text="05:00",
    fill="white",
    font=("Courier", 42, "bold")
)

def update_timer():

    global seconds

    mins = seconds // 60
    secs = seconds % 60

    canvas.itemconfig(
        timer,
        text=f"{mins:02}:{secs:02}"
    )

    if seconds > 0:

        seconds -= 1

        root.after(1000, update_timer)

# ==============================
#      TERMINAL LOGS
# ==============================

logs = [
    "Uploading device data...",
    "Accessing camera...",
    "Security bypassed...",
    "Tracking enabled...",
    "Injecting payload...",
    "Remote connection established..."
]

terminal = canvas.create_text(
    WIDTH // 2,
    HEIGHT - 120,
    text="",
    fill="#00ff66",
    font=("Courier", 13)
)

def terminal_effect():

    txt = random.choice(logs)

    canvas.itemconfig(
        terminal,
        text=txt
    )

    root.after(700, terminal_effect)

# ==============================
#      PASSWORD INPUT
# ==============================

entry = tk.Entry(
    root,
    show="*",
    font=("Courier", 22),
    bg="#050505",
    fg="#00ff66",
    insertbackground="#00ff66",
    relief="flat",
    justify="center"
)

entry.place(
    relx=0.5,
    rely=0.77,
    anchor="center",
    width=280,
    height=55
)

# ==============================
#      BUTTON
# ==============================

def flash():

    for i in range(3):

        root.configure(bg="#220000")
        canvas.configure(bg="#220000")

        root.update()

        time.sleep(0.05)

        root.configure(bg="black")
        canvas.configure(bg="black")

        root.update()

        time.sleep(0.05)

def unlock(event=None):

    if entry.get() == PASSWORD:

        root.destroy()

    else:

        flash()

        entry.delete(0, tk.END)

button = tk.Button(
    root,
    text="UNLOCK",
    command=unlock,
    bg="#111111",
    fg="#00ff66",
    activebackground="black",
    activeforeground="red",
    font=("Courier", 18, "bold"),
    relief="flat",
    borderwidth=0
)

button.place(
    relx=0.5,
    rely=0.87,
    anchor="center",
    width=240,
    height=55
)

root.bind("<Return>", unlock)

# ==============================
#      SCAN LINE
# ==============================

scan = canvas.create_rectangle(
    0,
    0,
    WIDTH,
    6,
    fill="#00ff66",
    outline=""
)

scan_y = 0

def scanner():

    global scan_y

    scan_y += 6

    canvas.coords(
        scan,
        0,
        scan_y,
        WIDTH,
        scan_y + 6
    )

    if scan_y > HEIGHT:

        scan_y = 0

    root.after(15, scanner)

# ==============================
#      SHAKE EFFECT
# ==============================

def shake():

    x = random.randint(-4, 4)
    y = random.randint(-4, 4)

    root.geometry(f"+{x}+{y}")

    root.after(80, shake)

# ==============================
#      START
# ==============================

animate_particles()

matrix()

glow_effect()

update_timer()

terminal_effect()

scanner()

shake()

root.mainloop()
