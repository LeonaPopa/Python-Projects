import tkinter as tk
from tkinter import messagebox
import time

# Variables for session lengths
work_session = 25
short_break = 5
long_break = 10

# Flags to track timer status
paused = False
completed = False

# Count to track the number of completed sessions
session_count = 0

def start_timer():
    global paused, completed, session_count
    if not paused:
        timer_label.config(text="00:00")
        start_time = time.time()

    while not completed:
        tk.update_idletasks()
        tk.update()
        time.sleep(1)

        if paused:
            break

        current_time = time.time()
        elapsed_time = round(current_time - start_time)

        # Determine the time remaining based on the session type
        if session_count % 4 == 0:
            time_remaining = long_break * 60 - elapsed_time
        elif session_count % 2 == 0:
            time_remaining = short_break * 60 - elapsed_time
        else:
            time_remaining = work_session * 60 - elapsed_time

        # If the time remaining is negative, switch to the next session
        if time_remaining <= 0:
            completed = True
            messagebox.showinfo("Session Completed", "Well done! Take a break.")
            session_count += 1
            if session_count % 4 == 0:
                timer_label.config(text=f"{long_break}:00")
            elif session_count % 2 == 0:
                timer_label.config(text=f"{short_break}:00")
            else:
                timer_label.config(text=f"{work_session}:00")
            time.sleep(2)
        else:
            minutes, seconds = divmod(time_remaining, 60)
            timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

    # Reset the completed flag so the timer can be restarted
    completed = False
    paused = False

def pause_timer():
    global paused
    paused = not paused

def reset_timer():
    global session_count, completed
    session_count = 0
    completed = False
    paused = False
    timer_label.config(text=f"{work_session}:00")

def set_work_session():
    global work_session
    work_session = int(work_session_entry.get())
    work_session_entry.delete(0, 'end')

def set_short_break():
    global short_break
    short_break = int(short_break_entry.get())
    short_break_entry.delete(0, 'end')

# Create the main window
window = tk.Tk()
window.title("Pomodoro Clock")

# Create the timer label
timer_label = tk.Label(window, text=f"{work_session}:00", font=("Arial", 40))
timer_label.pack(pady=20)

# Create the buttons
start_button = tk.Button(window, text="Start", command=start_timer)
start_button.pack(pady=20)

pause_button = tk.Button(window, text="Pause", command=pause_timer)
pause_button.pack(pady=10)

reset_button = tk.Button(window, text="Reset", command=reset_timer)
reset_button.pack(pady=10)

# Create the work session and break session entry boxes
work_session_label = tk.Label(window, text="Work Session (minutes):")
work_session_label.pack(pady=10)

work_session_entry = tk.Entry(window)
work_session_entry.pack(pady=10)

set_work_session_button = tk.Button(window, text="Set", command=set_work_session)
set_work_session_button.pack(pady=10)

short_break_label = tk.Label(window, text="Short Break (minutes):")
short_break_label.pack(pady=10)

short_break_entry = tk.Entry(window)
short_break_entry.pack(pady=10)

set_short_break_button = tk.Button(window, text="Set", command=set_short_break)
set_short_break_button.pack(pady=10)

# Start the main loop
window.mainloop()