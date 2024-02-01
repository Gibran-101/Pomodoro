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
CHECK_MARK = "✔"
reps = 0
timer_mech = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer_mech)
    timer.config(text="Timer", fg=GREEN, font=(FONT_NAME, 26, "bold"), bg=YELLOW)
    check_mark.config(text="")
    canvas.itemconfig(timer_display, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 2 != 0:
        count_down(work_sec)
        timer.config(text= "WORK TIME", fg=PINK)
    elif reps % 2 == 0 and reps != 8:
        count_down(short_break_sec)
        timer.config(text="SHORT BREAK", fg=RED)
    elif reps == 8:
        count_down(long_break_sec)
        timer.config(text="LONG BREAK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_display, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_mech
        timer_mech = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor((reps/2))
        for m in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

window.after(1000, )
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_display = canvas.create_text(100, 130, text="00:00", fill="yellow", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 26, "bold"), bg=YELLOW)
timer.grid(column=1, row=0)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
check_mark.grid(column=1, row=3)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.config(padx=6, pady=0)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.config(padx=6, pady=0)
reset.grid(column=2, row=2)


window.mainloop()