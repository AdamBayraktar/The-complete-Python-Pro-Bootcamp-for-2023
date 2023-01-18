from tkinter import Tk, Canvas, Button, Entry, Label, PhotoImage
import time


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
timer_watch = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_time():
    if timer_watch:
        window.after_cancel(timer_watch)
    global reps
    reps = 0
    timer_label.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(text_id, text=f"00:00")
    green_tick['text'] = ''


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_machanism():
    global reps
    if reps > 7:
        return 1
    elif reps % 2 == 0:
        countdown_25_min()
        timer_label["text"] = "WORK"
        timer_label["fg"] = GREEN
    elif reps % 7 == 0:
        countdown_25_min(20*60)
        timer_label["text"] = "BREAK"
        timer_label["fg"] = RED
    else:
        countdown_25_min(5*60)
        timer_label["text"] = "BREAK"
        timer_label["fg"] = PINK
    
    if reps % 2 == 1:
        green_tick["text"] += tick

def launch():
    reset_time()
    timer_machanism()



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown_25_min(t=(25*60)):
    minutes, secs = divmod(t, 60)
    canvas.itemconfig(text_id, text=f"{minutes:02.0f}:{secs:02.0f}")
    if t > 0:
        global timer_watch
        timer_watch = window.after(1000, countdown_25_min, t - 1)
    else: 
        global reps
        reps += 1
        return timer_machanism()

    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
# window.minsize()
window.config(padx=50, pady=70, bg=YELLOW)
# window.config(padx=50, pady=20)

# tomato canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
the_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=the_image)
canvas.grid(column=1, row=1)
text_id = canvas.create_text(100, 100, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))

# timer label over tmato
timer_label = Label(text="TIMER", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

# start button
start = Button(text="Start", command=launch)
start.grid(column=0, row=3)

# reset button
reset = Button(text="Reset", command=reset_time)
reset.grid(column=2, row=3)


# green ticks
tick = "✓"
green_tick = Label(text="", fg=GREEN, font=(FONT_NAME, 25, "bold"), width=13, bg=YELLOW)
green_tick.grid(column=1, row=4)



window.after(100000, countdown_25_min)


window.mainloop()

