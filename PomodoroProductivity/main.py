from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
FONT = ("Roman", 25, "bold")
iteration = 0
check_pos_x = 915
addition = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #\


def reset():
    global addition
    global iteration
    start_button.config(state="normal")
    window.after_cancel(timer)
    canvas.itemconfig(counter, text="00:00")
    label.config(text="Activity")
    addition = ""
    iteration = 0
    indicator.config(text="")
    pass


def bring_front():
    window.attributes('-topmost', True)
    window.after_idle(window.attributes, '-topmost', False)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    # global iteration
    # if iteration % 4 == 0:
    #     countdown(WORK_MIN * 60)
    #     countdown(LONG_BREAK_MIN * 60)
    # else:
    #     countdown(WORK_MIN * 60)
    #     countdown(SHORT_BREAK_MIN * 60)
    # iteration += 1
    global iteration
    iteration += 1
    start_button.config(state="disabled")
    if iteration % 8 == 0:
        countdown(LONG_BREAK_MIN)
        label.config(text="Long Rest!!!", fg=GREEN)
        bring_front()
    elif iteration % 2 == 0:
        countdown(SHORT_BREAK_MIN)
        label.config(text="Rest!", fg=GREEN)
        bring_front()
    else:
        countdown(WORK_MIN)
        label.config(text="Work!", fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global addition
    global check_pos_x
    check_pos_y = 830
    indicator.place(x=check_pos_x, y=check_pos_y)
    count_min, count_sec = count // 60, count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(counter, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        if iteration % 8 == 0:
            addition += "💊\n"
        elif iteration % 2 != 0:
            addition += "🛎"
        indicator.config(text=addition)
        start()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(bg=PINK)

# Canvas
canvas = Canvas(width=1000, height=1000, bg=PINK, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(500, 500, image=tomato)
counter = canvas.create_text(500, 390, text="00:00", font=FONT, fill="black")
canvas.place(x=960, y=540, anchor=CENTER)

# Labels
label = Label(text="Activity", font=("Roman", 80), bg=PINK, fg=YELLOW)
indicator = Label(text=addition, fg=YELLOW, bg=PINK)
label.place(x=960, y=230, anchor=CENTER)

# Buttons
start_button = Button(text="Start", bg=PINK, highlightthickness=0, highlightbackground=PINK, command=start)
reset_button = Button(text="Reset", bg=PINK, highlightthickness=0, highlightbackground=PINK, command=reset)
start_button.place(x=740, y=830, anchor=CENTER)
reset_button.place(x=1170, y=830, anchor=CENTER)

# Checkmarks
# indicator = Label(text="🎃", fg=YELLOW, bg=PINK)
# indicator.place(x=955, y=830, anchor=CENTER)


# Loop continuously
window.mainloop()
