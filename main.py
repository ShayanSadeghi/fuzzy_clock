import time
from tkinter import *
from PIL import ImageTk, Image
from utility import get_fuzzy_time

root = Tk()
root.title("Fuzzy Clock")
root.geometry("1024x720")
fuzzy_time_prime = ""

while True:
    fuzzy_time = get_fuzzy_time()
    my_label = Label(root, text=fuzzy_time)
    my_label.pack()
    root.update_idletasks()
    root.update()

    if fuzzy_time != fuzzy_time_prime:
        fuzzy_time_prime = fuzzy_time

    time.sleep(60)
    my_label.pack_forget()
