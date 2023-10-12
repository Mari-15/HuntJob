import tkinter as tk
from tkinter import messagebox


def info_message(message):
    window = tk.Tk()
    window.withdraw()
    messagebox.showinfo('Information', f'{message}')
    window.destroy()


def warning_message(message):
    window = tk.Tk()
    window.withdraw()
    messagebox.showwarning('Warning', f'{message}')
    window.destroy()


def error_message(message):
    window = tk.Tk()
    window.withdraw()
    messagebox.showerror('Error', f'{message}')
    window.destroy()