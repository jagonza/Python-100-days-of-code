from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    start_btn["state"] = "normal"
    reset_btn["state"] = "disabled"
    global reps
    reps = 0
    ticks_table.config(text="")
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    global reps
    start_btn["state"] = "disabled"
    reset_btn["state"] = "normal"
    # if reps < 4:
    reps += 1
    if reps % 2 != 0:
        ticks = ""
        for _ in range(int(reps / 2)):
            ticks += "✔︎"
        ticks_table.config(text=ticks)

    if reps % 8 == 0:
        seconds = LONG_BREAK_MIN * 60
        timer_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        seconds = SHORT_BREAK_MIN * 60
        timer_label.config(text="BREAK", fg=PINK)
    else:
        seconds = WORK_MIN * 60
        timer_label.config(text="WORK", fg=GREEN)

    count_down(seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count_in_seconds):
    global timer
    minutes = math.floor(count_in_seconds / 60)
    str_minutes = "{:0>2d}".format(minutes)
    seconds = count_in_seconds % 60
    str_seconds = "{:0>2d}".format(seconds)
    canvas.itemconfig(timer_text, text=f"{str_minutes}:{str_seconds}")
    if count_in_seconds >= 0:
        timer = window.after(1000, count_down, count_in_seconds - 1)
    else:
        start()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer",
                    fg=GREEN,
                    bg=YELLOW,
                    font=("Courier", 50, "bold"))
timer_label.grid(row=0, column=1, sticky='ew')

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130,
                                text="00:00",
                                fill="white",
                                font=("Courier", 36, "bold"))
canvas.grid(row=1, column=1, pady=10)

start_btn = Button(text="START", padx=10, pady=5,
                   highlightthickness=0, command=start)
start_btn.grid(row=2, column=0)
reset_btn = Button(text="RESET", padx=10, pady=5,
                   highlightthickness=0, command=reset)
reset_btn["state"] = "disabled"
reset_btn.grid(row=2, column=2)

ticks_table = Label(text="",
                    fg=GREEN,
                    bg=YELLOW,
                    font=("Courier", 36, "bold"))
ticks_table.grid(row=3, column=1, sticky='ew')

window.mainloop()
