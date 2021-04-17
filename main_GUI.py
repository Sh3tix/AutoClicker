import time
import threading
import tkinter as tk
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

"""
Author: G@b
Date: 13/04/2021
"""


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Autoclicker - G@b")
        self.master.iconbitmap('mouseclick.ico')
        self.master.resizable(False, False)
        self.widgets()

    def widgets(self):
        self.delay = tk.StringVar()
        self.start_stop_key = tk.StringVar()
        self.exit_key = tk.StringVar()

        # Widgets
        options_frame = tk.LabelFrame(self.master, text="options")

        label_delay = tk.Label(options_frame, text="Nombre de secondes entre chaque cliques")
        self.spinbox_delay = tk.Spinbox(options_frame, from_="0", to="300", textvariable=self.delay)

        label_start_stop = tk.Label(options_frame, text="Touche pour démarrer et pauser l'autoclick")
        self.start_stop = tk.Entry(options_frame, textvariable=self.start_stop_key)

        label_exit = tk.Label(options_frame, text="Touche pour arrêter l'autoclick")
        self.entry_exit = tk.Entry(options_frame, textvariable=self.exit_key)

        start_button = tk.Button(options_frame, text="Démarrer", command=self.get_attributes)

        # Positionnements
        label_delay.grid(row=0, column=0, padx=10)
        self.spinbox_delay.grid(row=1, column=0, padx=10)

        label_start_stop.grid(row=0, column=1, padx=10)
        self.start_stop.grid(row=1, column=1, pady=10)

        label_exit.grid(row=2, column=1)
        self.entry_exit.grid(row=4, column=1)

        start_button.grid(row=4, column=0)

        options_frame.grid()

    def get_attributes(self):
        delay = float(self.delay.get())
        start_stop_key = self.start_stop_key.get()
        exit_key = self.exit_key.get()

        if delay > 0.0 and start_stop_key != "" and exit_key != "":
            start_autoclick(delay, start_stop_key, exit_key)


def start_autoclick(delay, start_stop_key, exit_key):
    button = Button.left
    start_stop_key = KeyCode(char=start_stop_key)
    exit_key = KeyCode(char=exit_key)

    class ClickMouse(threading.Thread):
        def __init__(self, delay, button):
            super(ClickMouse, self).__init__()
            self.delay = delay
            self.button = button
            self.running = False
            self.program_run = True

        def start_clicking(self):
            self.running = True

        def stop_clicking(self):
            self.running = False

        def exit(self):
            self.stop_clicking()
            self.program_run = False

        def run(self):
            while self.program_run:
                while self.running:
                    mouse.click(self.button)
                    time.sleep(self.delay)
                time.sleep(0.1)

    mouse = Controller()
    thread = ClickMouse(delay, button)
    thread.start()

    def on_press(key):
        if key == start_stop_key:
            if thread.running:
                thread.stop_clicking()
            else:
                thread.start_clicking()
        elif key == exit_key:
            thread.exit()
            listener.stop()

    with Listener(on_press=on_press) as listener:
        listener.join()


if "__main__" == __name__:
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
