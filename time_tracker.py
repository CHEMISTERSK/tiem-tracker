import time
import tkinter as tk
from db.db_init import *
from datetime import date

start_time = None
timer_running = False
task_time = None

def start_timer():
    global start_time, timer_running
    if task_name.get() and not timer_running:
        start_time = time.time()
        timer_running = True
        start_button.config(state="disabled")
        stop_button.config(state="normal")
        update_timer()
    elif not task_name.get():
        canvas.delete("all")
        canvas.create_text(200, 200, text="Please enter a task name", font=("Arial", 24))

def update_timer():
    global timer_running, task_time
    if timer_running:
        current_time = time.time()
        elapsed_time = current_time - start_time
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        secunds = int(elapsed_time - 60 * minutes)
        task_time = f"{hours}:{minutes}:{secunds}"
        canvas.delete("all")
        canvas.create_text(200, 70, text = "Task:", font = ("Arial", 20), fill = "white")
        canvas.create_text(200, 100, text = task_name.get(), font = ("Arial", 20), fill = "white")
        canvas.create_text(200, 200, text = f"Elapsed Time:\n {hours:02d} : {minutes:02d} : {secunds:02d}", font = ("Arial", 24), fill = "white")
        root.after(10, update_timer) # 10

def stop_timer():
    global timer_running, task_time
    timer_running = False
    start_button.config(state="normal")
    stop_button.config(state="disabled")
    save_task(task_name.get(), task_time, date.today())
    canvas.create_text(80, 10, text = "Task Saved Successfully", font = ("Arial", 10, "bold"), fill = "white")


root = tk.Tk()
root.title("Time Tracker")
root.config(bg = "#232628")
icon = tk.PhotoImage(file="C:\\Users\\Tomáš\\Desktop\\Tomáš\\Dokumenty\\VSCode\\Python\\doucko\\tiem-tracker\\timer_icon.png")
root.iconphoto(True, icon)

canvas = tk.Canvas(root, width = 400, height = 400, bg = "#232628")
canvas.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

connection = connection_check()

if connection:
    connection = "Connection successful"
else:
    connection = "Connection failed"
canvas.create_text(75, 10, text = connection, font = ("Arial", 10, "bold"), fill = "white")

task_name = tk.Entry(root, width=25, font = ("Arial", 20), bg = "#3A3B3B", fg = "white")
task_name.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 5)

start_button = tk.Button(root, text = "Start", command = start_timer, width = 25, bg = "#3A3B3B", fg = "white", font = ("arial", 10, "bold"))
start_button.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 5)

stop_button = tk.Button(root, text = "Stop", command = stop_timer, width = 25, bg = "#3A3B3B", fg = "white", font = ("arial", 10, "bold"))
stop_button.grid(row = 2, column = 2, padx = 5, pady = 5)

root.mainloop()