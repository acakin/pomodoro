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
def reset_button():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_button():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    minute = math.floor(count / 60)
    second = count % 60
    if second < 10:
        second = f"0{second}"
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1, count_down, count - 1)
    else:
        start_button()
        mark = 0
        for _ in range(math.floor(reps / 2)):
            mark += 1
        check_mark.config(text=f"{mark}x✔")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=240, height=240, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(120, 120, image=tomato_img)
timer_text = canvas.create_text(120, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"), highlightthickness=0)
label.grid(row=0, column=1)

start = Button(text="Start", highlightthickness=0, command=start_button)
start.grid(row=2, column=0)

reset = Button(text="Reset", highlightthickness=0, command=reset_button)
reset.grid(row=2, column=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"), highlightthickness=0)
check_mark.grid(row=3, column=1)

window.mainloop()
