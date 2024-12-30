'''
Temporizador Pomodoro con Python y Tkinter

Descripción del proyecto
Esta aplicación utiliza la técnica Pomodoro para ayudarte a mantenerte productivo cronometrando 
las sesiones de trabajo y los descansos.

Cada sesión Pomodoro consta de 25 minutos de trabajo concentrado, seguidos de un descanso de 5 
minutos. El usuario puede iniciar, pausar y reiniciar las sesiones. Después de cada cuatro 
Pomodoros, se agrega un descanso más largo de 15 minutos.

'''

import tkinter as tk
from tkinter import messagebox

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")

        self.is_running = False
        self.pomodoro_duration = 25 * 60  # 25 minutos
        self.break_duration = 5 * 60       # 5 minutos
        self.long_break_duration = 15 * 60  # 15 minutos
        self.pomodoros_completed = 0

        self.remaining_time = self.pomodoro_duration
        self.label = tk.Label(master, text="", font=("Helvetica", 48), fg="green")
        self.label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(master, text="Pause", command=self.pause_timer)
        self.pause_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT)

        self.update_timer_display()

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.countdown()

    def pause_timer(self):
        self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.pomodoros_completed = 0
        self.remaining_time = self.pomodoro_duration
        self.update_timer_display()

    def countdown(self):
        if self.remaining_time > 0 and self.is_running:
            self.remaining_time -= 1
            self.update_timer_display()
            self.master.after(1000, self.countdown)
        elif self.remaining_time == 0:
            self.pomodoros_completed += 1
            
            if self.pomodoros_completed % 4 == 0:
                self.remaining_time = self.long_break_duration
                self.show_message("Take a long break!")
            else:
                self.remaining_time = self.break_duration
                self.show_message("Take a break!")
                
            self.update_timer_display()
            self.start_timer()  # Reinicia el temporizador automáticamente para el siguiente ciclo

    def update_timer_display(self):
        minutes, seconds = divmod(self.remaining_time, 60)
        self.label.config(text=f"{minutes:02}:{seconds:02}")

    def show_message(self, message):
        messagebox.showinfo("Break Time", message)

if __name__ == "__main__":
    root = tk.Tk()
    timer = PomodoroTimer(root)
    root.mainloop()