from tkinter import *

FONT = ("Roman", 10)
window = Tk()
window.title("Track GUI Program")
window.minsize(width=300, height=300)
window.config(padx=120, pady=100)

# Labels
target_timing = Label(text="Your Target Timing (Hours:Minutes:Seconds) :", font=FONT)
equals = Label(text="is equal to", font=FONT)
miles = Label(text="Miles", font=FONT)
final_pace = Label(text="Final Pace (per km)", font=FONT)
km = Label(text="Km", font=FONT)
miles.grid(row=0, column=2)
equals.grid(row=1, column=0)
km.grid(row=1, column=2)
target_timing.grid(row=2, column=0)
final_pace.grid(row=3, column=0)

# Entry Boxes
timing_entry = Entry(width=7)
miles_entry = Entry(width=7)
km_entry = Entry(width=7)
final_entry = Entry(width=17)
miles_entry.grid(row=0, column=1)
km_entry.grid(row=1, column=1)
timing_entry.grid(row=2, column=1)
final_entry.grid(row=3, column=1)

# Buttons


def resolve():
    if miles_entry.get():
        b = round(float(miles_entry.get()) * 1.60934, 2)
        km_entry.delete(0, END)
        km_entry.insert(0, str(b))
    if timing_entry.get():
        duration = timing_entry.get().split(":")
        hours, minutes, seconds = int(duration[0]), int(duration[1]), int(duration[2])
        # Conversion to seconds
        total_timing_s = hours * 3600 + minutes * 60 + seconds
        km_split = total_timing_s // float(km_entry.get())
        min_s = str(int(km_split // 60)) + " minutes : " + str(int(km_split % 60)) + " seconds"
        final_entry.delete(0, END)
        final_entry.insert(0, min_s)


calculate = Button(text="Calculate", command=resolve)
calculate.grid(row=4, column=1)


# Keeps window on screen and allows for listening of commands, command must be at the end of script to ensure continuity
window.mainloop()
